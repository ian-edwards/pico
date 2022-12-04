import led
import wlan
import http
from time import sleep
from urequests import get

print('system init...')
print('wlan init...')
(wlan_ssid, wlan_connected, wlan_status) = wlan.connect()
if wlan_connected:
    print('wlan connected')
    http.get('http://ip-api.com/json/')
else:
    print(f'wlan error: {wlan_status}')

while True:
    led.toggle()
    sleep(1)