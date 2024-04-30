import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print("Connecting via SSH => show run")
#
from netmiko import ConnectHandler
router1 = ConnectHandler(
    device_type="cisco_ios",
    host="172.17.1.2",
    port="22",
    username="admin",
    password="cisco"
    )
router2 = ConnectHandler(
    device_type="cisco_ios",
    host="172.17.1.2",
    port="22",
    username="admin",
    password="cisco"
    )
output=router1.send_command("show run")
output2=router2.send_command("show run")
print("Router1: " + output)
print("Router2: " + output2)