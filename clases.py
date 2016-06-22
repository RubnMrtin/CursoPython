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

# Ejemplo de clases

class Producto:
	def __init__(self, producto, precio, unidades):
		self.producto = producto
		self.precio = precio
		self.unidades = unidades

	def costo_total(self):
		costo = self.precio * self.unidades
		return costo

	def nuevo_precio(self, precio):
		self.precio = precio

	def agrega(self, cantidad):
		self.unidades += cantidad

	def saca(self, cantidad):
		if cantidad <= self.unidades:
			self.unidades -= cantidad
		else:
			self.unidades = 0
			print 'No hay suficientes'

	def vender(self,uds):
		if uds > self.unidades:
			print 'Se han podido vender solo ' + str(self.unidades) + ' unidades'
			print 'No se han podido vender ' + str(uds - self.unidades) + ' unidades'
			self.precio += (10*self.unidades)
			self.unidades -= self.unidades
		else:
			self.unidades -= uds
			self.precio += (10*uds)

	def informe(self):
		print 'Producto: ' + self.producto
		print 'Precio: ' + str(self.precio)
		print 'Unidades: ' + str(self.unidades)
		print 'Total: ' + str(self.costo_total())

objetos = [Producto('corbata', 35, 67), Producto('cinturon', 35, 28), Producto('camisa', 55, 15), Producto('pantalon', 50, 15)]

objetos[0].informe()