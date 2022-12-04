import log
import led
import wlan
from time import sleep

log.info('init system...')
log.info('init wlan...')
(wlan_connected, wlan_status) = wlan.connect()
log.info(wlan_connected)

while True:
    led.toggle()
    sleep(1)