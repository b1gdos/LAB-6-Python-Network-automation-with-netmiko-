import datetime
from netmiko import ConnectHandler

def connect_to_device(device):
    return ConnectHandler(**device)

if __name__ == "__main__":
    print("Current date and time: ", datetime.datetime.now())
    
    print("Connecting to switches...")
    router1 = connect_to_device({
        "device_type": "cisco_ios",
        "host": "172.17.1.4",
        "port": 22,
        "username": "admin",
        "password": "cisco"
    })
    
    router2 = connect_to_device({
        "device_type": "cisco_ios",
        "host": "172.17.1.5",
        "port": 22,
        "username": "admin",
        "password": "cisco"
    })
    
    print("\nSwitch 1: Connected successfully!")
    print("Swtich 2: Connected successfully!")
