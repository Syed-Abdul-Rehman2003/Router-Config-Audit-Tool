# Router Configuration Audit Tool  

## Project Overview  
The **Router Configuration Audit Tool** automates the auditing of router security configurations. It connects to routers via SSH, extracts configurations, and identifies security risks such as:  
- Weak passwords  
- Open Telnet ports (23, 2323)  
- Enabled unnecessary services (FTP, SNMP, etc.)  
- Default or insecure credentials  

The tool generates an **audit report** with **remediation recommendations** and provides a **web-based dashboard** for viewing results.  

---

## Features  
✔️ Automated security audit for router configurations  
✔️ Identification of vulnerabilities  
✔️ Security compliance report with recommendations  
✔️ Web-based Flask dashboard for audit results  

---

## Technologies Used  
- **Python** (for automation & SSH connection)  
- **Flask** (for the web dashboard)  
- **GitHub** (for version control & code sharing)  

---

## Installation & Setup  
### **1. Clone Repository**  
```bash
git clone https://github.com/YOUR_USERNAME/Router-Config-Audit-Tool.git
cd Router-Config-Audit-Tool
