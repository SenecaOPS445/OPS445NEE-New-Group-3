import argparse
import ipaddress

# Step 1: Setting up argparse to handle command-line arguments
def setup_argparse():
    """Set up argparse to handle IP and subnet mask as arguments."""
    parser = argparse.ArgumentParser(description="Calculate subnet details from IP and subnet mask")
    parser.add_argument("ip", help="IP address (e.g., 192.168.1.10)")
    parser.add_argument("mask", help="Subnet mask (e.g., 255.255.255.0)")
    
    # Return parsed arguments
    return parser.parse_args()

# Step 2: Validate input
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

    # Step 3: Validate user input
    if not validate_ip_and_mask(args.ip, args.mask):
        print("Failed: Invalid IP or subnet mask.")
        return

    print("Inputs are valid! Proceeding with subnet calculation...")

if __name__ == "__main__":
    main()
