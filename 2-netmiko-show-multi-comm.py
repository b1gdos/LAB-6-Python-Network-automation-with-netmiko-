import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print("Connecting via SSH => Show multi commands")
from netmiko import ConnectHandler
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="172.17.1.1",
    port="22",
    username="admin",
    password="cisco"
    )
intBrief=sshCli.send_command("show ip interface brief")
routingTable=sshCli.send_command("show ip route")
print(intBrief + routingTable)