#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# 23 junio 2016
# Archivo correspondiente al 4º día del curso: "Programando en Python: curso completo"
# del 20 al 24 de junio de 2016 en la Facultad de Ciencias - UGR
# http://www.darwineventur.com/2016/05/programando-en-python-curso-completo.html
#

#
# Rubén Martín Moreno
#

# USO DEL PROGRAMA 'MODULO.PY'

#mi_cadena = 'En un lugar de la Mancha, de cuyo nombre no quiero acordarme.'
#
#mi_lista = mi_cadena.split(' ')
#
#for elemento in mi_lista:
#	print elemento


# LEER UN ARCHIVO
#fichero = open('modulo.py', 'r')

#rel1 = fichero.readline()
#rel2 = fichero.readline()

#print rel1
#print rel2

#resultado = fichero.readlines()

#for elemento in resultado:
#	print elemento

#fichero.close()

#import os

#content = os.popen('dir')
#resultado = content.read()
#print resultado

fichero_escrito = open('otro_archivo.txt', 'w')
fichero_escrito.write('0123456789 hola mundo ')

fichero_escrito.seek(6)

fichero_escrito.write('xD')

fichero_escrito.close()

# UTILIZAR ESTO PARA CREAR PLANTILLAS A TOPE
