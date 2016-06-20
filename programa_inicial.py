#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# 20 junio 2016
# Primera clase del curso: "Programando en Python: curso completo"
# del 20 al 24 de junio de 2016 en la Facultad de Ciencias - UGR
# http://www.darwineventur.com/2016/05/programando-en-python-curso-completo.html
#

#
# Rubén Martín Moreno
#


mi_tupla = ('cadena de texto', 15, 2.8, 'otro dato', 25)

print mi_tupla

print mi_tupla[1]

print mi_tupla[-1]
print mi_tupla[2:4]

print '\n'

mi_tupla = 7.0,7,7L
print mi_tupla.count(int(7))

milista = [1, 2, 3, 'cuatro', '5']
print milista

milista.append(6)
print milista

milista.insert(0,0)
print milista

milista.remove(2)
print milista

print 2 in milista
print 'cuatro' in milista

print milista
del milista[3:5] 
print milista

tupla = (1, 2)
lista = [3, 4]
suma = list(tupla) + lista
print suma

#DICCIONARIO
diccionario = {'dia' : 20, 'mes' : 'junio', 'year' : 2016}
print diccionario['dia']
print diccionario

#ITERADOS
for clave, valor in diccionario.iteritems():
	print 'El valor de la clave %s es %s' % (clave, valor)