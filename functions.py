#Used libraries
from tkinter import *
from functools import partial
from math import *

#Class
class Calculator():
	def __init__(self, window):

		#fonts
		self.font = ('Verdana', 10)
		self.font2 = ('Verdana', 11)

		#Frame where is the history
		self.frame_hist = Frame(window)

		#Frase where is the main box
		self.frame_box = Frame(window, padx = 1, pady = 1)

		#Frame where is the buttons
		self.frame_btt = Frame(window,padx = 2.5,pady = 2)

		#Frame operators
		self.frame_op = Frame(self.frame_btt)

		#Frase Diverses
		self.frame_diver = Frame(window,padx = 2.5)

		#History
		self.history = Listbox(self.frame_hist, height=3,font = self.font, width = 23, borderwidth = 1)
		self.history.pack(side = LEFT)
		self.history.selection_set(first=0, last=None)
		self.history.configure(exportselection = False, state = DISABLED)

		#Scrollbar history
		self.scroll = Scrollbar(self.frame_hist, command = self.history.yview, width = 18)
		self.history.configure(yscrollcommand=self.scroll.set)
		self.scroll.pack(side = RIGHT, fill = Y)

		#Main text box
		self.box = Entry(self.frame_box, font=self.font2, width=20)
		self.box.pack()

		#Pack order
		self.frame_hist.pack()
		self.frame_box.pack()
		self.frame_diver.pack()
		self.frame_btt.pack()
		self.frame_op.pack(side = RIGHT)

		#Buttons

			#Numbers
		buttons = ('0','1','2','3','4','5','6','7','8','9')
		for c in range(len(buttons)):
			if c % 3 == 0:
				subframe = Frame(self.frame_btt)
				subframe.pack()

			bt = Button(subframe, text=buttons[c], width=5,height=2, font = self.font, bg='sky blue', command = partial(self.PutButtons, buttons[c]))
			bt.pack(side = LEFT)

			#Diverses
		self.bt_clr = Button(subframe, text='CE', width=5, height=2, bg='gray80', font = self.font, command = self.clear)
		self.bt_clr.pack(side=LEFT)

		self.bt_equal = Button(subframe, text='=', width=5, height=2, bg='gray80', font = self.font, command = self.equal)
		self.bt_equal.pack(side=LEFT)

		diverses = ('<<','x²','√')
		for c in diverses:
			div_bt = Button(self.frame_diver, text = c, width=5, height=2, bg='steel blue', font = self.font, command= partial(self.diverses, c))
			div_bt.pack(side = LEFT)

		self.bt_sv = Button(self.frame_diver, text = 'Save', width=5, height=2, bg='steel blue', font = self.font, command = self.save)
		self.bt_sv.pack(side=LEFT)
		
			#Operators
		buttons1 = ('+','-','*','/')
		for c in buttons1:
			bt = Button(self.frame_op, text=c, width=5, height=2, bg='steel blue', font = self.font, command =partial(self.PutButtons, c))
			bt.pack()
		
	#Methods

	def PutButtons(self, button):
		a = self.box.index(INSERT)
		self.box.insert(a, button)

	def equal(self):
		self.aux = self.box.get().replace(' ','')
		aux2 = self.aux + ' = ' + str(eval(self.aux))
		self.box.delete(0, END)
		self.box.insert(END, eval(self.aux))
		self.history.configure(state = NORMAL)
		self.history.insert(END, aux2)
		self.history.configure(state = DISABLED)

	def clear(self):
		self.box.delete(0, END)
		self.history.configure(state=NORMAL)
		self.history.delete(0, END)

	def diverses(self, button):
		if button == '√':
			self.box.insert(END, ('sqrt()'))
		elif button == 'x²':
			self.box.insert(END, (' ** 2'))
		elif button == '<<':
			a = int(len(self.box.get()))
			self.box.delete(a-1)
		
	def save(self):
		self.save = str(eval(self.aux))
		self.bt_sv = Button(self.frame_diver, text = self.save, width=5, height=2, bg='steel blue', font = self.font, command = self.save)