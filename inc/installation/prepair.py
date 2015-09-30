import os
import sys
from inc.variables import *

def run():
    print(print_line)
    input(print_message(print_yellow("Press [ENTER] to setup the encryption ")))

    os.system('truncate -s 2M header.img')
    os.system('cryptsetup luksFormat /dev/sda --header header.img')
    os.system('cryptsetup open --header header.img --type luks /dev/sda enc')
    execute('pvcreate /dev/mapper/enc')
    execute('vgcreate store /dev/mapper/enc')
    print(print_line)  
    print(print_exclamation("Please specify the size of your logical volumes"))
    root = input(print_question(print_yellow("Set the size of your root volume [G] : ")))
    swap = input(print_question(print_yellow("Set the size of your swap volume [G] : ")))
    execute("lvcreate -L " + root + " store -n root")
    execute("lvcreate -L " + swap + " store -n swap")
    print(print_exclamation("Your home volume will use all remaining space [+100%FREE]"))
    execute("lvcreate -l +100%FREE store -n home")
    print(print_exclamation("Logical volumes created!"))
    print(print_line)  
                                   
    input(print_message(print_yellow("Press [ENTER] to build the file system and mount the volumes ")))
    execute("mkfs.ext4 /dev/store/root")
    execute("mkfs.ext4 /dev/store/home")
    execute("mount /dev/store/root /mnt")
    execute("mkdir /mnt/home")
    execute("mount /dev/store/home /mnt/home")
    execute("mkswap /dev/store/swap")
    execute("swapon /dev/store/swap")
    execute("mkfs.ext2 /dev/sdb1")
    execute("mkdir /mnt/boot")
    execute("mount /dev/sdb1 /mnt/boot")
    execute("mv header.img /mnt/boot")
    print(print_line)  
    
    input(print_message(print_yellow("Press [ENTER] to install the base system ")))
    os.system("pacstrap -i /mnt base base-devel")
    execute("genfstab -U -p /mnt >> /mnt/etc/fstab")
    print(print_line)
    print(print_message(print_green("You have now prepair your arch linux installation. Please moves the 'install' folder to '/mnt' and continue with step two (2)")))
    
    print(print_line)
