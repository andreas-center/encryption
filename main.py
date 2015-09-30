import sys
import inc.color
from inc.variables import *
import inc.installation.prepair
import inc.installation.install

print(print_line)
print(print_logo)
print(print_line)

def intro():
    print(print_question("What do you want to do?\n"))
    print(print_green("1 : Prepair your system disk and USB stick\n".rjust(46)))
    print("2 : Edit files and start configuring your system\n".rjust(52))
    print("3 : Install packages from your self-made list\n".rjust(49))
    install = input(print_white(" > "))
    if install == "1":
# ----------------------------------------------------------------------------------------------------
        inc.installation.prepair.run()
        sys.exit()
# ----------------------------------------------------------------------------------------------------
    if install == "2":
# ----------------------------------------------------------------------------------------------------
        inc.installation.install.run()
        sys.exit()
# ----------------------------------------------------------------------------------------------------
    if install == "3":
# ----------------------------------------------------------------------------------------------------
        print("3")
        sys.exit()
# ----------------------------------------------------------------------------------------------------
    else:
# ----------------------------------------------------------------------------------------------------
        print("error")
        sys.exit()
# ----------------------------------------------------------------------------------------------------
intro()
