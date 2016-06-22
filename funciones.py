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

def saluda(nom, edad):
	print 'Hola ' + nom
	print 'es bueno saludar'
	print 'resulta elegante'

	if edad >= 42:
		print 'Eres un viejuno'

nombre = raw_input('Dime tu nombre: ')
anhos = raw_input('...y tu edad: ')

saluda(str(nombre), int(anhos))


# Otro ejemplo

def dame_pi():
	return 3.141592



numero = dame_pi()

print numero