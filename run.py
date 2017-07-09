#
# Controller view by Brian Wilbur
# https://github.com/oblivion-hymns
#
from contextlib import contextmanager;
import sys, os;
import pygame;

class Buttons:
    A = 0;
    B = 1;
    X = 2;
    Y = 3;
    LEFT_BUMPER = 4;
    RIGHT_BUMPER = 5;
    BACK = 6;
    START = 7;
    LEFT_STICK = 8;
    RIGHT_STICK = 9;

def resolveButtonIndex(i):
    """Resolves a button index to a name"""
    if (i == Buttons.A):
        return 'A Button';
    elif (i == Buttons.B):
        return 'B Button';
    elif (i == Buttons.X):
        return 'X Button';
    elif (i == Buttons.Y):
        return 'Y Button';
    elif (i == Buttons.LEFT_BUMPER):
        return 'Left Bumper';
    elif (i == Buttons.RIGHT_BUMPER):
        return 'Right Bumper';
    elif (i == Buttons.BACK):
        return 'Back Button';
    elif (i == Buttons.START):
        return 'Start Button';
    elif (i == Buttons.LEFT_STICK):
        return 'LS Button';
    elif (i == Buttons.RIGHT_STICK):
        return 'RS Button';

    return 'Unknown Button';

def main():
    pygame.init();
    pygame.joystick.init();
    screenSize = [200, 200];
    screen = pygame.display.set_mode(screenSize);
    pygame.display.set_caption('Controller View');

    joystick = None;
    joystickCount = pygame.joystick.get_count();
    for x in range(joystickCount):
        potentialJoystick = pygame.joystick.Joystick(x);

        if potentialJoystick:
            joystick = potentialJoystick;
            break;

    runLoop = True;

    if (joystick):
        print('Controller found. Listening for input...');
        joystick.init();
        runLoop = True;

        while runLoop:
            for event in pygame.event.get():

                if event.type == pygame.JOYBUTTONDOWN:
                    buttons = joystick.get_numbuttons();
                    for i in range(buttons):
                        button = joystick.get_button(i);
                        if button:
                            buttonName = resolveButtonIndex(i);
                            print(buttonName + ' pressed');

                if event.type == pygame.JOYBUTTONUP:
                    print("Joystick button released.")
    else:
        print('No controllers found. Please ensure your controller is plugged in and turned on.');

    for event in pygame.event.get():
        print(pygame.JOYBUTTONUP);
        if event == pygame.JOYBUTTONUP:
            button = joystick.get_button();

main();
