import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print("Connecting via SSH => disable vlan 1 from unused ports")

from netmiko import ConnectHandler

sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="172.17.1.4",
    port="22",
    username="admin",
    password="cisco"
    )

# Establish SSH connection
#ssh_connection = ConnectHandler(**device)

# Configuration to shut down VLAN 1 on ports 2 to 19
vlan_config = [
    'interface range g 1/0/2 - 19',
    'shutdown',
]

# Execute configuration commands
output = sshCli.send_config_set(vlan_config)
print(output)

# Configuration to allow SSH access for the new user
ssh_config = [
    'username ozzie privilege 15 secret cisco',  # Create a new user
    'line vty 0 15',
    'login local',
    'transport input ssh'
]

# Execute configuration commands
output = sshCli.send_config_set(ssh_config)
print(output)

# Close SSH connection
#ssh_connection.disconnect()