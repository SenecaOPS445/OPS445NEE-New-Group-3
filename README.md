# Winter 2025 Assignment 2


# Network Configuration & Subnet Calculator

This Python script calculates subnet details such as the network address, broadcast address, usable IPs, subnet mask, and more, based on a given IP address and subnet mask.

#Group 3 - NEE - Professor Eric Brauer
## Team Members
- Jhanlyn Brita Dannuy (jdannuy)
- Haiwei Liu (hliu232)


## Subnet Calculator
### Functionality:
The subnet calculator accepts an IP address and subnet mask as input and computes the following details:

- **Network Address:** The address that identifies the network portion of the IP.
- **Broadcast Address:** The address used to send data to all hosts in the subnet.
- **First Usable IP:** The first available host IP in the subnet (if applicable).
- **Last Usable IP:** The last available host IP in the subnet (if applicable).
- **Subnet Mask:** The mask that defines the network portion and host portion of the address.
- **Total Hosts:** The total number of IP addresses in the subnet.
- **Usable Hosts:** The number of available host IPs (total hosts minus the network and broadcast addresses).

### Example Output:
For the ip and subnet mask:

- IP = `192.168.1.10`
- subnet mask = `255.255.255.0`

The output will show:

- Network Address: 192.168.1.0
- Broadcast Address: 192.168.1.255
- First Usable IP: 192.168.1.1
- Last Usable IP: 192.168.1.254
- Subnet Mask: 255.255.255.0
- Total Hosts: 256
- Usable Hosts: 254