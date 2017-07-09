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
        'position': [368, 128],
        'size': [48, 48],
        'rotation': 0
    };
    B = {
        'index': 1,
        'image': pygame.image.load("./img/buttons/b.png"),
        'isPressed': False,
        'position': [400, 96],
        'size': [48, 48],
        'rotation': 0
    };
    X = {
        'index': 2,
        'image': pygame.image.load("./img/buttons/x.png"),
        'isPressed': False,
        'position': [336, 96],
        'size': [48, 48],
        'rotation': 0
    };
    Y = {
        'index': 3,
        'image': pygame.image.load("./img/buttons/y.png"),
        'isPressed': False,
        'position': [368, 66],
        'size': [48, 48],
        'rotation': 0
    };
    LEFT_BUMPER = {
        'index': 4,
        'image': pygame.image.load("./img/buttons/lb.png"),
        'isPressed': False,
        'position': [64, -38],
        'size': [112, 112],
        'rotation': 10
    };
    RIGHT_BUMPER = {
        'index': 5,
        'image': pygame.image.load("./img/buttons/rb.png"),
        'isPressed': False,
        'position': [318, -38],
        'size': [112, 112],
        'rotation': -10
    };
    BACK = {
        'index': 6,
        'image': pygame.image.load("./img/buttons/back.png"),
        'isPressed': False,
        'position': [200, 102],
        'size': [32, 32],
        'rotation': 0
    };
    START = {
        'index': 7,
        'image': pygame.image.load("./img/buttons/start.png"),
        'isPressed': False,
        'position': [280, 102],
        'size': [32, 32],
        'rotation': 0
    };
    LEFT_STICK = {
        'index': 8,
        'image': pygame.image.load("./img/buttons/ls.png"),
        'isPressed': False,
        'position': [88, 80],
        'size': [80, 80],
        'rotation': 0
    };
    RIGHT_STICK = {
        'index': 9,
        'image': pygame.image.load("./img/buttons/rs.png"),
        'isPressed': False,
        'position': [280, 152],
        'size': [80, 80],
        'rotation': 0
    };

def resolveButtonIndex(i):
    """Resolves a button index to a name"""
    if (i == Buttons.A['index']):
        return 'A';
    elif (i == Buttons.B['index']):
        return 'B';
    elif (i == Buttons.X['index']):
        return 'X';
    elif (i == Buttons.Y['index']):
        return 'Y';
    elif (i == Buttons.LEFT_BUMPER['index']):
        return 'LEFT_BUMPER';
    elif (i == Buttons.RIGHT_BUMPER['index']):
        return 'RIGHT_BUMPER';
    elif (i == Buttons.BACK['index']):
        return 'BACK';
    elif (i == Buttons.START['index']):
        return 'START';
    elif (i == Buttons.LEFT_STICK['index']):
        return 'LEFT_STICK';
    elif (i == Buttons.RIGHT_STICK['index']):
        return 'RIGHT_STICK';

    return 'Unknown Button';

def draw(screen, bgImage):
    screen.fill((40, 40, 40));

    buttonKeys = dir(Buttons);

    screen.blit(bgImage, [0, 0]);


    for key in buttonKeys:
        if not key.startswith('__'):
            buttonConst = getattr(Buttons, key);
            if buttonConst and buttonConst['isPressed'] == True:

                buttonPosition = buttonConst['position'];
                buttonImage = buttonConst['image'];
                buttonSize = buttonConst['size'];
                buttonRotation = buttonConst['rotation'];

                transformedButton = pygame.transform.scale(buttonImage, buttonSize);
                transformedButton = pygame.transform.rotate(transformedButton, buttonRotation);

                screen.blit(transformedButton, buttonPosition);

    #for key in buttonKeys:
    #    if not key.startswith('__'):
    #        buttonConst = getattr(Buttons, key);
    #        if buttonConst:
#
#                buttonPosition = buttonConst['position'];
#                buttonImage = buttonConst['image'];
#                buttonScale = buttonConst['size'];
#                buttonRotation = buttonConst['rotation'];
#
#                transformedButton = pygame.transform.scale(buttonImage, buttonScale);
#                transformedButton = pygame.transform.rotate(transformedButton, buttonRotation);
#
#                screen.blit(transformedButton, buttonPosition);

    pygame.display.flip();
    return;

def main():
    pygame.init();
    pygame.joystick.init();
    screenSize = [512, 342];
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
    bgImage = pygame.image.load("./img/controller.png");

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
                            buttonConst = getattr(Buttons, buttonName);

                            if buttonConst:
                                buttonConst['isPressed'] = True;
                                print(buttonName + ' pressed');

                if event.type == pygame.JOYBUTTONUP:
                    buttons = joystick.get_numbuttons();
                    for i in range(buttons):
                        button = joystick.get_button(i);
                        if not button:
                            buttonName = resolveButtonIndex(i);
                            buttonConst = getattr(Buttons, buttonName);

                            if buttonConst:
                                buttonConst['isPressed'] = False;
                                print(buttonName + ' released');

                draw(screen. bgImage);
    else:
        print('No controllers found. Please ensure your controller is plugged in and turned on.');

        while True:
            draw(screen, bgImage);

main();
