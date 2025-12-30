"""
Generates comparison plots for Baseline vs Adaptive strategies
"""
import pandas as pd
import matplotlib.pyplot as plt
import os


# CONFIG

LOG_DIR = "logs"
PLOT_DIR = "plots"
os.makedirs(PLOT_DIR, exist_ok=True)

baseline_file = f"{LOG_DIR}/mm_logs_baseline.csv"
adaptive_file = f"{LOG_DIR}/mm_logs_adaptive.csv"


# READ LOGS

baseline = pd.read_csv(baseline_file)
adaptive = pd.read_csv(adaptive_file)

# Convert timestamp to datetime
baseline['timestamp'] = pd.to_datetime(baseline['timestamp'])
adaptive['timestamp'] = pd.to_datetime(adaptive['timestamp'])


# PLOT PnL COMPARISON

plt.figure(figsize=(12, 6))
plt.plot(baseline['timestamp'], baseline['pnl'], label='Baseline', color='red', alpha=0.7)
plt.plot(adaptive['timestamp'], adaptive['pnl'], label='Adaptive', color='green', alpha=0.7)
plt.title('PnL Comparison: Baseline vs Adaptive')
plt.xlabel('Time')
plt.ylabel('PnL')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(f"{PLOT_DIR}/pnl_comparison.png")
plt.show()


# PLOT INVENTORY COMPARISON
plt.figure(figsize=(12, 6))
plt.plot(baseline['timestamp'], baseline['inventory'], label='Baseline', color='red', alpha=0.7)
plt.plot(adaptive['timestamp'], adaptive['inventory'], label='Adaptive', color='green', alpha=0.7)
plt.title('Inventory Comparison: Baseline vs Adaptive')
plt.xlabel('Time')
plt.ylabel('Inventory')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(f"{PLOT_DIR}/inventory_comparison.png")
plt.show()

print(f"Plots saved to {PLOT_DIR}/")