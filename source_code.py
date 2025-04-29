import paramiko  # Import the Paramiko library for SSH communication
import time      # Import time to pause the script for output retrieval

# --------------------------------------------
# Define Router SSH Access Parameters
# --------------------------------------------
router_ip = '192.168.10.1'     # IP address of the router
username = 'admin'            # Username to login to the router
password = 'cisco'         # Password for SSH and enable mode
port = 22                     # SSH runs on port 22

# --------------------------------------------
# Create SSH Client
# --------------------------------------------
ssh = paramiko.SSHClient()

# Automatically add router's SSH key to known hosts (avoid manual approval)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # --------------------------------------------
    # Establish SSH connection to the router
    # --------------------------------------------
    print(f"Connecting to {router_ip}...")
    ssh.connect(
        router_ip,
        port=port,
        username=username,
        password=password,
        look_for_keys=False,   # Don't use SSH keys stored on system
        allow_agent=False      # Don't use SSH agent authentication
    )
    print("Connected successfully!")

    # --------------------------------------------
    # Open interactive shell session on the router
    # --------------------------------------------
    remote_conn = ssh.invoke_shell()

    # --------------------------------------------
    # Send commands to router
    # --------------------------------------------
    remote_conn.send('enable\n')           # Enter privileged EXEC mode
    remote_conn.send(password + '\n')      # Provide enable password
    remote_conn.send('terminal length 0\n')  # Disable paging (no 'more' prompts)
    remote_conn.send('show running-config\n') # Command to get the full config

    # --------------------------------------------
    # Wait for the command to complete
    # --------------------------------------------
    time.sleep(2)  # Delay to allow router to generate full output

    # --------------------------------------------
    # Receive and decode the output from the router
    # --------------------------------------------
    output = remote_conn.recv(10000).decode('utf-8')

    # --------------------------------------------
    # Save the configuration to a text file
    # --------------------------------------------
    with open('router_config.txt', 'w') as f:
        f.write(output)
    
    print("Configuration saved to router_config.txt")

    # --------------------------------------------
    # Close the SSH connection
    # --------------------------------------------
    ssh.close()

# --------------------------------------------
# Error Handling for SSH connection issues
# --------------------------------------------
except Exception as e:
    print(f"Connection failed: {e}")
