# Auto py files for sys-botbase
Here is a compilation of Python files that use the sys-botbase to automate actions on the switch.

## Set up
This relies on [sys-botbase](https://github.com/olliz0r/sys-botbase) to automate the actions on your switch.

You will also need [Python](https://www.python.org/downloads/) so that you can run the .py files,

After these two things are installed, then edit the config.py file to configure your switch's IP address and specify file locations for certain Python scripts. Make sure your switch and pc are conneced to the same WiFi otherwise the scripts will not work.

Then you can run any of these files to automate actions on your switch! Just download the zip, extract, and double click a py file.

# Current Auto Scripts

## Press A
Auto presses A until you close the script. Useful for long dialogue sections without needing input.

## Single day skip from game
This will skip one day forward. Run it while you are in game. Make sure you already have "Synchronize Clock via Internet" turned off! This script also assumes that you are not on the last day of the month.

## Get Dodo Code
In Animal Crossing, walk up to Orville and then start the script. It will automatically go through the dialogue to get a Dodo code. It will leave the Dodo Code on screen.

## Inject Pokemon
In Pokemon Sword/Shield, this will inject any Pokemon exported from PKHex as an ek8 file. Make sure you specified the path to this file in the config file, and also renamed the ek8 file to "toInject.ek8". The Pokemon will be put in your 1st box in the 1st position. It WILL overwite any Pokemon that is currently in that position, so use this wisely.

## Exctract Pokemon
In Pokemon Sword/Shield, this will read the Pokemon in your 1st box in the 1st position. It will then create an ek8 file in the path you specified in the config file that is readable by PKHex. This will not remove the Pokemon from your box.

## Skip to shiny frame
In Pokemon Sword/Shield, this will skip the amount of frames you specified in the config file. It will stop 4 days before the shiny frame. This assumes you have done the [Date-Spam Exploit](https://www.youtube.com/watch?v=CUTpProiDwU). To make sure this works correctly, you need to do the following:
-Turn off "Synchronize Clock via Internet"
-Change the date to January 1st 2020 at 1:00 am
-Make sure your cursor is on "Date and Time"
-Make sure that when you select "Date and Time" the cursor is on "OK"
With all of these set up, it will automatically skip the correct amount offrames for you. (It also takes leap year into account... you're welcome)

# Notes
You are free to use and modify these as you wish. I am not liable for any modifications that you make to your switch that corrupt or damage it. I will be adding more as I think of them. I'd love any advice and critiques that you with to give.
