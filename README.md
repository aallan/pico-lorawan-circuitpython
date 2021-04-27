# Raspberry Pi Pico and LoRaWAN from CircuitPython

Enable LoRaWAN communications on your [Raspberry Pi Pico](https://www.raspberrypi.org/products/raspberry-pi-pico/) or any RP2040-based board using [CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/) and the Adafruit [TinyLoRa](https://github.com/adafruit/TinyLoRa) library. 


![Wiring diagram](/images/pico-and-rfm9x.png)

Pico | RP2040 | SX1276 Module | RFM95W Breakout
------------ | ------------- | ------------ | -------------
3V3 (OUT) | — | VCC | VIN
GND | GND | GND | GND
Pin 10 | GP7 | DIO0 | G0
Pin 11 | GP8 | NSS | CS
Pin 12 | GP9 | RESET | RST
Pin 14 | GP10 | DIO1 | G1
Pin 21 | GP16 (SPI0 RX) | MISO | MISO
Pin 24 | GP 18 (SPI0 SCK) | SCK | SCK
Pin 25 | GP19 (SPI0 TX) | MOSI | MOSI

## Setting up The Things Network


## Adding Keys


## Deploying to Pico

Copy the contents of the [`src/`](https://github.com/aallan/pico-lorawan-circuitpython/tree/main/src) directory to your `CIRCUITPY` drive.

* the code.py file
* the `lib/` folder and all of its contents (including subfolders and `.mpy` files)


## Decoder

We're sending out temperature reading as a byte array

```C
temp = microcontroller.cpu.temperature
temp = int(temp * 100)

data = bytearray(2)
data[0] = (temp >> 8) & 0xFF
data[1] = temp & 0xFF
```

By default the payload is displayed as a hexidecimal values in the Network Console. However we can add a 

```javascript
function Decoder(bytes, port) {
  var decoded = {};

  // Decode bytes to int
  var celciusInt = (bytes[0] << 8) | bytes[1];
  
  // Decode int to float
  decoded.temp = celciusInt / 100;

  return decoded;
```

## Bill of Materials

Item | Link 
------------ | -------------
Raspberry Pi Pico | https://www.raspberrypi.org/products/raspberry-pi-pico/
Adafruit FRM95x Lora Radio | https://www.adafruit.com/product/3072
Edge-Mount SMA Connector | https://www.adafruit.com/product/1865
868MHz or 915MHz Antenna | https://www.adafruit.com/product/3340
Male-Female Jumper Wires | https://www.adafruit.com/product/1953

## License

This software is released under the [MIT License](https://opensource.org/licenses/MIT).

Copyright 2021, Alasdair Allan

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.