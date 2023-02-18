"""
Modulo: testServo.py
Autore: Marco Beltrame
Data: 08 settembre 2022
Gestione delle principali operazioni/attuazioni che si possono sperimentare sul servo del Mars Rover Picar-B:
    girare le ruote a destra
    girare le ruote a sinistra --> AL MOMENTO NON FUNZIONANTE
    alzare la testa
    abbassare la testa

Devo gestire il chip: PCA9685  che mi serve per controllare il servo 180°
In VS Code: ctrl+k+c commentare più righe di codie insieme
Per decommentare usare: ctrl+k+u
"""
from nis import match
import sys
sys.path.append("./Adafruit_PCA9685")
import Adafruit_PCA9685  # Import the library used to communicate with PCA9685
import time
from threading import Thread


pwm = Adafruit_PCA9685.PCA9685()  # Instantiate the object used to control the PWM
# Set the frequency of the PWM signal DEVE SEMPRE ESSERE A 50
pwm.set_pwm_freq(50)


def clean_all():
	pwm = Adafruit_PCA9685.PCA9685()
	pwm.set_pwm_freq(50)
	pwm.set_all_pwm(0, 0)

def riposa2secondi():
    """time.sleep(2)"""
    time.sleep(2)

def giraRuoteDestra(velocita=20, inclinazione=300):
    """  Una velocità ad esempio di 20 è considerata buona """
    for i in range(0,100, velocita):
        pwm.set_pwm(3,0,(inclinazione+i))
        time.sleep(0.05)
    pwm.set_pwm(3,0,0) # spegnere sempre

def giraRuoteSinistra(velocita=20): # NON SI RIESCE A GIRARE LE RUOTE A SINISTRA
    """ !!! NON FUNZIONANTE !!! """
    for i in range(0,300,velocita):
        pwm.set_pwm(3,200,(200-i))
        time.sleep(0.05)
    pwm.set_pwm(3,0,0) # spegnere sempre

def abbassaTesta(velocita, inclinazione=100):
    """  Una velocità ad esempio di 1 è considerata  molto lenta, 30 è molto veloce 
         inclinazione: 100
    """
    for i in range(0, 100, velocita): # aggiungere step 1
        pwm.set_pwm(2, 0, (inclinazione-i))
        time.sleep(0.05)
    pwm.set_pwm(2, 0, 0) # spegnere sempre

def alzaTesta(velocita, inclinazione=200):
    """  Una velocità ad esempio di 1 è considerata  molto lenta, 30 è molto veloce
            inclinazione: 200 di default       
    """
    for i in range(0, 100, velocita): # aggiungere step 1
        pwm.set_pwm(2, 0, (inclinazione+i))
        time.sleep(0.05)
    pwm.set_pwm(2, 0, 0) # spegnere sempre

def ruotaTestaDestra(velocita, inclinazione=200):
    """  Una velocità ad esempio di 1 è considerata  molto lenta, 30 è molto veloce
            inclinazione: 200 di default       
    """
    for i in range(0, 100, velocita): # aggiungere step 1
        pwm.set_pwm(0, 0, (inclinazione+i))
        time.sleep(0.05)
    pwm.set_pwm(0, 0, 0) # spegnere sempre
	

# if __name__ == '__main__':
#     ruotaTestaDestra(30, 300)
#     velocita_ruote = 20 # Ad esempio: 
#     # pwm.set_pwm(1,100, 300)
#     # time.sleep(1)
#     # pwm.set_pwm(1,0,0)
#     ruotaTestaDestra(1,300)

#     # print("Gira ruote a destra:")
#     # giraRuoteDestra(velocita_ruote)

#     # riposa2secondi()

#     print("Gira ruote a sinistra:")
#     giraRuoteSinistra(velocita_ruote)
    
#     riposa2secondi()
    
#     velocita_testa = 30 # Ad esempio: 1 è molto lenta, 30 è molto veloce 
#     print("Abbassa la testa:")
#     alzaTesta(velocita_testa)
#     # abbassaTesta(velocita_testa)

#     riposa2secondi()
    
#     print("Alza la testa:")
#     # alazaTesta(velocita_testa)
#     abbassaTesta(velocita_testa)
#     # for i in range(0, 100, 30): # aggiungere step 1
#     #     pwm.set_pwm(2, 0, (200+i))
#     #     time.sleep(0.05)
#     # pwm.set_pwm(2, 0, 0) # spegnere sempre