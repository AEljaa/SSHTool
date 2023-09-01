import paramiko

def ssh_run_script(hostname, username, password, script_path):
    try:
        # Create an SSH client instance
        ssh_client = paramiko.SSHClient()

        # Automatically add the server's host key (this is insecure, consider using ssh-keyscan)
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the remote host
        ssh_client.connect(hostname, username=username, password=password)

        # Execute the script on the remote computer
        stdin, stdout, stderr = ssh_client.exec_command(f"python {script_path}")
        
        # Optionally, you can handle the output and errors
        # output = stdout.read().decode('utf-8')
        # errors = stderr.read().decode('utf-8')

        # Close the SSH connection
        ssh_client.close()
        
        print("Script execution completed.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace these values with your own remote server's details
remote_hostname = "remote_server_ip_or_hostname"
remote_username = "your_remote_username"
remote_password = "your_remote_password"
remote_script_path = "/path/to/your/script.py"

# Call the function to execute the script remotely
ssh_run_script(remote_hostname, remote_username, remote_password, remote_script_path)
