from machine import Pin

__all__ = ['on', 'off', 'toggle']

led = Pin('LED', Pin.OUT)

def on():
    led.on()

def off():
    led.off()

def toggle():
    led.toggle()