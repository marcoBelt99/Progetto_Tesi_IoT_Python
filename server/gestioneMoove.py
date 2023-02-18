"""
Modulo: gestioneMoove.py
Autore: Marco Beltrame
Data: 09/09/2022
Gestione del motore DC. Serve per far andare la macchina avanti oppure in retromarcia
		avanti
		retromarcia
"""            


import RPi.GPIO as GPIO
import RPi.GPIO as GPIO
import time
from time import sleep

from gestioneServo import alzaTesta, abbassaTesta, giraRuoteDestra

Motor_A_EN    = 7
Motor_B_EN    = 11

Motor_A_Pin1  = 8
Motor_A_Pin2  = 10
Motor_B_Pin1  = 13
Motor_B_Pin2  = 12

Dir_forward   = 0
Dir_backward  = 1



aggiustamentoVelocità = 1 # Caldamente consigliato di lasciarlo ad 1 spd_ad     = 1

status     = 1          #Motor rotation
forward    = 1          #Motor forward
backward   = 0          #Motor backward

# left_spd   = 100         #Speed of the car
# right_spd  = 100         #Speed of the car
left       = 100         #Motor Left
right      = 100         #Motor Right

spd_ad_1 = 1
spd_ad_2 = 1
spd_ad_u = 1
          
            
MOTOR_START = 1
MOTOR_STOP = 0


pwm_A = 0
# pwm_B = 0

def setup():#Motor initialization
	global pwm_A, pwm_B
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(Motor_A_EN, GPIO.OUT)
	GPIO.setup(Motor_B_EN, GPIO.OUT)
	GPIO.setup(Motor_A_Pin1, GPIO.OUT)
	GPIO.setup(Motor_A_Pin2, GPIO.OUT)
	GPIO.setup(Motor_B_Pin1, GPIO.OUT)
	GPIO.setup(Motor_B_Pin2, GPIO.OUT)
	try:
		pwm_A = GPIO.PWM(Motor_A_EN, 1000)
		pwm_B = GPIO.PWM(Motor_B_EN, 1000)
	except:
		pass

def motorStop():#Motor stops
	GPIO.output(Motor_A_Pin1, GPIO.LOW)
	GPIO.output(Motor_A_Pin2, GPIO.LOW)
	GPIO.output(Motor_B_Pin1, GPIO.LOW)
	GPIO.output(Motor_B_Pin2, GPIO.LOW)
	GPIO.output(Motor_A_EN, GPIO.LOW)
	GPIO.output(Motor_B_EN, GPIO.LOW)

def motor_right(status, direction, speed):#Motor 2 positive and negative rotation
	global  pwm_B
	if status == 0: # stop
		motorStop()
	else:
		if direction == Dir_forward:
			GPIO.output(Motor_B_Pin1, GPIO.HIGH)
			GPIO.output(Motor_B_Pin2, GPIO.LOW)
			pwm_B.start(100)
			pwm_B.ChangeDutyCycle(speed)
		elif direction == Dir_backward:
			GPIO.output(Motor_B_Pin1, GPIO.LOW)
			GPIO.output(Motor_B_Pin2, GPIO.HIGH)
			pwm_B.start(0)
			pwm_B.ChangeDutyCycle(speed)
			
def motor_left(status, direction, speed):#Motor 1 positive and negative rotation
	global pwm_A
	if status == 0: # stop
		motorStop()
	else:
		if direction == Dir_forward:#
			GPIO.output(Motor_A_Pin1, GPIO.HIGH)
			GPIO.output(Motor_A_Pin2, GPIO.LOW)
			pwm_A.start(100)
			pwm_A.ChangeDutyCycle(speed)
		elif direction == Dir_backward:
			GPIO.output(Motor_A_Pin1, GPIO.LOW)
			GPIO.output(Motor_A_Pin2, GPIO.HIGH)
			pwm_A.start(0)
			pwm_A.ChangeDutyCycle(speed)
	return direction


def destroy():
	motorStop()
	GPIO.cleanup()             # Release resource


try:
	pass
except KeyboardInterrupt:
	destroy()



def avanti(velSinistra=100, velDestra=100):
    """ avanti: manda l'auto in avanti 
		:param velSinistra: deve essere sempre comprese tra 0 e 100. Di default è al massimo cioè a 100
		:param velDestra: deve essere sempre comprese tra 0 e 100. Di default è al massimo cioè a 100
	"""
    setup()
    print ()
    print ("-------------------")
    print ("Muovi in avanti")
    print ("-------------------")
    motor_left(MOTOR_START, forward, velSinistra*aggiustamentoVelocità)
    motor_right(MOTOR_START,backward, velDestra*aggiustamentoVelocità)
    time.sleep(1.0)
    motor_left(MOTOR_STOP, forward,velSinistra*aggiustamentoVelocità)
    motor_right(MOTOR_STOP,backward,velDestra*aggiustamentoVelocità)
    destroy() # test

def retromarcia(velSinistra=100, velDestra=100):
    """ Retromarcia: manda l'auto in retromarcia 
		:param velSinistra: deve essere sempre comprese tra 0 e 100. Di default è al massimo cioè a 100
		:param velDestra: deve essere sempre comprese tra 0 e 100. Di default è al massimo cioè a 100
	"""
    setup()
    print ()
    print ("-------------------")
    print ("Retromarcia")
    print ("-------------------")
    motor_left(MOTOR_START, backward, velSinistra*aggiustamentoVelocità)
    motor_right(MOTOR_START, forward, velDestra*aggiustamentoVelocità)
    time.sleep(1.0)
    motor_left(MOTOR_STOP, backward, velSinistra*aggiustamentoVelocità)
    motor_right(MOTOR_STOP, forward, velDestra*aggiustamentoVelocità)
    destroy() # test

def avantiTemporizzato(secondi=5):
	timeout = time.time()  + secondi # ora in secondi di adesso + (secondi desiderati) Es. 20 secondi == 60/3. 2 ore == 60*2
	while True:
		sleep(0.05)
		avanti(85,85)
		if time.time() > timeout:
			break

def retromarciaTemporizzata(secondi=5):
	timeout = time.time()  + secondi # ora in secondi di adesso + (secondi desiderati) Es. 20 secondi == 60/3. 2 ore == 60*2
	while True:
		sleep(0.05)
		retromarcia(85,85)
		if time.time() > timeout:
			break    


# if __name__ == "__main__":
#     try:
#         velocitaDiSinistra = 100
#         velocitaDiDestra = 100
#         avanti(velocitaDiSinistra, velocitaDiDestra)
#         time.sleep(5)
#         retromarcia(velocitaDiSinistra, velocitaDiDestra)
#         time.sleep(2)
#         alzaTesta(5)
#         time.sleep(1)
#         giraRuoteDestra(20)
#         time.sleep(1)
#         abbassaTesta(5)

#     except KeyboardInterrupt:
# 	    destroy() # ctrl + c
    
# # !/usr/bin/python3 # Se servono queste due ultime istruzioni, metterle in fondo 

# # runs through a set of tests for the PiCar-B