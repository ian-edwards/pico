import network
from time import ticks_ms, ticks_add, ticks_diff, sleep
from ucollections import namedtuple
from secrets import NETWORK_SSID, NETWORK_PASSWORD
from settings import WLAN_CONNECT_TIMEOUT

def connect():
    timeout = ticks_add(ticks_ms(), WLAN_CONNECT_TIMEOUT)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(NETWORK_SSID, NETWORK_PASSWORD)
    while not wlan.isconnected() and ticks_diff(timeout, ticks_ms()) > 0:
        pass
    Result = namedtuple('WlanConnectResult', 'ssid connected status')
    return Result(NETWORK_SSID, wlan.isconnected(), wlan.status()) # todo stringify status
