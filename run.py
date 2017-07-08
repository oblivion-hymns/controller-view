#
# Controller view by Brian Wilbur
# https://github.com/oblivion-hymns
#
from contextlib import contextmanager;
import sys, os;
import pygame;

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout

def getJoystick():
    """Just get first connected joystick for now"""

    joystick = None;
    joystickIndex = -1;
    joystickCount = pygame.joystick.get_count();
    for x in range(joystickCount):

        with suppress_stdout():
            sys.stdout = os.devnull
            sys.stderr = os.devnull
            potentialJoystick = pygame.joystick.Joystick(x);
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__

        if potentialJoystick:
            return potentialJoystick;

    return None;

def readInput(joystick):
    numButtons = joystick.get_numbuttons();

    print('0');
    for i in range(numButtons):
        print('1')
        button = joystick.get_button(i);
        print('2');
        if (button):
            print('3');
            print('Button ' + str(i) + ' pushed down');

    print('4');

    return;

def main():
    pygame.joystick.init();

    joystick = getJoystick();
    runLoop = True;

    if (joystick):
        print('Controller found. Listening for input...');
        joystick.init();
        while (runLoop):
            readInput(joystick);
    else:
        print('No controllers found. Please ensure your controller is plugged in and turned on.');

main();
