# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-FileContributor: Modified 2021 by Alasdair Allan for Babilim Light Industries
# SPDX-License-Identifier: MIT

# Modified from Si7021 sensor example to use Raspberry Pi Pico on-board LED and RP2040 on-chip temperature sensor
# https://learn.adafruit.com/using-lorawan-and-the-things-network-with-circuitpython/using-tinylora

import time
import busio
import digitalio
import board
import microcontroller
from adafruit_tinylora.adafruit_tinylora import TTN, TinyLoRa

# Board LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Create library object using our bus SPI port for radio
spi = busio.SPI(board.GP18, MOSI=board.GP19, MISO=board.GP16)

# RFM9x Breakout Pinouts
cs = digitalio.DigitalInOut(board.GP8)
irq = digitalio.DigitalInOut(board.GP7)
rst = digitalio.DigitalInOut(board.GP9)

# TTN Device Address, 4 Bytes, MSB
devaddr = bytearray([0x00, 0x00, 0x00, 0x00])

# TTN Network Key, 16 Bytes, MSB
nwkey = bytearray( [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ] )

# TTN Application Key, 16 Bytess, MSB
app = bytearray( [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ] )

ttn_config = TTN(devaddr, nwkey, app, country="EU")

lora = TinyLoRa(spi, cs, irq, rst, ttn_config)

# Data Packet to send to TTN
data = bytearray(2)

while True:
    temp_val = microcontroller.cpu.temperature
    print("Temperature: %0.2f C" % temp_val)

    # Encode float as int
    temp_val = int(temp_val * 100)

    # Encode payload as bytes
    data[0] = (temp_val >> 8) & 0xFF
    data[1] = temp_val & 0xFF

    # Send data packet
    print("Sending packet...")
    lora.send_data(data, len(data), lora.frame_counter)
    print("Packet Sent!")
    led.value = True
    lora.frame_counter += 1
    time.sleep(2)
    led.value = False
