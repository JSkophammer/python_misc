from tkinter import *
import os
import webbrowser
import json

#shortcuts = {}
shortcuts = json.load(open('shortcuts.json'))

def launch(event):
    command = ent.get()
    if command in shortcuts.keys():
        command = shortcuts[command]
    if command[:3] == 'www':
        webbrowser.open('http://' + command)
    elif command[0] == '-':
        key = command.split()[0][1:]
        value = ' '.join(command.split()[1:])
        if ' ' in value:
            value = "'" + value + "'"
        shortcuts[key] = value
        json.dump(shortcuts, open('shortcuts.json', 'w'))
    else:
        if command == 'py':
            os.system('open /users/jason/python/python.command')
        else:
            os.system('open /applications/' + command + '.app')
    ent.delete(0, 'end')


root = Tk()
root.title('App Launch', )


w = 250 # width for the Tk root
h = 30 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = ((hs/2) - (h/2)) + 50

# set the dimensions of the screen
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

ent = Entry(root, takefocus=True, bg='gray90', fg='black', width=30)
ent.focus_force()
ent.pack(side=TOP)

ent.bind('<Return>', launch)

root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',False)

root.mainloop()



