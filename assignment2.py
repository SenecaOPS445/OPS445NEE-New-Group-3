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

def main():
    # Initialize argparse
    args = setup_argparse()

    # Step 3: If IP or mask are not passed, prompt the user to enter them
    if not args.ip:
        args.ip = input("Enter IP address (e.g., 192.168.1.10): ")
    if not args.mask:
        args.mask = input("Enter subnet mask (e.g., 255.255.255.0): ")

    # Step 4: Validate user input
    if not validate_ip_and_mask(args.ip, args.mask):
        print("Failed: Invalid IP or subnet mask.")
        return

    print(f"IP Address: {args.ip}, Subnet Mask: {args.mask}")
    print("Inputs are valid! Proceeding with subnet calculation...")

if __name__ == "__main__":
    main()
