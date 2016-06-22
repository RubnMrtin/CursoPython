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

#def operaciones(num1, *num2):
#	suma = num1 + num2
#	resta = num1 - num2
#	multiplicacion = num1 * num2
#
#	return suma, resta, multiplicacion


#n1 = float(raw_input("Dame un numero: "))
#n2 = float(raw_input("Dame otro numero: "))

#print operaciones(n1, n2)


def tres_cosas(num1, *num2):
	print 'El primero es: ' + str(num1)

	i = 0
	for segundo in num2:
		print 'El elemento ' + str(i+1) + 'del segundo es: ' + num2[0]
		i += 1

n1 = float(raw_input("Dame un numero: "))
n2 = float(raw_input("Dame otro numero: "))
n3 = float(raw_input("Dame otro numero: "))

print tres_cosas(n1, n2, n3)