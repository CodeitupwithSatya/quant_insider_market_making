import random

def get_order_book():
    mid = 10000 + random.randint(-20, 20)
    spread = random.choice([2, 4])

    return {
        "bid": mid - spread / 2,
        "ask": mid + spread / 2,
        "bid_qty": random.randint(50, 200),
        "ask_qty": random.randint(50, 200),
    }
