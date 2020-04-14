import paramiko
import getpass
import time

print(">>>Mikrotik Script Sender<<<")

hostname = input('Tujuan : ')
username = input('Username : ')
password = getpass.getpass()

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=hostname, username=username, password=password, allow_agent=False, look_for_keys=False)


config_list = [
    'ip dns set servers=5.5.5.5',
    'ip address add address=192.168.1.1/24 interface=ether2',
]


for config in config_list:
    ssh_client.exec_command(config)
    time.sleep(0.2)
