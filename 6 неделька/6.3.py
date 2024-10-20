from tkinter import *
from tkinter import ttk
import pandas as pd
import random



films = pd.read_csv(r'C:\Users\taisi\Desktop\study\inf\6 неделька\top_250.csv')
film_genres_list = list(films['Genre'])
name_film=list(films['Title'])
Sport=[]
War=[]
Family=[]
Comedy=[]
Adventure=[]
Musical=[]
History=[]
Action=[]
Animation=[]
Fantasy=[]
Music=[]
Crime=[]
Drama=[]
Romance=[]
Mystery=[]
Western=[]
Horror=[]
Thriller=[]
Biography=[]
for i in range(len(film_genres_list)):
    x=film_genres_list[i]
    k=x.count('|')
    if k>0:
        for y in range (k):
            index=x.find('|')
            p=x[:index]
            if p=='Sport ':
                Sport.append(name_film[i])
                x=x.replace("Sport | ", "")
            elif p=='War ':
                War.append(name_film[i]) 
                x=x.replace("War | ", "")
            elif p=='Family ':
                Family.append(name_film[i])
                x=x.replace("Family | ", "",)
            elif p=='Comedy ':
                Comedy.append(name_film[i])
                x=x.replace("Comedy | ","") 
            elif p=='Adventure ':
                Adventure.append(name_film[i])
                x=x.replace("Adventure | ", "") 
            elif p=='Musical ':
                Musical.append(name_film[i])
                x=x.replace("Musical | ", "")
            elif p=='History ':
                History.append(name_film[i])
                x=x.replace("History | ", "") 
            elif p=='Action ':
                Action.append(name_film[i])
                x=x.replace("Action | ", "") 
            elif p=='Animation ':
                Animation.append(name_film[i])
                x=x.replace("Animation | ", "") 
            elif p=='Fantasy ':
                Fantasy.append(name_film[i])
                x=x.replace("Fantasy | ", "")
            elif p=='Music ':
                Music.append(name_film[i])
                x=x.replace("Music | ", "")
            elif p=='Crime ':
                Crime.append(name_film[i]) 
                x.replace("Crime | ", "") 
            elif p=='Drama ':
                Drama.append(name_film[i])
                x=x.replace("Drama | ", "")
            elif p=='Romance ':
                Romance.append(name_film[i]) 
                x=x.replace("Romance | ", "")
            elif p=='Mystery ':
                Mystery.append(name_film[i])
                x=x.replace("Mystery | ", "")
            elif p=='Western ':
                Western.append(name_film[i])
                x=x.replace("Western | ", "")
            elif p=='Horror ':
                Horror.append(name_film[i])
                x=x.replace("Horror | ","")
            elif p=='Thriller ':
                Thriller.append(name_film[i]) 
                x=x.replace("Thriller | ", "") 
            elif p=='Biography ':
                Biography.append(name_film[i])   
                x=x.replace("Biography | ", "")   
            k2=x.count('|')    
            if k2+1-y==1:
                if x=='Sport':
                    Sport.append(name_film[i]) 
                elif x=='War':
                    War.append(name_film[i])  
                elif x=='Family':
                    Family.append(name_film[i])
                elif x=='Comedy':
                    Comedy.append(name_film[i]) 
                elif x=='Adventure':
                    Adventure.append(name_film[i]) 
                elif x=='Musical':
                    Musical.append(name_film[i]) 
                elif x=='History':
                    History.append(name_film[i])
                elif x=='Action':
                    Action.append(name_film[i])
                elif x=='Animation':
                    Animation.append(name_film[i])
                elif x=='Fantasy':
                    Fantasy.append(name_film[i])
                elif x=='Music':
                    Music.append(name_film[i])
                elif x=='Crime':
                    Crime.append(name_film[i]) 
                elif x=='Drama':
                    Drama.append(name_film[i]) 
                elif x=='Romance':
                    Romance.append(name_film[i]) 
                elif x=='Mystery':
                    Mystery.append(name_film[i]) 
                elif x=='Western':
                    Western.append(name_film[i])
                elif x=='Horror':
                    Horror.append(name_film[i]) 
                elif x=='Thriller':
                    Thriller.append(name_film[i]) 
                elif x=='Biography':
                    Biography.append(name_film[i])   
    else:
        if x=='Sport':
            Sport.append(name_film[i]) 
        elif x=='War':
            War.append(name_film[i])  
        elif x=='Family':
            Family.append(name_film[i])
        elif x=='Comedy':
             Comedy.append(name_film[i]) 
        elif x=='Adventure':
            Adventure.append(name_film[i]) 
        elif x=='Musical':
            Musical.append(name_film[i]) 
        elif x=='History':
            History.append(name_film[i])
        elif x=='Action':
            Action.append(name_film[i])
        elif x=='Animation':
            Animation.append(name_film[i])
        elif x=='Fantasy':
            Fantasy.append(name_film[i])
        elif x=='Music':
            Music.append(name_film[i])
        elif x=='Crime':
            Crime.append(name_film[i]) 
        elif x=='Drama':
            Drama.append(name_film[i]) 
        elif x=='Romance':
            Romance.append(name_film[i]) 
        elif x=='Mystery':
            Mystery.append(name_film[i]) 
        elif x=='Western':
            Western.append(name_film[i])
        elif x=='Horror':
            Horror.append(name_film[i]) 
        elif x=='Thriller':
            Thriller.append(name_film[i]) 
        elif x=='Biography':
            Biography.append(name_film[i]) 
print(Music)            
def film(*args):
        t = str(feet.get())
        if t=='Sport':
            v=random.randint(0, len(Sport)-1)
            meters.set(Sport[v])
        elif t=='War':
            v=random.randint(0, len(War)-1)
            meters.set(War[v])  
        elif t=='Family':
            v=random.randint(0, len(Family)-1)
            meters.set(Family[v])
        elif t=='Comedy':
            v=random.randint(0, len(Comedy)-1)
            meters.set(Comedy[v])
        elif t=='Adventure':
            v=random.randint(0, len(Adventure)-1)
            meters.set(Adventure[v]) 
        elif t=='Musical':
            v=random.randint(0, len(Musical)-1)
            meters.set(Musical[v])
        elif t=='History':
            v=random.randint(0, len(History)-1)
            meters.set(History[v])
        elif t=='Action':
            v=random.randint(0, len(Action)-1)
            meters.set(Action[v])
        elif t=='Animation':
            v=random.randint(0, len(Animation)-1)
            meters.set(Animation[v])
        elif t=='Fantasy':
            v=random.randint(0, len(Fantasy)-1)
            meters.set(Fantasy[v])
        elif t=='Music':
            v=random.randint(0, len(Music)-1)
            meters.set(Music[v])
        elif t=='Crime':
            v=random.randint(0, len(Crime)-1)
            meters.set(Crime[v]) 
        elif t=='Drama':
            v=random.randint(0, len(Drama)-1)
            meters.set(Drama[v])
        elif t=='Romance':
            v=random.randint(0, len(Romance)-1)
            meters.set(Romance[v])
        elif t=='Mystery':
            v=random.randint(0, len(Mystery)-1)
            meters.set(Mystery[v]) 
        elif t=='Western':
            v=random.randint(0, len(Western)-1)
            meters.set(Western[v])
        elif t=='Horror':
            v=random.randint(0, len(Horror)-1)
            meters.set(Horror[v])
        elif t=='Thriller':
            v=random.randint(0, len(Thriller)-1)
            meters.set(Thriller[v]) 
        elif t=='Biography':
            v=random.randint(0, len(Biography)-1)
            meters.set(Biography[v])
root = Tk()
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1)
meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2)
ttk.Button(mainframe, text="Film", command=film).grid(column=3, row=2) 
root.mainloop()