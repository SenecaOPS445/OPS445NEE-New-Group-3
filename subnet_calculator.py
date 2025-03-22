def calculate_subnet(ip, mask):
    """Calculates subnet details from IP and mask."""
    return {}

import ipaddress

def calculate_subnet(ip, mask):
    """Calculates subnet details from IP and mask."""
    try:
        network = ipaddress.IPv4Network(f"{ip}/{mask}", strict=False)
        return {
            "Network Address": str(network.network_address),
            "Broadcast Address": str(network.broadcast_address),
        }
    except ValueError as e:
        return {"Error": f"Invalid input: {e}"}

def calculate_subnet(ip, mask):
    """Calculates subnet details from IP and mask."""
    try:
        network = ipaddress.IPv4Network(f"{ip}/{mask}", strict=False)
        return {
            "Network Address": str(network.network_address),
            "Broadcast Address": str(network.broadcast_address),
            "First Usable IP": str(list(network.hosts())[0]) if network.num_addresses > 2 else "N/A",
            "Last Usable IP": str(list(network.hosts())[-1]) if network.num_addresses > 2 else "N/A",
        }
    except ValueError as e:
        return {"Error": f"Invalid input: {e}"}
