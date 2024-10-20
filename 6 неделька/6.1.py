import tkinter as tk

gui = tk.Tk()
gui.mainloop()
def press(btn, expr):
    prev_expr = expr.get()
    new_expr  = prev_expr + btn
    expr.set(new_expr)

def press_equal(expr):
    new_expr = str(eval(expr.get()))
    expr.set(new_expr)

def press_clear(expr):
    expr.set(" ")
def main():
    gui = tk.Tk()

    expression = tk.StringVar()

    expression_field = tk.Entry(gui, textvariable=expression)
    expression_field.grid(row=0, columnspan=4)

    button_0 = tk.Button(gui, text='0', command=lambda: press("0", expression))
    button_0.grid(row=5,column=0)

    button_1 = tk.Button(gui, text='1', command=lambda: press("1", expression))
    button_1.grid(row=4, column=0)
    
    button_2 = tk.Button(gui, text='2', command=lambda: press("2", expression))
    button_2.grid(row=4, column=1)
    
    button_3 = tk.Button(gui, text='3', command=lambda: press("3", expression))
    button_3.grid(row=4, column=2)
    
    button_4 = tk.Button(gui, text='4', command=lambda: press("4", expression))
    button_4.grid(row=3, column=0)
    
    button_5 = tk.Button(gui, text='5', command=lambda: press("5", expression))
    button_5.grid(row=3, column=1)
    
    button_6 = tk.Button(gui, text='6', command=lambda: press("6", expression))
    button_6.grid(row=3, column=2)
    
    button_7 = tk.Button(gui, text='7', command=lambda: press("7", expression))
    button_7.grid(row=2, column=0)
    
    button_8 = tk.Button(gui, text='8', command=lambda: press("8", expression))
    button_8.grid(row=2, column=1)
    
    button_9 = tk.Button(gui, text='9', command=lambda: press("9", expression))
    button_9.grid(row=2, column=2)

    button_plus = tk.Button(gui, text='+', command=lambda: press("+", expression))
    button_plus.grid(row=4, column=3)

    button_minus = tk.Button(gui, text='-', command=lambda: press("-", expression))
    button_minus.grid(row=3, column=3)

    button_equal = tk.Button(gui, text='=', command=lambda: press_equal(expression))
    button_equal.grid(row=5, column=3)

    button_clear = tk.Button(gui, text='AC', command=lambda: press_clear(expression))
    button_clear.grid(row=1, column=0)
    
    button_multiply = tk.Button(gui, text='*', command=lambda: press("*", expression))
    button_multiply.grid(row=2, column=3)
    
    button_remainder = tk.Button(gui, text='%', command=lambda: press("%", expression))
    button_remainder.grid(row=1, column=3)
    
    button_whole_part = tk.Button(gui, text='//', command=lambda: press("//", expression))
    button_whole_part.grid(row=1, column=2)

    gui.mainloop()
    
    return 0

main()




