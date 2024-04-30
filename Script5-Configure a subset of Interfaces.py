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
    print("Current date and time: ", datetime.datetime.now())
    
    print("Connecting to routers...")
    router1 = connect_to_device("172.17.1.2")
    router2 = connect_to_device("172.17.1.3")
    
    interface_commands = [
        "interface GigabitEthernet0/0/0.20",
        "description Link to Switch",
        "ip address 192.168.1.1 255.255.255.0",
        "no shutdown"
    ]
    
    print("\nRouter 1: Configuring interfaces...")
    output1 = router1.send_config_set(interface_commands)
    print(output1)
    
    print("\nRouter 2: Configuring interfaces...")
    output2 = router2.send_config_set(interface_commands)
    print(output2)
