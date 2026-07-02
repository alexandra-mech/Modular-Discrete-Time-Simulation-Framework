import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.block import Block
from typing import List, Dict, Any, Optional
from abc import ABC, abstractmethod


class Constant(Block):
    # CONSTRUCTOR
    def __init__(self, value):
        super().__init__(
            name = "Constant",
            inputs = {},
            outputs = {"y": value},
            state = None,
            connections = []
        )

        self.value = value

    # METHODS
    def compute(self, dt):
        self.outputs["y"] = self.value

    def update_state(self, dt):
        pass