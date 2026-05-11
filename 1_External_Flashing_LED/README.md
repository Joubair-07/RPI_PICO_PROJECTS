# External Flashing LED


## Description
  In this project, an external LED is connected to Pico, and the LED is flashed
every second.

## Aim
  The aim of this project is to show how an external LED can be connected to Pico.

## Installation
  The LED can be connected in either current-sourcing or in current-sinking modes:

Current-sourcing mode : the LED is turned on when logic HIGH is applied to the port pin.
<img width="181" height="127" alt="curent_sourcing_mode" src="https://github.com/user-attachments/assets/0797e873-0b67-4376-990b-ab358373ed14" />

Curent-sniking mode   : the LED is turned on when logic LOW is applied to the port pin.
<img width="178" height="121" alt="current_sniking_mode" src="https://github.com/user-attachments/assets/b3e6eb26-e734-4709-9f54-88b9332eaae8" />

##Finding current-limiting resistor
To calculate the current-limiting resistor we use "Lois de Maille":
<img width="2316" height="1900" alt="demenstrartion" src="https://github.com/user-attachments/assets/1e30f96d-cdd2-4a3a-a023-ea43aa4e71ff" />

In the current-sourcing mode, 
	The output HIGH voltage is 3.3V.
	The voltage drop across the LED is 2V.
	The current through the LED is 3mA.


	Then, R = (3.3 - 2) / 3 = 433 ohm
We are going to use 470 ohms as the nearest resistor

Final result : 
<img width="195" height="236" alt="block_diagram_of_the_project" src="https://github.com/user-attachments/assets/c0ea3824-5b81-4cab-9512-a9a590918a36" />



