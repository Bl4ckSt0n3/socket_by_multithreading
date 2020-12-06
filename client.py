import socket
import sys

_host = "127.0.0.1"
_port = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:

    try:
        sc.connect((_host, _port))
    except:
        print("Connection Error!")
        sys.exit()

    message = "hello, this is client !"
    
    while True:

        sc.send(message.encode())
        data = sc.recv(1024).decode()
        print("Recieved from the server : " + str(data))
        ans = input('\nDo you want to continue(y/n) :') 

        if ans == 'y': 
            continue
        else: 
            break

    sc.close()
