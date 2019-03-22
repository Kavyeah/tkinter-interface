from tkinter import *
from shlex import split
import subprocess 
root = Tk() 
root.geometry("1200x6000")
root.title("Decompress your file") 
lblInfo = Label(root, font = ('helvetica', 50, 'bold'), 
          text = "DECOMPRESS YOUR FILE", 
                     fg = "Black", bd = 10, anchor='w') 
                       
lblInfo.grid(row = 0, column = 0)
filename = StringVar() 
e1 = Entry(root, font = ('arial', 16, 'bold'),textvariable = filename, bd = 10, insertwidth = 9,width=50,bg = "powder blue", justify = 'right')
e1.grid(row=50, column=0)
def decompress():
	//write your algorithm

    root.destroy()
btnExit =Button(root, padx = 20, pady = 20, bd = 16,  
                 fg = "black", font = ('arial', 16, 'bold'), 
                      width = 20, text = "DECOMPRESS", bg = "red", 
                  command = decompress).grid(row = 50, column = 29) 
  
# keeps window alive 
root.mainloop()
