# Step-by-Step Guide: Configuring SSH on a Cisco Router and Switch Using Packet Tracer

## 📌 Prerequisites
- **Cisco Packet Tracer** installed.
- A network setup including:
  - 🖥️ A PC
  - 🌐 A Cisco Router
  - 🏢 A Cisco Switch
  - 📡 Connected via **straight-through cables**.

---

## ⚙️ Step 1: Configure the PC's IP Address  
1. Open the **PC** in Packet Tracer.  
2. Navigate to **Desktop > IP Configuration**.  
3. Set:  
   - **IP Address:** `192.168.1.3`  
   - **Subnet Mask:** `255.255.255.0`  
   - **Default Gateway:** `192.168.1.1`  

---

## ⚙️ Step 2: Establish Console Connection to Router  
1. Use a **console cable** to connect the **PC** to the **Router**.  
2. Open **Terminal** on the PC.  
3. If prompted for **initial configuration**, enter **No**.  

---

## ⚙️ Step 3: Configure the Router (R1)  
1. Enter **Enable Mode**:  

enable

2. Enter **Global Configuration Mode**:  

configure terminal

3. Set **Hostname**:  
hostname R1

4. Configure a **Banner Message**:  
banner motd "This is a Cisco Router - Authorized Access Only!"

5. Assign **IP Address** to Router's Interface:  
interface g0/0 ip address 192.168.1.1 255.255.255.0 no shutdown exit

6. Set **Domain Name**:  
ip domain-name admin

7. Create **User and Encrypted Password**:  
username admin privilege 15 secret Cisco123 enable secret Cisco123

8. Enable **Service Password Encryption**:  
service password-encryption

9. Generate **RSA Keys for SSH**:  
crypto key generate rsa (Enter 1024 for key size)

10. Enable **SSH Version 2**:  
ip ssh version 2

11. Allow **SSH Connections on Virtual Terminal Lines**:  
line vty 0 4 transport input ssh login local

12. Save Configuration:  
write memory

## ⚙️ Step 4: Configure the Switch (S1)  
1. Enter **Enable Mode**:  
enable

2. Enter **Global Configuration Mode**:  
configure terminal

3. Set **Hostname**:  
hostname S1

4. Configure **Banner Message**:  
banner motd "This is a Cisco Switch - Authorized Access Only!"

5. Assign **IP Address to VLAN 1**:  
interface vlan 1 ip address 192.168.1.2 255.255.255.0 no shutdown exit

6. Set **Default Gateway (Router’s IP)**:  
ip default-gateway 192.168.1.1

7. Create **User and Encrypted Password**:  
username admin privilege 15 secret Cisco123 enable secret Cisco123

8. Enable **Service Password Encryption**:  
service password-encryption

9. Generate **RSA Keys for SSH**:  
crypto key generate rsa (Enter 1024 for key size)

10. Enable **SSH Version 2**:  
ip ssh version 2

11. Allow **SSH Connections on Virtual Terminal Lines**:  
line vty 0 4 transport input ssh login local

12. Save Configuration:  
write memory

## ✅ Step 5: Test SSH on Router & Switch  
1. Open **Command Prompt** on PC.  
2. **Test connectivity to Router**:  
ping 192.168.1.1

3. **SSH into Router**:  
ssh -l admin 192.168.1.1

- Enter **password: Cisco123**.  
- You should be logged into the router via SSH.  
4. **Test connectivity to Switch**:  
ping 192.168.1.2

5. **SSH into Switch**:  
ssh -l admin 192.168.1.2

- Enter **password: Cisco123**.  
- You should now have SSH access to the switch.  

## 🏆 Conclusion  
You have successfully configured **SSH on a Cisco Router and Switch** using Packet Tracer. You can now securely manage your network devices remotely.  
