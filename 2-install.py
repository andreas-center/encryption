import sys
import os

class Output:
    def message(self,message):
        return "\n [*] - ".rjust(10) + message.ljust(10)
    def question(self,question):
        return "\n [?] - ".rjust(10) + question.ljust(10)
    def exclamation(self,exclamation):
        return "\n [!] - ".rjust(10) + exclamation.ljust(10)
    def null(self,osSystem):
        null = " > /dev/null"
        os.system(osSystem + null)
output = Output()

global line
line = "\n--------------------------------------------------------"

def execute():
    print(line)
    print(output.exclamation("Attention! This script should be run after you've chrooted into your new system (arch-chroot /mnt /bin/bash)"))
    input(output.message("Press [ENTER] to install your system."))
    print(output.message("Moving file 'locale.gen' to '/etc/locale.gen'")
    output.null("cp files/locale.gen /etc/locale.gen")
    print(output.message("Running 'locale-gen'")
    output.null("locale-gen")
    print(output.message("Adding 'sv_SE.UTF-8' to '/etc/locale.conf'")
    output.null("echo LANG=sv_SE.UTF-8 > /etc/locale.conf")
    print(output.message("Running 'Export LANG=sv_SE.UTF-8'")
    output.null("export LANG=sv_SE.UTF-8")
    print(output.message("Moving file 'vconsole.conf' to '/etc/vconsole'")
    output.null("cp files/vconsole.conf /etc/vconsole.conf")
    print(output.message("Setting zone 'Europe/Stockholm' in '/etc/localtime'")
    output.null("ln -s /usr/share/zoneinfo/Europe/Stockholm /etc/localtime")
    print(output.message("Setting hwclock")
    output.null("hwclock --systohc --utc")
    hostname = input(output.question("Enter your hostname: "))
    output.null("echo " + hostname + " > /etc/hostname")
    print(output.message("Making copies of '/hooks/encrypt' and 'install/encrypt'")
    output.null("cp /lib/initcpio/hooks/encrypt{,2}")
    output.null("cp /usr/lib/initcpio/install/encrypt{,2}")
    print(output.message("moving file 'encrypt2' to '/lib/initcpio/hooks/encrypt2'")
    output.null("cp files/encrypt2 /lib/initcpio/hooks/encrypt2")
    output.null("Moving file 'mkinitcpio.conf' to '/etc/mkinitcpio.conf'")
    output.null("cp files/mkinitcpio.conf /etc/mkinitcpio.conf")
    print(output.message("Running 'pacman -S grub'")
    output.null("pacman -S grub")
    print(output.message("Moving file 'grub' to '/etc/default/grub'")
    output.null("cp files/grub /etc/default/grub")
    print(output.message("Running 'grub-install --recheck /dev/sdb'")
    output.null("grub-install --recheck /dev/sdb")
    print(output.message("grub-mkconfig -o /boot/grub/grub.cfg")
    output.null("grub-mkconfig -o /boot/grub/grub.cfg")
    print(output.message("Runnimg mkinitcpio")
    output.null("mkinitcpio -p linux")
    print(line)

execute()
