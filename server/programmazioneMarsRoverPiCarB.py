from gestioneLED import *
from gestioneServo import *
from gestioneMoove import *
from gestioneRGB import *
from gestioneSensoreUltrasonico import *
from time import sleep
import sys
sys.path.append("./Adafruit_PCA9685")
sys.path.append("./rpi_ws281x")
sys.path.append("/home/rasp/python_venv/lib/python3.9/site-packages/RPi/")
sys.path.append("./RPi.GPIO") # prima commentato
import Adafruit_Python_PCA9685
from rpi_ws281x import * # per la gestione del colore dei LED
import RPi.GPIO as GPIO # per gestione del GPIO


if __name__ == "__main__":
    try:
        alzaTesta(20)
        sleep(2)
        abbassaTesta(20,50) #  con inclinazione custom

        GPIO.cleanup()  # Serve per il fastidioso errore tra BCM vs BOARD (Per poter usare i LED)

        rosso()
        sleep(1.5)

        avanti()

        GPIO.cleanup()  # Serve per il fastidioso errore tra BCM vs BOARD (Per poter usare i LED)

        # print("Modalità: ", GPIO.getmode())
        # GPIO.setmode(GPIO.BCM) # controlla con BOARD
        sleep(0.5)
        verde(3)
        retromarcia()
        sleep(1.5)
        ciano()
        # # # IDEA: quando va in retromarcia prima accende i led dietro e poi quando finisce li spegne
        sleep(0.5)
        abbassaTesta(30,450)
        sleep(1)
        giallo()

        avantiTemporizzato(2)
        sleep(0.5)
        abbassaTesta(10)
        sleep(0.5)
        stampaDistanza(calcolaDistanza())

        GPIO.cleanup()  # Serve per il fastidioso errore tra BCM vs BOARD (Per poter usare i LED)

        giraRuoteDestra()
        rosa()
        
        # GESTIONE DEI LED
        # led = LED()
        led.colorWipe(0, 255, 255) # Cambia il colore di tutti e 3 i LED
        sleep(4)
        
        # # ##### Accensione singolo LED. Ci sono 3 LED per ogni modulo hw
        # led.strip.setPixelColor(2, Color(100, 5, 100))
        led.strip.setPixelColor(1, Color(165, 42, 42))
        # led.strip.setPixelColor(0, Color(0, 51, 0))
        led.strip.show() # necessario per accensione del singolo LED
        sleep(4)
        led.colorWipe(0,0,0) # Spegnimento LED
        clean_all()
    except KeyboardInterrupt:
        clean_all()
