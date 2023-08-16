import machine
import time

led = machine.Pin(2, machine.Pin.OUT)

while True:
    for i in range(3):
        print("ON")
        led.on()
        time.sleep(0.1)

        print("OFF")
        led.off()
        time.sleep(0.1)
    time.sleep(1)
