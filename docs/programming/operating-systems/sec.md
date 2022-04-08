# :material-server-security:{ .security } Security, Troubleshooting, and Performance

## :material-linux: System Performance Monitoring

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

## Web Performance

How can we think critically about performance and how to make a website faster?

### Keys to Performance

There are three places where work needs to happen when displaying websites:

1. GET request to server
2. Server does some work, sends data back
3. Display data from server

So we can improve the client side, we can improve our transfer time, and we can improve backend processing.

Part one of performance we'll focus on critical render path

### Minimize Images

You want to pick the right types of images (jpg, png, gif, svg) and compress them as small as you can without taking from their quality.

- If you want transparency: use a PNG
  - Reduce PNG with [TinyPNG](https://tinypng.com/)
- If you want animations: use a GIF
- If you want colorful images: use a JPG
  - Reduce JPG with [jpeg-optimizer](http://jpeg-optimizer.com/)
  - Try to choose simple illustrations over highly detailed photographs
  - Always lower JPG image quality (30-60%)
  - Resize image based on size it will be displayed
  - Display different sized images for different backgrounds
- If you want simple icons, logos, illustrations: use SVGs
- Use CDNs like [imgix](https://www.imgix.com/?utm_term=imgix&utm_campaign=adwords-branded&utm_source=adwords&utm_medium=ppc&hsa_tgt=kwd-347244981599&hsa_grp=98890898611&hsa_src=g&hsa_net=adwords&hsa_mt=p&hsa_ver=3&hsa_ad=456649958299&hsa_acc=8534109361&hsa_kw=imgix&hsa_cam=9210499657&gclid=Cj0KCQiA0MD_BRCTARIsADXoopbaiwxfrkrZx62gTorkL9bRTwyBzhM8GmSj43MR-8P0QpWrNtiBiB8aAlP3EALw_wcB)
- Remove image metadata

### [HTTP/2](https://developers.google.com/web/fundamentals/performance/http2/)

Update to HTTP that updates network latency

### Resources

- [Performance analysis in a table](https://developers.google.com/web/tools/chrome-devtools/evaluate-performance/reference#activities)
- [Analyze frames per second (FPS)](https://developers.google.com/web/tools/chrome-devtools/evaluate-performance/reference#fps)
- [Monitor: CPU usage, JS heap size, DOM nodes (event listeners, documents, frames per page), layouts and style recalculations per second](https://developers.google.com/web/updates/2017/11/devtools-release-notes#perf-monitor)
- [View Interactions](https://developers.google.com/web/tools/chrome-devtools/evaluate-performance/reference#interactions)
- [Find scroll performance issues in realtime](https://developers.google.com/web/tools/chrome-devtools/evaluate-performance/reference#scrolling-performance-issues)
- [View painting events in real time](https://developers.google.com/web/tools/chrome-devtools/evaluate-performance/reference#paint-flashing)

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
