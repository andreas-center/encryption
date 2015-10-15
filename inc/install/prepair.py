import sys
import os
import inc.functions

printMessage = inc.functions.lines.message
printQuestion = inc.functions.lines.question
printExclamation = inc.functions.lines.exclamation

class Run:
    def encryption(self):
        os.system("clear")
        input(printMessage("Press [ENTER] to setup the encryption "))
        print(printMessage("Creating 'header.img'"))
        os.system('truncate -s 2M header.img')
        self.disk1 = input(printQuestion("Specify your system disk. (/dev/sdx) : "))
        print(printMessage("Using " + self.disk1 + " as system disk."))
        self.disk2 = input(printQuestion("Specify your USB stick. (/dev/sdx) : "))
        print(printMessage("Using " + self.disk2 + " as USB stick."))
        print(printMessage("Running luksFormat with 'header.img'"))
        os.system('cryptsetup luksFormat ' + self.disk1 + ' --header header.img')
        print(printMessage("Unlocking '/dev/sda'"))
        os.system('cryptsetup open --header header.img --type luks ' + self.disk1 + ' enc')
        os.system('pvcreate /dev/mapper/enc > /dev/null')
        os.system('vgcreate store /dev/mapper/enc > /dev/null')
        print(printMessage("Please specify the size of your logical volumes"))
        self.root = input(printQuestion("Set the size of your root volume [G] : "))
        self.swap = input(printQuestion("Set the size of your swap volume [G] : "))
        os.system("lvcreate -L " + self.root + " store -n root > /dev/null")
        os.system("lvcreate -L " + self.swap + " store -n swap > /dev/null")
        print(printExclamation("Your home volume will use all remaining space [+100%FREE]"))
        os.system("lvcreate -l +100%FREE store -n home > /dev/null")
        print(printExclamation("Logical volumes created!"))
    def filesystem(self):
        os.system("clear")
        input(printMessage("Press [ENTER] to setup the filesystem "))
        print(printMessage("Setting up '/dev/store/root'"))
        os.system("mkfs.ext4 /dev/store/root > /dev/null")
        print(printMessage("Setting up '/dev/store/home'"))
        os.system("mkfs.ext4 /dev/store/home > /dev/null")
        print(printMessage("Mounting '/dev/store/root' in '/mnt'"))
        os.system("mount /dev/store/root /mnt > /dev/null")
        print(printMessage("Creating directory '/mnt/home'"))
        os.system("mkdir /mnt/home > /dev/null")
        print(printMessage("Mounting '/dev/store/home' in '/mnt/home'"))
        os.system("mount /dev/store/home /mnt/home > /dev/null")
        print(printMessage("Creating swap at '/dev/store/swap'"))
        os.system("mkswap /dev/store/swap > /dev/null")
        print(printMessage("Enabling swap at '/dev/store/swap'"))
        os.system("swapon /dev/store/swap > /dev/null")
        self.disk2 = input(printQuestion("Specify your USB stick. (/dev/sdx) : "))
        print(printMessage("Setting up '" + self.disk2 + "'"))
        os.system("mkfs.ext2 /dev/sdb1 > /dev/null")
        print(printMessage("Creating directory '/mnt/boot'"))
        os.system("mkdir /mnt/boot > /dev/null")
        print(printMessage("Mounting '"+self.disk2+"' in '/mnt/boot'"))
        os.system("mount /dev/sdb1 /mnt/boot > /dev/null")
        print(printMessage("Moving 'header.img' to '/mnt/boot'"))
        os.system("mv header.img /mnt/boot > /dev/null")
    def baseSystem(self):
        os.system("clear")
        input(printMessage("Press [ENTER] to setup the base system "))
        print(printMessage("Running bacstrap and installing base / base-devel"))
        os.system("pacstrap -i /mnt base base-devel > /dev/null")
        print(printMessage("Generating fstab"))
        os.system("genfstab -U -p /mnt >> /mnt/etc/fstab > /dev/null")
        print(printMessage("Moving folder 'files' to '/mnt'"))
        os.system("cp -r files /mnt/ > /dev/null")
        input(printMessage("You've now installed the base system! Press [enter] to continue "))
        print(printMessage("Running 'arch-chroot'"))
        os.system("arch-chroot /mnt /bin/bash > /dev/null")


run = Run()
