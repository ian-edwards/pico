from machine import Pin

_led = Pin("LED", Pin.OUT)

def led_on():
    _led.on()

def led_off():
    _led.off()

def led_toggle():
    _led.toggle()