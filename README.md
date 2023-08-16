# Pre-requisites

- Python3
- `pip`

# Install `esptool.py`

```
pip install esptool
```

# Flash ESP32 Micropython Firmware

- Download the firmware at https://micropython.org/download/esp32/ under _Releases_
- Refer to instructions at https://micropython.org/download/esp32/ to erase flash and flash the firmware again.

# Setup VSCode (PyMakr)

- Install `PyMakr` plugin.
- Right-click on **doorlock** folder -> **pymakr** menu item -> **Upload to device**.
- Press the **en** button on ESP32 to reboot.

> Tip: Every time code is uploaded to ESP32 will require a reboot.

# Setup Wifi

- Make a copy of `boot.secrets.sample.json` and name it `boot.secrets.json`.
- Fill in your SSID and password in there.
- Upload the code using PyMakr

# Setup WebRepl (Optional)

> It is optional to setup WebRepl. But it is not setup, the `boot.py` will encounter an error, but will continue to boot.

- Open a terminal connected to the ESP32.
- Type in the following script:

```
import webrepl_setup
```

- Follow the on-screen instruction.

## Connecting to WebRepl

- You will need the IP address of the ESP32.
- Using the terminal connected to the ESP32, look at the logs during startup which will print out the IP address.
- Go to the browser and put in the address `ws://<ESP32 IP address>:8266` to connect.

# Checking Boot Sequence

- Using a terminal connected to the ESP32, observe the boot logs which should print out some basic information (e.g. IP address).
