# Circuitpython slideshow on TFT Display with sdcard and XIAO RP2040  

## Hardware
- 1.8" SPI TFT Display w/ sdcard
- Seeed Studio XIAO RP2040


## Dependencies  
- adafruit_sdcard  
- adafruit_st7735r  
- adafruit_slideshow

Get these dependencies from the [Adafruit_CircuitPython_Bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle) and place them in your ```lib``` directory.  
Or use the [circup](https://learn.adafruit.com/keep-your-circuitpython-libraries-on-devices-up-to-date-with-circup) utility.  
```circup install adafruit_sdcard adafruit_st7735r adafruit_slideshow```

your lib directory will look something like this:
```
lib
├── adafruit_bus_device
│   ├── i2c_device.mpy
│   ├── __init__.py
│   └── spi_device.mpy
├── adafruit_sdcard.mpy
├── adafruit_slideshow.mpy
└── adafruit_st7735r.mpy
```

## Usage  
Put your images in a directory on the sd card. In ```main.py``` adjust the IMAGES_DIR variable.  
```IMAGES_DIR = "/sd/cats"```


## Wiring

| DEVICE PIN 	| BOARD PIN 	|
|------------	|-----------	|
| LED        	| 3v3       	|
| SCK        	| D8        	|
| SDA        	| D9        	|
| AO         	| D4        	|
| RESET      	| D5        	|
| CS         	| D7        	|
| GND        	| GND       	|
| VCC        	| 3v3       	|
|            	|           	|
| SD_CS      	| D3        	|
| SD_MOSI    	| D9        	|
| SD_MISO    	| D10       	|
| SD_SCK     	| D8        	|

![1.8" TFT Display w/ sdcard](/home/david/Documents/microcontrollers/xiao_rp2040/tft1.8display/img/TFT-Display.jpg)  
![Seeed Studio XIAO RP2040](/home/david/Documents/microcontrollers/xiao_rp2040/tft1.8display/img/xinpin.jpg)

