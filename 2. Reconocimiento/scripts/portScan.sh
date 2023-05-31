#!/bin/bash

# ctrl + c
trap ctrl_c SIGINT

# functions

function ctrl_c(){
  echo -e "\n\n [!]Saliendo...!"
  tput cnorm; exit 1
  
}

function checkPort(){
  (exec 3<> /dev/tcp/$1/$2) 2>/dev/null 
  
  if [ $? -eq 0 ]; then
    echo -e "\n[+] Host $1 -> Port $2(OPEN)"
  fi

  exec 3<&-
  exec 3>&-
}

declare -a ports=( $(seq 1 65535) )

tput civis
if [ $1 ]; then

  for port in ${ports[@]}; do
    checkPort $1 $port &
  done

else
  echo -e "\n[!] Uso: $0 <ip-address>\n"
fi

wait
tput cnorm


