# Arch Linux installation with remote GRUB2 / LUKS header

## ABOUT
With these scripts you'll be able to install arch linux with a two-way authentication. You'll be abke to login with a password and a usb stick. GRUB and the LUKS header will be stored on the USB stick which makes it impossible to boot the system as the luks header is unique to your system disk.

This is a dirty build that I threw together for myself. It requires that your systemdisk is /dev/sda and your empty USB disk is at /dev/sda.(i'll fix that later). You will also need to prepair your disks before you run the script (use cfdisk). Your systemdisk should be set typ use 'linux LVM' and your usb disk should be set to 'bootable'.

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/RffpFvku2SQ/0.jpg)](http://www.youtube.com/watch?v=RffpFvku2SQ)
