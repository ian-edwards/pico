import re

__all__ = ['port']

regex = re.compile('^[^:]*')

def port(url):
    match = regex.match(url)
    value = match.group(0)
    if value == 'http':
        return (True, 80)
    elif value == 'https':
        return 443
    else:
        return None