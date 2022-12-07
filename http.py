import socket
import url

def get(urlv):
    (address, port) = url.info(urlv)
    addr = socket.getaddrinfo(address, port)[0][-1]
    print(addr)