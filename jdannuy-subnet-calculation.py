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

def main():
    print("="*36)
    print("Group 3 - Network Configuration & Subnet Calculator")
    print("Members:")
    print("Jhanlyn Brita Dannuy - jdannuy")
    print("Haiwei Liu - hliu232")
    print("="*36)

    # Setup argparse (from Member 1)
    args = setup_argparse()

    # Validate the inputs (from Member 1)
    try:
        ipaddress.IPv4Address(args.ip)
        ipaddress.IPv4Address(args.mask)
    except ValueError:
        print("Failed: Invalid IP or subnet mask.")
        return

    # Calculate and output subnet details
    subnet_info = calculate_subnet(args.ip, args.mask)

    if "Error" in subnet_info:
        print(f"Failed: {subnet_info['Error']}")
    else:
        print("\n=== Subnet Details ===")
        for key, value in subnet_info.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
