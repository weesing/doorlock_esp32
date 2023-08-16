# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
# esp.osdebug(None)
import webrepl
import network
import json
import time

webrepl.start()

secretsJson = open('boot.secrets.json', "r")
secrets = json.load(secretsJson)
wifiSsid = secrets["wifi_ssid"]
wifiPassword = secrets["wifi_password"]
print(wifiSsid)
print(wifiPassword)

sta_if = network.WLAN(network.STA_IF)
print(sta_if.active())
sta_if.active(True)
sta_if.connect(wifiSsid, wifiPassword)
sta_if.active()
while not sta_if.isconnected():
    print("Waiting...")
    time.sleep(1)

print(sta_if.ifconfig())
print(sta_if.isconnected())
