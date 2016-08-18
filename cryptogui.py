from tkinter import *
from tkinter.messagebox import showinfo


def binary(text):
    #text = input('Enter message to encode: ')
    alpha = ' abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    cipher = ''
    binumd = {}
    for x in range(32):
        binumd[x] = ''
        y = x
        for n in range(4,-1,-1):
            if y >= 2**n:
                binumd[x] = binumd[x] + '1'
                y -= 2**n
            else:
                binumd[x] = binumd[x] + '0'

    for symb in text:
        indx = alpha.find(symb)
        bin = binumd[indx]
        cipher = cipher + bin + ' '
    #print(cipher)
    showinfo(title='Encrypted Code', message=cipher)

top = Tk()
top.title('Binary Encoder')
Label(top, text='Enter message:', bg='gray60', fg='black', font=('arial', 16,)).pack(side=TOP, expand=YES, fill=BOTH)
top.geometry('300x100')
ent = Entry(top, bg='gray90', fg='black')
ent.pack(side=TOP)
btn = Button(top, text='Encrypt', command=(lambda: binary(ent.get())))
btn.pack()

top.mainloop()