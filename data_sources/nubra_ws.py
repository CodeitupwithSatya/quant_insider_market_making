"""
Nubra WebSocket Data Source (UAT)

This module is designed to consume real-time order book data
from Nubra's UAT WebSocket feed.

NOTE:
For stability and reproducibility, this repository uses a
simulated order book by default. This file demonstrates how
live integration would be done.
"""

class NubraWebSocketClient:
    def __init__(self):
        self.connected = False

    def connect(self):
        """
        Establish WebSocket connection to Nubra UAT
        
        NOTE:
        Actual WebSocket connection is intentionaklly disablked for stability and reproducibility.
        """
        
        print("[INFO] Nubra WebSocket client initialized")
        self.connected = True

    def on_message(self, message):
        """
        Parse incoming order book message
        """
        # Extract:
        # best_bid
        # best_ask
        # bid_qty
        # ask_qty
        pass

    def get_order_book(self):
        """
        Returns latest order book snapshot in standard format
        """
        if not self.connected:
            raise RuntimeError("WebSocket not connected")

       
        return {
            "bid": self.best_bid,
            "ask": self.best_ask,
            "bid_qty": self.bid_qty,
            "ask_qty": self.ask_qty
        }
