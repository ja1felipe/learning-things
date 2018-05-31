from tkinter import *
import sys
import os

def arruma(entrada):
	nova = ''
	entrada = entrada.replace(' ','')
	for c in range(len(entrada)):
		if c < len(entrada)-1:
			if entrada[c+1] in '+/*-' or entrada[c] in '+/*-':
				nova += entrada[c] + ' '
			else:
				nova += entrada[c]
		else:
			nova += entrada[-1]
	return nova

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def calculator():
	historico = []
	tudo = arruma(entrada.get())
	tudo1 = tudo.split(' ')
	x = float(tudo1[0])
	y = float(tudo1[2])
	operador = tudo1[1]
	if operador == '+':
		resultado = x + y
	if operador == '-':
		resultado = x - y
	if operador == '*':
		resultado = x * y
	if operador == '/':
		resultado = x / y
	historia = tudo + ' = ' + '{:.2f}'.format(resultado)
	historico.append(historia)
	lb2['text'] += historia + '\n'
	lb['text'] = tudo + ' = ' + str(resultado)
	

janela = Tk()

entrada = Entry(janela, width=15)
entrada.place(x=100,y=120)

lb = Label(janela, text='',)
lb.place(x=100,y=140)

lb2 = Label(janela, text='')
lb2.place(x=225,y=120)

bt = Button(janela, width=12, text='OK', command=calculator)
bt.place(x=100,y=160)

bt_limpa = Button(janela,width=12, text='Restart', command=restart)
bt_limpa.place(x=100,y=200)










janela.geometry('400x300+400+200')
janela.title('Calculadora')
janela.mainloop()