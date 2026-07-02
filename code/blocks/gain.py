import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.block import Block
from typing import List, Dict, Any, Optional
from abc import ABC, abstractmethod


class Gain(Block):
    # CONSTRUCTOR
    def __init__(self, k):
        super().__init__(
            name = "Gain",
            inputs = {"u": 0},
            outputs = {"y": 0},
            state = None,
            connections = []
        )
        self.k = k      # Block parameter

    # METHODS
    def compute(self):
        # y = k * u
        self.outputs["y"] = self.k * self.inputs["u"]
    
    def update_state(self, dt):
        pass