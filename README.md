# Winter 2025 Assignment 2


# Network Configuration & Subnet Calculator

This Python script calculates subnet details such as the network address, broadcast address, usable IPs, subnet mask, and more, based on a given IP address and subnet mask.

#Group 3 - NEE - Professor Eric Brauer
## Team Members
- Jhanlyn Brita Dannuy (jdannuy)
- Haiwei Liu (hliu232)

## 📌 Introduction
This is a simple **Subnet Calculator** written in Python as part of **OPS445 Assignment 2**.  
It allows users to input an **IP address** and a **subnet mask** to calculate network details.

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

```
Network Address: 192.168.1.0
Broadcast Address: 192.168.1.255
First Usable IP: 192.168.1.1
Last Usable IP: 192.168.1.254
Subnet Mask: 255.255.255.0
Total Hosts: 256
Usable Hosts: 254
```

### Error Handling and Validation
The script validates user input to ensure the IP address and subnet mask are valid. If either input is invalid, the script will return an error message indicating the issue:

### Failed: Invalid IP or subnet mask.
This helps users quickly identify and resolve any input mistakes.

## 🚀 Usage Instructions
1. **Run the script**:
   ```bash
   python3 assignment2.py

## Files:
1. **assignment2.py**  
   The main Python script that calculates subnet details based on user input for IP address and subnet mask.

## How to Contribute
1. Fork the repository and clone it locally.
2. Create a new branch for your feature or fix.
3. Make your changes and test them thoroughly.
4. Create a pull request with a description of the changes you made.
5. Once your pull request is reviewed, it will be merged into the `main` branch.

