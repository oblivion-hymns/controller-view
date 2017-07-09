# controller-view
Simple Python app that sticks an XBox Controller view on the screen.

## Dependencies
You need the following things to run this:
- python 2.7.x (https://www.python.org/downloads/) (Make sure you add Python to your PATH)
- pygame (https://www.pygame.org/news)

You can test your Python installation on Windows by opening a new Command Line window and typing `python -v`. If it says something like "Python is not executable" or "Python is not a valid command", you need to add the directory containing your Python executable to your system path. If you are using Linux, I assume you know how to install Python.

## To Use
There are no binaries or installers or anything right now, just raw code. So, in Windows:

1. Download the .zip file from the upper-right corner of this page.
2. Extract its contents somewhere easy to remember (e.g. `C:\controllerview`)
3. Open up a command prompt window. One way to do this is by holding the Windows key and pressing R to open the "Run" dialog, then type `cmd` into the Run dialog and press `Enter`.
4. In the command prompt window, type `cd C:\controllerview`, where `C:\controllerview` is the path to the folder you extracted that contains `run.py`. Then press `Enter` to navigate to that directory.
5. Type `python run.py` and hit Enter. It should open and run. You're good to go!

## Future Plans
There are no plans for Playstation support, multiple controllers, profiles, etc.

## Known bugs
- The app only picks up the first connected controller it finds.
- There is no constant controller detection; so if you start the app without a controller plugged in and turned on, it will not detect anything until you restart the app.
