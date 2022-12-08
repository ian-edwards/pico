import socket

def get(url):
    protocol, _, host, path = url.split('/', 3)
    port = 443 if protocol.startswith('https') else (80 if protocol.startswith('http') else None)
    addr = socket.getaddrinfo(host, port, 0, socket.SOCK_STREAM)[0][-1]
    sock = socket.socket()
    sock.connect(addr)
    sock.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = sock.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    sock.close()