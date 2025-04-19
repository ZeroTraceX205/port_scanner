import socket
from datetime import datetime

target = input("Enter target IP or domain: ")
print(f"\nScanning target: {target}")
print("Scan started at:", datetime.now())
print("-" * 50)

try:
    for port in range(1, 101):  # You can increase range
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
except socket.gaierror:
    print("Hostname could not be resolved.")
except socket.error:
    print("Couldn't connect to server.")
