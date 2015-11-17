# Arch Linux installation with remote GRUB2 / LUKS header

## **1. Introduction:**

(This walkthrough was mainly created for myself but i thought i could share it publicly)
This guide is stripped down from the Arch-Linux Wiki page and will go through the steps to encrypt 100% of your system disk and place GRUB and the LUKS header on a remote disk. With this solution you will achieve a 2 way authentication to access your computer. If the remote disk is not connected to your USB port the bios will prompt you with a message saying that no bootable device was found. This solution is perfect for Laptops.

## **2. What you will need:**

Arch Linux USB / CD (Release used: 2015.04.01)

System disk

Empty USB stick

I did **NOT** use UEFI for this setup

## **3. Prepair your disks:**
* Example tool: **cfdisk**
* **/dev/sda** will represent the system disk
 * I used all space available. Set it to '**Linux LVM**'
* **/dev/sdb** will represent the remote USB stick
 * I used all space available. Set this one to use the '**boot**' flag

`truncate -s 2M header.img`

`cryptsetup luksFormat /dev/sda --header header.img`

`cryptsetup open --header header.img --type luks /dev/sda enc`

`pvcreate /dev/mapper/enc`

`vgcreate store /dev/mapper/enc`

`lvcreate -L 20G store -n root`

`lvcreate -L 4G store -n swap`

`lvcreate -l +100%FREE store -n home`

`mkfs.ext4 /dev/store/root`

`mkfs.ext4 /dev/store/home`

`mount /dev/store/root /mnt`

`mkdir /mnt/home`

`mount /dev/store/home /mnt/home`

`mkswap /dev/store/swap`

`swapon /dev/store/swap`

`mkfs.ext2 /dev/sdb1`

`mkdir /mnt/boot`

`mount /dev/sdb1 /mnt/boot`

`mv header.img /mnt/boot`

truncate -s 2M header.img && cryptsetup luksFormat /dev/sda --header header.img && cryptsetup open --header header.img --type luks /dev/sda enc && pvcreate /dev/mapper/enc && vgcreate store /dev/mapper/enc && lvcreate -L 20G store -n root && lvcreate -L 4G store -n swap && lvcreate -l +100%FREE store -n home && mkfs.ext4 /dev/store/root && mkfs.ext4 /dev/store/home && mount /dev/store/root /mnt && mkdir /mnt/home && mount /dev/store/home /mnt/home && mkswap /dev/store/swap && swapon /dev/store/swap && mkfs.ext2 /dev/sdb1 && mkdir /mnt/boot && mount /dev/sdb1 /mnt/boot && mv header.img /mnt/boot

## **4. Install base system**

`pacstrap -i /mnt base base-devel`

`genfstab -U -p /mnt >> /mnt/etc/fstab`

`arch-chroot /mnt /bin/bash`

## **5. Set Locale / fonts / time zone / hostname**

**Unmark the one you want to use. I am using swedish**

`nano /etc/locale.gen`

**Generate**

`locale-gen`

**Again, I'm using swedish**

`echo LANG=sv_SE.UTF-8 > /etc/locale.conf`

`export LANG=sv_SE.UTF-8`

`nano /etc/vconsole.conf`

```
KEYMAP=sv-latin1

FONT=lat9w-16
```

`ln -s /usr/share/zoneinfo/Zone/SubZone /etc/localtime`

_Example : /usr/share/zoneinfo/Europe/Stockholm_

`hwclock --systohc --utc`

`echo [hostname here] > /etc/hostname`

## **6. Now we are going to edit some hooks**

### Make a copy of these files

`cp /lib/initcpio/hooks/encrypt{,2}`

`cp /usr/lib/initcpio/install/encrypt{,2}`

### Edit ../hooks/encrypt2

`nano /lib/initcpio/hooks/encrypt2`

#### If using nano, Press ctrl+w to search and locate:

`warn_deprecated() {`

#### .. and make it look like this:

```
warn_deprecated() {
    echo "The syntax 'root=${root}' where '${root}' is an encrypted volume is deprecated"
    echo "Use 'cryptdevice=${root}:root root=/dev/mapper/root' instead."
}

local headerFlag=false
for cryptopt in ${cryptoptions//,/ }; do
    case ${cryptopt} in
        allow-discards)
            cryptargs="${cryptargs} --allow-discards"
            ;;
        header)
            cryptargs="${cryptargs} --header /boot/header.img"
            headerFlag=true
            ;;
        *)
            echo "Encryption option '${cryptopt}' not known, ignoring." >&2
            ;;
    esac
done

if resolved=$(resolve_device "${cryptdev}" ${rootdelay}); then
    if $headerFlag || cryptsetup isLuks ${resolved} >/dev/null 2>&1; then
        [ ${DEPRECATED_CRYPT} -eq 1 ] && warn_deprecated
        dopassphrase=1
```

### Edit mkinitcpio.conf

`nano /etc/mkinitcpio.conf`

```
MODULES="loop"

FILES="/boot/header.img"

HOOKS="... encrypt2 lvm2 ... filesystems ..."
```

**For some reason i had to move the "_block_" hook between base and udev.**

Otherwise i could not unlock the partition.

## **7. Setup grub and fstab**

`pacman -S grub`

`nano /etc/default/grub`

`GRUB_CMDLINE_LINUX="cryptdevice=/dev/sda:enc:header"`

### Install grub to your USB stick

`grub-install --recheck /dev/sdb`

### Edit fstab

`nano /etc/fstab`

#### Locate your USB device and add these options:

`/dev/sdb /boot ext2 noauto,rw,noatime 0 2`

#### Run grub-mkconfig & mkinitcpio

`grub-mkconfig -o /boot/grub/grub.cfg`

`mkinitcpio -p linux`

## **8. Add user and unmount devices.**
Here you can add your users and make other changes if you want. When you're done type **exit** , then **umount -R /mnt** and finaly reboot.
