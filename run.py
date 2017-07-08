#
# Controller view by Brian Wilbur
# https://github.com/oblivion-hymns
#
import pygame;

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

def readInput(joystick):
    numButtons = joystick.get_numbuttons();

    for i in range(numButtons):
        button = joystick.get_button(i);
        if (button):
            print('Button ' + str(i) + ' pushed down');

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
