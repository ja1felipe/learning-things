from tkinter import *

def calculator():
	tudo = entrada.get()
	x = float(tudo[0])
	y = float(tudo[2])
	operador = tudo[1]
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