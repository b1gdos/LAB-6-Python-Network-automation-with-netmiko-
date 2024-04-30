import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print("Connecting via SSH => Connect to Multiple Devices")

from netmiko import ConnectHandler

def connect_to_devices(devices):
    connections = []
    for device in devices:
        connection = ConnectHandler(**device)
        connections.append(connection)
    return connections

if __name__ == "__main__":
    devices = [
        {
            'device_type': 'cisco_ios',
            'host': '172.17.1.2',
            'username': 'admin',
            'password': 'cisco',
        },
        {
            'device_type': 'cisco_ios',
            'host': '172.17.1.3',
            'username': 'admin',
            'password': 'cisco',
        }
    ]
    connections = connect_to_devices(devices)
    print("Connections established successfully.")
