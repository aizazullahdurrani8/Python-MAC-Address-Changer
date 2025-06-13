#!/usr/bin/env python3
import subprocess
import argparse
import random
import re

# Function to generate a simple random MAC address
def generate_random_mac():
    mac = [random.randint(0x00, 0xff),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: f"{x:02x}", mac))

# Function to get the current MAC address
def get_current_mac(interface):
    try:
        result = subprocess.check_output(["ip", "addr", "show", interface]).decode("utf-8")
        mac_address = re.search(r"([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}", result)
        if mac_address:
            return mac_address.group(0)
        else:
            return None
    except subprocess.CalledProcessError:
        print("[-] Could not read MAC address. Check your interface name.")
        return None

# Function to get command line arguments
def get_arguments():
    import sys
    if len(sys.argv) == 1:
        print("[-] Please provide arguments. Use --help for usage.")
        exit(1)

    parser = argparse.ArgumentParser(description="MAC Address Changer Script")
    parser.add_argument("-i", "--interface", dest="interface", help="Interface name")
    parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC address")
    parser.add_argument("-r", "--random", action="store_true", dest="random_mac", help="Use a random MAC address")
    parser.add_argument("-c", "--current", action="store_true", dest="show_current", help="Show current MAC address and exit")
    args = parser.parse_args()

    if not args.interface:
        print("[-] Please specify an interface using -i or --interface")
        exit(1)

    if args.show_current:
        current_mac = get_current_mac(args.interface)
        if current_mac:
            print(f"[+] Current MAC address of {args.interface}: {current_mac}")
        else:
            print("[-] Could not read MAC address.")
        exit(0)

    if args.random_mac:
        args.new_mac = generate_random_mac()
    elif not args.new_mac:
        print("[-] Please specify a new MAC address using -m or use -r for random")
        exit(1)

    return args

# Function to change MAC address
def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    subprocess.run(["ip", "link", "set", interface, "down"])
    subprocess.run(["ip", "link", "set", interface, "address", new_mac])
    subprocess.run(["ip", "link", "set", interface, "up"])

    final_mac = get_current_mac(interface)
    if final_mac == new_mac:
        print(f"[+] MAC address successfully changed to {final_mac}")
    else:
        print("[-] MAC address change failed.")

# Main execution
if __name__ == "__main__":
    args = get_arguments()
    change_mac(args.interface, args.new_mac)