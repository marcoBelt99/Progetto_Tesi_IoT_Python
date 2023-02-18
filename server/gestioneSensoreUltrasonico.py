from audioop import avg
import RPi.GPIO as GPIO
from time import sleep
import time
import Adafruit_PCA9685


Tr = 11 # Numermo del pin della parte finale di input del sensore ultrasonico
Ec = 8 # Numero del pin della parte finale di output del sensore ultrasonico

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Tr, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Ec, GPIO.IN)

def calcolaDistanza(*args): 
   # GPIO.output(Tr, GPIO.HIGH) 
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Tr, GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(Ec, GPIO.IN)
    GPIO.output(Tr, GPIO.HIGH) # Imposto l'input terminale del modulo ad un alto livello e spedisco fuori un'onda sonica iniziale
    time.sleep(0.000015)
    GPIO.output(Tr, GPIO.LOW)
    while not GPIO.input(Ec):
        pass
    t1 = time.time()
    while GPIO.input(Ec):
        pass
    t2 = time.time()
    return round((t2-t1)*340/2,2)

def stampaDistanza(distanza):
    print ("Distanza = {:6.3f}cm ".format( distanza*100)) # stampa formattata in centimetri 

def stampa(distanza):
    return "Distanza = {:6.3f}cm ".format( distanza*100)
     
def calcolaDistanzaMedia(tempoDiCalcolo=15):
    """ Calcola media delle distanze calcolate in un determinato intervallo di tempo in secondi.
        :param tempoDiCalcolo: tempo di rilevazione delle distanze (equivalente al numero di distanze da prelevare).
         Di default vale 15 secondi. 
    """
    vettoreDistanze = [] # contiene tutte le distanze
    timeout = time.time()  + tempoDiCalcolo # ora in secondi di adesso + (secondi desiderati) Es. 20 secondi == 60/3. 2 ore == 60*2
    while True:
        sleep(1)
        distanza = calcolaDistanza()
        # print(distanza)
        print ("Distanza = {:6.3f}cm ".format( distanza*100)) # stampa formattata in centimetri 
        vettoreDistanze.append(distanza)
        if time.time() > timeout:
            break    
    return sum(vettoreDistanze)/len(vettoreDistanze)



def clean_all():
	pwm = Adafruit_PCA9685.PCA9685()
	pwm.set_pwm_freq(50)
	pwm.set_all_pwm(0, 0)
   

if __name__ == "__main__":
    # vettoreDistanze = [] # contiene tutte le distanze

    # # !!! Mi sono calcolato la media!!!
    # timeout = time.time()  + (60/3) # ora in secondi di adesso + (secondi desiderati)
    # while True:
    #     sleep(1)
    #     distanza = calcolaDistanza()
    #     # print(distanza)
    #     print ("Distance = {:6.3f}cm ".format( distanza*100)) # stampa formattata in centimetri 
    #     vettoreDistanze.append(distanza)
    #     if time.time() > timeout:
    #         break    
    # # print ("Distance = {:6.3f}cm ".format( distance*100))
    # # print("Distanza media:", calcolaDistanzaMedia())
    stampaDistanza(calcolaDistanzaMedia())
    # print ("Distanza = {:6.3f}cm ".format( calcolaDistanza()*100)) # stampa formattata in centimetri 
    clean_all()
    GPIO.cleanup()

    