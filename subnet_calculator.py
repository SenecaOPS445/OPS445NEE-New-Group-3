import ipaddress

def calculate_subnet(ip, mask):
    """Calculates subnet details from IP and mask."""
    try:
        network = ipaddress.IPv4Network(f"{ip}/{mask}", strict=False)
        return {
            "Network Address": str(network.network_address),
            "Broadcast Address": str(network.broadcast_address),
            "First Usable IP": str(list(network.hosts())[0]) if network.num_addresses > 2 else "N/A",
            "Last Usable IP": str(list(network.hosts())[-1]) if network.num_addresses > 2 else "N/A",
            "Subnet Mask": str(network.netmask),
            "Total Hosts": network.num_addresses,
            "Usable Hosts": network.num_addresses - 2 if network.num_addresses > 2 else 0
        }
    except ValueError as e:
        return {"Error": f"Invalid input: {e}"}
