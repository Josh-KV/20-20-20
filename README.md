20-20-20 Vision Health
---
Do you ever need a reminder to look up from your screen? Perhaps an "eye break" every 20 minutes?
20-20-20 is a simple python application which opens a fullscreen window for 20 seconds at 20 minute intervals. During the 20 seconds, you are supposed to blink often and look at an object 20 feet away as per the [20-20-20 rule](https://en.wikipedia.org/wiki/Computer_vision_syndrome#:~:text=One%20of%20the%20catch%20phrases,from%20the%20optometrist%20and%20ophthalmologist.).

README Contents:
- [Details](#Details)
- [Improvements](#Improvements)
- [Installation and Use](#Installation-and-Use)

# Details
---
This application opens a window on launch, which displays an animation for 20 seconds, and then minimizes for 20 minutes. After 20 minutes the window opens again, and the whole cycle reapeats until the app is closed.

The window that opens is forced to jump to the front by enabling the window attribute `-topmost`. It also

If the app is left running for roughly 24 hours, it will self-terminate.

# Improvements
---
✔ Package for Mac
- Package for windows
- Correct app behavior to switch back to previusly active Mac OS desktop after minimizing. (Currently, the app changes the active desktop to the one it was launched in, and switches users to this desktop during each 20 second break, but does not switch back if the user had been using another desktop)
- Improve efficiancy and track resource consumption to ensure the app requires the minimum resources to run continuously and smoothly
- Add menu GUI with config options like time interval, animation colors, welcome message and information. This would replace the initial 20 second break which begins on launch
- Add sound option for starting and ending breaks
  
# Installation and Use
---
(CURRENTLY THE PACKAGED APP SEEMS TO ONLY RUN WHEN THE DMG IS PACKAGED ON THE SAME MACHINE, SO THE BELOW INSTRUCTIONS MAY NOT WORK. FOR NOW THE ONLY WAY I'VE FOUND TO INSTALL PACKAGE ON OTHER MACHINES IS TO CLONE THE REPO AND RUN THE BUILD SCRIPT AFTER INSTALLING THE PYINSTALLER AND CREATE-DMG UTILITIES)
- Download and open [20-20-20.dmg](dist/20-20-20.dmg)
- Copy the 20-20-20.app to your applications folder when prompted
- Choose to 'Keep in dock' if desired
- Click on the app icon from your dock and you are done, spend these first 20 seconds taking deep breaths and thinking about the Universe
