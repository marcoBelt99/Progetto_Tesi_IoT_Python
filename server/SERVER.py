"""
Modulo: serverProva
Autore: Marco Beltrame
Data: 10/09/2022
Permette la comunicazione con uno o più client che effettuano richieste Rest.
È implementato attraverso il micro framework Flask, che consente di creare RestAPI in maniera estremamente semplice.
Infatti, tramite i decoratori (riche che iniziano con la '@'), Flask permette di mappare una richiesta HTTP (sia il metodo che l'URL)
ad una determinata funzione che viene scritta dallo sviluppatore. Questa funzione ovviamente definisce che cosa andrà ad effettuare
il codcie alla ricezione di una GET, POST, ... (di un qualsiasi metodo). Per interagire con delle risorse (per recuperarle, modificarle, inserirle, etc.)
si ha bisogno di una sorgente di dati

############ Esempio1: #################
from flask import Flask, request, jsonify

app = Flask(__name__) # proprietà del file python che sta girando in questo momento

@app.get("/todos") # Decoratore: tramite esso si va subito sotto a definire una funzione che dice: 'rendi JSON questo elenco e poi restituiscilo all'utente con stato HTTP 200'
def get_todos():
    return jsonify(todos), 200 # Restituisco al Client una lista di todo in formato JSON (con stato HTTP 200)

Grazie alla riga @app.get("/todos") sto dicendo all'application Web che lo gestirà (in questo Flask) che quello è il metodo a cui passare tutte le richieste
che arrivano a questo server all'URL "/todos". Quindi, il matching tra l'URL che viene richiesto da un client remoto e come gestirlo viene fatto in modo
molto semplice e anche visivamente immediato semplicemente dicendo: 'guarda che per le GET alla web app all'URL "/todos" sono gestite dalla funzione che ti metto qui sotto'.
Questo lo posso fare per tutti gli URL che voglio e per tutti i verbi HTTP che voglio (GET, POST, DELETE, ...)

############ Esempio2: #################
# Per prendere un parametro inserito all'interno dell'URL:
@app.get("todos/<id>")
def get_toto_by_id(id):
    to_return = _find_todo_by_id(id)
    if to_return is None:
        return "{}", 404
    else:
        return jsonify(to_return), 200

In questo caso il client vuole ottenere i todos con un determiato id, ma questo può variare (perchè un utente può fare una get "/todos/1" ma anche "/todos/5"),
dunque ci deve essere un modo per dire al framework di comprendere qual'è questo id e passarlo poi al metodo che effettuerà le operazioni richieste per servire
la richiesta del client. Per fare ciò, nel decoratore inserisco il parametro tra parentesi angolari <id>.
Successivamente, nel metodo (che va scritto nella riga successiva) fra parentesi  si passa come argomento il nome che ho dato a questo parametro.
La funzione dell'esempio va a chiamare un metodo che cerca dentro (un database, un dizionario di elenchi) il todos con id desiderato. Se lo trova, allora lo
rappresenta in formato JSON e lo restituisce al client; alternativamente, crea un oggetto JSON vuoto "{}" con stato HTTP 404 not fuond.

Grazie al decoratore si ottiene un duplice effetto: 1) la parte fissa "/todos/" sto identificando quali URL richiesti a questo server devono essere
gestiti dalla funzione sottostante. Tutto ciò che ha todos sarà gestito da questa funzione.
2) Grazie a questo approccio del <identificativo>, sono in grado di parametrizzare: dunque, parte dell'URL mi serve per identificare quale funzione dovrà
gestire questa API, parte dell'URL diventa un input della funzione stessa.
Qui vedo l'esempio con Python, ma lo stesso Design Pattern in realtà lo trovo in molti altri framework di altri linguaggi di programmazione.

Creare un'API Rest lo posso fare con il framework Flask. Per testare la propria API Rest si può utilizzare un programma quale Insomnia:
Mi serve per capire se un metodo è stato implementato correttamente, per vedere se un metodo risponde come dovrebbe alle richieste di un client.
Per fare questo tipo di test sarebbe necessario andarsi a scrivere anche un client che poi contatta la mia applicazione. In questo caso, Insomnia o 
Postman che consentono di effettuare diversi tipi di richieste a un qualsiasi server Rest (In questo caso, quello sviluppato da me)   
"""
from tokenize import Double
from flask import Flask, request, jsonify # Importo Flask, request, jsonify
# from neopixel import *
# from gestioneLED import accendiTuttiLED, LED 
from gestioneRGB import *
from gestioneMoove import *
from gestioneSensoreUltrasonico import *
from gestioneServo import *
import os
import subprocess

# sys.path.append("./rpi_ws281x")
# import _rpi_ws281x as ws

app = Flask(__name__) # proprietà del file python che sta girando in questo momento
# app.config['SERVER_NAME'] = 'marsroverpicarb'

@app.route('/')
def root_response():
    return "<h1>Benvenuto/a nel Server Restful di attuazione del Mars Rover PiCar-B.</h1>"
"""
@app.get("/todos") # Decoratore
def get_todos():
    return jsonify(todos), 200 # Restituisco al Client una lista di todo in formato JSON (con stato HTTP 200)
"""
########################################### GESTIONE RGB ##############################################

""" 
DIZIONARI NECESSARIO PER AGEVOLARE IL CONTROLLO DEI COMPONENTI DEL MARS ROVER: permettono di automatizzare la scelta sul tipo di attuazione.
Nota che sto mappando strighe --> funzioni().
LISTE NECESSARIE COME "DATABASE" PER IL TIPO DI OPERAZIONI
"""
# RGB
coloriRGB = {
             'rosso': rosso,
             'verde':verde,
             'blu': blu,
             'giallo':giallo,
             'ciano':ciano,
             'rosa':rosa
            }

listaRGB = [ "rosso",
             "verde",
             "blu",
             "giallo",
             "ciano",
             "rosa"
            ]


# MOOVE
movimentiMoove = {
                    "avanti": avanti,
                    "retromarcia":retromarcia,
                    "avantiTemporizzato" : avantiTemporizzato,
                    "retromarciaTemporizzato" : retromarciaTemporizzata
                }
listaMoove = [
                "avanti",
                "retromarcia",
                "avantiTemporizzato",
                "retromarciaTemporizzato"
             ]



# SERVO
movimentiServo = {
                  "alzaTesta": alzaTesta,
                  "abbassaTesta": abbassaTesta,
                  "giraRuoteDestra": giraRuoteDestra,
                 }
listaServo =    [
                 "alzaTesta",
                 "abbassaTesta",
                 "giraRuoteDestra"
                ]



# SENSORE ULTRASONICO
sensorizzazioni =   {
                        "calcolaDistanza": calcolaDistanza,
                        "calcolaDistanzaMedia": calcolaDistanzaMedia
                    }
listaSensorizzazioni = ["calcolaDistanza", "calcolaDistanzaMedia"]

# LED POSTERIORI
ledPosteriori = {}



@app.get("/RGB/rosso/<durata>") # Decoratore GET di prova
def get_rosso(durata):
    """IL CLIENT RICHIEDE L'ACCENSIONE DI UN LED RGB DI COLORE ROSSO"""
    try:
        rosso(int(durata))
    except ValueError:
        GPIO.cleanup()  # Serve per il fastidioso errore tra BCM vs BOARD (Per poter usare i LED)
        rosso(int(durata))
    

@app.get("/RGB")
def get_colori():
    """ IL CLIENT VUOLE L'ELENCO DEI COLORI """
    #return coloriRGB.keys(), 200 # ottengo l'elenco delle chiavi sotto forma di lista di stringhe e le ritorno in formato json al client
    # listaRGB = []
    # for i in coloriRGB.keys():
    #     listaRGB.append(coloriRGB.keys()[i])
    return jsonify(listaRGB), 200




@app.post("/RGB/<colore>/<durata>") # Decoratore POST valido per tutti i led RGB
def accendi_RGB(colore, durata):
    """ IL CLIENTE RICHIEDE L'ACCENSIONE DI UN LED RGB """
    durata = int(durata)
    if colore in coloriRGB:
        try:
            coloriRGB[colore](durata)
        except ValueError:
            GPIO.cleanup()  # Serve per il fastidioso errore tra BCM vs BOARD (Per poter usare i LED)
            print("Cambio settaggi per il GPIO")
            coloriRGB[colore](durata)
        return {"messaggio": "Acceso il led RGB " + colore},200
    else:
        return {"messaggio": "Errore sulla scelta del colore"}, 415

@app.post("/RGB/spegni")
def spegni_RGB():
    """ IL CLIENT RICHIEDE LO SPEGNIMENTO DI UN LED RGB"""
    both_off()
    return {"messaggio": "Spento i led RGB"}, 200







####################################### GESTIONE MOOVE ################################################################
@app.get("/moove/avanti/<velocita>") # Decoratore GET di prova
def get_moove_avanti(velocita):
    """IL CLIENT RICHIEDE L'AVANZAMENTO IN AVANTI DELL'AUTO"""
    velocita = float(velocita)
    avanti(velocita,velocita)

@app.get("/moove")
def get_movimenti():
    """ IL CLIENT VUOLE L'ELENCO DEI MOVIMENTI """
    return jsonify(listaMoove), 200

@app.post("/moove/<movimento>/<velocita>") 
def muovi_Robot(movimento, velocita):
    """ IL CLIENT RICHIEDE L'ATTUAZIONE DI UN MOVIMENTO AD UNA CERTA VELOCITA'"""
    # Controlli sugli "input"
    velocita = float(velocita)
    if 0 > velocita < 100:
        return {"messaggio": "Attenzione: la velocità deve essere un numero compreso tra 0 e 100), inserire nuovamente un valore di veloctità: "}, 415
    if movimento in movimentiMoove:
        try:
            movimentiMoove[movimento](velocita,velocita)
        except ValueError:
            GPIO.cleanup()  # Serve per il fastidioso errore tra BCM vs BOARD (Per poter usare i LED)
            print("Cambio settaggi per il GPIO")
            movimentiMoove[movimento](velocita,velocita)
        return {"messaggio": "Attuato il seguente movimento: " + movimento }, 200
    else:
        return {"messaggio": "Il movimento: "+ movimento + " non può essere attuato. "}, 415

@app.post("/moovetemporizzata/<movimento>/<tempo>")
def muovi_Robot_Temporizzato(movimento, tempo):
    """ IL CLIENT RICHIEDE L'ATTUAZIONE DI UN MOVIMENTO PER UN CERTO NUMERO DI SECONDI'"""
    # Controlli sugli "input"
    tempo = int(tempo)
    if 0 > tempo < 15:
        return {"messaggio": "Attenzione: il tempo massimo è di 15 secondi: "}, 415
    if movimento in movimentiMoove:
        try:
            movimentiMoove[movimento](tempo)
        except ValueError:
            GPIO.cleanup()  # Serve per il fastidioso errore tra BCM vs BOARD (Per poter usare i LED)
            print("Cambio settaggi per il GPIO")
            movimentiMoove[movimento](tempo)
        return {"messaggio": "Attuato il seguente movimento: " + movimento }, 200
    else:
        return {"messaggio": "Il movimento: "+ movimento + " non può essere attuato. "}, 415








##################################### GESTIONE SERVO #########################################
@app.get("/servo")
def get_movimenti_servo():
    """ IL CLIENT VUOLE L'ELENCO DEI MOVIMENTI DEL SERVO"""
    return jsonify(listaServo), 200

@app.post("/servo/<movimento>/<velocita>/<inclinazione>") 
def muovi_servo_Robot(movimento, velocita, inclinazione):
    """ IL CLIENT RICHIEDE L'ATTUAZIONE DEL SERVO AD UNA CERTA VELOCITA'"""
    # Controlli sugli "input"
    velocita = int(velocita)
    inclinazione = int(inclinazione)
    if 0 > velocita < 100:
        return {"messaggio": "Attenzione: la velocità deve essere un numero compreso tra 0 e 100), inserire nuovamente un valore di veloctità: "}, 415
    if movimento in movimentiServo:
        movimentiServo[movimento](velocita, inclinazione)
        return {"messaggio": "Attuato il seguente movimento: " + movimento }, 200
    else:
        return {"messaggio": "Il movimento: "+ movimento + " non può essere attuato. "}, 415










############################## GESTIONE SENSORE ULTRASONICO ##############################
@app.get("/ultra")
def get_ultra():
    """ IL CLIENT VUOLE L'ELENCO DELLE OPERAZIONI DEL SENSORE ULTRASONICO"""
    return jsonify(listaSensorizzazioni), 200

@app.get("/ultra/<operazione>/<durata>")
def get_risultato_ultra(operazione, durata):
    """ IL CLIENT VUOLE AVVIARE IL SENSORE ULTRASONICO PER CALCOLARE UN RISULTATO"""
    durata = int(durata)
    if operazione in sensorizzazioni:
        try:
            return jsonify(stampa(sensorizzazioni[operazione](durata)))
        except ValueError:
            GPIO.cleanup()  # Serve per il fastidioso errore tra BCM vs BOARD (Per poter usare i LED)
            print("Cambio settaggi per il GPIO")
            return jsonify(stampa(sensorizzazioni[operazione](durata)))
        # return {"messaggio": "Attuato il seguente movimento: " + movimento }, 200
    else:
        return {"messaggio": "Operazione non implementata. "}, 415

# Sarebbe bello poter fare delle azioni coordinate








############################################### GESTIONE PIXEL LED #########################################
# led = LED() # VARIABILE GLOBALE NECESSARIA PER ESSERE PILOTATA

@app.post("/led/<R>/<G>/<B>") 
def accendi_led(R, G, B):
    """ IL CLIENT RICHIEDE L'ACCENSIONE DEI UN LED PIXEL'"""
    # # accendiTuttiLED(R,G,B)
    # # os.sys("gestioneLED.py")
    # Blu = B
    # Verde = G
    # Rosso = R
    subprocess.call(['sh', 'avviaGestioneLED.sh', R, G, B]) 
    return {"risposta": "Acceso tutti i LED"}, 200



@app.post("/led/<R>/<G>/<B>/<led_i>") 
def accendi_led_i(R, G, B,led_i ):
    """ IL CLIENT RICHIEDE L'ACCENSIONE DEI UN LED PIXEL'"""
    subprocess.call(['sh', 'avviaGestioneLED.sh', R, G, B, led_i]) 
    return {"risposta": "Acceso tutti i LED"}, 200

@app.post("/led/spegni") 
def spegni_led():
    """ IL CLIENT RICHIEDE LO SPEGNIMENTO DEI  LED PIXEL'"""
    subprocess.call(['sh', 'avviaGestioneLED.sh', "spegni"]) 
    return {"risposta": "Spento tutti i LED"}, 200




if __name__ == '__main__':
    app.run(host='0.0.0.0', port="5000", debug=True)
    try:
        pass
    except RuntimeError:
        GPIO.cleanup()  # Serve per il fastidioso errore tra BCM vs BOARD (Per poter usare i LED)
    except KeyboardInterrupt:
        print("Il server ha terminato l'esecuzione.")



