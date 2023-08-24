import stepper_motor as sm

SM = sm.StepperMotor(4, 5, 0)  # TODO: change pins
armoire = True


def lock():
    global armoire
    if armoire:
        SM.step_n(SM.degres_to_step(180), 1)
    else:
        SM.step_n(SM.degres_to_step(180), 0)
    armoire = not armoire
