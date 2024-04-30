import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print("Connecting via SSH => show run")
#
from netmiko import ConnectHandler
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="172.17.1.2",
    port="22",
    username="admin",
    password="cisco"
    )
output=sshCli.send_command("show run")
print(output)