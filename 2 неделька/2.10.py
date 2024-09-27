gl = ['у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ё']
cg = ['й', 'ц', 'к', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ф', 'в', 'ъ', 'п', 'р', 'л', 'д', 'ж', 'ч', 'с', 'м', 'т', 'ь', 'б']
f = open('свист.txt', 'r', encoding="utf-8")
a = str(f.readline())
a = list(a)
print(a)
for i in range(0, len(a) - 1):
    if a[i] in cg and a[i+1] in gl:
        a[i+1] = a[i+1] + 'c' + a[i+1]
print(*a, sep = '')