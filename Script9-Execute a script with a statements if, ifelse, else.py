# Script using Functions or Classes

from netmiko import ConnectHandler

class RouterConfigurator:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.connection = self.connect_to_device()

    def connect_to_device(self):
        return ConnectHandler(
            device_type="cisco_ios",
            host=self.host,
            port=22,
            username=self.username,
            password=self.password
        )

    def configure_interface(self, interface, description, ip_address, subnet_mask):
        interface_commands = [
            f"interface {interface}",
            f"description {description}",
            f"ip address {ip_address} {subnet_mask}",
            "no shutdown"
        ]
        return self.connection.send_config_set(interface_commands)

if __name__ == "__main__":
    router1 = RouterConfigurator("172.17.1.2", "admin", "cisco")
    router2 = RouterConfigurator("172.17.1.3", "admin", "cisco")

    router1.configure_interface("GigabitEthernet0/0/0.20", "Link to Switch", "192.168.1.1", "255.255.255.0")
    router2.configure_interface("GigabitEthernet0/0/0.20", "Link to Switch", "192.168.1.1", "255.255.255.0")
