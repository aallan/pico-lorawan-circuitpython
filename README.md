# Raspberry Pi Pico and LoRaWAN from CircuitPython



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