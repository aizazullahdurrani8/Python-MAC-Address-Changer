# Python MAC Address Changer

This script allows you to easily change the MAC address of a specified network interface on your system. It's a simple command-line tool designed for quick modifications.

## Getting Started

To get a copy of this project up and running on your local machine, follow these steps.

### Prerequisites

- Python 3 installed on your system.
- Permissions to modify network configurations (e.g., sudo on Linux).

### Cloning the Repository

You can clone this repository using HTTPS:

    git clone https://github.com/aizazullahdurrani8/python-mac-address-changer.git

## Usage

Navigate into the cloned directory and run the script with the required arguments.

### Arguments

- `-i` or `--interface`: Specify the network interface (e.g., `eth0`, `wlan0`).
- `-m` or `--mac`: Specify the new MAC address you want to set.
- `-r` or `--random`: Generate and assign a random MAC address.
- `-c` or `--current`: Show the current MAC address of the specified interface and exit.

### Example

To change the MAC address of `eth0` to `00:11:22:33:44:55`:

    sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55

To assign a random MAC address to `eth0`:

    sudo python3 mac_changer.py -i eth0 -r

To check the current MAC address of `eth0`:

    python3 mac_changer.py -i eth0 -c

## How it Works

The script performs the following actions:

1. **Takes Command-Line Arguments**: Uses `argparse` to get the interface name and the desired action from the user.

2. **Validates Input**: Ensures proper arguments are provided and displays help or error messages if not.

3. **Changes MAC Address**:

   - Brings the specified network interface **down**.
   - Changes its MAC address using the `ip` command.
   - Brings the interface **up** again.

## Disclaimer

This tool is for educational purposes only. Misuse of this tool may lead to unintended consequences or violate local laws. Always ensure you have the necessary permissions before modifying network settings.
