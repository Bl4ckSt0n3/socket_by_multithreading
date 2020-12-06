import socket
import threading
import sys
import traceback

lock = threading.Lock()

def thread_function(cnn):

    while True:

        data = cnn.recv(1024)

        if not data:
            break
            lock.release()
            break
        cnn.send(data)
        
    cnn.close()

def run():

    _host = "127.0.0.1"
    _port = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:
    
        try:
            sc.bind((_host, _port))
        except:
            print("Bind failed. Error " + str(sys.exc_info()))
            sys.exit()

        sc.listen(6)
        print("Port listening...")
        
        while True:

            cnn, addr = sc.accept()
            lock.acquire()
            print("Connected with " + str(addr[0])+" : "+str(addr[1]))

            try:
                thread = threading.Thread(target=thread_function, args=(cnn, ))
                thread.start()
            except:
                traceback.print_exc()
        sc.close()


if __name__ == "__main__":

    run()   







