import hashlib

# Sunucu listesi
servers = ["backend1.example.com", "backend2.example.com", "backend3.example.com"]

def get_server(ip_address):
    """
    Purpose:
      this function gets the ip-address and perform the result
    Parameters:
      ip_address (array(string)): string array
    Return:
      int value
    """
    # IP adresini SHA-256 ile hash yap
    hashed_ip = hashlib.sha256(ip_address.encode()).hexdigest()

    # Hash değerini integer'a dönüştür
    hash_value = int(hashed_ip, 16)

    # Hash değerini sunucu sayısına mod alarak hangi sunucuya yönlendirileceğine karar ver
    server_index = hash_value % len(servers)

    return servers[server_index]

# Test
client_ips = ["123.23.45.123", "192.168.1.1", "10.0.0.1","23.34.156.201"]

for ip in client_ips:
    selected_server = get_server(ip)
    print(f"IP: {ip} => Redirected Server at : {selected_server}")
