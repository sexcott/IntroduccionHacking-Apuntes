En esta clase, explicamos cómo calcular para la dirección IP **192.168.1.0/26**, su máscara de red, el número total de hosts a repartir, el identificador de red y la dirección Broadcast.

A continuación, se detalla paso a paso cómo hemos ido calculando cada apartado:

1.  **Cálculo de la máscara de red:**

La dirección IP que se nos dio es **192.168.1.0/26**, lo que significa que los primeros **26 bits** de la dirección IP corresponden a la **red** y los últimos **6 bits** corresponden a los **hosts**.

Para calcular la **máscara de red**, necesitamos colocar los primeros **26 bits** en **1** y los últimos **6 bits** en **0**. En binario, esto se ve así:

-   **11111111.11111111.11111111.11000000**

Cada octeto de la máscara de red se compone de **8 bits**. El valor de cada octeto se determina convirtiendo los **8 bits** a **decimal**. En este caso, los primeros **24 bits** son todos **1s**, lo que significa que el valor decimal de cada uno de estos octetos es **255**. El último octeto tiene los últimos **6 bits** en **0**, lo que significa que su valor decimal es **192**.

Por lo tanto, la máscara de red para esta dirección IP es **255.255.255.192**.

2.  **Cálculo del total de hosts a repartir:**

En este caso, se pueden utilizar los **6 bits** que quedan disponibles para representar la parte de **host**. En una máscara de red de **26 bits**, los **6 bits** restantes representan **2^6 – 2 = 62** hosts disponibles para asignar.

El número máximo de hosts disponibles se calcula como **2^(n) – 2**, donde **n** es la cantidad de bits utilizados para representar la parte de red en la máscara de red.

3.  **Cálculo del Network ID:**

Para calcular el **Network ID**, lo que debemos hacer es aplicar la máscara de red a la dirección IP de la red. En este caso, la máscara de red es **255.255.255.192**, lo que significa que los primeros **26 bits** de la dirección IP pertenecen a la parte de **red**.

Para calcular el **Network ID**, convertimos tanto la dirección IP como la máscara de red en **binario** y luego hacemos una operación “**AND**” lógica entre los dos. La operación “**AND**” compara los bits correspondientes en ambas direcciones y devuelve un resultado en el que todos los bits coincidentes son iguales a “**1**” y todos los bits no coincidentes son iguales a “**0**“.

En este caso, la dirección **IP** es **192.168.1.0** en decimal y se convierte en binario como **11000000.10101000.00000001.00000000**. La máscara de red es **255.255.255.192** en decimal y se convierte en binario como **11111111.11111111.11111111.11000000**.

Luego, aplicamos la operación “**AND**” entre estos dos valores binarios bit a bit. Los bits correspondientes en ambos valores se comparan de la siguiente manera:

![[Pasted image 20230409203928.png]]
![](https://hack4u.io/wp-content/uploads/2022/12/bitsAND-693x129.png)

El resultado final es el **Network ID**, que es **192.168.1.0**. Este es el identificador único de la subred a la que pertenecen los hosts.

4.  **Cálculo de la Broadcast Address:**

La **Broadcast Address** es la dirección de red que se utiliza para enviar paquetes a **todos los hosts de la subred**. Para calcularla, necesitamos saber el **Network ID** y la **cantidad de hosts** disponibles en la subred.

En el ejemplo que estamos trabajando, ya hemos calculado el **Network ID** como **192.168.1.0**. La cantidad de hosts disponibles se calcula como **2^(n) – 2**, donde **n** es la cantidad de bits utilizados para representar la parte de host en la máscara de red. En este caso, **n** es igual a **6**, ya que hay **6** bits disponibles para la parte de **host**.

Para calcular la **Broadcast Address**, debemos asignar todos los bits de la parte del **host** de la dirección IP a “**1**“. En este caso, la dirección IP es **192.168.1.0** y se convierte en binario como **11000000.10101000.00000001.00000000**.

Para encontrar la dirección **Broadcast**, llenamos con unos la parte correspondiente a los bits de host, es decir, los últimos **6 bits**:

**11000000.10101000.00000001.00111111** (dirección IP con bits de host asignados a “**1**“)

Luego, convertimos este valor binario de regreso a decimal y obtenemos la dirección de Broadcast: **192.168.1.63**. Esta es la dirección a la que se enviarán los paquetes para llegar a todos los hosts de la subred.