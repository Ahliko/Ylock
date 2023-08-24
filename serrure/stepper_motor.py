from time import sleep

import machine


class StepperMotor:
    def __init__(self, step, dir, enable):
        self.step = machine.Pin(step, machine.Pin.OUT)
        self.dir = machine.Pin(dir, machine.Pin.OUT)
        self.enable = machine.Pin(enable, machine.Pin.OUT)
        self.enable.value(1)
        self.dir.value(0)
        self.step.value(0)

    def step_forward(self):
        self.dir.value(0)
        self.step.value(1)
        sleep(0.001)
        self.step.value(0)

    def step_backward(self):
        self.dir.value(1)
        self.step.value(1)
        sleep(0.001)
        self.step.value(0)

    def step_n(self, n, direction):
        if direction:
            for i in range(n):
                self.step_forward()
        else:
            for i in range(n):
                self.step_backward()

    def degres_to_step(self, degres):
        return int(degres * 4096 / 360)
