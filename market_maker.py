"""
Core responsibilities:
- Consume order book (simulator or Nubra)
- Compute quotes
- Simulate fills
- Track inventory & PnL
- Log results
"""
"""
Core responsibilities:
- Consume order book (simulator or Nubra)
- Compute quotes
- Simulate fills
- Track inventory & PnL
- Log results
"""

import time
import csv
import random
from datetime import datetime
import os


# CONFIG

USE_NUBRA = False
NUM_TICKS = 500
SLEEP_TIME = 0.3

os.makedirs("logs", exist_ok=True)

# IMPORTS

from strategy.signals import (
    compute_mid,
    compute_imbalance,
    compute_quotes,
    compute_quotes_baseline
)

from strategy.config import INVENTORY_CAP

if USE_NUBRA:
    from data_sources.nubra_ws import NubraWebSocketClient
else:
    from data_sources.simulator import get_order_book

# MAIN RUN FUNCTION

def run_market_maker(strategy_mode="adaptive"):

    assert strategy_mode in ["baseline", "adaptive"]

    inventory = 0
    cash = 0.0

    log_path = f"logs/mm_logs_{strategy_mode}.csv"

    log_file = open(log_path, "w", newline="")
    writer = csv.writer(log_file)

    writer.writerow([
        "timestamp",
        "best_bid",
        "best_ask",
        "mid",
        "bid_quote",
        "ask_quote",
        "imbalance",
        "inventory",
        "cash",
        "pnl"
    ])

    # Optional Nubra client
    if USE_NUBRA:
        nubra_client = NubraWebSocketClient()
        nubra_client.connect()

    # MAIN LOOP
    for tick in range(NUM_TICKS):

        # GET ORDER BOOK
        if USE_NUBRA:
            book = nubra_client.get_order_book()
        else:
            book = get_order_book()

        best_bid = book["bid"]
        best_ask = book["ask"]

        # SIGNALS
        mid = compute_mid(book)
        imbalance = compute_imbalance(book)

        if strategy_mode == "baseline":
            bid_quote, ask_quote = compute_quotes_baseline(mid)
        else:
            bid_quote, ask_quote = compute_quotes(
                mid=mid,
                imb=imbalance,
                inventory=inventory
            )

        # SIMULATED PASSIVE FILLS 
        fill_prob = 0.15  # 15% chance of getting hit

        # Buy fill (someone sells to us)
        if bid_quote >= best_bid and inventory < INVENTORY_CAP:
            if random.random() < fill_prob:
                inventory += 1
                cash -= bid_quote

        # Sell fill (someone buys from us)
        elif ask_quote <= best_ask and inventory > -INVENTORY_CAP:
            if random.random() < fill_prob:
                inventory -= 1
                cash += ask_quote


        # MARK-TO-MARKET PNL
        pnl = cash + inventory * mid

        # LOG
        writer.writerow([
            datetime.now().isoformat(),
            round(best_bid, 2),
            round(best_ask, 2),
            round(mid, 2),
            round(bid_quote, 2),
            round(ask_quote, 2),
            round(imbalance, 4),
            inventory,
            round(cash, 2),
            round(pnl, 2)
        ])

        time.sleep(SLEEP_TIME)

    log_file.close()
    print(f"{strategy_mode.upper()} run complete → {log_path}")


# ENTRY POINT
if __name__ == "__main__":

    run_market_maker(strategy_mode="baseline")
    run_market_maker(strategy_mode="adaptive")

    print("\nAll market making runs completed.")

