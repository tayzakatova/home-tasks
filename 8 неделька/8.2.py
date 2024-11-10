#5 задача создаем новую матрицу с максимальными возможными квадратами 
#стек структурра данных в которую можно складывать и ытаскивать из объекты и всегда достается тот который клали последним
def calc(s):
    a = s.split()
    stack = []
    for i in a:
        if i in '+-/*':
            try:
                second = stack.pop()
                first = stack.pop()
            except IndexError:
                print('Некорректное выражение')
                return
            stack.append(str(eval(first + i + second)))
        else:
            stack.append(i)
    
    if len(stack) != 1:
        print('Некорректное выражение')
        return
    return stack[0]

print(calc(input()))
