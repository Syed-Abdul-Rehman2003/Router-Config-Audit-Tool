import paramiko
import time

def enable_ssh(router_ip, port, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        client.connect(router_ip, port=port, username=username, password=password)
        print(f"Connected to {router_ip} successfully.")
        commands = [
            "configure terminal",
            "ip ssh version 2",
            "crypto key generate rsa modulus 1024",
            "ip ssh time-out 60",
            "ip ssh authentication-retries 3",
            "exit"
        ]
        for cmd in commands:
            print(f"Executing command: {cmd}")
            stdin, stdout, stderr = client.exec_command(cmd)
            time.sleep(1)
            output = stdout.read().decode().strip()
            error = stderr.read().decode().strip()
            if output:
                print("Output:", output)
            if error:
                print("Error:", error)
                
    except Exception as e:
        print("SSH connection or command execution failed:", str(e))
        
    finally:
        client.close()
        print("Connection closed.")

if __name__ == "__main__": 
    #Defualt values (not the actual one's)
    router_ip = "192.168.1.1"
    port = 22
    username = "admin"
    password = "admin_password"
    enable_ssh(router_ip, port, username, password)
