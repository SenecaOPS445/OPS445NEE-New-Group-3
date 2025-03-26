#!/usr/bin/env python3
'''
Project: Network Configuration & Subnet Calculator
Group: 3
SenecaID: hliu232

Description:
This script calculates subnet details including network address, IP range, broadcast address, and more, 
based on a given IP address and subnet mask.
'''
import ipaddress
import argparse

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
    
# The setup_argparse() function comes from member 1
def setup_argparse():
    """Set up argparse to handle IP and subnet mask as arguments."""
    parser = argparse.ArgumentParser(description="Calculate subnet details from IP and subnet mask")
    parser.add_argument("ip", help="IP address (e.g., 192.168.1.10)")
    parser.add_argument("mask", help="Subnet mask (e.g., 255.255.255.0)")
    
    # Return parsed arguments
    return parser.parse_args()


if __name__ == "__main__":

     # Reuse the setup and validation from Member 1
    args = setup_argparse()

    subnet_info = calculate_subnet(args.ip, args.mask)
   
    print("\n========= Subnet Details =========")
    for key, value in subnet_info.items():
        print(f"{key}: {value}")
    print("==================================\n")
