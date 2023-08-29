from machine import Pin, PWM


class Lock:
    def __init__(self):
        self.locked = True
        self.SG = PWM(Pin(5, mode=Pin.OUT))
        self.SG.freq(50)
        self.SG.duty(0)

    def lock(self):
        if self.locked:
            return
        self.SG.duty(1023)
        self.locked = not self.locked

    def unlock(self):
        if not self.locked:
            return
        self.SG.duty(0)
        self.locked = not self.locked
