import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.block import Block
from typing import List, Dict, Any, Optional
from abc import ABC, abstractmethod


class Integrator(Block):
    # CONSTRUCTOR
    def __init__(self, initial_value):
        super().__init__(
            name = "Integrator",
            inputs = {"u": 0},
            outputs = {"y": initial_value},
            state = {"x": initial_value},
            connections = []
        )

    # METHODS
    def compute(self):
        self.outputs["y"] = self.state["x"]
    
    def update_state(self, dt):
        u = self.inputs["u"]
        x = self.state["x"]
        # x(t + delta_t) = x(t) + u(t) * delta_t
        x_new = x + u * dt
        self.state["x"] = x_new