import socket
import url

def get(uri):
    #sock = socket.socket()
    port = url.port(uri)
    print(port)
    addr = socket.getaddrinfo('google.com', port)[0][-1]
    print(addr)