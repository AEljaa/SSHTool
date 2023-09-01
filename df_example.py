import paramiko

command = "df"

# Update the next three lines with your
# server's information

host = "YOUR_IP_ADDRESS"
username = "YOUR_LIMITED_USER_ACCOUNT"
password = "YOUR_PASSWORD"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
_stdin, _stdout,_stderr = client.exec_command("df")
print(_stdout.read().decode())
client.close()