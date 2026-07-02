import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.block import Block
from typing import List, Dict, Any, Optional
from abc import ABC, abstractmethod


class Step(Block):
    # CONSTRUCTOR
    def __init__(self, initial_value, final_value, step_time):
        super().__init__(
            name = "Step",
            inputs = {},
            outputs = {"y": initial_value},
            state = {"t": 0},
            connections = []
        )

        self.initial_value = initial_value
        self.final_value = final_value
        self.step_time = step_time

    # METHODS
    def compute(self):
        if self.state["t"] < self.step_time:
            self.outputs["y"] = self.initial_value
        elif self.state["t"] >= self.step_time:
            self.outputs["y"] = self.final_value
        

    def update_state(self, dt):
        self.state["t"] += dt