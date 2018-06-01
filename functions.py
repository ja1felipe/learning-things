#Used libraries
from tkinter import *

#Class
class Calculator():
	def __init__(self, window):
		#Frame where is the history
		self.frame_hist = Frame(window)

		#Frase where is the main box
		self.frame_box = Frame(window)

		#Frame where is the buttons
		self.frame_btt = Frame(window)

		#Frame operators
		self.frame_op = Frame(self.frame_btt)

		#History
		self.history = Text(self.frame_hist)
		self.history.pack

		#Main text box
		self.box = Entry(self.frame_box,width=34)
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

			bt = Button(subframe, text=buttons[c], width=6,height=2)
			bt.pack(side = LEFT)

		self.bt_clr = Button(subframe, text='CE',width=6, height=2, bg='gray')
		self.bt_clr.pack(side=LEFT)

		self.bt_equal = Button(subframe, text='=',width=6, height=2, bg='gray')
		self.bt_equal.pack(side=LEFT)

		buttons1 = ('+','-','*','/')
		for c in buttons1:
			bt = Button(self.frame_op, text=c, width=6,height=2,bg='green')
			bt.pack()
		

	def equal(self):
		self.box.insert(0, 'teste')
