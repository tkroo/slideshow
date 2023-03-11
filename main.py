from time import sleep

import board
import busio
import displayio
import sdcardio
import storage
from adafruit_slideshow import PlayBackOrder, SlideShow
from adafruit_st7735r import ST7735R

IMAGES_DIR = "/sd/cats"

# these pin assignments are specific to the Seed Stuido XIAO RP2040
miso_pin = board.MISO
mosi_pin = board.MOSI
clk_pin = board.D8
dc_pin = board.D4
reset_pin = board.D5
cs_pin = board.D7
sd_cs_pin = board.D3


displayio.release_displays()

# shared SPI bus for sdcard and display
spi = busio.SPI(clock=clk_pin, MOSI=mosi_pin, MISO=miso_pin)

# init the sdcard first
sdcard = sdcardio.SDCard(spi, sd_cs_pin)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")


display_bus = displayio.FourWire(
    spi, command=dc_pin, chip_select=cs_pin, reset=reset_pin
)

display = ST7735R(display_bus, width=128, height=160, bgr=True, colstart=2, rowstart=1)

slideshow = SlideShow(
    display,
    folder=IMAGES_DIR,
    loop=True,
    order=PlayBackOrder.ALPHABETICAL,
    dwell=2,
    auto_advance=True,
)

while slideshow.update():
    pass
