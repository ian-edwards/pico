import led
import wlan
import http
from time import sleep

led.off()
print('system init...')
print('wlan init...')
(wlan_ok, wlan_status, wlan_ssid) = wlan.connect()
if wlan_ok:
    print(f'wlan \'{wlan_ssid}\' OK!')
    http.get('http://micropython.org/ks/test.html')
else:
    print(f'wlan ERROR! {wlan_status}')