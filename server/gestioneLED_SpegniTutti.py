"""
ULTIMO MODULO PYTHON DA CUSTOMIZZARE. Serve per il controllo dei LED posteriori.
"""
import atexit
from cProfile import run
import time
# from rpi_ws281x import *
import argparse
import threading
# from neopixel import *
import _rpi_ws281x as ws
# import rpi_ws281x as ws
from time import sleep
import sys
from sys import argv # Necessario per 

# LED strip configuration:
LED_COUNT      = 12      # Number of LED pixels. #
LED_PIN        = 12      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# ledfunc = ''
# ledfunc = 'rainbow' # PER ABILITARE IL RAINBOW CYCLE
ledfunc = 'police'

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

class LED:
    def __init__(self):
        self.LED_COUNT      = 16      # Number of LED pixels.
        self.LED_PIN        = 12      # GPIO pin connected to the pixels (18 uses PWM!).
        self.LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
        self.LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
        self.LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
        self.LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
        self.LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
        # parser = argparse.ArgumentParser()
        # parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
        # args = parser.parse_args()

        # Create NeoPixel object with appropriate configuration.
        self.strip = Adafruit_NeoPixel(self.LED_COUNT, self.LED_PIN, self.LED_FREQ_HZ, self.LED_DMA, self.LED_INVERT, self.LED_BRIGHTNESS, self.LED_CHANNEL)
        # Intialize the library (must be called once before other functions).
        self.strip.begin()

    # Define functions which animate LEDs in various ways.
    def colorWipe(self, R, G, B):
        """Wipe color across display a pixel at a time."""
        color = Color(R,G,B)
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)
            self.strip.show()

    def rainbow(self, wait_ms=20, iterations=1):
        """Draw rainbow that fades across all pixels at once."""
        for j in range(256 * iterations):
            if ledfunc == 'rainbow':
                for i in range(self.strip.numPixels()):
                    if ledfunc == 'rainbow':
                        self.strip.setPixelColor(i, wheel((i + j) & 255))
                    else:
                        break
                self.strip.show()
                time.sleep(wait_ms / 1000.0)
            else:
                break
    
    def SideAWipe(self, R, G, B):
        """Wipe color across display a pixel at a time."""
        color = Color(R,G,B)
        for i in range(0, 6):
            self.strip.setPixelColor(i, color)
            self.strip.show()

    def SideBWipe(self, R, G, B):
        """Wipe color across display a pixel at a time."""
        color = Color(R,G,B)
        for i in range(6, 12):
            self.strip.setPixelColor(i, color)
            self.strip.show()

    def theaterChaseRainbow(strip, wait_ms=50):
        """Rainbow movie theater light style chaser animation."""
        for j in range(256):
            for q in range(3):
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)
    @staticmethod
    def polizia():
        for x in range(0,5):
            time.sleep(0.1)
            led.SideAWipe(0, 0, 255)
            led.SideBWipe(0, 255, 0)
            time.sleep(0.03)
            led.colorWipe(0,0,0)
            time.sleep(0.03)

            led.SideAWipe(0, 0, 255)
            led.SideBWipe(0, 255, 0)
            time.sleep(0.03)
            led.colorWipe(0,0,0)
            time.sleep(0.03)

            led.SideAWipe(0, 0, 255)
            led.SideBWipe(255, 0, 0)
            time.sleep(0.03)
            led.colorWipe(0,0,0)
            time.sleep(0.03)

            time.sleep(0.1)
            led.SideAWipe(255, 0, 0)
            led.SideBWipe(0, 0, 255)
            time.sleep(0.03)
            led.colorWipe(0,0,0)
            time.sleep(0.03)

            led.SideAWipe(255, 0, 0)
            led.SideBWipe(0, 0, 255)
            time.sleep(0.03)
            led.colorWipe(0,0,0)
            time.sleep(0.03)

            led.SideAWipe(255, 0, 0)
            led.SideBWipe(0, 0, 255)
            time.sleep(0.03)
            led.colorWipe(0,0,0)
            time.sleep(0.03)

class LED_ctrl(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(LED_ctrl, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()
        self.__flag.set()
        self.__running = threading.Event()
        self.__running.set()

    def run(self):
        global goal_pos, servo_command, init_get, functionMode
        while self.__running.isSet():
            self.__flag.wait()
            if ledfunc == 'police':
                time.sleep(0.1)
                led.SideAWipe(0, 0, 255)
                led.SideBWipe(255, 0, 0)
                time.sleep(0.03)
                led.colorWipe(0,0,0)
                time.sleep(0.03)

                led.SideAWipe(0, 0, 255)
                led.SideBWipe(255, 0, 0)
                time.sleep(0.03)
                led.colorWipe(0,0,0)
                time.sleep(0.03)

                led.SideAWipe(0, 0, 255)
                led.SideBWipe(255, 0, 0)
                time.sleep(0.03)
                led.colorWipe(0,0,0)
                time.sleep(0.03)

                time.sleep(0.1)
                led.SideAWipe(255, 0, 0)
                led.SideBWipe(0, 0, 255)
                time.sleep(0.03)
                led.colorWipe(0,0,0)
                time.sleep(0.03)

                led.SideAWipe(255, 0, 0)
                led.SideBWipe(0, 0, 255)
                time.sleep(0.03)
                led.colorWipe(0,0,0)
                time.sleep(0.03)

                led.SideAWipe(255, 0, 0)
                led.SideBWipe(0, 0, 255)
                time.sleep(0.03)
                led.colorWipe(0,0,0)
                time.sleep(0.03)
            elif ledfunc == 'rainbow':
                led.rainbow()
            elif ledfunc == '':
                self.pause()

    def pause(self):
        self.__flag.clear()

    def resume(self):
        self.__flag.set()

    def stop(self):
        self.__flag.set()
        self.__running.clear()


def Color(red, green, blue, white = 0):
	"""Convert the provided red, green, blue color to a 24-bit color value.
	Each color component should be a value 0-255 where 0 is the lowest intensity
	and 255 is the highest intensity.
	"""
	return (white << 24) | (red << 16)| (green << 8) | blue



############################ INIZIO CLASSE ##################
class _LED_Data(object):
	"""Wrapper class which makes a SWIG LED color data array look and feel like
	a Python list of integers.
	"""
	def __init__(self, channel, size):
		self.size = size
		self.channel = channel

	def __getitem__(self, pos):
		"""Return the 24-bit RGB color value at the provided position or slice
		of positions.
		"""
		# Handle if a slice of positions are passed in by grabbing all the values
		# and returning them in a list.
		if isinstance(pos, slice):
			return [ws.ws2811_led_get(self.channel, n) for n in xrange(*pos.indices(self.size))]
		# Else assume the passed in value is a number to the position.
		else:
			return ws.ws2811_led_get(self.channel, pos)

	def __setitem__(self, pos, value):
		"""Set the 24-bit RGB color value at the provided position or slice of
		positions.
		"""
		# Handle if a slice of positions are passed in by setting the appropriate
		# LED data values to the provided values.
		if isinstance(pos, slice):
			index = 0
			for n in xrange(*pos.indices(self.size)):
				ws.ws2811_led_set(self.channel, n, value[index])
				index += 1
		# Else assume the passed in value is a number to the position.
		else:
			return ws.ws2811_led_set(self.channel, pos, value)

class Adafruit_NeoPixel(object):
	def __init__(self, num, pin, freq_hz=800000, dma=10, invert=False,
			brightness=255, channel=0, strip_type=ws.WS2811_STRIP_RGB):
		"""Class to represent a NeoPixel/WS281x LED display.  Num should be the
		number of pixels in the display, and pin should be the GPIO pin connected
		to the display signal line (must be a PWM pin like 18!).  Optional
		parameters are freq, the frequency of the display signal in hertz (default
		800khz), dma, the DMA channel to use (default 10), invert, a boolean
		specifying if the signal line should be inverted (default False), and
		channel, the PWM channel to use (defaults to 0).
		"""
		# Create ws2811_t structure and fill in parameters.
		self._leds = ws.new_ws2811_t()

		# Initialize the channels to zero
		for channum in range(2):
			chan = ws.ws2811_channel_get(self._leds, channum)
			ws.ws2811_channel_t_count_set(chan, 0)
			ws.ws2811_channel_t_gpionum_set(chan, 0)
			ws.ws2811_channel_t_invert_set(chan, 0)
			ws.ws2811_channel_t_brightness_set(chan, 0)

		# Initialize the channel in use
		self._channel = ws.ws2811_channel_get(self._leds, channel)
		ws.ws2811_channel_t_count_set(self._channel, num)
		ws.ws2811_channel_t_gpionum_set(self._channel, pin)
		ws.ws2811_channel_t_invert_set(self._channel, 0 if not invert else 1)
		ws.ws2811_channel_t_brightness_set(self._channel, brightness)
		ws.ws2811_channel_t_strip_type_set(self._channel, strip_type)

		# Initialize the controller
		ws.ws2811_t_freq_set(self._leds, freq_hz)
		ws.ws2811_t_dmanum_set(self._leds, dma)

		# Grab the led data array.
		self._led_data = _LED_Data(self._channel, num)

		# Substitute for __del__, traps an exit condition and cleans up properly
		atexit.register(self._cleanup)

	def _cleanup(self):
		# Clean up memory used by the library when not needed anymore.
		if self._leds is not None:
			ws.delete_ws2811_t(self._leds)
			self._leds = None
			self._channel = None

	def begin(self):
		"""Initialize library, must be called once before other functions are
		called.
		"""
		resp = ws.ws2811_init(self._leds)
		if resp != ws.WS2811_SUCCESS:
			message = ws.ws2811_get_return_t_str(resp)
			raise RuntimeError('ws2811_init failed with code {0} ({1})'.format(resp, message))

	def show(self):
		"""Update the display with the data from the LED buffer."""
		resp = ws.ws2811_render(self._leds)
		if resp != ws.WS2811_SUCCESS:
			message = ws.ws2811_get_return_t_str(resp)
			raise RuntimeError('ws2811_render failed with code {0} ({1})'.format(resp, message))

	def setPixelColor(self, n, color):
		"""Set LED at position n to the provided 24-bit color value (in RGB order).
		"""
		self._led_data[n] = color

	def setPixelColorRGB(self, n, red, green, blue, white = 0):
		"""Set LED at position n to the provided red, green, and blue color.
		Each color component should be a value from 0 to 255 (where 0 is the
		lowest intensity and 255 is the highest intensity).
		"""
		self.setPixelColor(n, Color(red, green, blue, white))

	def setBrightness(self, brightness):
		"""Scale each LED in the buffer by the provided brightness.  A brightness
		of 0 is the darkest and 255 is the brightest.
		"""
		ws.ws2811_channel_t_brightness_set(self._channel, brightness)

	def getBrightness(self):
		"""Get the brightness value for each LED in the buffer. A brightness
		of 0 is the darkest and 255 is the brightest.
		"""
		return ws.ws2811_channel_t_brightness_get(self._channel)

	def getPixels(self):
		"""Return an object which allows access to the LED display data as if
		it were a sequence of 24-bit RGB values.
		"""
		return self._led_data

	def numPixels(self):
		"""Return the number of pixels in the display."""
		return ws.ws2811_channel_t_count_get(self._channel)

	def getPixelColor(self, n):
		"""Get the 24-bit RGB color value for the LED at position n."""
		return self._led_data[n]
############################## FINE CLASSE ################


def accendiTuttiLED(R,G,B):
    led = LED()
    led.colorWipe(R, G, B)  
    sleep(5)

def spegniLED():
    # led = LED()
    led.colorWipe(0, 0, 0)   #Tutte le luci diventano basse 

def accendiSingoloLED(i,R,G,B):
     # ##### Accensione singolo LED. Ci sono 3 LED per ogni modulo hw
    led = LED()
    led.strip.setPixelColor(i, Color(R, G, B))
    led.strip.show() # necessario per accensione del singolo LED

# def spegniSingoloLED(i):
#     led = LED()
#     led.strip.setPixelColor(i,Color(0,0,0))

led = LED() # VARIABILE GLOBALE NECESSARIA PER ESSERE PILOTATA



# time.sleep(3)
# # spegniSingoloLED(0)
# spegniLED()
if __name__ == '__main__':
    led = LED()
    parser = argparse.ArgumentParser()
    parser.add_argument("-u","--upgrade", help="fully automatized upgrade", action="store_true")
    
    print(argv[1])
    led.colorWipe(0,0,0) # Spegnimento LED
    print("Spenti tutti i LED")