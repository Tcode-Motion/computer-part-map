import socket
import os
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

# Function to get the local IP address
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))  # Connect to an external server to get your local IP
    local_ip = s.getsockname()[0]
    s.close()
    return local_ip

# Check if we are on a Wi-Fi network
def is_on_wifi():
    # You can add your condition here to check if you're connected to a Wi-Fi network
    # For example, check if a specific network interface is active, or rely on IP address
    ip = get_local_ip()
    if ip.startswith("192.168."):  # Common range for local network IPs
        return True
    return False

# Start the server only if we're on Wi-Fi
if is_on_wifi():
    # Get the local IP address dynamically
    ip = get_local_ip()

    # Print the local IP address and let the user know the port to use
    print(f"Server is running on http://{ip}:8000")

    # Run the server without changing the directory (uses the current working directory)
    handler = SimpleHTTPRequestHandler
    httpd = TCPServer((ip, 8000), handler)
    httpd.serve_forever()
else:
    print("Not connected to a Wi-Fi network.")
