#!/bin/bash


# ctrl + c
trap ctrl_c SIGINT

#funciones

function ctrl_c(){
  echo -e "\n\n[!] Saliendo..."
  tput cnorm; exit 1
}


tput civis
for host in $(seq 1 254); do
  for port in 21 22 23 25 139 445 80 8080; do
    timeout 2 bash -c "echo '' > /dev/tcp/192.168.100.$host/$port" 2>/dev/null && echo "[+] Hosts 192.168.100.$host (ACTIVO) - Port $port (ACTIVO)" &

done
done

wait

tput cnorm
