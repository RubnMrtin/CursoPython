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

# Ejemplo de clases heredadas

class Animal:
	'''Clases base para heredar'''

	def __init__(self, nombre, patas):
		self.nombre = nombre
		self.patas = patas

	def saluda(self):
		print 'El animal llamado ' + str(self.nombre) + ' saluda!'


class Perro(Animal):
	'''Clase hija para mostrar la herencia'''

	def ladra(self):
		print 'Guau!'

mascota = Perro('Rufo', 4)
mascota.saluda()
mascota.ladra()