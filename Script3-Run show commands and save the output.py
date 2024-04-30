import datetime
from netmiko import ConnectHandler

def connect_to_device(host):
    return ConnectHandler(
        device_type="cisco_ios",
        host=host,
        port=22,
        username="admin",
        password="cisco"
    )

if __name__ == "__main__":
    with open("showCommands.txt", "w") as f:
        f.write("Current date and time: {}\n".format(datetime.datetime.now()))
        
        f.write("Connecting to routers...\n")
        router1 = connect_to_device("172.17.1.2")
        router2 = connect_to_device("172.17.1.3")
        
        show_commands = ["show interfaces", "show ip route"]
        
        f.write("\nRouter 1: Sending show commands...\n")
        output1 = {}
        for cmd in show_commands:
            output1[cmd] = router1.send_command(cmd)
            f.write(output1[cmd] + "\n")
        
        f.write("\nRouter 2: Sending show commands...\n")
        output2 = {}
        for cmd in show_commands:
            output2[cmd] = router2.send_command(cmd)
            f.write(output2[cmd] + "\n")
