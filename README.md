# System Reconnaissance Tool (Non-Admin)

This is a **Python-based System Reconnaissance Tool** designed for **educational purposes** and **cybersecurity learning**. It allows users to collect **comprehensive system information**, display it in the console, save a report locally, and optionally send a copy to a Discord server via webhook.  

The tool is **beginner-friendly**, runs **without admin privileges**, and demonstrates key concepts in **system enumeration, process monitoring, network analysis, and automation**.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Requirements](#requirements)  
4. [Installation](#installation)  
5. [Usage](#usage)  
6. [Sample Output](#sample-output)  
7. [Learning Outcomes](#learning-outcomes)  
8. [Notes](#notes)  
9. [License](#license)  
10. [Contact](#contact)  

---

## Project Overview

System reconnaissance is a critical skill in **cybersecurity**, allowing professionals to understand the target system’s structure, resources, and current state. This tool simulates a **real-world system auditing tool**, providing detailed information that can help beginners **practice system monitoring, reporting, and automation**.

This version of the tool is **non-admin**, making it **safe to run on any Windows machine** while still demonstrating **practical cybersecurity skills**.

---

## Features

- **System Information:** OS, architecture, CPU, memory, hostname, current user, and current directory  
- **Network Interfaces:** All available interfaces with IP and MAC addresses  
- **Running Processes:** Lists all processes accessible to the current user  
- **Reporting:**  
  - Generates a **timestamped TXT report** saved locally in the `reports/` folder  
  - Sends a copy of the report to Discord via webhook (optional)  
- **Non-Admin Execution:** Runs safely without elevated privileges  
- **Console Display:** Easy-to-read console output for immediate analysis  

---

## Requirements

- Python 3.x  
- [psutil](https://pypi.org/project/psutil/)  
- [requests](https://pypi.org/project/requests/)  

Install dependencies via pip:

```bash
pip install psutil requests
