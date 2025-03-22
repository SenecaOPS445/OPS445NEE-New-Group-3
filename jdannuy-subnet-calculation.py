import argparse
import ipaddress

# Set up argparse to handle command line arguments
def setup_argparse():
    parser = argparse.ArgumentParser(description="Calculate subnet details from IP and subnet mask")
    parser.add_argument("ip", help="IP address (e.g., 192.168.1.10)")
    parser.add_argument("mask", help="Subnet mask (e.g., 255.255.255.0)")

    # Parse the arguments
    return parser.parse_args()

def main():
    print("="*36)
    print("Group 3 - Network Configuration & Subnet Calculator")
    print("Members:")
    print("Jhanlyn Brita Dannuy - jdannuy")
    print("Haiwei Liu - hliu232")
    print("="*36)

    # Setup argparse
    args = setup_argparse()

    # Validate the inputs
    try:
        ipaddress.IPv4Address(args.ip)  # Validate IP
        ipaddress.IPv4Address(args.mask)  # Validate mask
    except ValueError:
        print("Failed: Invalid IP or subnet mask.")
        return

    # Proceed to next section in the script (Calculation)

if __name__ == "__main__":
    main()
