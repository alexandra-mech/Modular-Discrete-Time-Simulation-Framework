import numpy as np
from core.block import Block

# ALLOWS: slow signal variations
# MITIGATES: quick sigal variations (noise)

# alpha (0.05 - 0.2): very mild signal
# alpha (0.5 - 0.9): barely filters

class LowPassFilter(Block):
    def __init__(self, alpha=0.1, initial_value=0.0):
        super().__init__(
            name="LowPassFilter",
            inputs={"u": 0.0},
            outputs={"y": initial_value},
            state={"y_prev": initial_value},
            connections=[]
        )
        self.alpha = alpha

    def compute(self, dt):
        u = self.inputs["u"]
        y = self.outputs["y"]
        y_new = y + self.alpha * (u - y)
        self.outputs["y"] = y_new
        self.state["y_prev"] = y_new

    def update_state(self, dt):
        pass
