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
        'imagePressed': pygame.image.load("./img/buttons/a_pressed.png"),
        'isPressed': False,
        'position': [368, 128],
        'size': [48, 48],
        'rotation': 0
    };
    B = {
        'index': 1,
        'image': pygame.image.load("./img/buttons/b.png"),
        'imagePressed': pygame.image.load("./img/buttons/b_pressed.png"),
        'isPressed': False,
        'position': [400, 96],
        'size': [48, 48],
        'rotation': 0
    };
    X = {
        'index': 2,
        'image': pygame.image.load("./img/buttons/x.png"),
        'imagePressed': pygame.image.load("./img/buttons/x_pressed.png"),
        'isPressed': False,
        'position': [336, 96],
        'size': [48, 48],
        'rotation': 0
    };
    Y = {
        'index': 3,
        'image': pygame.image.load("./img/buttons/y.png"),
        'imagePressed': pygame.image.load("./img/buttons/y_pressed.png"),
        'isPressed': False,
        'position': [368, 66],
        'size': [48, 48],
        'rotation': 0
    };
    LEFT_BUMPER = {
        'index': 4,
        'image': pygame.image.load("./img/buttons/lb.png"),
        'imagePressed': pygame.image.load("./img/buttons/lb_pressed.png"),
        'isPressed': False,
        'position': [64, -38],
        'size': [112, 112],
        'rotation': 10
    };
    RIGHT_BUMPER = {
        'index': 5,
        'image': pygame.image.load("./img/buttons/rb.png"),
        'imagePressed': pygame.image.load("./img/buttons/rb_pressed.png"),
        'isPressed': False,
        'position': [318, -38],
        'size': [112, 112],
        'rotation': -10
    };
    BACK = {
        'index': 6,
        'image': pygame.image.load("./img/buttons/back.png"),
        'imagePressed': pygame.image.load("./img/buttons/back_pressed.png"),
        'isPressed': False,
        'position': [200, 102],
        'size': [32, 32],
        'rotation': 0
    };
    START = {
        'index': 7,
        'image': pygame.image.load("./img/buttons/start.png"),
        'imagePressed': pygame.image.load("./img/buttons/start_pressed.png"),
        'isPressed': False,
        'position': [280, 102],
        'size': [32, 32],
        'rotation': 0
    };
    LEFT_STICK = {
        'index': 8,
        'image': pygame.image.load("./img/buttons/stick.png"),
        'imagePressed': pygame.image.load("./img/buttons/stick_pressed.png"),
        'isPressed': False,
        'position': [88, 80],
        'size': [80, 80],
        'rotation': 0
    };
    RIGHT_STICK = {
        'index': 9,
        'image': pygame.image.load("./img/buttons/stick.png"),
        'imagePressed': pygame.image.load("./img/buttons/stick_pressed.png"),
        'isPressed': False,
        'position': [280, 152],
        'size': [80, 80],
        'rotation': 0
    };

class DPad:
    UP = {
        'isPressed': False,
    }

    RIGHT = {
        'isPressed': False,
    }

    DOWN = {
        'isPressed': False,
    }

    LEFT = {
        'isPressed': False,
    }

class LeftStick:
    UP = {
        'isPressed': False,
    }

    RIGHT = {
        'isPressed': False,
    }

    DOWN = {
        'isPressed': False,
    }

    LEFT = {
        'isPressed': False,
    }

class RightStick:
    UP = {
        'isPressed': False,
    }

    RIGHT = {
        'isPressed': False,
    }

    DOWN = {
        'isPressed': False,
    }

    LEFT = {
        'isPressed': False,
    }

class Trigger:
    LEFT = {
        'isPressed': False
    }

    RIGHT = {
        'isPressed': False
    }

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
    screen.fill((255, 0, 255));

    buttonKeys = dir(Buttons);

    screen.blit(bgImage, [0, 0]);

    #Left stick background
    stickImage = pygame.image.load("./img/buttons/stick.png");
    transformedImage = pygame.transform.scale(stickImage, Buttons.LEFT_STICK['size']);
    screen.blit(transformedImage, Buttons.LEFT_STICK['position']);

    #Right stick background
    stickImage = pygame.image.load("./img/buttons/stick.png");
    transformedImage = pygame.transform.scale(stickImage, Buttons.RIGHT_STICK['size']);
    screen.blit(transformedImage, Buttons.RIGHT_STICK['position']);

    #buttons
    for key in buttonKeys:
        if not key.startswith('__'):
            buttonConst = getattr(Buttons, key);
            if buttonConst:
                buttonImage = buttonConst['image'];
                if buttonConst['isPressed'] == True:
                    buttonImage = buttonConst['imagePressed'];

                buttonPosition = buttonConst['position'];
                buttonSize = buttonConst['size'];
                buttonRotation = buttonConst['rotation'];

                transformedButton = pygame.transform.scale(buttonImage, buttonSize);
                transformedButton = pygame.transform.rotate(transformedButton, buttonRotation);

                screen.blit(transformedButton, buttonPosition);

    dpadImage = pygame.image.load("./img/buttons/dpad.png");
    transformedImage = pygame.transform.scale(dpadImage, [80, 80]);
    screen.blit(transformedImage, [152, 152]);

    #DPad
    if DPad.UP['isPressed']:
        dpadImage = pygame.image.load("./img/buttons/dpad_up.png");
        transformedImage = pygame.transform.scale(dpadImage, [80, 80]);
        screen.blit(transformedImage, [152, 152]);
    elif DPad.DOWN['isPressed']:
        dpadImage = pygame.image.load("./img/buttons/dpad_down.png");
        transformedImage = pygame.transform.scale(dpadImage, [80, 80]);
        screen.blit(transformedImage, [152, 152]);
    if DPad.LEFT['isPressed']:
        dpadImage = pygame.image.load("./img/buttons/dpad_left.png");
        transformedImage = pygame.transform.scale(dpadImage, [80, 80]);
        screen.blit(transformedImage, [152, 152]);
    elif DPad.RIGHT['isPressed']:
        dpadImage = pygame.image.load("./img/buttons/dpad_right.png");
        transformedImage = pygame.transform.scale(dpadImage, [80, 80]);
        screen.blit(transformedImage, [152, 152]);

    #Triggers
    triggerSize = [80, 80];
    leftTriggerPos = [8, 14];
    if Trigger.LEFT['isPressed']:
        ltImage = pygame.image.load("./img/buttons/lt_pressed.png");
        transformedImage = pygame.transform.scale(ltImage, triggerSize);
        transformedImage = pygame.transform.rotate(transformedImage, 13);
        screen.blit(transformedImage, leftTriggerPos);
    else:
        ltImage = pygame.image.load("./img/buttons/lt.png");
        transformedImage = pygame.transform.scale(ltImage, triggerSize);
        transformedImage = pygame.transform.rotate(transformedImage, 13);
        screen.blit(transformedImage, leftTriggerPos);

    rightTriggerPos = [407, 14];
    if Trigger.RIGHT['isPressed']:
        rtImage = pygame.image.load("./img/buttons/rt_pressed.png");
        transformedImage = pygame.transform.scale(rtImage, triggerSize);
        transformedImage = pygame.transform.rotate(transformedImage, -13);
        screen.blit(transformedImage, rightTriggerPos);
    else:
        rtImage = pygame.image.load("./img/buttons/rt.png");
        transformedImage = pygame.transform.scale(rtImage, triggerSize);
        transformedImage = pygame.transform.rotate(transformedImage, -13);
        screen.blit(transformedImage, rightTriggerPos);

    # Left stick
    if LeftStick.UP['isPressed']:
        stickImage = pygame.image.load("./img/buttons/stick_up.png");
        transformedImage = pygame.transform.scale(stickImage, Buttons.LEFT_STICK['size']);
        screen.blit(transformedImage, Buttons.LEFT_STICK['position']);
    elif LeftStick.DOWN['isPressed']:
        stickImage = pygame.image.load("./img/buttons/stick_down.png");
        transformedImage = pygame.transform.scale(stickImage, Buttons.LEFT_STICK['size']);
        screen.blit(transformedImage, Buttons.LEFT_STICK['position']);

    if LeftStick.LEFT['isPressed']:
        stickImage = pygame.image.load("./img/buttons/stick_left.png");
        transformedImage = pygame.transform.scale(stickImage, Buttons.LEFT_STICK['size']);
        screen.blit(transformedImage, Buttons.LEFT_STICK['position']);
    elif LeftStick.RIGHT['isPressed']:
        stickImage = pygame.image.load("./img/buttons/stick_right.png");
        transformedImage = pygame.transform.scale(stickImage, Buttons.LEFT_STICK['size']);
        screen.blit(transformedImage, Buttons.LEFT_STICK['position']);

    #Right stick
    if RightStick.UP['isPressed']:
        stickImage = pygame.image.load("./img/buttons/stick_up.png");
        transformedImage = pygame.transform.scale(stickImage, Buttons.RIGHT_STICK['size']);
        screen.blit(transformedImage, Buttons.RIGHT_STICK['position']);
    elif RightStick.DOWN['isPressed']:
        stickImage = pygame.image.load("./img/buttons/stick_down.png");
        transformedImage = pygame.transform.scale(stickImage, Buttons.RIGHT_STICK['size']);
        screen.blit(transformedImage, Buttons.RIGHT_STICK['position']);

    if RightStick.LEFT['isPressed']:
        stickImage = pygame.image.load("./img/buttons/stick_left.png");
        transformedImage = pygame.transform.scale(stickImage, Buttons.RIGHT_STICK['size']);
        screen.blit(transformedImage, Buttons.RIGHT_STICK['position']);
    elif RightStick.RIGHT['isPressed']:
        stickImage = pygame.image.load("./img/buttons/stick_right.png");
        transformedImage = pygame.transform.scale(stickImage, Buttons.RIGHT_STICK['size']);
        screen.blit(transformedImage, Buttons.RIGHT_STICK['position']);

    pygame.display.flip();
    return;

def main():
    # Initialize
    pygame.init();
    pygame.joystick.init();
    screenSize = [512, 342];
    screen = pygame.display.set_mode(screenSize);
    pygame.display.set_caption('Controller View');

    # Detect joystick
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
        # Begin app
        joystick.init();
        runLoop = True;

        while runLoop:
            for event in pygame.event.get():

                # Exit window via X icon
                if event.type == pygame.QUIT:
                    runLoop = False;
                    break;

                # Button pressed
                if event.type == pygame.JOYBUTTONDOWN:
                    buttons = joystick.get_numbuttons();
                    for i in range(buttons):
                        button = joystick.get_button(i);
                        if button:
                            buttonName = resolveButtonIndex(i);
                            buttonConst = getattr(Buttons, buttonName);

                            if buttonConst:
                                buttonConst['isPressed'] = True;

                # Button released
                if event.type == pygame.JOYBUTTONUP:
                    buttons = joystick.get_numbuttons();
                    for i in range(buttons):
                        button = joystick.get_button(i);
                        if not button:
                            buttonName = resolveButtonIndex(i);
                            buttonConst = getattr(Buttons, buttonName);

                            if buttonConst:
                                if buttonConst['isPressed'] == True:
                                    buttonConst['isPressed'] = False;

                # D-Pad
                if event.type == pygame.JOYHATMOTION:
                    hats = joystick.get_numhats();
                    for i in range(hats):
                        hat = joystick.get_hat(i);

                        # Left/right
                        if hat[0] == 1:
                            DPad.LEFT['isPressed'] = False;
                            DPad.RIGHT['isPressed'] = True;
                        elif hat[0] == -1:
                            DPad.LEFT['isPressed'] = True;
                            DPad.RIGHT['isPressed'] = False;
                        else:
                            DPad.LEFT['isPressed'] = False;
                            DPad.RIGHT['isPressed'] = False;

                        # Up/down
                        if hat[1] == 1:
                            DPad.UP['isPressed'] = True;
                            DPad.DOWN['isPressed'] = False;
                        elif hat[1] == -1:
                            DPad.UP['isPressed'] = False;
                            DPad.DOWN['isPressed'] = True;
                        else:
                            DPad.UP['isPressed'] = False;
                            DPad.DOWN['isPressed'] = False;

                # Axes (left stick, right stick, triggers)
                if event.type == pygame.JOYAXISMOTION:
                    axes = joystick.get_numaxes();
                    for i in range(axes):
                        axis = joystick.get_axis(i);

                        if i == 0:
                            # Left stick - x axis
                            if axis <= -0.075:
                                LeftStick.LEFT['isPressed'] = True;
                                LeftStick.RIGHT['isPressed'] = False;
                            elif axis >= 0.075:
                                LeftStick.LEFT['isPressed'] = False;
                                LeftStick.RIGHT['isPressed'] = True;
                            else:
                                LeftStick.LEFT['isPressed'] = False;
                                LeftStick.RIGHT['isPressed'] = False;
                        elif i == 1:
                            # Left stick - y axis
                            if axis <= -0.075:
                                LeftStick.UP['isPressed'] = True;
                                LeftStick.DOWN['isPressed'] = False;
                            elif axis >= 0.075:
                                LeftStick.UP['isPressed'] = False;
                                LeftStick.DOWN['isPressed'] = True;
                            else:
                                LeftStick.UP['isPressed'] = False;
                                LeftStick.DOWN['isPressed'] = False;
                        elif i == 2:
                            # Triggers - Both triggers count as one axis
                            if axis <= -0.05:
                                Trigger.LEFT['isPressed'] = True;
                                Trigger.RIGHT['isPressed'] = False;
                            elif axis >= 0.05:
                                Trigger.LEFT['isPressed'] = False;
                                Trigger.RIGHT['isPressed'] = True;
                            else:
                                Trigger.LEFT['isPressed'] = False;
                                Trigger.RIGHT['isPressed'] = False;
                        elif i == 3:
                            # Right stick - y axis
                            if axis <= -0.075:
                                RightStick.UP['isPressed'] = True;
                                RightStick.DOWN['isPressed'] = False;
                            elif axis >= 0.075:
                                RightStick.UP['isPressed'] = False;
                                RightStick.DOWN['isPressed'] = True;
                            else:
                                RightStick.UP['isPressed'] = False;
                                RightStick.DOWN['isPressed'] = False;
                        elif i == 4:
                            # Right stick - x axis
                            if axis <= -0.075:
                                RightStick.LEFT['isPressed'] = True;
                                RightStick.RIGHT['isPressed'] = False;
                            elif axis >= 0.075:
                                RightStick.LEFT['isPressed'] = False;
                                RightStick.RIGHT['isPressed'] = True;
                            else:
                                RightStick.LEFT['isPressed'] = False;
                                RightStick.RIGHT['isPressed'] = False;

                draw(screen, bgImage);
    else:
        print('No controllers found. Please ensure your controller is plugged in and turned on.');

main();
