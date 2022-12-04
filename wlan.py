import network
from secret import NETWORK_SSID, NETWORK_PASSWORD
from ucollections import namedtuple

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(NETWORK_SSID, NETWORK_PASSWORD)
    Result = namedtuple('WlanConnectResult', 'connected status')
    return Result(wlan.isconnected(), wlan.status()) # todo stringify status
