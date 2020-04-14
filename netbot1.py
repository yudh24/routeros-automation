import paramiko
import getpass
import time

print(">>>Mikrotik Script Sender<<<")

hostname = '192.168.18.1'
username = 'admin'
password = ''

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=hostname, username=username, password=password, allow_agent=False, look_for_keys=False)

config_template = input('Nomer Template : ')

if config_template == "1":
    config_list = [
        'ip dns set servers=5.5.5.5',
        'ip address add address=192.168.1.1/24 interface=ether2',
    ]
else:
    config_list = [
        'ip dns set servers=2.2.2.2',
        'ip address add address=192.168.2.1/24 interface=ether2',
    ]

for config in config_list:
    ssh_client.exec_command(config)
    time.sleep(0.2)
