Savitar dice que: "Las direcciones IP son identificadores numéricos únicos que se utilizan para identificar dispositivos en una red, como ordenadores, routers, servidores y otros dispositivos conectados a Internet.

Existen dos versiones de direcciones IP: **IPv4** e **IPv6**. La versión **IPv4** utiliza un formato de dirección de **32 bits** y se utiliza actualmente en la mayoría de las redes. La versión **IPv6** utiliza un formato de dirección de **128 bits** y se está implementando gradualmente en todo el mundo para hacer frente a la escasez de direcciones IPv4.

Las direcciones IPv4 se representan como cuatro números separados por puntos, como **192.168.0.1**, mientras que las direcciones IPv6 se representan en notación hexadecimal y se separan por dos puntos, como **2001:0db8:85a3:0000:0000:8a2e:0370:7334**."

El siguiente comando ayuda a convertir la IP en bits(8 bits que corresponden):
`echo "$(echo "obase=2; 192" | bc).$(echo "obase=2; 168" | bc).$(echo "obase=2; 100" | bc).$(echo "obase=2; 11" | bc)"`

