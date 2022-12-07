import led
import wlan
import http
from time import sleep

print('system init...')
print('wlan init...')
(wlan_ssid, wlan_connected, wlan_status) = wlan.connect()
if wlan_connected:
    print('wlan OK!')
    http.get('https://google.com')
else:
    print(f'wlan error: {wlan_status}')

while True:
    led.toggle()
    sleep(1)