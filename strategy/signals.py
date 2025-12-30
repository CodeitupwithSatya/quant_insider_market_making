from .config import BASE_SPREAD,ALPHA_IMB,GAMMA_INV

def compute_mid(book):
    return (book["bid"] + book["ask"]) / 2

def compute_imbalance(book):
    bq, aq = book["bid_qty"], book["ask_qty"]
    return (bq - aq) / (bq + aq)

def compute_quotes(mid, imb, inventory):
    skew = - inventory / 10
    spread = BASE_SPREAD + abs(inventory) * 0.5

    bid = mid - spread + ALPHA_IMB * imb + GAMMA_INV * skew
    ask = mid + spread + ALPHA_IMB * imb + GAMMA_INV * skew
    return bid, ask

def compute_quotes_baseline(mid):
    spread = BASE_SPREAD
    return mid - spread, mid + spread
