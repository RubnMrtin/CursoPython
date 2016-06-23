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


from Tkinter import *

app = Tk()

app.title('Aplicación gráfica en Python')

Etiqueta = Label(app,text='Hola ventana\n')

boton = Button(app, text='OK')

Etiqueta.pack()
boton.pack()
app.mainloop()