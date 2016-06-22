#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# 22 junio 2016
# Archivo correspondiente al 3er día del curso: "Programando en Python: curso completo"
# del 20 al 24 de junio de 2016 en la Facultad de Ciencias - UGR
# http://www.darwineventur.com/2016/05/programando-en-python-curso-completo.html
#

#
# Rubén Martín Moreno
#


#EJERCICIO
## Crear función que dados dos numeros
## Si son iguales nos imprime 0
## Si el primero es mayor imprime 1
## Si el segundo es mayor imprime 2


#def comparar(num1, num2):
#	if num1 > num2:
#		return 1
#	elif num1 < num2:
#		return 2
#	else:
#		return 0
#
#
#print comparar(5,5)


#OTRO EJERCICIO

def genera_lista(num):
	i = 1
	while i <= num:
		yield i
		i += 1

for i in genera_lista(100):
	print i