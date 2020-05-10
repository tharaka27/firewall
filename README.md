# Design and Implement a Firewall

In this assignment we have implemented a firewall. 

A firewall is a network security device that monitors incoming and outgoing network traffic and decides whether to allow or block specific traffic based on a defined set of security rules.
Firewalls have been a first line of defense in network security for over 25 years. They establish a barrier between secured and controlled internal networks that can be trusted and untrusted outside networks, such as the Internet. 
A firewall can be hardware, software, or both. The Firewall we have built in this assignment is a software based firewall.
Design Decisions

In the design we used two configuration files to implement inbound rules ( inbound rules.ini file ) and outbound rules ( outbound rules.ini file ) 

The inbound rules define the traffic allowed to the server on which ports and from which sources. If no inbound rules are configured, no incoming traffic is permitted.

Outbound firewall rules define the traffic allowed to leave the server on which ports and to which destinations. If no outbound rules are configured, no outbound traffic is permitted.

We have implemented 3 operations Accept, Decline and Reject which can be performed in the data packet. 


# Data preparation

First the network traffic was captured using wireshark.

![Image of Yaktocat](https://github.com/tharaka27/firewall/blob/master/images/tcp_wireshark.PNG)



The captured data were saved in two files tcp.txt and udp.txt

![Image of Yaktocat](https://github.com/tharaka27/firewall/blob/master/images/tcp_notepad.PNG)

# Process

First we check whether the packet is TCP or UDP packet using the 23rd byte in Packet.

![Image of Yaktocat](https://github.com/tharaka27/firewall/blob/master/images/check%20for%20TCP%20and%20UDP.PNG)

Second the data packets are checked for incoming or outgoing packets using the MAC address of the packet. For incoming packets inbound rules are applied. For outgoing packets outbound rules are applied.

![Image of Yaktocat](https://github.com/tharaka27/firewall/blob/master/images/check%20for%20MAC.PNG)

If the packet is allowed then it will be allowed to cross the firewall.

# Working example

![Image of Yaktocat](https://github.com/tharaka27/firewall/blob/master/images/explanation.png)


* 1 - The packet is detected as an outgoing packet hence outbound rules are applied. Since src and destination IPs and Ports are allowed to communicate, transmission is successful.
* 2 - The packet is detected as an incoming packet hence inbound rules are applied. Since src and destination IPs and Ports are allowed to communicate, transmission is successful.
* 3, 4- The source IP, port or destination IP,port is declined or rejected, transmission is unsuccessful.
* 5 - Rules are not set for the given source IP address. Hence program request to assign rules. 
