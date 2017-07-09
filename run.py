#
# Controller view by Brian Wilbur
# https://github.com/oblivion-hymns
#
from contextlib import contextmanager;
import sys, os;
import pygame;

class Buttons:
    A = {
        'index': 0,
        'image': pygame.image.load("./img/buttons/a.png"),
        'isPressed': False,
        'size': [0, 0, 32, 32]
    };
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
    if (i == Buttons.A['index']):
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

def draw(screen):
    screen.fill((40, 40, 40));

    if Buttons.A['isPressed']:
        screen.blit(Buttons.A['image'], Buttons.A['image'].get_rect());

    pygame.display.flip();
    return;

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
                            for buttonKey in dir(Buttons):
                                if not buttonKey.startswith('__'):
                                    if i == Buttons.buttonKey['index']:
                                        Buttons.buttonKey['isPressed'] = True;
                                        print(resolveButtonIndex(i) + ' pressed');

                if event.type == pygame.JOYBUTTONUP:
                    buttons = joystick.get_numbuttons();
                    for i in range(buttons):
                        button = joystick.get_button(i);
                        if not button:
                            buttonName = resolveButtonIndex(i);
                            for buttonKey in dir(Buttons):
                                if not buttonKey.startswith('__'):
                                    if i == getattr(Buttons, buttonKey)['index']:
                                        getattr(Buttons, buttonKey)['isPressed'] = False;
                                        print(resolveButtonIndex(i) + ' released');

                draw(screen);
    else:
        print('No controllers found. Please ensure your controller is plugged in and turned on.');

        while True:
            draw(screen);

main();
