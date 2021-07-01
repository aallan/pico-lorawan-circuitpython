# Raspberry Pi Pico and LoRaWAN from CircuitPython

![Hero image](/images/hero-image.jpg)

Enable LoRaWAN communications on your [Raspberry Pi Pico](https://www.raspberrypi.org/products/raspberry-pi-pico/) or any RP2040-based board using [CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/) and the Adafruit [TinyLoRa](https://github.com/adafruit/Adafruit_CircuitPython_TinyLoRa) library. Based on the TinyLoRa [example code](https://learn.adafruit.com/using-lorawan-and-the-things-network-with-circuitpython/using-tinylora#the-code-3010429-2) by Adafruit.

## Bill of Materials

The following hardware is needed:

Item | Link 
------------ | -------------
Raspberry Pi Pico | https://www.raspberrypi.org/products/raspberry-pi-pico/
Adafruit RFM95x Lora Radio | https://www.adafruit.com/product/3072
Edge-Mount SMA Connector | https://www.adafruit.com/product/1865
868MHz or 915MHz Antenna | https://www.adafruit.com/product/3340
Male-Female Jumper Wires | https://www.adafruit.com/product/1953
Breadboard | https://www.adafruit.com/product/64

## Wiring the RFM9x Radio Module

![Wiring diagram](/images/pico-and-rfm9x.png)

After [soldering](https://learn.adafruit.com/adafruit-rfm69hcw-and-rfm96-rfm95-rfm98-lora-packet-padio-breakouts/assembly#step-2433237) your RFM95x module and attaching [an antenna](https://learn.adafruit.com/adafruit-rfm69hcw-and-rfm96-rfm95-rfm98-lora-packet-padio-breakouts/assembly#antenna-options-2433239-6) the mapping between the pins on the module breakout board and your Pico should be as follows:

Pico | RP2040 | SX1276 Module | RFM95W Breakout
------------ | ------------- | ------------ | -------------
3V3 (OUT) | — | VCC | VIN
GND | GND | GND | GND
Pin 10 | GP7 | DIO0 | G0
Pin 11 | GP8 | NSS | CS
Pin 12 | GP9 | RESET | RST
Pin 14 | GP10 | DIO1 | G1
Pin 21 | GP16 (SPI0 RX) | MISO | MISO
Pin 24 | GP18 (SPI0 SCK) | SCK | SCK
Pin 25 | GP19 (SPI0 TX) | MOSI | MOSI

## The Things Network

To make use of a LoraWAN-enabled Pico you’re going to need to be in range of a LoRa gateway. Fortunately there is [The Things Network](https://www.thethingsnetwork.org/), an open-source community LoRaWAN network that has [global coverage](https://www.thethingsnetwork.org/map). Depending on where you are located, it’s quite possible that you’re already in coverage. However, if you aren’t, then you needn’t worry too much, the days when the cost of a LoRaWAN base station was of the order of several thousand dollars are long gone. You can now pick up a LoRa gateway for [under $100](https://amzn.to/3tFwFMZ).

While any LoRa device in range of your new gateway will have its packets received and sent upstream to The Things Network, the data packets will be dropped on the ground unless they have somewhere to go. In other words, The Things Network needs to know where to route the packets your gateway is receiving.

### Setting up The Things Network

Adafruit has written up a [full walkthrough](https://learn.adafruit.com/using-lorawan-and-the-things-network-with-circuitpython/tinylora-ttn-setup) on how to set up and application and register your device with The Things Network. You'll need to set three unique identifiers in the [`code.py`](https://github.com/aallan/pico-lorawan-circuitpython/blob/main/src/code.py) file; the Device Address, Network Session Key, and Application Session Key. These can be found [on the Device Overview page](https://learn.adafruit.com/using-lorawan-and-the-things-network-with-circuitpython/using-tinylora#setting-up-the-code-for-the-things-network-3010430-10).

**NOTE:** The example code uses ABP rather than OTAA as the Activation Method.

## Deploying to your Pico

Copy the contents of the [`src/`](https://github.com/aallan/pico-lorawan-circuitpython/tree/main/src) directory in the repo to your `CIRCUITPY` drive. This includes the `code.py` file and the `lib/` folder and all of its contents, including subfolders and any `.mpy` files present in the library directory.

## Sending data

Restart the board. The code should start running immediately, there will be debug output available on the USB CDC Serial console. If you see "Packet Sent!" then the packets are being sent up to The Things Network via LoRaWAN and you should be able to see your data arriving in the Network Console.

## Adding a decoder

We're sending out temperature reading as a byte array.

```C
temp = microcontroller.cpu.temperature
temp = int(temp * 100)

data = bytearray(2)
data[0] = (temp >> 8) & 0xFF
data[1] = temp & 0xFF
```

By default the payload is displayed as a hexidecimal values in the Network Console. However we can [add a data decoder](https://learn.adafruit.com/using-lorawan-and-the-things-network-with-circuitpython/using-tinylora#decoding-the-payload-3010444-33);

```javascript
function Decoder(bytes, port) {
  var decoded = {};
  var celciusInt = (bytes[0] << 8) | bytes[1];
  decoded.temp = celciusInt / 100;

  return decoded;
```

this will auto-magically decode the raw payload and display the real value in The Things Network Console.

## More information

You can find more information about [using LoRaWAN and The Things Network from CircuitPython](https://learn.adafruit.com/using-lorawan-and-the-things-network-with-circuitpython/overview) in the Adafruit RFM95x tutorial pages. Alternatively you may want to use the RFM95x module using C, in which case you should take a look at Sandeep Mistry's [`pico-lorawan`](https://github.com/sandeepmistry/pico-lorawan) library, and [getting started instructions](https://www.raspberrypi.org/blog/how-to-add-lorawan-to-raspberry-pi-pico/).

## Libraries

The following libraries are used:

Library | License | Github
------------ | ------------- | -------------
Bus Device | MIT | https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
RFM95x | MIT | https://github.com/adafruit/Adafruit_CircuitPython_RFM9x
TinyLoRa | LGPL | https://github.com/aallan/pico-lorawan-circuitpython

## License

This software is released under the [MIT License](https://opensource.org/licenses/MIT).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

