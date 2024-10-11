a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(set(a), set(b), set(a+b), set(a).intersection(b))