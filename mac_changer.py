#!/usr/bin/env python3
import subprocess
import optparse

# Function to get command line arguments
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()

    # Check if interface and MAC address are provided
    if not options.interface:
        print("[-] Please specify an interface using -i or --interface")
        exit()
    elif not options.new_mac:
        print("[-] Please specify a new MAC address using -m or --mac")
        exit()

    return options

# Function to change MAC address
def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    subprocess.call(["ifconfig", interface, "down"])  # Disable the interface
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])  # Set new MAC
    subprocess.call(["ifconfig", interface, "up"])  # Enable the interface
    print("[+] MAC address successfully changed")

# Main execution
args = get_arguments()
change_mac(args.interface, args.new_mac)