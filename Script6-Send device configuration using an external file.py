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
    
    print("\nRouter 1: Sending configuration from file...")
    with open("router1_config.txt", "r") as f1:
        config1 = f1.read()
    output1 = router1.send_config_set(config1.splitlines())
    print(output1)
    
    print("\nRouter 2: Sending configuration from file...")
    with open("router2_config.txt", "r") as f2:
        config2 = f2.read()
    output2 = router2.send_config_set(config2.splitlines())
    print(output2)
