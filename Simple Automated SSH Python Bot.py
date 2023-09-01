import getpass
from fabric import Connection, Config

#for loop to iterate through a list of ip addresses and run the script on each one
#ask how many connections are needed
password=getpass.getpass('Enter your root password: ')
username=input('Enter your username: ')
ip=input('Enter your ip address: ')
config = Config(overrides={'sudo': {'password': password}})

connection = Connection(ip,user=username,config=config)
#run command for pyjmt
connection.run('pwd')
#wait for simualtion data to be produced and then upload it 
#connection.put('data.csv', remote='/home/username/data.csv')???

