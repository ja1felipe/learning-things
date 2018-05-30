from tkinter import *

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

def calculator():
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
	lb['text'] = resultado

janela = Tk()
entrada = Entry(janela, width=15)
entrada.place(x=135,y=120)

lb = Label(janela, text='Resultado')
lb.place(x=240,y=120)

bt = Button(janela, width=12, text='OK', command=calculator)
bt.place(x=135,y=150)











janela.geometry('400x300+400+200')
janela.title('Calculadora')
janela.mainloop()