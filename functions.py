#Used libraries
from tkinter import *
from functools import partial

#Class
class Calculator():
	def __init__(self, window):
		#font
		self.font = ('Verdana', 10)
		self.font2 = ('Verdana', 13)


		#Frame where is the history
		self.frame_hist = Frame(window)

		#Frase where is the main box
		self.frame_box = Frame(window, pady = 2, padx = 1)

		#Frame where is the buttons
		self.frame_btt = Frame(window,padx = 2,pady = 2)

		#Frame operators
		self.frame_op = Frame(self.frame_btt)

		#History
		self.history = Text(self.frame_hist)
		self.history.pack

		#Main text box
		self.box = Entry(self.frame_box, font=self.font2,width=18)
		self.box.pack()

		#Pack order
		self.frame_hist.pack()
		self.frame_box.pack()
		self.frame_btt.pack()
		self.frame_op.pack(side = RIGHT)

		#Buttons
		buttons = ('0','1','2','3','4','5','6','7','8','9')
		for c in range(len(buttons)):
			if c % 3 == 0:
				subframe = Frame(self.frame_btt)
				subframe.pack()

			bt = Button(subframe, text=buttons[c], width=5,height=2, font = self.font, bg='gray83', command = partial(self.PutButtons, buttons[c]))
			bt.pack(side = LEFT)

		self.bt_clr = Button(subframe, text='CE', width=5, height=2, bg='snow', font = self.font, command = self.clear)
		self.bt_clr.pack(side=LEFT)

		self.bt_equal = Button(subframe, text='=', width=5, height=2, bg='snow', font = self.font, command = self.equal)
		self.bt_equal.pack(side=LEFT)

		buttons1 = ('+','-','*','/')
		for c in buttons1:
			bt = Button(self.frame_op, text=c, width=5, height=2, bg='snow', font = self.font, command =partial(self.PutButtons, c))
			bt.pack()
		
	def PutButtons(self, button):
		self.box.insert(END, button)


	def equal(self):
		aux = self.box.get()
		self.box.delete(0, END)
		self.box.insert(END, eval(aux))

	def clear(self):
		self.box.delete(0, END)