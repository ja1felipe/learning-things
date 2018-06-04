#Used libraries
from tkinter import *
from functions import *

#Main window settings:
window = Tk()
Calculator(window)
window.title('Calculator')
window.geometry('207x305+200+200')
window['bg'] = 'gray70'
window.resizable(0,0)
window.wm_iconbitmap('icon.ico')

#Run the program
window.mainloop()
