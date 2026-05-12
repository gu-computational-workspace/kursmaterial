import configparser

# Skapa en konfigurationsparser
config = configparser.ConfigParser()

# Läs in konfigurationsfilen
config.read('configuration/config.ini')

# Hämta värden från konfigurationsfilen
username = config.get('Settings', 'username')
password = config.get('Settings', 'password')
server = config.get('Settings', 'server')
port = config.getint('Settings', 'port')

# Använd inställningarna i din kod
print(f"Ansluter till {server} på port {port} med användarnamn {username} och lösenord {password}")

if False:
    # Uppdatera värden
    config.set('Settings', 'password', 'new_secret')

    # Spara ändringar till konfigurationsfilen
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
