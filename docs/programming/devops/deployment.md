## What is Deployment?

**Deployment** is the general process of making a piece of software available to its users.

Pre-internet days, it meant storing software on floppy disks :fontawesome-solid-floppy-disk: or CD-ROMs, shipping them to users, and having those users manually install the software on their own devices. This process was slow and expensive, and any bugs that slipped through the cracks could be catastrophic.

Today, software developers are able to deploy their software via the internet with greater ease and speed of delivery than ever before due to nearly the entire tech industry providing cloud services.

What I'll attempt to do in this article is discuss the deployment process generally, covering the most commonly used tools and practices, such as:

- Infrastructure management
- Version control systems
- Testing:
    - unit
    - integration
    - acceptance
    - end-to-end
- Deployment environments

!!! info "Why is it called DevOps?

    **DevOps** is a clever word smithing technique that mashes the two words, "Development" and "Operations(IT)," into one word. Coined by Patrick Debois in 2009, it's clever in that it rightly joins two specialty fields in the tech industry and is referred to as a "culture" rather than a process or standard.

## Infrastructure Management

Web applications today are stored and executed on servers. 

Servers are computers that run software that can be accessed by another device (client), via the internet. Servers respond to requests with website code, images, and other content which are rendered by the client, which is mostly in the browser.

Servers require a lot of maintenance in order to be used by developers, and the infrastructure of a server is managed by an Operations team.

**Infrastructure** is is the full set of resources that support the development, testing, and deployment that consists of:

- Hardware components such as servers, routers, switches and cables
- Software components such as operating systems, version control systems, and applications

The responsibilites of an Operations team is extensive, it includes:

- Installing, provisioning (replacing) physical components
- Performing software and firmware upgrades to keep systems secure
- Configuring infrastructure firewalls, user access, ports
- Monitor network health and alert personnel when issues arise



