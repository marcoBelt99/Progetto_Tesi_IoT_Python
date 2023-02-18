#!/bin/bash

# # Test su passaggio dei parametri
# echo "I parametri raccolti dal server sono:"
# cont=0
for i in "$@" # Ciclo tutti i parametri passati a linea di comando dal server
do
    echo $i
    cont=$((cont+1))
done
echo "In tutto sono stati raccolti: $cont parametri" 
# Leggo la password di sistema, la passo come stdin a sudo e passo i parametri al file gestionLED

case $cont in

  1)
    echo `cat pwd.dat` | sudo -S python3 gestioneLED_SpegniTutti.py "$@"
    ;;

  3)
    echo `cat pwd.dat` | sudo -S python3 gestioneLED_AccendiTutti.py "$@"
    ;;

  4)
    echo `cat pwd.dat` | sudo -S python3 gestioneLED_Accendi_i_Esimo.py "$@"
    ;;

  *)
    echo -n "Passare il giusto numero di parametri"
    ;;
esac
