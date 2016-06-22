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

def suma(num1, num2):

	resultado = num1 + num2 

	print 'El resultado es: ' + str(resultado)


def resta(num1, num2):

	resultado = num1 - num2 

	return resultado


def multiplica(num1, num2):

	resultado = num1 * num2 

	return resultado


def divide(num1, num2):

	resultado = num1 / num2 

	return resultado



n1 = float(raw_input("Dame un numero: "))
n2 = float(raw_input("Dame otro numero: "))

suma(n1, n2)
print resta(n1, n2)
print multiplica(n1, n2)
print divide(n1, n2)