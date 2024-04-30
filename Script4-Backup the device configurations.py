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
    
    print("\nRouter 1: Saving configuration...")
    output1 = router1.send_command("show running-config")
    with open("router1_config.txt", "w") as f1:
        f1.write(output1)
    print("Configuration saved to router1_config.txt")
    
    print("\nRouter 2: Saving configuration...")
    output2 = router2.send_command("show running-config")
    with open("router2_config.txt", "w") as f2:
        f2.write(output2)
    print("Configuration saved to router2_config.txt")
