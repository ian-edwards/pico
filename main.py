import log
import led
import wlan
from time import sleep

log.info('system init...')
log.info('wlan init...')
(wlan_ssid, wlan_connected, wlan_status) = wlan.connect()
if wlan_connected:
    log.info(f'wlan connected')
else:
    log.error(f'wlan error: {wlan_status}')

while True:
    led.toggle()
    sleep(1)