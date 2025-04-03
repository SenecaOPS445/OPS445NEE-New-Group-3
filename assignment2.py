#!/usr/bin/env python3
'''
Project: Network Configuration & Subnet Calculator
Description:
This script calculates subnet details including network address, IP range, broadcast address, and more, 
based on a given IP address and subnet mask.
'''

# Group Information
group_info = """

===================================
Group 3
Network Configuration and Subnetting
Members:
Jhanlyn Brita Dannuy (jdannuy)
Haiwei Liu (hliu232)
===================================
"""

import argparse
import ipaddress

# Step 1: Setting up argparse for optional arguments
def setup_argparse():
    """Set up argparse to handle optional arguments."""
    parser = argparse.ArgumentParser(description="Calculate subnet details from IP and subnet mask")
    parser.add_argument("--ip", help="IP address (e.g., 192.168.1.10)")
    parser.add_argument("--mask", help="Subnet mask (e.g., 255.255.255.0)")

    # Return parsed arguments
    return parser.parse_args()

# Step 2: Validate input (checks if IP and mask are valid)
def validate_ip_and_mask(ip, mask):
    """Validate the IP and mask."""
    try:
        ipaddress.IPv4Address(ip)  # Validate IP
        ipaddress.IPv4Address(mask)  # Validate mask
        return True
    except ValueError:
        return False

# Step 3: Implemented the calculate_subnet() function
def calculate_subnet(ip, mask):
    """Calculates subnet details from IP and mask."""

    try:
        network = ipaddress.IPv4Network(f"{ip}/{mask}", strict=False)

        net_address = network.network_address
        bro_address = network.broadcast_address
        net_host_list = list(network.hosts())
        firstip = net_host_list[0]
        lastip = net_host_list[-1]
        sub_mask = network.netmask
        total_hosts = network.num_addresses
        usable_hosts = total_hosts - 2

        return {
                "Network Address": str(net_address),
                "Broadcast Address": str(bro_address),
                "First Usable IP": str(firstip if network.num_addresses > 2 else "N/A"),  # if the total hosts <=2, no usable ip
                "Last Usable IP": str(lastip if network.num_addresses > 2 else "N/A"),  # if the total hosts <=2, no usable ip
                "Subnet Mask": str(sub_mask),
                "Total Hosts": total_hosts,
                "Usable Hosts": usable_hosts if network.num_addresses > 2 else 0  # if the total hosts <=2, no usable ip
            }
    except ValueError as e:
        return {"Error": f"Invalid input: {e}"}

def main():
    # Initialize argparse
    args = setup_argparse()

    # Step 4: If IP or mask are not passed, prompt the user to enter them
    if not args.ip:
        args.ip = input("Enter IP address (e.g., 192.168.1.10): ")
    if not args.mask:
        args.mask = input("Enter subnet mask (e.g., 255.255.255.0): ")

    # Step 5: Validate user input
    if not validate_ip_and_mask(args.ip, args.mask):
        print("Failed: Invalid IP or subnet mask.")
        return
    else:
        # Calculate subnet info
        subnet_info = calculate_subnet(args.ip, args.mask)

        # Display results
        if "Error" in subnet_info:
            print(f"Failed: {subnet_info['Error']}")
        else:
            print("\n=== Subnet Details ===")
            for key, value in subnet_info.items():
                print(f"{key}: {value}")



if __name__ == "__main__":
    main()