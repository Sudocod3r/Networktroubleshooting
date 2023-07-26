import os
import socket
import subprocess
import platform

def clear_screen():
    if platform.system() == "Windows":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)

def ping_test(hostname):
    try:
        response = os.system(f"ping -n 4 {hostname}" if platform.system() == "Windows" else f"ping -c 4 {hostname}")
        if response == 0:
            print(f"Ping to {hostname} succeeded.")
        else:
            print(f"Ping to {hostname} failed.")
    except:
        print(f"Ping to {hostname} failed.")

def dns_resolution(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        print(f"DNS resolution for {hostname}: {ip}")
    except socket.gaierror:
        print(f"DNS resolution for {hostname} failed.")

def check_internet_connection():
    try:
        socket.create_connection(("www.google.com", 80))
        print("Internet connection is available.")
    except:
        print("No internet connection.")

def network_interface_info():
    ifconfig_output = subprocess.getoutput("ipconfig" if platform.system() == "Windows" else "ifconfig")
    print(ifconfig_output)

def main():
    while True:
        clear_screen()
        print("Network Troubleshooting Menu:")
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
            print("Exiting the Network Troubleshooting Tool.")
            break
        else:
            print("Invalid choice. Please try again.")

        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
