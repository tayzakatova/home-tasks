from random import randrange as rnd, choice
from tkinter import *
import math
 
import time
root = Tk()
fr = Frame(root)
root.geometry('800x600')
canv = Canvas(root, bg = 'white')
canv.pack(fill=BOTH,expand=1)


class Ball():
    """ Класс Ball описывает мяч. """

    def __init__(self,x=40,y=450):
        """ Конструктор класса Ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue','green','red','brown'])
        self.id = canv.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill=self.color)
        self.live = 30

        
    def set_coords(self):
        '''
        Перерисовывает шарик с актуальными координатами
        '''
        canv.coords(self.id, self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r)

    def move(self):
        """ 
        Метод move описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения 
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
            и стен по краям окна (размер окна 800х600).
        """
        # TODO
        self.vy -= 1
        self.x += self.vx
        self.y -= self.vy
        self.set_coords()
        if self.x > 800:
            self.x = 800
            self.vx = -self.vx*0.5
        if self.y > 550:
            self.y = 550
            self.vy = -self.vy*0.5
        if self.x < 0:
            self.x = 0
            self.vx = -self.vx*0.5
        if self.y < 0:
            self.y = 0
            self.vy = -self.vy*0.5
        if self.y == 550 and abs(self.vy) < 1:
            self.live -= 15
            self.vy = 0
            self.vx = 0
        self.set_coords()
        
    def hittest(self,ob):
        """ Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте ob.

        Args:
            ob: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.r+ob.r) >= (abs(self.x - ob.x)**2 + abs(self.y - ob.y)**2)**0.5:
            return True
        #TODO
        return False

class gun():
    """ Класс gun описывает пушку. """
    def __init__(self,x=40,y=450):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20,450,50,420,width=7) # FIXME: don't know how to set it...
         
    def fire2_start(self,event):
        self.f2_on = 1
 
    def fire2_end(self,event):
        """ Выстрел мячом происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y)/(event.x-new_ball.x))
        new_ball.vx = self.f2_power*math.cos(self.an)
        new_ball.vy = -self.f2_power*math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10
 
 
    def targetting (self,event=0):
        """ Прицеливание. Зависит от положения мыши.
        """
        if event:
            self.an = math.atan((event.y-450)/(event.x-20))    
        if self.f2_on:
            canv.itemconfig(self.id,fill = 'orange')
        else:
            canv.itemconfig(self.id,fill = 'black')
        canv.coords(self.id, 20, 450, 20 + max(self.f2_power, 20) * math.cos(self.an), 450 + max(self.f2_power, 20) * math.sin(self.an))
         

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id,fill = 'orange')
        else:
            canv.itemconfig(self.id,fill = 'black')
        
class target():
    """ Класс target описывает цель. """ 
    def __init__(self,x=40,y=450):
        self.points = 0
        self.live = 1
        #TODO: don't work!!! How to call this functions when object is created?
        self.id = canv.create_oval(0,0,0,0)
        self.id_points = canv.create_text(30,30,text = self.points,font = '28')
        
         
    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600,780)
        y = self.y = rnd(300,550)
        r = self.r = rnd(2,50)
        color = self.color = 'red'
        canv.coords(self.id, x-r,y-r,x+r,y+r)
        canv.itemconfig(self.id, fill = color)
         
    def hit(self,points = 1):
        """ Попадание шарика в цель. """
        canv.coords(self.id,-10,-10,-10,-10)
        self.points += points
        canv.itemconfig(self.id_points, text = self.points)
        #self.new_target()

t1 = target()
screen1 = canv.create_text(400,300, text = '',font = '28')
g1 = gun()
bullet = 0
balls = []


def new_game(event=''):
    global gun, t1, screen1, balls, bullet
    t1.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
 
    z = 0.03
    t1.live = 1
    while t1.live or balls:
        if not t1.live:
            canv.unbind('<Button-1>')
            canv.unbind('<ButtonRelease-1>')
        for b in balls:
            b.move()
            if not b.live:
                canv.delete(b.id) 
                balls.remove(b)
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                
                canv.bind('<Button-1>', g1.fire2_start)
                canv.bind('<ButtonRelease-1>', g1.fire2_end)
                
                canv.itemconfig(screen1, text = 'Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                
                canv.delete(t1)
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    
    canv.itemconfig(screen1, text = '')
    canv.delete(gun)
    root.after(1,new_game)

new_game()  
 
root.mainloop()