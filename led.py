from machine import Pin

_led = Pin('LED', Pin.OUT)

def on():
    _led.on()

def off():
    _led.off()

def toggle():
    _led.toggle()