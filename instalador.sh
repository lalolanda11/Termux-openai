#!bin/bash

if [ -e /data/data/com.termux/files/usr/lib/python ];then
  continue

else    
  pkg update && pkg upgrade -y
  sleep 1
  pkg install python -y
  pkg install termux-api -y
  pkg install termux-service -y
  fi

verde="\033[1;32m"
echo -n "Si para crear un entorno nuevo \n No para crearlo de manera global" 
read dato 
case $dato in 
  "Si")
    ruta=$(pwd)

    python -m venv env 
    sleep 5
    source $ruta/env/bin/activate
    sleep 3
    pip install pip --upgrade
    sleep 2
    pip install openai
    
    ;;
  "no")
    continue
    ;;
esac



  
