import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.block import Block
from typing import List, Dict, Any, Optional
from abc import ABC, abstractmethod


class Scope(Block):
    def __init__(self):
        super().__init__(
            name="Scope",
            inputs={"u": 0.0},
            outputs={},
            state={"values": []},
            connections=[]
        )

    def compute(self, dt):
        # Register the input value at each step
        self.state["values"].append(self.inputs["u"])

    def update_state(self, dt):
        pass
