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

def calculate_subnet(ip, mask):
    """Calculates subnet details from IP and mask."""

    network = ipaddress.IPv4Network(f"{ip}/{mask}")

    net_add = network.network_address
    bro_add = network.broadcast_address
    net_host_list = list(network.hosts())
    firstip = net_host_list[0]
    lastip = net_host_list[-1]
    sub_mask = network.netmask
    total_hosts = network.num_addresses
    usable_hosts = total_hosts - 2

    return {
            "Network Address": str(net_add),
            "Broadcast Address": str(bro_add),
            
            "First Usable IP": str(firstip),
            "Last Usable IP": str(lastip),
            "Subnet Mask": str(sub_mask),
            "Total Hosts": total_hosts,
            "Usable Hosts": usable_hosts
        }



if __name__ == "__main__":

    ip1 = '192.168.10.0'
    mask1 = '255.255.255.240'
    subnet = calculate_subnet(ip1,mask1)
    
    for (key, value) in subnet.items():
        print(f"{key}: {value}")
    
    
