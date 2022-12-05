import socket

def get(url):
    sock = socket.socket()
    sockaddr = socket.getaddrinfo('www.micropython.org', 80)[0][-1]
    print(addr)