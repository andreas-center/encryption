import sys
import os
import inc.functions

printMessage = inc.functions.lines.message
printQuestion = inc.functions.lines.question
printExclamation = inc.functions.lines.exclamation

def run():
    os.system("clear")
    input(printMessage("Press [ENTER] to setup the encryption "))
    print(printMessage("Creating 'header.img'"))
    os.system('truncate -s 2M header.img > /dev/null')
    disk1 = input(printQuestion("Specify your system disk. (/dev/sdx) : "))
    print(printMessage("Using " + disk1 + " as system disk."))
    disk2 = input(printQuestion("Specify your USB stick. (/dev/sdx) : "))
    print(printMessage("Using " + disk2 + " as USB stick."))
    print(printMessage("Running luksFormat with 'header.img'"))
    os.system('cryptsetup luksFormat " + disk1 + " --header header.img > /dev/null')
    print(printMessage("Unlocking '/dev/sda'"))
    os.system('cryptsetup open --header header.img --type luks " + disk1 + " enc > /dev/null')
    os.system('pvcreate /dev/mapper/enc > /dev/null')
    os.system('vgcreate store /dev/mapper/enc > /dev/null')
    print(printMessage("Please specify the size of your logical volumes"))
    root = input(printQuestion("Set the size of your root volume [G] : "))
    root = input(printQuestion("Set the size of your swap volume [G] : "))
    os.system("lvcreate -L " + root + " store -n root > /dev/null")
    os.system("lvcreate -L " + swap + " store -n swap > /dev/null")
    print(printExclamation("Your home volume will use all remaining space [+100%FREE]"))
    os.system("lvcreate -l +100%FREE store -n home > /dev/null")
    print(printExclamation("Logical volumes created!"))

    input(printMessage("Press [ENTER] to build the file system and mount the volumes "))

    os.system("mkfs.ext4 /dev/store/root > /dev/null")
    os.system("mkfs.ext4 /dev/store/home > /dev/null")
    os.system("mount /dev/store/root /mnt > /dev/null")
    os.system("mkdir /mnt/home > /dev/null")
    os.sustem("mount /dev/store/home /mnt/home > /dev/null")
    os.system("mkswap /dev/store/swap > /dev/null")
    os.system("swapon /dev/store/swap > /dev/null")
    os.system("mkfs.ext2 /dev/sdb1 > /den/null")
    os.system("mkdir /mnt/boot > /dev/null")
    os.system("mount /dev/sdb1 /mnt/boot > /dev/null")
    os.system("mv header.img /mnt/boot > /dev/null")

    input(printMessage("Press [ENTER] to install the base system "))
    os.system("pacstrap -i /mnt base base-devel")
    os.system("clear")
    os.system("genfstab -U -p /mnt >> /mnt/etc/fstab > /dev/null")
    os.system("mkdir install")
    os.system("cp -r * install/")
    os.system("cp -r install /mnt/")
    input(printMessage("You have now prepair your arch linux installation. Press [enter] to chroot "))
    print(printMessage("Running arch-chroot"))
    os.system("arch-chroot /mnt /bin/bash")
