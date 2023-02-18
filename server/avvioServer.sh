#!/bin/sh

# #Attivare sempre l'ambiente virtuale all'interno della Working Directory
# source /home/rasp/programmazioneMarsRoverPiCarB/venv/bin/activate 

# #Esportare la variabile FLASK
# export FLASK_APP=serverProva.py
# #Avvio server con operazioni di debug
# export FLASK_DEBUG=1

# #Metto il server in  ascolto su tutti gli IP pubblici e non solo all'interno dell'ambiente locale
# flask run --host=0.0.0.0
# source venv/bin/activate
# pip install Adafruit_PCA9685
# pip3 install RPi.GPIO
# pip install requests Flask
export FLASK_APP=SERVER.py
export FLASK_DEBUG=1
flask run --host=0.0.0.0