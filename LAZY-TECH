import os
import socket
import subprocess
import platform

# ANSI escape codes for green text on a black background
GREEN_TEXT = "\033[32m"
RESET_COLOR = "\033[0m"

# Function to clear the terminal or command prompt screen
def clear_screen():
    if platform.system() == "Windows":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)

# Function to perform a ping test to a given hostname
def ping_test(hostname):
    try:
        # Execute ping command based on the platform
        response = os.system(f"ping -n 4 {hostname}" if platform.system() == "Windows" else f"ping -c 4 {hostname}")
        if response == 0:
            print(f"{GREEN_TEXT}Ping to {hostname} succeeded.{RESET_COLOR}")
        else:
            print(f"{GREEN_TEXT}Ping to {hostname} failed.{RESET_COLOR}")
    except:
        print(f"{GREEN_TEXT}Ping to {hostname} failed.{RESET_COLOR}")

# Function to perform DNS resolution for a given hostname
def dns_resolution(hostname):
    try:
        # Get IP address associated with the hostname
        ip = socket.gethostbyname(hostname)
        print(f"{GREEN_TEXT}DNS resolution for {hostname}: {ip}{RESET_COLOR}")
    except socket.gaierror:
        print(f"{GREEN_TEXT}DNS resolution for {hostname} failed.{RESET_COLOR}")

# Function to check internet connection by creating a socket connection
def check_internet_connection():
    try:
        # Attempt to create a socket connection to Google's web server
        socket.create_connection(("www.google.com", 80))
        print(f"{GREEN_TEXT}Internet connection is available.{RESET_COLOR}")
    except:
        print(f"{GREEN_TEXT}No internet connection.{RESET_COLOR}")

# Function to display network interface information
def network_interface_info():
    # Retrieve network interface information using subprocess
    ifconfig_output = subprocess.getoutput("ipconfig" if platform.system() == "Windows" else "ifconfig")
    print(f"{GREEN_TEXT}{ifconfig_output}{RESET_COLOR}")

# Main function to present a menu and handle user choices
def main():
    while True:
        clear_screen()
        print(f"{GREEN_TEXT}LAY-Z TECH TROUBLE-SHOOTER:{RESET_COLOR}")
        print("1. Ping Test")
        print("2. DNS Resolution")
        print("3. Check Internet Connection")
        print("4. Network Interface Information")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            hostname = input("Enter the host to ping: ")
            ping_test(hostname)
        elif choice == "2":
            hostname = input("Enter the host for DNS resolution: ")
            dns_resolution(hostname)
        elif choice == "3":
            check_internet_connection()
        elif choice == "4":
            network_interface_info()
        elif choice == "5":
            print(f"{GREEN_TEXT}Exiting the Network Troubleshooting Tool.{RESET_COLOR}")
            break
        else:
            print(f"{GREEN_TEXT}Invalid choice. Please try again.{RESET_COLOR}")

        input("Press Enter to continue...")

# Execute the main function when the script is run
if __name__ == "__main__":
    main()
