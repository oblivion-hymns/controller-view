# controller-view
Simple Python app that sticks an XBox Controller view on the screen. Useful for displaying on video game broadcasts.

## About
This was a quick one-off done for a friend so he could have a display for his video game streaming -- so, the code is pretty rudimentary and may be bug-prone -- plenty of magic numbers to be found.

## Dependencies
You need the following things to run this:
- python 2.7.x (https://www.python.org/downloads/) (Make sure you add Python to your PATH)
- pygame (https://www.pygame.org/news)

You can test your Python installation on Windows by opening a new Command Line window and typing `python -v`. If it says something like "Python is not executable" or "Python is not a valid command", you need to add the directory containing your Python executable to your system path. If you are using Linux, I assume you know how to install Python.

## To Use
There are no binaries or installers or anything right now, just raw code. In Windows, the easiest way to do this is:
1. Download the .zip file from the upper-right corner of this page
2. Extract its contents somewhere easy to remember (e.g. `C:\controllerview`)
3. On Windows, simply run `controller-view.pyw` from within the extracted folder by double-clicking it. If it doesn't work, make sure Python is in your system PATH (see Dependencies above)

## Future Plans
There are no plans for Playstation support, multiple controllers, profiles, etc. There are a few minor bugs and nice-to-haves that I will add if there is demand for them.

## Known bugs
- The app only picks up the first connected controller it finds. This is based on the way the system indexes them internally, so it could be based on a number of factors. If you absolutely must have several controllers plugged in, you might have to swap their USB ports around to get them to work.
- There is no constant controller detection; so if you start the app without a controller plugged in and turned on, it will not detect anything until you restart the app.

I will address these bugs, they aren't anything crazy
