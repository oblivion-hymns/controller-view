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
        potentialJoystick = pygame.joystick.Joystick(x);

        if potentialJoystick:
            return potentialJoystick;

    return None;

def main():
    pygame.init();
    screenSize = [200, 200];
    screen = pygame.display.set_mode(screenSize);
    pygame.display.set_caption('Controller View');

    pygame.joystick.init();

    joystick = getJoystick();
    runLoop = True;

    if (joystick):
        print('Controller found. Listening for input...');
        runLoop = True;

        while runLoop:
            for event in pygame.event.get():
                print('event found');
                if event.type == pygame.JOYBUTTONDOWN:
                    print("Joystick button pressed.")
                if event.type == pygame.JOYBUTTONUP:
                    print("Joystick button released.")
    else:
        print('No controllers found. Please ensure your controller is plugged in and turned on.');

    for event in pygame.event.get():
        print(pygame.JOYBUTTONUP);
        if event == pygame.JOYBUTTONUP:
            button = joystick.get_button();

main();
