# IP-Based Load Balancer

This Python script distributes incoming clients among different servers based on a given IP address, creating a mechanism similar to `ip_hash`.

## How it Works?

1. The `servers` list contains the list of servers to be used as a load balancer.

2. The `get_server(ip_address)` function hashes the provided IP address and then uses the hash value to decide which server to route to.

3. To test with sample IP addresses, a `client_ips` list is created.

## Usage

```python
import hashlib

# List of servers
servers = ["backend1.example.com", "backend2.example.com", "backend3.example.com"]

def get_server(ip_address):
    
    return servers[server_index]

# Test
client_ips = ["123.23.45.123", "192.168.1.1", "10.0.0.1"]

for ip in client_ips:
    selected_server = get_server(ip)
    print(f"IP: {ip} => Routed Server: {selected_server}")
