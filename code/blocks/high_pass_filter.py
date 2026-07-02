import numpy as np
from core.block import Block


# ALLOWS: quick signal variations
# MITIGATES: slow sigal variations


class HighPassFilter(Block):
    def __init__(self, alpha=0.1, initial_value=0.0):
        super().__init__(
            name="HighPassFilter",
            inputs={"u": 0.0},
            outputs={"y": initial_value},
            state={"u_prev": 0.0, "y_prev": initial_value},
            connections=[]
        )
        self.alpha = alpha

    def compute(self, dt):
        u = self.inputs["u"]
        u_prev = self.state["u_prev"]
        y_prev = self.state["y_prev"]

        y_new = self.alpha * (y_prev + u - u_prev)

        self.outputs["y"] = y_new
        self.state["y_prev"] = y_new
        self.state["u_prev"] = u

    def update_state(self, dt):
        pass
