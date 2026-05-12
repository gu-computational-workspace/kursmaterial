# main.py

from config import config

# Använd inställningarna
username = config['username']
password = config['password']
server = config['server']
port = config['port']

# Använd inställningarna i din kod
print(
    f"Ansluter till {server} på port {port} med användarnamn {username} och lösenord {password}")
