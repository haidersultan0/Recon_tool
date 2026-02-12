import os
import platform
import socket
import getpass


def get_os_info():
    return platform.system() + " " + platform.release()


def get_hostname():
    return socket.gethostname()


def get_ip_address():
    return socket.gethostbyname(get_hostname())


def get_current_user():
    return getpass.getuser()


def get_architecture():
    return platform.machine()


def get_current_directory():
    return os.getcwd()


def main():
    print("===== System Reconnaissance Report =====\n")

    print(f"Operating System : {get_os_info()}")
    print(f"Hostname         : {get_hostname()}")
    print(f"IP Address       : {get_ip_address()}")
    print(f"Current User     : {get_current_user()}")
    print(f"Architecture     : {get_architecture()}")
    print(f"Current Dir      : {get_current_directory()}")

    print("\n===== Recon Completed =====")


if __name__ == "__main__":
    main()
