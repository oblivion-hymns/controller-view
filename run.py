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
        'position': [0, 0]
    };
    B = {
        'index': 1,
        'image': pygame.image.load("./img/buttons/b.png"),
        'isPressed': False,
        'position': [32, 0]
    };
    X = {
        'index': 2,
        'image': pygame.image.load("./img/buttons/x.png"),
        'isPressed': False,
        'position': [64, 0]
    };
    Y = {
        'index': 3,
        'image': pygame.image.load("./img/buttons/y.png"),
        'isPressed': False,
        'position': [96, 0]
    };
    LEFT_BUMPER = {
        'index': 4,
        'image': pygame.image.load("./img/buttons/lb.png"),
        'isPressed': False,
        'position': [128, 0]
    };
    RIGHT_BUMPER = {
        'index': 5,
        'image': pygame.image.load("./img/buttons/rb.png"),
        'isPressed': False,
        'position': [0, 32]
    };
    BACK = {
        'index': 6,
        'image': pygame.image.load("./img/buttons/back.png"),
        'isPressed': False,
        'position': [32, 32]
    };
    START = {
        'index': 7,
        'image': pygame.image.load("./img/buttons/start.png"),
        'isPressed': False,
        'position': [64, 32]
    };
    LEFT_STICK = {
        'index': 8,
        'image': pygame.image.load("./img/buttons/ls.png"),
        'isPressed': False,
        'position': [96, 32]
    };
    RIGHT_STICK = {
        'index': 9,
        'image': pygame.image.load("./img/buttons/rs.png"),
        'isPressed': False,
        'position': [128, 32]
    };

def resolveButtonIndex(i):
    """Resolves a button index to a name"""
    if (i == Buttons.A['index']):
        return 'A';
    elif (i == Buttons.B):
        return 'B';
    elif (i == Buttons.X):
        return 'X';
    elif (i == Buttons.Y):
        return 'Y';
    elif (i == Buttons.LEFT_BUMPER):
        return 'LEFT_BUMPER';
    elif (i == Buttons.RIGHT_BUMPER):
        return 'RIGHT_BUMPER';
    elif (i == Buttons.BACK):
        return 'BACK';
    elif (i == Buttons.START):
        return 'START';
    elif (i == Buttons.LEFT_STICK):
        return 'LEFT_STICK';
    elif (i == Buttons.RIGHT_STICK):
        return 'RIGHT_STICK';

    return 'Unknown Button';

def draw(screen):
    screen.fill((40, 40, 40));

    buttonKeys = dir(Buttons);

    for key in buttonKeys:
        if not key.startswith('__'):
            buttonConst = getattr(Buttons, key);
            if buttonConst and buttonConst['isPressed'] == True:
                screen.blit(pygame.transform.scale(buttonConst['image'], (32, 32)), buttonConst['position']);

    #screen.blit(pygame.transform.scale(Buttons.A['image'], (32, 32)), Buttons.A['position']);
    #screen.blit(pygame.transform.scale(Buttons.B['image'], (32, 32)), Buttons.B['position']);
    #screen.blit(pygame.transform.scale(Buttons.X['image'], (32, 32)), Buttons.X['position']);
    #screen.blit(pygame.transform.scale(Buttons.Y['image'], (32, 32)), Buttons.Y['position']);
    #screen.blit(pygame.transform.scale(Buttons.LEFT_BUMPER['image'], (32, 32)), Buttons.LEFT_BUMPER['position']);
    #screen.blit(pygame.transform.scale(Buttons.RIGHT_BUMPER['image'], (32, 32)), Buttons.RIGHT_BUMPER['position']);
    #screen.blit(pygame.transform.scale(Buttons.BACK['image'], (32, 32)), Buttons.BACK['position']);
    #screen.blit(pygame.transform.scale(Buttons.START['image'], (32, 32)), Buttons.START['position']);
    #screen.blit(pygame.transform.scale(Buttons.LEFT_STICK['image'], (32, 32)), Buttons.LEFT_STICK['position']);
    #screen.blit(pygame.transform.scale(Buttons.RIGHT_STICK['image'], (32, 32)), Buttons.RIGHT_STICK['position']);

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

                if event.type == pygame.JOYBUTTONUP:
                    buttons = joystick.get_numbuttons();
                    for i in range(buttons):
                        button = joystick.get_button(i);
                        if not button:
                            buttonName = resolveButtonIndex(i);
                            print(buttonName);
                            buttonConst = getattr(Buttons, buttonName);

                            if buttonConst:
                                buttonConst['isPressed'] = False;
                                print(buttonName + ' released');

                draw(screen);
    else:
        print('No controllers found. Please ensure your controller is plugged in and turned on.');

        while True:
            draw(screen);

main();
