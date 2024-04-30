# LAB-6-Python-Network-automation-with-netmiko

Network Automation with Netmiko
Netmiko is a Python library that simplifies the process of interacting with network devices using various network protocols such as SSH and Telnet. It provides a simple and consistent interface to automate tasks on network devices, making it an essential tool for network engineers and administrators.

Features
SSH and Telnet Support: Netmiko supports both SSH and Telnet connections to network devices, allowing for secure remote management.
Device Agnostic: It works with a wide range of network devices from different vendors, including Cisco, Juniper, Arista, and more.
Simplified Automation: Netmiko provides a simple and consistent interface to send commands, configure devices, and retrieve information from network devices.
Parallel Execution: It supports parallel execution of commands on multiple devices, improving efficiency and reducing execution time.
Configuration Backup: Netmiko enables easy backup of device configurations, helping to maintain configuration backups for disaster recovery and auditing purposes.
Getting Started
To get started with Netmiko, you'll need to install the library using pip:
```
pip install netmiko
```

Once installed, you can start writing Python scripts to automate tasks on network devices. Here's a simple example to establish an SSH connection to a device and send a command:
```
from netmiko import ConnectHandler

# Define device parameters
device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'password'
}

# Connect to the device
connection = ConnectHandler(**device)

# Send a command
output = connection.send_command('show version')
print(output)

# Disconnect from the device
connection.disconnect()
```

# My labo and script are based on this labo design

![image](https://github.com/b1gdos/LAB-6-Python-Network-automation-with-netmiko-/assets/70448476/8eff871f-7a67-47e9-92ae-e4bd06ac8ed5)

And is configured as follow:

```
# Switch 1 Configuration

hostname LAB-RA0X-A01-SW01
banner motd ^No Unauthorized Access Allow^
line con 0
  password cisco
  login
  exit
ip domain name data.labnet.local
crypto key generate rsa
line vty 0 15
  password cisco
  login local
  transport input ssh
  exit
username admin privilege 15 secret cisco
service password-encryption
vlan 11
  name Management
vlan 12
  name Data_Users
vlan 13
  name Voice-Users
vlan 14
  name Reserved
vlan 99
  name Native
spanning-tree mode rapid-pvst
spanning-tree vlan 11,12,13,14 root primary 
interface range GigabitEthernet1/0/21 - 22
  channel-group 1 mode active
interface Port-channel 1
  description LAG SW1-SW2
  switchport mode trunk
  switchport trunk allowed vlan 11,12,13,14
  switchport trunk native vlan 99
  spanning-tree link-type point-to-point
  exit
ip default-gateway 172.17.1.1
interface Vlan11
  ip address 172.17.1.4 255.255.255.240

```
```
# Switch 1 to Switch 3 Configuration

interface range GigabitEthernet1/0/23 - 24
  channel-group 2 mode active
interface Port-channel 2
  description LAG SW1-SW3
  switchport mode trunk
  switchport trunk allowed vlan 11,12,13,14,99
  switchport trunk native vlan 99
  spanning-tree link-type point-to-point
```

```
# Switch 1 to Router 1 Configuration

interface GigabitEthernet 1/0/20
  description LAG SW1-R1
  switchport mode trunk
  switchport trunk allowed vlan 11,12,13,14,99
  switchport trunk native vlan 99
  spanning-tree link-type point-to-point
```

```
# Switch 2 Configuration

hostname LAB-RA0X-A01-SW02
banner motd ^No Unauthorized Access Allow^
line con 0
  password cisco
  login
  exit
ip domain name data.labnet.local
crypto key generate rsa
line vty 0 15
  password cisco
  login local
  transport input ssh
  exit
username admin privilege 15 secret cisco
service password-encryption
vlan 11
  name Management
vlan 12
  name Data_Users
vlan 13
  name Voice-Users
vlan 14
  name Reserved
vlan 99
  name Native
spanning-tree mode rapid-pvst
spanning-tree vlan 11,12,13,14 priority 4096
interface range GigabitEthernet 1/0/21 - 22
  channel-group 1 mode passive
interface Port-channel 1
  description LAG SW2-SW1
  switchport mode trunk
  switchport trunk allowed vlan 11,12,13,14,99
  switchport trunk native vlan 99
  spanning-tree link-type point-to-point
ip default-gateway 172.17.1.1
interface Vlan11
  ip address 172.17.1.5 255.255.255.240
```

```
# Switch 2 to Switch 3 Configuration

interface range GigabitEthernet1/0/23 - 24
  channel-group 3 mode active
interface Port-channel 3
  description LAG SW2-SW3
  switchport mode trunk
  switchport trunk allowed vlan 11,12,13,14,99
  switchport trunk native vlan 99
  spanning-tree link-type point-to-point
```

```
# Switch 2 to Router 2 Configuration

interface GigabitEthernet 1/0/20
  description SW2-R2
  switchport mode trunk
  switchport trunk allowed vlan 11,12,13,14,99
  switchport trunk native vlan 99
  spanning-tree link-type point-to-point
```

```
# Switch 3 to Switch 1 Configuration

hostname LAB-RA0X-A01-SW03
banner motd ^No Unauthorized Access Allow^
line con 0
  password cisco
  login
  exit
ip domain name data.labnet.local
crypto key generate rsa
line vty 0 15
  password cisco
  login local
  transport input ssh
  exit
username admin privilege 15 secret cisco
service password-encryption
vlan 11
  name Management
vlan 12
  name Data_Users
vlan 13
  name Voice-Users
vlan 14
  name Reserved
vlan 99
  name Native
spanning-tree mode rapid-pvst
spanning-tree vlan 11,12,13,14 priority 8192
interface range FastEthernet0/21 - 22
  channel-group 2 mode passive
interface Port-channel 2
  description LAG SW3-SW1
  switchport mode trunk
  switchport trunk allowed vlan 11,12,13,14,99
  switchport trunk native vlan 99
  spanning-tree link-type point-to-point
interface range FastEthernet0/23 - 24
  channel-group 3 mode passive
interface Port-channel 3
  description LAG SW3-SW2
  switchport mode trunk
  switchport trunk allowed vlan 11,12,13,14,99
  switchport trunk native vlan 99
  spanning-tree link-type point-to-point
ip default-gateway 172.17.1.1
interface Vlan11
  ip address 172.17.1.6 255.255.255.240
```

```
# Router 1 Configuration

hostname LAB-RA0X-C01-R01
enable secret cisco
banner motd ^No Unauthorized Access Allow^
ip domain name data.labnet.be
username admin privilege 15 secret cisco
service password-encryption 
line con 0
  password cisco
  login
line vty 0  4
  password cisco
  login local
  transport input ssh
  exit
crypto key generate rsa modulus 2048
ip ssh version 2
ip ssh time-out 120
ip ssh authentication-retries 3
login block-for 180 attempts 3 within 50
interface GigabitEthernet0/0/0
  no shutdown
interface GigabitEthernet0/0/0.11
  encapsulation dot1Q 11
  ip address 172.17.1.2 255.255.255.240
  standby 110 ip 172.17.1.1
  standby 110 priority 110
  standby 110 preempt
  no shutdown
interface GigabitEthernet0/0/0.12
  encapsulation dot1Q 12
  ip address 172.17.1.18 255.255.255.240
  standby 110 ip 172.17.1.17
  standby 110 priority 110
  standby 110 preempt
  no shutdown
interface GigabitEthernet0/0/0.13
  encapsulation dot1Q 13
  ip address 172.17.1.34 255.255.255.240
  standby 110 ip 172.17.1.33
  standby 110 priority 110
  standby 110 preempt
  no shutdown
interface GigabitEthernet0/0/0.14
  encapsulation dot1Q 14
  ip address 172.17.1.50 255.255.255.240
  standby 110 ip 172.17.1.49
  standby 110 priority 110
  standby 110 preempt
  no shutdown
interface GigabitEthernet0/0/1
  no shutdown
  ip address 10.199.65.101 255.255.255.224
  ip route 172.17.1.0 255.255.255.240 10.199.65.100
  ip route 172.17.1.16 255.255.255.240 10.199.65.100
  ip route 172.17.1.32 255.255.255.240 10.199.65.100
  ip route 172.17.1.48 255.255.255.240 10.199.65.100
  ip route 0.0.0.0 0.0.0.0 10.199.65.100
  ip helper-address 10.199.64.66
```

```
# Router 2 Configuration

hostname LAB-RA0X-C01-R02
enable secret cisco
banner motd ^No Unauthorized Access Allow^
ip domain name data.labnet.be
username admin privilege 15 secret cisco
service password-encryption 
line con 0
  password cisco
  login
line vty 0  4
  password cisco
  login local
  transport input ssh
  exit
crypto key generate rsa modulus 2048
ip ssh version 2
ip ssh time-out 120
ip ssh authentication-retries 3
login block-for 180 attempts 3 within 50
interface GigabitEthernet0/0/0
  no shutdown
interface GigabitEthernet0/0/0.11
  encapsulation dot1Q 11
  ip address 172.17.1.3 255.255.255.240
  standby 110 ip 172.17.1.1
  standby 110 priority 100
  standby 110 preempt
  no shutdown
interface GigabitEthernet0/0/0.12
  encapsulation dot1Q 12
  ip address 172.17.1.19 255.255.255.240
  standby 110 ip 172.17.1.17
  standby 110 priority 100
  standby 110 preempt
  no shutdown
interface GigabitEthernet0/0/0.13
  encapsulation dot1Q 13
  ip address 172.17.1.35 255.255.255.240
  standby 110 ip 172.17.1.33
  standby 110 priority 100
  standby 110 preempt
  no shutdown
interface GigabitEthernet0/0/0.14
  encapsulation dot1Q 14
  ip address 172.17.1.51 255.255.255.240
  standby 110 ip 172.17.1.49
  standby 110 priority 100
  standby 110 preempt
  no shutdown
interface GigabitEthernet0/0/1
  no shutdown
  ip address 10.199.65.201 255.255.255.224
  ip route 172.17.1.0 255.255.255.240 10.199.65.200
  ip route 172.17.1.16 255.255.255.240 10.199.65.200
  ip route 172.17.1.32 255.255.255.240 10.199.65.200
  ip route 172.17.1.48 255.255.255.240 10.199.65.200
  ip route 0.0.0.0 0.0.0.0 10.199.65.200
  ip helper-address 10.199.64.66
```
