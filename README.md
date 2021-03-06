# Arch Linux installation with remote GRUB2 / LUKS header

(This walkthrough was mainly created for myself but i thought i could share it publicly)

## ABOUT
With this documentation you'll install arch linux with a two-way authentication. You'll be abke to login with a password and a usb stick. GRUB and the LUKS header will be stored on the USB stick which makes it impossible to boot the system as the luks header is unique to your system disk.

## Howto
use cfdisk to setup your disks. Your system disk should use all of your space and also set to "Linux LVM". The USB device should have the boot flag set to on. Continue from the arch-install file. All documentation is available on the arch wik.

## Links
* [Arch wiki - Encrypt an entinre system](https://wiki.archlinux.org/index.php/Dm-crypt/Encrypting_an_entire_system#Plain_dm-crypt)
* [Arch wiki - Remote LUKS header](https://wiki.archlinux.org/index.php/Dm-crypt/Specialties#Encrypted_system_using_a_remote_LUKS_header)

![Image](http://pngimg.com/uploads/usb/usb_PNG8883.png)
