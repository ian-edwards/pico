from network import WLAN, STA_IF
from network_ssid import *
from network_password import *

wlan = WLAN(STA_IF)
wlan.active(True)
wlan.connect(NETWORK_SSID, NETWORK_PASSWORD)

print(wlan.isconnected())