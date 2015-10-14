import sys
import os
import inc.functions

printMessage = inc.functions.lines.message
printQuestion = inc.functions.lines.question
printExclamation = inc.functions.lines.exclamation

def run():
    os.system("cp files/locale.gen /etc/locale.gen")
    os.system("locale-gen")
    os.system("echo LANG=sv_SE.UTF-8 > /etc/locale.conf")
    os.system("export LANG=sv_SE.UTF-8")
    os.system("cp files/vconsole.conf /etc/vconsole.conf")
    os.system("ln -s /usr/share/zoneinfo/Europe/Stockholm /etc/localtime")
    os.system("hwclock --systohc --utc")
    hostname = input(printQuestion("Enter your hostname : "))
    os.system("echo " + hostname + " > /etc/hostname")
    os.system("cp /lib/initcpio/hooks/encrypt{,2}")
    os.system("cp /usr/lib/initcpio/install/encrypt{,2}")
    os.system("cp files/encrypt2 /lib/initcpio/hooks/encrypt2")
    os.system("cp files/mkinitcpio.conf /etc/mkinitcpio.conf")
    os.system("pacman -S grub")
    os.system("cp files/grub /etc/default/grub")
    disk2 = input(printQuestion("Were is your USB stick located? (/dev/sdx) : "))
    os.system("grub-install --recheck /dev/sdb")
    os.system("grub-mkconfig -o /boot/grub/grub.cfg")
    os.system("mkinitcpio -p linux")
    print(printMessage("Installation is now complete! You can now install all the packages you need.\n"))
