# import tkinter module 
from tkinter import *
# creating root object 
root = Tk() 
# defining size of window 
root.geometry("1200x6000") 
# setting up the title of window 
root.title("Message Encryption and Decryption") 
Tops = Frame(root, width = 1600, relief = SUNKEN) 
Tops.pack(side = TOP) 
f1 = Frame(root, width = 800, height = 700, 
                            relief = SUNKEN)
f1.pack(side = LEFT)
lblInfo = Label(Tops, font = ('helvetica', 50, 'bold'), 
          text = "FILE COMPRESSION", 
                     fg = "Black", bd = 10, anchor='w') 
                       
lblInfo.grid(row = 0, column = 0) 
# exit function 
def qExit(): 
    root.destroy()
def compress():
     import compressgu
def decompress():
    import decompressgu 
def encrypt():
    import encryptgu
def decrypt():
    import decryptgu
  

  
  
# Show message button 
btnTotal = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black", 
                        font = ('arial', 16, 'bold'), width = 10, 
                       text = "COMPRESS", bg = "indian red", 
                         command = compress).grid(row = 7, column = 1) 
btnTotal = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black", 
                        font = ('arial', 16, 'bold'), width = 10, 
                       text = "DECOMPRESS", bg = "brown4", 
                         command = decompress).grid(row = 7, column = 2) 
btnTotal = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black", 
                        font = ('arial', 16, 'bold'), width = 10, 
                       text = "ENCRYPT", bg = "brown4", 
                         command = encrypt).grid(row = 8, column = 1) 
  
# Reset button 
btnReset = Button(f1, padx = 16, pady = 8, bd = 16, 
                  fg = "black", font = ('arial', 16, 'bold'), 
                    width = 10, text = "DECRYPT", bg = "indian red", 
                   command = decrypt).grid(row = 8, column = 2) 
  
# Exit button 
exit = Button(root,bd = 16,  
                 fg = "black", font = ('arial', 16, 'bold'),width=10,
                      text = "Exit", bg = "brown4", 
                  command = qExit) 
exit.place(relx=1.0, rely=1.0, anchor=SE)
# keeps window alive 
root.mainloop() 

