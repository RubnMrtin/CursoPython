#!/usr/bin/python
# -*- coding: 850 -*-
# -*- encoding: UTF-8 -*-

#
# 21 junio 2016
# Archivo correspondiente al 2º día del curso: "Programando en Python: curso completo"
# del 20 al 24 de junio de 2016 en la Facultad de Ciencias - UGR
# http://www.darwineventur.com/2016/05/programando-en-python-curso-completo.html
#

#
# Rubén Martín Moreno
#

# Hacemos una variable
var = 11

# Aquí está la declaración de un 'if'. ¡La indentación es importante en Python!
# imprime "var es menor que 10"

if var > 10:
	print "var es completamente más grande que 10"
elif var > 7:
	print "var mayor que 7"
else:
	print "var es un valor distinto (7:10)"


# range(n) retorna una lista de números desde cero hasta el número dado

for animal in ['dog', 'cat', 'mouse']:
	# Puedes usar % para interpolar strings(srt) formateados
	print '%s is a mammal' % animal

print '\n\n\n\n\n\n\n'

# Otro ejemplo

lista = ['calcetin', 'pantalon', 'camisa', 'camiseta', 'otro calcetin', 'gorra']
i = 1

for prenda in lista:
	print str(i) + ' ' + prenda
	i += 1

print '\n\n\n\n\n\n\n'

# Otro ejemplo

saludo = "Hola mundo"

i = 1

for letra in saludo[:]:
	print letra * i
	i += 1

print '\n\n'

for letra in saludo[1:5]:
	print letra

print '\n\n\n\n\n\n\n'

# Otro ejemplo

datos = {'Nombre' : 'Jose', 'Apellido' : 'Gonzalez', 'Altura' : '1,80'}

for concepto in datos:
	print concepto + ': ' + datos[concepto]

print '\n\n\n\n\n\n\n'

# Otro ejemplo

a = 0

while a < 10 :
	a += 1
	if a == 3:
		break
	print a
else:
	print 'Número muy grande'