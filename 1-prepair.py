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
    input(output.message("Press [ENTER] to setup the encryption "))
    output.null("truncate -s 2M header.img")
    output.null("cryptsetup luksFormat /dev/sda --header header.img")
    output.null("cryptsetup open --header header.img --type luks /dev/sda enc")
    output.null("pvcreate /dev/mapper/enc")
    output.null("vgcreate store /dev/mapper/enc")
    print(line)
    print(output.exclamation("Please specify the size of your logical volumes"))
    root = input(output.question("Set the size of your root volume [G] : "))
    swap = input(output.question("Set the size of your swap volume [G] : "))
    input(output.exclamation("Your home volume will use the rest of your space (+100%FREE) Press [ENTER] to continue "))
    output.null("lvcreate -L " + root + " store -n root")
    output.null("lvcreate -L " + swap + " store -n swap")
    output.null("lvcreate -l +100%FREE store -n home")

    print(output.exclamation("Logical volumes created."))

    print(line)

    input(output.message("Press [ENTER] to build the file system and mount the volumes."))

    output.null("mkfs.ext4 /dev/store/root")
    output.null("mkfs.ext4 /dev/store/home")
    output.null("mount /dev/store/root /mnt")
    output.null("mkdir /mnt/home")
    output.null("mount /dev/store/home /mnt/home")
    output.null("mkswap /dev/store/swap")
    output.null("swapon /dev/store/swap")
    output.null("mkfs.ext2 /dev/sdb1")
    output.null("mkdir /mnt/boot")
    output.null("mount /dev/sdb1 /mnt/boot")
    output.null("mv header.img /mnt/boot")

    print(line)

    input(output.message("Press [ENTER] to install the base system"))

    output.null("pacstrap -i /mnt base base-devel")
    output.null("genfstab -U -p /mnt >> /mnt/etc/fstab")

    print(line)

execute()
