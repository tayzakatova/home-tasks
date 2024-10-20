from tkinter import *
from tkinter import ttk

def film():
    a=float(feet1.get())
    b=float(feet2.get())
    c= (a/100)**2
    new=b/c
    if new<=16:
        k=new//1
        n=str(k)
        meters.set('ИМТ='+n+'-Выраженный дефицит массы тела')
    elif new>16 and new<=18.5:
        k=new//1
        n=str(k)
        meters.set('ИМТ='+n+'-Недостаточная (дефицит) масса тела')
    elif new>18.5 and new<=25:
        k=new//1
        n=str(k)
        meters.set('ИМТ='+n+'-Норма')
    elif new>25 and new<=30:
        k=new//1 
        n=str(k)
        meters.set('ИМТ='+n+'-Избыточная масса тела (предожирение)')
    elif new>30 and new<=35:
        k=new//1 
        n=str(k)
        meters.set('ИМТ'+n+ 'Ожирение 1 степени')
    elif new>35 and new<=40:
        k=new//1
        n=str(k)
        meters.set('ИМТ='+n+'Ожирение 2 степени')
    elif new>40:
        k=new//1 
        n=str(k)
        meters.set('ИМТ='+n+'-Ожирение 3 степени')
        
    
root=Tk()
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
feet1 = StringVar()
feet1_entry = ttk.Entry(mainframe, width=7, textvariable=feet1)
feet1_entry.grid(column=0, row=0)

feet2 = StringVar()
feet2_entry = ttk.Entry(mainframe, width=7, textvariable=feet2)
feet2_entry.grid(column=0, row=1)

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=1, row=3)
ttk.Button(mainframe, text="Расчет", command=film).grid(column=0, row=3) 
write=ttk.Label(mainframe, text="Напишите свой рост в сантиметрах").grid(column = 1, row=0,)
write2=ttk.Label(mainframe, text="Напишите свой вес").grid(column=1, row=1)
    
root.mainloop()   