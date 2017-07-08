# Controller view by Brian Wilbur
#
import pygame;

pygame.joystick.init();

joystick = None;
joystickIndex = -1;
joystickCount = pygame.joystick.get_count();
for x in range(joystickCount):
    if pygame.joystick.Joystick(x):
        joystick = pygame.joystick.Joystick(x);
        joystickIndex = x;

if joystickIndex > -1:
    print('Controller found in slot ' + joystickIndex);
else:
    print('No controllers found. Please ensure your controller is plugged in and turned on.');
