"""
Modulo: gestioneLED.py
Autore: Marco Beltrame
Data: 09/09/2022
Gestione dei LED RGB. Serve per far accendere/spegnere e cambiare i led RGB posti sul davanti (i fari)
    rosso
    verde
    blu
    giallo
    rosa
    ciano
""" 
import RPi.GPIO as GPIO
import time

left_R = 15
left_G = 16
left_B = 18

right_R = 19
right_G = 21
right_B = 22

on  = GPIO.LOW
off = GPIO.HIGH

def both_on():
    GPIO.output(left_R, on)
    GPIO.output(left_G, on)
    GPIO.output(left_B, on)

    GPIO.output(right_R, on)
    GPIO.output(right_G, on)
    GPIO.output(right_B, on)

def both_off():
    GPIO.output(left_R, off)
    GPIO.output(left_G, off)
    GPIO.output(left_B, off)

    GPIO.output(right_R, off)
    GPIO.output(right_G, off)
    GPIO.output(right_B, off)

def setup(): #initialization # va richiamato sempre all'inizio del "main"
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD) # controlla con BOARD
    GPIO.setup(left_R, GPIO.OUT)
    GPIO.setup(left_G, GPIO.OUT)
    GPIO.setup(left_B, GPIO.OUT)
    GPIO.setup(right_R, GPIO.OUT)
    GPIO.setup(right_G, GPIO.OUT)
    GPIO.setup(right_B, GPIO.OUT)

    # aggiunte: (forse non servono a niente)
    # pwmR = GPIO.PWM(pins['pin_R'], 50)
    # pwmG = GPIO.PWM(pins['pin_G'], 50)
    # pwmB = GPIO.PWM(pins['pin_B'], 50)
    both_off()



def side_on(side_X): # accendi il led desiderato X sta per destra o sinistra
    GPIO.output(side_X, on)

def side_off(side_X): # spegni il led desiderato X sta per destra o sinistra
    GPIO.output(side_X, off)

def police(police_time): # fa un ciclo per fare il lampeggiante della polizia, effetto ad intermittenda fatto con lo sleep
    for i in range (1,police_time):
        for i in range (1,3):
            side_on(left_R)
            side_on(right_B)
            time.sleep(0.1)
            both_off()
            side_on(left_B)
            side_on(right_R)
            time.sleep(0.1)
            both_off()
        for i in range (1,5):
            side_on(left_R)
            side_on(right_B)
            time.sleep(0.3)
            both_off()
            side_on(left_B)
            side_on(right_R)
            time.sleep(0.3)
            both_off()

def red():
    """ ROSSO DI BASE"""
    side_on(right_R) # accendi il led RGB di destra e fallo di colore rosso
    side_on(left_R) # accendi il led RGB di sinistra e fallo di colore rosso

def green():
    """ VERDE DI BASE"""
    side_on(right_G)
    side_on(left_G)

def blue():
    """ BLU DI BASE"""
    side_on(right_B)
    side_on(left_B)

def yellow():
    """ GIALLO """
    red()
    green()    

def pink():
    """ ROSA """
    red()
    blue()

def cyan():
    """ CIANO """
    blue()
    green()

def orange():
    red()
    yellow()

def brown():
    """ NOT WORKS """
    yellow()
    red()
    blue



# Mappa da 0-255 a 0-100
def map(self, x, in_min, in_max, out_min, out_max):
    return (x-in_min) / (in_max-in_min) * (out_max - out_min) + out_min


def side_color_on(side_X,side_Y):
    GPIO.output(side_X, on)
    GPIO.output(side_Y, on)

def side_color_off(side_X,side_Y):
    GPIO.output(side_X, off)
    GPIO.output(side_Y, off)

def turn_left(times):
    for i in range(0,times):
        both_off()
        side_on(left_G)
        side_on(left_R)
        time.sleep(0.5)
        both_off()
        time.sleep(0.5)

def turn_right(times):
    for i in range(0,times):
        both_off()
        side_on(right_G)
        side_on(right_R)
        time.sleep(0.5)
        both_off()
        time.sleep(0.5)


def rosso(tempoDiAccensione=2):
    """ ROSSO DI BASE
        :param tempoDiAccensione: indica per quanto tempo resterà acceso. il led RGB. Di default è 2 secondi
    """
    setup() # sempre chiamarlo
    red()
    time.sleep(tempoDiAccensione)
    both_off()
    time.sleep(0.5)

def verde(tempoDiAccensione=2):
    """ VERDE DI BASE
        :param tempoDiAccensione: indica per quanto tempo resterà acceso.. Di default è 2 secondi
    """
    setup() # sempre chiamarlo
    green()
    time.sleep(tempoDiAccensione)
    both_off()
    time.sleep(0.5)

def blu(tempoDiAccensione=2):
    """ BLU DI BASE
        :param tempoDiAccensione: indica per quanto tempo resterà acceso. Di default è 2 secondi
    """
    setup() # sempre chiamarlo
    blue()
    time.sleep(tempoDiAccensione)
    both_off()
    time.sleep(0.5)

def giallo(tempoDiAccensione=2):
    """ GIALLO
        :param tempoDiAccensione: indica per quanto tempo resterà acceso.
    """
    setup() # sempre chiamarlo
    yellow()
    time.sleep(tempoDiAccensione)
    both_off()
    time.sleep(0.5)

def rosa(tempoDiAccensione=2):
    """ ROSA
        :param tempoDiAccensione: indica per quanto tempo resterà acceso.
    """
    setup() # sempre chiamarlo
    pink()
    time.sleep(tempoDiAccensione)
    both_off()
    time.sleep(0.5)

def ciano(tempoDiAccensione=2):
    """ CIANO.
        :param tempoDiAccensione: indica per quanto tempo resterà acceso.
    """
    setup() # sempre chiamarlo
    cyan()
    time.sleep(tempoDiAccensione)
    both_off()
    time.sleep(0.5)

def arancione(tempoDiAccensione=2):
    """ ARANCIONE.
        :param tempoDiAccensione: indica per quanto tempo resterà acceso.
    """
    setup() # sempre chiamarlo
    orange()
    time.sleep(tempoDiAccensione)
    both_off()
    time.sleep(0.5)


# if __name__ == '__main__':
#     setup() # sempre chiamarlo
#     police(2)
#     both_on() # deve sempre essere abilitato
#     time.sleep(1)
#     both_off() # spegnere sempre per ottenere il successivo colore
#     yellow()
#     time.sleep(2)
#     both_off() # spegnere sempre per ottenere il successivo colore
#     pink()
#     time.sleep(2)
#     both_off() # spegnere sempre per ottenere il successivo colore
#     cyan()
#     time.sleep(2)
#     both_off()  # spegnere sempre per ottenere il successivo colore
#     orange()
#     time.sleep(2)
#     both_off()  # spegnere sempre per ottenere il successivo colore
#     #brown()
#     #time.sleep(2)
#     #both_off()
#     # rossoRosa()
#     time.sleep(3)
#     # spegnili tutti
#     both_off()
