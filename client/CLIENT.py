from concurrent.futures import thread
from fileinput import filename
from tkinter import *
from tkinter import font
from tkinter import colorchooser
from tkinter import messagebox
from turtle import bgcolor, st, width
import requests
import threading # Per gestire azioni coordinate: così si può schiacciare più pulsanti e rendere il tutto asincrono
import os
import sys


api_url = "http://192.168.1.114:5000"  # URL da contattare
my_headers = {"Content-type": "application/json"} # Formato json


master = Tk() # Finestra principale
master.title("Client Grafico Progetto Tesi") # titolo finestra
master.geometry("2000x850") # dimensioni finestra
master.config(bg="#a3c2c2") # colore di sfondo finestra
# master.after() # non srve a nulla
# font.families()
# master.option_add("*Font", "Times New Roman")












#####################################################################################################################
####################################### GESTIONE COLORE RGB #########################################################
#####################################################################################################################

# RECUPERO L'INSIEME DI TUTTI I COLORI RGB DAL SERVER
print("GET /RGB")
richiestaListaRGB = requests.get(f"{api_url}/RGB", headers=my_headers)
print("La richiesta è stata fatta al seguente URL: ", richiestaListaRGB.url) # risposta.url mi mostra l'url "espanso"
print(f"Stato HTTP: {richiestaListaRGB.status_code}")
print(f"Risposta dal server:\n{richiestaListaRGB.json()}")
richiestaListaRGB = richiestaListaRGB.json()



# ETICHETTA RGB
etichettaRGB = Label(text="GESTIONE RGB", bg="#a3c2c2", font="helvetica 15 bold") ## testo in grassetto
etichettaRGB.grid(row=0,column=0,  sticky=W , padx=20, pady=10) # Disposto in prima riga e prima colonna

# MENU SELEZIONE COLORE RGB
# Etichetta durata di accensioen
etichettaSelezionaColoreRGB = Label(text="Seleziona un colore:", bg="#a3c2c2", font="helvetica 10") ## testo in grassetto
etichettaSelezionaColoreRGB.grid(row=1,column=0,  sticky=W ,pady=0, padx=20) # Disposto in prima riga e prima colonna

variabileColoreRGB = StringVar(master)
variabileColoreRGB.set(richiestaListaRGB[0]) # di default in cima alla lista compare il primo
selezioneRGB = OptionMenu(master, variabileColoreRGB, *richiestaListaRGB)
selezioneRGB.grid(row=2,column=0,  sticky=W , padx=20, pady=10)# # Viene disposto sotto all'elemento definito sopra



# ENTRY TEMPO DI ACCENSIONE
# Etichetta
etichettaDurataRGB = Label(text="Tempo di accensione:", bg="#a3c2c2", font="helvetica 10") ## testo in grassetto
etichettaDurataRGB.grid(row=3,column=0,  sticky=W ,pady=0, padx=20) # Disposto in prima riga e prima colonna
# Entry
variabileDurataDiAccensione = IntVar(master, value=4)
durataDiAccensione = Entry(textvariable=variabileDurataDiAccensione, justify=RIGHT, width=10)
# durataDiAccensione.insert(0,"4")
durataDiAccensione.grid(row=4,column=0,  sticky=W , padx=20,)



# BOTTONE CHE GESTISCE ACCENSIONE LED RGB: quando viene cliccato scatena una richiesta di tipo POST al server
button = Button(master, text="Accendi", command=lambda: threading.Thread(target=print(requests.post(f"{api_url}/RGB/"f"{variabileColoreRGB.get()}/"f"{variabileDurataDiAccensione.get()}").json())).start()) # necessario che il colore sia quello appena selezionato variabilecoloreRGB.get() e lo stesso per la durata
button.grid(row=5, column=0,  sticky=W , padx=20, pady=10)

# BOTTONE CHE GESTISCE SPEGNIMENTO LED RGB: quando viene cliccato scatena una richiesta di tipo POST al server
button = Button(master, text="Spegni", command=lambda: threading.Thread(target=print(requests.post(f"{api_url}/RGB/spegni").json())).start()) #
button.grid(row=6, column=0, sticky=W , padx=20, pady=10)


























##############################################################################################
####################################### GESTIONE MOOVE #######################################
##############################################################################################



# RECUPERO L'INSIEME DI TUTTI I MOVIMENTI DAL SERVER
print("GET /moove")
richiestaListaMovimenti = requests.get(f"{api_url}/moove", headers=my_headers)
print("La richiesta è stata fatta al seguente URL: ", richiestaListaMovimenti.url) # risposta.url mi mostra l'url "espanso"
print(f"Stato HTTP: {richiestaListaMovimenti.status_code}")
print(f"Risposta dal server:\n{richiestaListaMovimenti.json()}")
richiestaListaMovimenti = richiestaListaMovimenti.json()


# ETICHETTA MOOVE
etichettaMoove = Label(text="GESTIONE MOOVE", bg="#a3c2c2", font="helvetica 15 bold") ## testo in grassetto
etichettaMoove.grid(row=0,column=1,  sticky=W , padx=20, pady=10) # Disposto in prima riga e prima colonna

# MENU SELEZIONE MOVIMENTO
# Etichetta selezione movimento
etichettaSelezionaMovimento = Label(text="Seleziona un movimento:", bg="#a3c2c2", font="helvetica 10") ## testo in grassetto
etichettaSelezionaMovimento.grid(row=1,column=1,  sticky=W ,pady=0, padx=20) # Disposto in prima riga e prima colonna

variabileMovimento = StringVar(master)
variabileMovimento.set(richiestaListaMovimenti[0])
selezioneMovimenti = OptionMenu(master, variabileMovimento, *richiestaListaMovimenti)
selezioneMovimenti.grid(row=2,column=1,  sticky=W , padx=20, pady=10)# # Viene disposto sotto all'elemento definito sopra


# ENTRY VELOCITA'
# Etichetta durata di accensioen
etichettaVelocitaMovimento = Label(text="Velocità movimento:", bg="#a3c2c2", font="helvetica 10") ## testo in grassetto
etichettaVelocitaMovimento.grid(row=3,column=1,  sticky=W ,pady=0, padx=20) # Disposto in prima riga e prima colonna

variabileVelocitaMovimento = IntVar(master, value=100)
velocitaMovimento = Entry(textvariable=variabileVelocitaMovimento, justify=RIGHT, width=10,)
velocitaMovimento.grid(row=4,column=1,  sticky=W , padx=20,)


# BOTTONE CHE GESTISCE AVVIO MOVIMENTO: quando viene cliccato scatena una richiesta di tipo POST al server
button = Button(master, text="Muoviti", command=lambda: threading.Thread(target=print(requests.post(f"{api_url}/moove/"f"{variabileMovimento.get()}/"f"{variabileVelocitaMovimento.get()}").json())).start()) # necessario che il colore sia quello appena selezionato variabilecoloreRGB.get() e lo stesso per la durata
button.grid(row=5, column=1,  sticky=W , padx=20, pady=10)




# ENTRY DURATA MOVIMENTO TEMPORIZZATO
# Etichetta durata di accensione
etichettaDurataMovimento = Label(text="Durata movimento:", bg="#a3c2c2", font="helvetica 10") ## testo in grassetto
etichettaDurataMovimento.grid(row=6,column=1,  sticky=W , padx=20) # Disposto in prima riga e prima colonna

variabileDurataMovimento = IntVar(master, value=3)
durataMovimento = Entry(textvariable=variabileDurataMovimento, justify=RIGHT, width=10)
durataMovimento.grid(row=7,column=1,  sticky=W , padx=20,)


# BOTTONE CHE GESTISCE AVVIO MOVIMENTO TEMPORIZZATO: quando viene cliccato scatena una richiesta di tipo POST al server
button = Button(master, text="Muoviti a tempo", command=lambda: threading.Thread(target=print(requests.post(f"{api_url}/moovetemporizzata/"f"{variabileMovimento.get()}/"f"{variabileDurataMovimento.get()}").json())).start()) 
button.grid(row=8, column=1,  sticky=W , padx=20, pady=10)


























##############################################################################################
####################################### GESTIONE SERVO #######################################
##############################################################################################

# RECUPERO L'INSIEME DI TUTTI I MOVIMENTI DEL SERVO DAL SERVER
print("GET /servo")
richiestaListaMovimentiServo = requests.get(f"{api_url}/servo", headers=my_headers)
print("La richiesta è stata fatta al seguente URL: ", richiestaListaMovimentiServo.url)
print(f"Stato HTTP: {richiestaListaMovimentiServo.status_code}")
print(f"Risposta dal server:\n{richiestaListaMovimentiServo.json()}")
richiestaListaMovimentiServo = richiestaListaMovimentiServo.json()


# ETICHETTA SERVO
etichettaServo = Label(text="GESTIONE SERVO", bg="#a3c2c2", font="helvetica 15 bold") ## testo in grassetto
etichettaServo.grid(row=0,column=2,  sticky=W , padx=20, pady=10) # Disposto in prima riga e prima colonna

# MENU SELEZIONE MOVIMENTO SERVO
# Etichetta selezione movimento
etichettaSelezionaMovimentoServo = Label(text="Seleziona un movimento:", bg="#a3c2c2", font="helvetica 10") ## testo in grassetto
etichettaSelezionaMovimentoServo.grid(row=1,column=2,  sticky=W ,pady=0, padx=20) # Disposto in prima riga e prima colonna
# Menù
variabileMovimentoServo = StringVar(master)
variabileMovimentoServo.set(richiestaListaMovimentiServo[0])
selezioneMovimentiServo = OptionMenu(master, variabileMovimentoServo, *richiestaListaMovimentiServo)
selezioneMovimentiServo.grid(row=2,column=2,  sticky=W , padx=20, pady=10)# # Viene disposto sotto all'elemento definito sopra


# ENTRY VELOCITA'
# Etichetta 
etichettaVelocitaMovimentoServo = Label(text="Velocità movimento servo:", bg="#a3c2c2", font="helvetica 10") ## testo in grassetto
etichettaVelocitaMovimentoServo.grid(row=3,column=2,  sticky=W ,pady=0, padx=20) # Disposto in prima riga e prima colonna
# Entry
variabileVelocitaMovimentoServo = IntVar(master, value=3)
velocitaMovimentoServo = Entry(textvariable=variabileVelocitaMovimentoServo, justify=RIGHT, width=10)
velocitaMovimentoServo.grid(row=4,column=2,  sticky=W , pady=10, padx=20,)


# ENTRY INCLINAZIONE'
# Etichetta
etichettaInclinazioneServo = Label(text="Angolo di inclinazione del servo:", bg="#a3c2c2", font="helvetica 10") ## testo in grassetto
etichettaInclinazioneServo.grid(row=5,column=2,  sticky=W ,pady=0, padx=20) # Disposto in prima riga e prima colonna
# Entry
variabileInclinazioneServo = IntVar(master, value=300)
inclinazioneServo = Entry(textvariable=variabileInclinazioneServo, justify=RIGHT, width=10)
inclinazioneServo.grid(row=6,column=2,  sticky=W , padx=20, pady=0)


# BOTTONE CHE GESTISCE AVVIO MOVIMENTO SERVO: quando viene cliccato scatena una richiesta di tipo POST al server
button = Button(master, text="Aziona", command=lambda: threading.Thread(target=print(requests.post(f"{api_url}/servo/"f"{variabileMovimentoServo.get()}/"f"{variabileVelocitaMovimentoServo.get()}/"f"{inclinazioneServo.get()}").json())).start())
button.grid(row=7, column=2,  sticky=W , padx=20, pady=10)














###############################################################################################################
#######################################   GESTIONE SENSORE ULTRASONICO  #######################################
###############################################################################################################
   
# RECUPERO L'INSIEME DI TUTTE LE OPERAZIONI POSSIBILI OFFERTE DAL SENSORE ULTRASONICO
print("GET /utra")
richiestaSensorizzazioniUltra = requests.get(f"{api_url}/ultra", headers=my_headers)
print("La richiesta è stata fatta al seguente URL: ", richiestaSensorizzazioniUltra.url) # risposta.url mi mostra l'url "espanso"
print(f"Stato HTTP: {richiestaSensorizzazioniUltra.status_code}")
print(f"Risposta dal server:\n{richiestaSensorizzazioniUltra.json()}")
richiestaSensorizzazioniUltra = richiestaSensorizzazioniUltra.json()



# ETICHETTA ULTRA
etichettaUltra = Label(text="GESTIONE ULTRA", bg="#a3c2c2", font="helvetica 15 bold") ## testo in grassetto
etichettaUltra.grid(row=0,column=3,  sticky=W , padx=20, pady=10) # Disposto in prima riga e prima colonna

# MENU SELEZIONE OPERAZIONE
# Etichetta
etichettaSelezionaOperazioneUltra = Label(text="Seleziona un'operazione:", bg="#a3c2c2", font="helvetica 10") ## testo in grassetto
etichettaSelezionaOperazioneUltra.grid(row=1,column=3,  sticky=W ,pady=0, padx=20) # Disposto in prima riga e prima colonna
# Entry
variabileOperazioneUltra = StringVar(master)
variabileOperazioneUltra.set(richiestaSensorizzazioniUltra[0]) # di default in cima alla lista compare il primo
selezioneUltra = OptionMenu(master, variabileOperazioneUltra, *richiestaSensorizzazioniUltra)
selezioneUltra.grid(row=2,column=3,  sticky=W , padx=20, pady=10)# # Viene disposto sotto all'elemento definito sopra



# ENTRY TEMPO DI SENSORIZZAZIONE
# Etichetta
etichettaDurataUltra = Label(text="Tempo di sensorizzazione:", bg="#a3c2c2", font="helvetica 10") ## testo in grassetto
etichettaDurataUltra.grid(row=3,column=3,  sticky=W ,pady=0, padx=20) # Disposto in prima riga e prima colonna
# Entry
variabileDurataUltra = IntVar(master, value=12)
durataUltra = Entry(textvariable=variabileDurataUltra, justify=RIGHT, width=10)
durataUltra.grid(row=4,column=3,  sticky=W , padx=20,)


risultatoUltra = []
# nomeFile = "risultatoUltra.txt"


# BOTTONE CHE GESTISCE AVVIO SENSORIZZAZIONE SENSORE ULTRASONICO: quando viene cliccato scatena una richiesta di tipo POST al server
button = Button(master, text="Avvia Sensorizzazione", command=lambda: messagebox.showinfo("Calcolo distanza", requests.get(f"{api_url}/ultra/"f"{variabileOperazioneUltra.get()}/"f"{variabileDurataUltra.get()}").json() ))
button.grid(row=5, column=3,  sticky=W , padx=20, pady=10)
# f.close()




















###############################################################################################################
#######################################   GESTIONE LED PIXEL  #######################################
###############################################################################################################



# ETICHETTA LED PIXEL
etichettaUltra = Label(text="GESTIONE LED IN PIXEL", bg="#a3c2c2", font="helvetica 15 bold") ## testo in grassetto
etichettaUltra.grid(row=0,column=4,  sticky=W , padx=20, pady=10) # Disposto in prima riga e prima colonna

def impostaColoreEAccendiLED():
    colore = colorchooser.askcolor()
    R, G, B = colore[0]
    requests.post(f"{api_url}/led/"f"{R}/"f"{G}/"f"{B}").json()

def impostaColoreEAccendiLED_i():
    colore = colorchooser.askcolor()
    R, G, B = colore[0]
    led_i = varLED2.get()
    requests.post(f"{api_url}/led/"f"{R}/"f"{G}/"f"{B}/"f"{led_i}").json()   


# Bottone per scelta del colore
bottoneColoreLED = Button(master,text="Accendi tutti i LED", command= impostaColoreEAccendiLED) 
# etichettaSelezionaOperazioneUltra.grid(row=1,column=4,  sticky=W ,pady=0, padx=20) # Disposto in prima riga e prima colonna
bottoneColoreLED.grid(row=2, column=4,  sticky=W , padx=20, pady=10)


# Bottone per scelta del colore
bottoneSpegniLED = Button(master,text="Spegni tutti i LED", command=lambda: print(requests.post(f"{api_url}/led/spegni").json() ))
bottoneSpegniLED.grid(row=3, column=4,  sticky=W , padx=20, pady=10)

# Checkbutton: accensione singolo colore
# 2 --> varLED2 --> LED sopra
# 1 --> varLED1 --> LED centrale
# 0 --> varLED0 --> LED sotto
etichettaLEDSingolo = Label(text="Accendi il singolo LED", bg="#a3c2c2", font="helvetica 10")
etichettaLEDSingolo.grid(row=4, column=4, sticky=NS, pady=0, padx=20)


varLED2 = IntVar(value=2)
chk1 = Radiobutton(text="LED 2", variable=varLED2, value=2, bg="#a3c2c2", font="helvetica 10", command=impostaColoreEAccendiLED_i)
chk1.grid(row=5,column=4, sticky=NS, pady=0, padx=20)

# varLED1 = IntVar
chk2 = Radiobutton(text="LED 1", variable=varLED2, value=1, bg="#a3c2c2", font="helvetica 10", command=impostaColoreEAccendiLED_i)
chk2.grid(row=6,column=4, sticky=NS, pady=0, padx=20)

# varLED0 = IntVar
chk3 = Radiobutton(text="LED 0", variable=varLED2, value=0, bg="#a3c2c2", font="helvetica 10", command=impostaColoreEAccendiLED_i)
chk3.grid(row=7,column=4, sticky=NS, pady=0, padx=20)



# Avvia la GUI
mainloop()
