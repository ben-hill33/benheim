# :material-server-security:{ .security } Security, Troubleshooting, and Performance

## :material-linux: System Performance Monitoring Project

Linux system performance could be affected by factors such as the amount of RAM, CPU utilization, storage device speed, and process load. The usual culprits include processes that generate many read/write requests to databases, processes that send and receive a large amount of data on the network, or simply too many processes that are running on a machine.

Monitoring Linux system performance and investigating performance problems are critical to keeping systems up and running. Various CLI and GUI monitoring tools can be used to monitor system performance and help identify the root causes of problems.

### :fontawesome-solid-list-ul: Objectives

- Monitor Linux processes.
- Monitor user activities.
- Monitor network bandwidth usage.

#### :octicons-terminal-16: Monitor Linux Processes

!!! example "Ubuntu"

    === "Terminal"

        ``` markdown title="htop and kill signals"
        1. Enter `htop` to launch the htop utility program that monitors Linux processes real time. The middle section displays a list of processes. Use arrow keys or
        page up/down keys to scroll the processes.
        2. Open the calculator app on your system and click anywhere in your terminal while htop is running. Search for the calculator app you just opened by running `/calculator` and press the Enter key. That app you opened should be highlighted in the running processes shown by htop.
        3. Press the `k` on your keyboard it's a hotkey for terminal to request the process you have hightlighted to be terminated. 
        4. The interface should have changed to where you're now highlighting `15 SIGTERM`, which is the signal to terminate the process.` Press Enter and Calculator will close.
        ```
??? question "What is the default action of `15 SIGTERM` kill signal?"
        The default action is implicit in the name of of the signal. Signal (SIG) 15 TERMinate. Terminate Signal.

#### :octicons-terminal-16: Monitor User Activities

!!! example "Ubuntu"

    === "Terminal"

        ``` markdown title="htop and kill signals"
        
        ```

## :card_index: Flashcards

??? question "Which utility allows you to view information about virtual memory usage on a Linux system?"
        `vmstat`

??? question "If you suspect that you have bad blocks on a file system, which of the following commands can be used to try and repair the file system?"
        `fsck`
??? question "You want to determine whether your Linux workstation was able to get assigned an IP address from the DHCP server once you connected it to the network. Name the legacy command that might help you determin this."
        `ifconfig eth0`

??? question "Which command can be used to determine the round trip time that a packet takes to traverse a network connection?"
        `ping`

??? question "Which command can be used for the command line version of a popular GUI-based program that is used to examine network traffic passing to and from a network interface?"
        `tshark`

??? question "What permissions should a standard user have on the `etc/shadow` file?"
        None

??? question "Give an example of results that the `nmap` command would give to an administrator to let them know they have an insecure service running on a Linux server?"
        23/tcp open telnet

??? question "What utilities can be used by a system admin to determine which services are responding to network requests?"
        nmap

??? question "What can you use to start network daemons in order to limit which computers are allowed to connect to the network service?"
        TCP wrapper

??? question "Give an example of multifactor authentication."
        Password and fingerprint reader
