# :material-lan: Networks

## :material-linux: Network Configuration tutorial in Linux


:fontawesome-solid-list-ul: **Procedure**

- Discover host IP configurations.
- Manage network inferfaces.
- Use network utilities

### :octicons-terminal-16: Discover host IP configurations

!!! example "Ubuntu"

    === "Terminal"

        ``` markdown title="Root Directory"

        - `ip addr` - Shows IP addresses assigned to all network interfaces.
        - IPv4 addresses are listed after the `inet` designation.
        - `ip route` to identify the default gateway IP address after the `via` designation.
        - Enter `cd /var/lib/dhcp` and then `ls` to list lease files in the `/var/lib/ dhcp` directory.
        - Enter `cat dhclient.leases` (replace `dhclient.leases` with your file name if necessary) to identify the DHCP server IP address in the option dhcp server identifier line.
        - Enter `cat /run/systemd/resolv.conf` and identify the DNS server IP address in the `nameserver` line. If the “no such file or directory ” error message pops up, re-enter the command and check the spelling.
        - Use the ping utility program to verify local network connectivity by using the `ping -c 4 192.168.1.1` command.
         
        ``` 

??? question "What is the IP address of your Ubuntu machine?"
        127.0.0.1

??? question "What is the IP address of its default gateway?"
        192.168.1.1

??? question "What is the IP address of its DHCP server?"
        192.168.1.1

??? question "What is the IP address of its DNS server?"
        192.168.1.1

### :octicons-terminal-16: Manage Network Interfaces

- Enter `cd ~` to return to the home directory.

!!! note inline end
        `ip link` omits the IP address information which is displayed by the `ip addr` command.

- Enter `ip link` to display all network interfaces.

!!! info inline
        The output from `ip link` should have a `eth0` option that likely would have produced a line with a `state UP`. Notice the `sudo ip link set eth0 down` command changes the state.

- Enter `sudo ip link set eth0 down`

??? question "Which DHCP message is shown in the output of the sudo  dhclient  –v  –r  eth0 command? [hint: the message name is in uppercase.]"

??? question "Which four DHCP messages are shown in the output of the sudo  dhclient  –v  eth0 command? [hint: the message names are in uppercase.]"

!!! note "Some questions to know the answers to:"

??? question "What is a valid APIPA address?"
    169.254.38.101
??? question "What is a comand that will send 4 ICMP echo requests to a remote host named server1 to determine the round trip time it takes a packet to travel?"
    `ping -c 4 server1`
??? question "Which port could you use to resolve a domain name to an IP address?"
    53
??? question "The output of the ifconfig shows a HWaddr expressed in hexadecimal. How many bits is the hardware address shown made up of?"
    48
??? question "The system administrator has shut ethernet interface eth0 down while making some changes to the system. Which of the following commands can they use to bring the network connection back up?"
    `ifup eth0`
??? question "What is the path and file name where DNS servers should be configured?"
    `/etc/resolv.conf`
??? question "What is a SQL statement to delete a table from a databse?"
    `DROP TABLE table_name;`
??? question "What is the command used to display any email messages awaiting delivery alongside the reason that they were not delivered?"
    `mailiq`
??? question "What type of DNS record need to be configured to faciliate e-mail delivery?"
    `MX`
??? question "What is used to graphically remotely administer a Linux machine?"
    VNC
??? question "What CM software only  requires that you specify attributes that the inventory members must have within a config file, not the individual procedures that must be3 executed"
    Declarative configuration
??? question "Which type of CM software can connect to inventory members via SSH to perform configuration management?"
    Agentless
??? question "What is used on modern Linux distro's that reads YAML configuration files to add apps, modify config settings, or perform admini tasks at boot time?"
    Cloud-init
??? question "Which of the following is not a way to remotely administer Linux servers?"
    Docker
