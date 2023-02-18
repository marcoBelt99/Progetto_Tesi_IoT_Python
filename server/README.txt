Nella directory corrente sono presenti alcuni moduli necessari al funzionamento del Mars Rover Picar-B.
Il file 'programmazioneMarsRoverPiCarB.py' è lo script python di test delle funzionalità analizzate di tale robot.
Questo stesso file è anche manutenibile e soprattutto estendibile: col tempo, se si vorranno studiare ulteriori funzionalità,
sarà necessario solamente aggiungere un modulo contente alcune funzioni che eseguono il comportamento desiderato.
Il succitato file è per testare la macchina nel concentrato.

Per utilizzare la macchina nel distribuito, si fa uso della Rest API di nome: "SERVER.py"

* Per problemi legati all'assenza di un modulo particolare eseguire:
>   pip3 install <nome_modulo> 
Ad Es. per il modulo RPi.GPIO fare:
>   pip3 install RPi.GPIO

* /home/rasp/programmazioneMarsRoverPiCarB/Adafruit_Python_PCA9685 questo direttorio contiene i file della libreria: Adafruit_PCA9685

* Attivare sempre l'ambiente virtuale con: 
>   source /home/rasp/programmazioneMarsRoverPiCarB/venv/bin/activate

**********  Far partire l'applicazione: ***********
>   export FLASK_APP=SERVER.py.py
>   flask run

Questo avvia un server integrato molto semplice, che è abbastanza buono per il test ma probabilmente non quello che vuoi usare in produzione. 
Per le opzioni di distribuzione, vedere Opzioni di distribuzione .

Ora vai su http://127.0.0.1:5000/ e dovresti vedere il tuo saluto mondiale.



**** SERVER VISIBILE ESTERNAMENTE ****
Se esegui il server, noterai che il server è accessibile solo dal tuo computer, non da nessun altro nella rete. 
Questa è l'impostazione predefinita perché in modalità di debug un utente dell'applicazione può eseguire codice Python arbitrario sul tuo computer.
Se hai il debugger disabilitato o ti fidi degli utenti sulla tua rete, 
puoi rendere il server pubblicamente disponibile semplicemente aggiungendo --host=0.0.0.0alla riga di comando:

>   flask run --host=0.0.0.0
Questo dice al tuo sistema operativo di ascoltare su tutti gli IP pubblici.

Opzioni di distribuzione
Sebbene sia leggero e facile da usare, il server integrato di Flask non è adatto per la produzione in quanto non si adatta bene. 
Alcune delle opzioni disponibili per eseguire correttamente Flask in produzione sono documentate qui.

Se desideri distribuire la tua applicazione Flask su un server WSGI non elencato qui, 
consulta la documentazione del server su come utilizzare un'app WSGI con essa. 
Ricorda solo che l' oggetto Flask dell'applicazione è l'effettiva applicazione WSGI.


Opzioni di debug:
export FLASK_DEBUG=1


**** Per problemi: ****
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python-is-python3 python3-pip python3-venv
python -m venv venv
source venv/bin/activate
pip install Adafruit_PCA9685
pip3 install RPi.GPIO
pip install requests Flask
export FLASK_APP=SERVER.py.py
flask run --host=0.0.0.0

