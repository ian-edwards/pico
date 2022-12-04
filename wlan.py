import network
from time import ticks_ms, sleep
from ucollections import namedtuple
from secret import NETWORK_SSID, NETWORK_PASSWORD
from settings import WLAN_CONNECT_TIMEOUT, WLAN_CONNECT_POLL_INTERVAL

def connect():
    start = ticks_ms()
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(NETWORK_SSID, NETWORK_PASSWORD)
    while not wlan.isconnected():
        sleep(WLAN_CONNECT_POLL_INTERVAL)
    Result = namedtuple('WlanConnectResult', 'ssid connected status')
    return Result(NETWORK_SSID, wlan.isconnected(), wlan.status()) # todo stringify status
