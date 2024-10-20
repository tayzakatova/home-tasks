from tkinter import *
from tkinter import ttk



def search():
    num_0 = color.get()
    num = num_0[1:]
       #Разделим все на xx yy zz
    raz = []
    razdel = []
    a = 0
    for i in range(1, 4):
        raz.append(num[a:2*i])
        a += 2
    for j in range(len(raz)):
        a = int(raz[j], 16)
        razdel.append(hex(255-a)[2:])
    u = '#' + razdel[0] + razdel[1] + razdel[2]
    ab.set(u)
    u.set(u)
    

root = Tk()
root.title('IMT')
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

color = StringVar()
color_entry = ttk.Entry(mainframe, width=7, textvariable=color)
color_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Button(mainframe, text="Найти идельное сочетание", command=search).grid(column=2, row=3, sticky=W)

ab = StringVar()




ttk.Label(mainframe, textvariable=ab).grid(column=2, row=5, sticky=W)
root.mainloop()