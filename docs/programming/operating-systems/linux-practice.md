#### Question 1

??? question inline "Click for Answer"
    
    - Ethernet
    - USB

In System Architechture, which of the following are hotplug devices?

- Hard disks
- CPU
- Ethernet
- USB

#### Question 2

??? question inline "Click for Answer"
    RAM

Which of the following is not a mass storage device?

- optical disc 
- hard disk 
- magnetic tape 
- RAM

#### Question 3

??? question inline "Click for Answer"
    Upstart

Which of the following is not a Linux bootloader program?

- ELILO
- GRUB 
- LILO 
- Upstart 

#### Question 4

You want to obtain information about the device drivers that are loaded on your Linux system. 
??? question inline "Click for Answer"

    `lsmod`

Which command would you recommend to use in this scenario?

- dmesg 
- lsmod 
- sysVinit 
- lspci 
- system

#### Question 5

You are a system Linux administrator. A user initiated process freezes. You are not able to locate the offending process as it has several other multiple child processes.

??? question inline "Click for Answer"
    You need to issue the `pstree -p|less` command to locate the process id of the parent process and then issue the `kill` command with no option.

- How will you locate and close the offending program without searching and terminating the list of child processes individually?
- You need to issue the pstree -p|less command to locate the process id of the parent process and then issue the kill command with no option. 
- You need to issue the ps |less command to locate the process id of the parent process and then issue the kill command with no option.
- You need to issue the ps -aux less command to locate the process id of the parent process and then issue the kill command with no option. 
- You need to issue the pstree | less command to locate the process id of the parent process and then issue the kill command with no option.

#### Question 6

You have issued a delayed shutdown. However, you want to cancel the pending shutdown. Which command you need to issue in this scenario?

??? question inline "Click for Answer"
    `shutdown -c`

- shutdown -r 
- shutdown -h 
- shutdown -c 
- shutdown 5 

#### Question 7

Which of the following commands is used to determine how much swap space is being used on each swap device?

??? question inline "Click for Answer"
    `swapon -s`

- swapon -e
- Swapon
- swapon -s
- swapon -a

#### Question 8

Which of the following files contains a list of operating systems and the commands used to define the global preferences for the GRUB menu interface?

??? question inline "Click for Answer"
    `/boot/grub/grub.conf`

- `/boot/grub/grub.cfg `
- `/boot/grub/os.conf `
- `/boot/grub/grub.conf `
- `/boot/grub/grub.cnf `

#### Question 9

Which of the following commands sets the LD_LIBRARY_PATH variable to the trusted directory usr/lib64?

??? question inline "Click for Answer"
    `export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib`

- set LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/lib64" 
- set LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib64 
- export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib 
- export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/lib64" 

#### Question 10

Daniel, a Linux administrator, would like to perform the following tasks on his system:

- Check for outdated packages
- Automatically upgrade the outdated packages
- Install base packages
- Install new packages
- Upgrade dependencies if required
- Remove packages if required

Which of the following commands will help Daniel to perform his tasks successfully?

??? question inline "Click for Answer"
    apt-get dist-upgrade 

- apt-get update 
- apt-get check 
- apt-get dist-upgrade 
- apt-get upgrade 

#### Question 11

Which of the following are the basic modes of the RPM command? (Choose all that apply.)

??? question inline "Click for Answer"
    - Delete
    - Verify
    - Install

- Delete 
- Verify 
- Upgrade 
- Install 

#### Question 12

You are in the process of configuring Yum package in your system. Which of the following directives will you configure to store cache and db files?

??? question inline "Click for Answer"
    Cachedir

- Keepcache 
- Cachedir 
- Persistdir 
- Reposdir 

#### Question 13

What is LVM?

??? question inline "Click for Answer"
    Logical Volume Manager

- Large Volume Maintenance 
- Logical Volume Manager 
- Large Volume Manager 
- Logical Volume Maintenance 

#### Question 14

You wish to reset the hardware clock to the current system time. You already know that you need to first read the hardware clock and then reset it but you are not sure about which command to use. Which of the following commands can you use to get help?

??? question inline "Click for Answer"
		man -k clock

- man -k clock 
- man man 
- man -f clock 
- man intro 

#### Question 15

Which of the following headers are added by default, when the pr command prepares a text file for printing? (Choose all that apply.)

??? question inline "Click for Answer"
		- Filename
		- Date and Time
		- Page Number

- Filename
- Number of lines 
- Page number 
- Date and time 

#### Question 16

What is the function of the -rf option in the rm command?

??? question inline "Click for Answer"
		Removes the directory along with its contents without prompting the user. 

- Removes the directory along with its contents after prompting the user. 
- Removes the contents of the directory only after prompting the user. 
- Removes the directory along with its contents without prompting the user.
- Removes the contents of the directory only without prompting the user. 

#### Question 17

What will be the output of the following command?  (Choose all that apply.)

```
$ ls /etc | tee file1.txt | grep ^p | tee file2.txt | sort -r
```

??? question inline "Click for Answer"
		- It will store the contents of the /etc in the file1.txt file 
		- It will sort and display the files starting with 'p' in reverse order and store the output in the file2.txt file
		- It will search for the file names starting with 'p' in the file1.txt file 

- It will store the contents of the /etc in the file1.txt file 
- It will sort and display the files starting with 'p' and store the output in the file2.txt file 
- It will sort and display the files starting with 'p' in reverse order and store the output in the file2.txt file 
- It will search for the file names starting with 'p' in the file1.txt file 

#### Question 18

Which of the following commands will count the number of lines in TechnicalForum.txt which begins with the word 'the'?

??? question inline "Click for Answer"
    egrep '^the' TechnicalForum.txt 

- fgrep 'the' TechnicalForum.txt 
- egrep -c '^the' TechnicalForum.txt 
- egrep '^the' TechnicalForum.txt 
- fgrep -c '^the' TechnicalForum.txt 

#### Question 19

What will be the output of the following command:

```
grep ABC /etc/passwd
```

??? question inline "Click for Answer"
    It will search for the user named ABC in /etc/passwd 

- It will search for the string ABC /etc/passwd 
- It will search for a file named ABC in /etc/passwd 
- It will search for directory named ABC in /etc/passwd 
- It will search for the user named ABC in /etc/passwd 

#### Question 20

You want to create a 4TB primary partition with the file system ext4 on the /dev/sda1 device

Which of the following set of commands will you use to accomplish this task?

??? question inline "Click for Answer"
    parted /dev/sda1 (parted) mklabel gpt (parted) unit TB (parted) mkpart primary 0.00TB 4.00TB (parted) quit mkfs.ext4 /dev/sda1

#### Question 21

You need to unmount a CD-ROM from your Linux system. However, when you issue the umount command, the system says device is busy. Which command do you need to use to find out the process that is keeping the CD-ROM busy?

??? question inline "Click for Answer"
    Fuser 

- Debugfs 
- Fuser 
- Fsck 
- Fdisk 

#### Question 22

You want to set the following default permissions for all new files and directories:

- Write permission for file owner
- Read permission for group
- Write permissions for others

Which command will help you to set the specified default permission?

??? question inline "Click for Answer"
    umask u+w,g=r,o+w 

- chmod 077 
- umask 252 
- umask u+w,g=r,o+w 
- chmod u+w,g=r,o+w 

#### Question 23

In which directory is fstab located on Linux?

??? question inline "Click for Answer"
    /etc 

- /media 
- /etc 
- /var 
- /usr 

#### Question 24

The locate command uses the database to search for files. However the database must be updated frequently for the locate command to operate efficiently.

Which of the following commands helps accomplish this task?

??? question inline "Click for Answer"
    Updatedb 

- "/etc/updatedb.conf" 
- Mlocate.db 
- /etc/updatedb.conf 
- Updatedb 
