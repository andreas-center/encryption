import sys
import os
import inc.functions
import inc.install.prepair
import inc.install.installation

printMessage = inc.functions.lines.message
printQuestion = inc.functions.lines.question
printExclamation = inc.functions.lines.exclamation

def run():
    disks = input(printExclamation("Don't forget to setup your disks! Is this done? [Y/N] : "))
    if disks == "N" or disks == "n":
        print(printMessage("Please go back and setup your disks before running this script. (Use cfdisk)\n\n"))
        sys.exit()
if disks == "Y" or disks == "y":
        print(printQuestion("What do you want to do?"))
        print(printMessage("1 : Prepair your system disk and USB stick"))
        print(printMessage("2 : Edit files and start configuring your system (not available yet)"))
        choice = input(printQuestion(": "))
        if choice == "1":
            inc.install.prepair.run.encryption()
            inc.install.prepair.run.filesystem()
            inc.install.prepair.run.baseSystem()
            sys.exit()
        if choice == "2":
            inc.install.installation.run()
            sys.exit()
        else:
            print(printMessage("I did not understand that. Try again!"))
            run()
    else:
        print(printMessage("I did not understand that. Try again!"))
        run()
run()
