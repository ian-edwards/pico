import network
from time import ticks_ms, ticks_add, ticks_diff, sleep
from ucollections import namedtuple
from secrets import NETWORK_SSID, NETWORK_PASSWORD
from settings import WLAN_CONNECT_TIMEOUT

def connect():
    timeout = ticks_add(ticks_ms(), WLAN_CONNECT_TIMEOUT)
    print(timeout)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(NETWORK_SSID, NETWORK_PASSWORD)
    while not (wlan.isconnected() or _istimeout(timeout)):
        pass
    if _istimeout(timeout):
        wlan.disconnect()
    Result = namedtuple('WlanConnectResult', 'ok, status, ssid')
    statuscode = wlan.status()
    return Result(wlan.isconnected(), wlan.status(), NETWORK_SSID)
    
def _istimeout(timeout):
    ticks_diff(timeout, ticks_ms()) <= 0