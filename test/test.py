import os
import sys
class Output:
    def message(self,x):
        return "\n[ * ] %s \n" % x
    def question(self,x):
        return "\n[ ? ] %s \n" % x
    def explamation(self,x):
        return "\n[ ! ] %s \n" % x
class Commands:
    def pacman(self,x):
        return "sudo pacman -Syy %s --noconfirm > log" % x
commands = Commands()
output = Output()
package_xorg = [
    'xorg-server ',
    'xorg-xinit ',
    'xorg-drivers ',
    'xorg-server-utils '
    ]
setup_xorg = [
    'cp /etc/X11/xinit/xinitrc ~/.xinitrc'
    ]
package_bumblebee = [
    'bumblebee',
    'mesa',
    'xf86-video-intel',
    'nvidia',
    'lib32-virtualgl',
    'lib32-nvidia-utils',
    'lib32-mesa-libgl'
    ]
setup_bumblebee = [
    'gpasswd -a master bumblebee',
    'systemctl enable bumblebeed'
    ]
package_enviorment = [
    'i3',
    'xterm',
    'dmenu',
    'luakit',
    'firefox',
    'compton'
    ]

os.system("clear")
input(output.message("Press [ENTER] to install packages"))
print(output.message("Installig xorg"))
''' ---------------------------------------------- '''
x = 0
while (x <= len(package_xorg) - 1):
    os.system(commands.pacman(package_xorg[x]))
    x = x + 1
os.system(commands.pacman(setup_xorg[0]))
os.system("clear")
print(output.explamation("Xorg installed"))
''' ---------------------------------------------- '''
x = 0
while (x <= len(package_bumblebee) - 1):
    os.system(commands.pacman(package_bumblebee[x]))
''' ---------------------------------------------- '''

