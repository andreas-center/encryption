import sys
import os
import time

class Output:
	def question(self,question):
		return "\n[?] - ".rjust(10) + question.ljust(10)
	def exclamation(self,exclamation):
		return "\n[!] - ".rjust(10) + exclamation.ljust(10)
output = Output()

def intro():
	os.system("clear")
	input(output.exclamation("This script will create, encrypt and mount your systemdisk. It will also prepair the USB stick.  Press [ENTER] to continue."))

	answer = input(output.question("Are you sure you want to continue? [Y/N] "))

	if answer == "Y":
		print(output.exclamation("You've selected 'YES'"))
		execute()
	if answer == "N":
		print(output.exclamation("You've Selected 'NO'. Exiting.."))
		sys.exit()
	else:
		print(output.exclamation("Please answer with 'yes' or 'no' > [Y/N] "))
		print(output.exclamation("Restarting in [5] ... "))
		time.sleep(5)
		intro()
def execute():
    print(output.exclamation("Before we begin you'll have to specify the size of your root,swap and home directory."))
    print(output.exclamation("Specify in gigabytes [G]"))

    rootSize = input(output.question("Set the size for root : "))
    swapSize = input(output.question("Set the size for swap : "))
    print(output.question("Your home partition will use 100% of the free space (+100%FREE)"))
    input(output.exclamation("Press [ENTER] to continue."))

    print(output.exclamation("Creating header"))
    os.system('truncate -s 2M header.img')
    time.sleep(1) 

    print(output.exclamation("Running cryptsetup"))
    os.system('cryptsetup luksFormat /dev/sda --header header.img')
    time.sleep(1)

    print(output.exclamation("Opening cryptsetup"))
    os.system('cryptsetup open --header header.img --type luks /dev/sda enc')
    time.sleep(1)

    os.system('pvcreate /dev/mapper/enc')
    time.sleep(1)
	
    os.system('vgcreate store /dev/mapper/enc')
    time.sleep(1)

    os.system('lvcreate -L ' +rootSize + '  store -n root')
    time.sleep(1)

    os.system('lvcreate -L ' + swapSize + ' store -n swap')
    time.sleep(1)

    os.system('lvcreate -l +100%FREE store -n home')
    time.sleep(1)

    os.system('mkfs.ext4 /dev/store/root')
    time.sleep(1)

    os.system('mkfs.ext4 /dev/store/home')
    time.sleep(1)

    os.system('mount /dev/store/root /mnt')
    time.sleep(1)

    os.system('mkdir /mnt/home')
    time.sleep(1)

    os.system('mount /dev/store/home /mnt/home')
    time.sleep(1)

    os.system('mkswap /dev/store/swap')
    time.sleep(1)

    os.system('swapon /dev/store/swap')
    time.sleep(1)

    os.system('mkfs.ext2 /dev/sdb1')
    time.sleep(1)

    os.system('mkdir /mnt/boot')
    time.sleep(1)

    os.system('mount /dev/sdb1 /mnt/boot')
    time.sleep(1)

    os.system('mv header.img /mnt/boot')
    time.sleep(1)

    os.system('pacstrap -i /mnt base base-devel')
    time.sleep(1)

    os.system('genfstab -U -p /mnt >> /mnt/etc/fstab')
    time.sleep(1)
	
    print(output.exclamation("You will now be chrooted into your new system."))
    os.system('arch-chroot /mnt /bin/bash')
    time.sleep(1)
    sys.exit()
intro()
