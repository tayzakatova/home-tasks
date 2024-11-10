oper = {'+': 1, '-': 1, '*': 2, '/': 2}

def calc(a):
    stack = [] 
    b = []
    number = ""
    for s in a:
        if s.isdigit(): 
            number += s
        else:
            if number:  
                b.append(number)
                number = "" 
            
            if s in oper: 
                while (stack and stack[-1] in oper and
                       oper[s] <= oper[stack[-1]]):
                    b.append(stack.pop())
                stack.append(s)
            elif s == '(': 
                stack.append(s)
            elif s == ')': 
                while stack and stack[-1] != '(':
                    b.append(stack.pop())
                stack.pop()

    if number: 
        b.append(number)
    while stack:
        b.append(stack.pop())

    return b


a = input()

print("инфиксная запись:", a)
print("обратная польская запись:", " ".join(calc(a)))
