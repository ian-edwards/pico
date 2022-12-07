from ucollections import namedtuple

def info(url):
    Result = namedtuple('UrlInfoResult', 'success address port')
    (port_ok, port, port_length) = _port(url)
    print(port_ok)
    print(port)
    print(port_length)
    return Result(True, _address(url), port)

def _address(url):
    return f'google.com'

def _protocol(url):
    Result = namedtuple('UrlProtocolResult', 'success value length')
    for i in range(len(url)):
        if (url[i] == ':'):
            return Result(True, url[:i-1], i)
    return Result(False, None, 0)

def _port(url):
    protocol = _protocol(url)
    if protocol == 'http':
        return (True, 80)
    elif protocol == 'https':
        return 443
    else:
        return None
    
def _root(url):
    return 'google'

def _tld(url):
    return 'com'
