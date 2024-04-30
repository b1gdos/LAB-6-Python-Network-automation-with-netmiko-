import datetime
from netmiko import ConnectHandler

def connect_to_device(host, username, password):
    return ConnectHandler(
        device_type="cisco_ios",
        host=host,
        username=username,
        password=password,
        port=22,  # Assuming SSH port
        secret=password  # Enable password if required
    )

def configure_interfaces(device, interface, ip_address, subnet_mask, description):
    config_commands = [
        f"interface {interface}",
        f"description {description}",
        f"ip address {ip_address} {subnet_mask}",
        "no shutdown",
        "exit"
    ]
    output = device.send_config_set(config_commands)
    return output

def configure_ntp(device, ntp_server):
    config_commands = [
        "ntp server " + ntp_server
    ]
    output = device.send_config_set(config_commands)
    return output

def disable_telnet(device):
    output = device.send_config_set(["no service telnet"])
    return output

def backup_config(device, filename):
    output = device.send_command("show running-config")
    with open(filename, "w") as file:
        file.write(output)

if __name__ == "__main__":
    print("Welcome to the Network Automation Script!")
    print("Current date and time: ", datetime.datetime.now())
    
    # Device details
    devices = [
        {
            "host": "172.17.1.2",
            "username": "admin",
            "password": "cisco"
        },
        {
            "host": "172.17.1.3",
            "username": "admin",
            "password": "cisco"
        }
    ]
    
    # Connect to devices
    for device_info in devices:
        device = connect_to_device(**device_info)
        
        # Configure NTP server
        print(f"\nConfiguring NTP server on {device_info['host']}...")
        ntp_output = configure_ntp(device=device, ntp_server="10.199.64.66")
        print(ntp_output)
        
        # Disable Telnet
        print(f"\nDisabling Telnet on {device_info['host']}...")
        telnet_output = disable_telnet(device=device)
        print(telnet_output)
        
        device.disconnect()
    
    print("\nScript execution completed successfully!")
    print("Goodbye!")