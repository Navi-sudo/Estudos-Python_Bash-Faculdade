#!/bin/bash


# exemplo de controle de fluxo IF


echo "Verificando o dia..."
sleep 2
echo " " 
if date | grep Dom
then 
	echo "Aproveite o dia!"
else
	echo "Vá estudar"
fi
