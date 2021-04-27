# Raspberry Pi Pico and LoRaWAN from CircuitPython

Based on example code 

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
