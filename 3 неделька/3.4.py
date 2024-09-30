def tr(x, y, z = 1):
    if x % 2 != 0 and z == (x // 2 + 1):
        print(y * z)
        return
    if x % 2 == 0 and z == (x // 2):
        print(y * z)
        print(y * z)
        return
    print(y * z)

    tr(x, y, z = z + 1)

    print(y * z)
s = list(input().split())
x = int(s[0])
y = s[1]
tr(x, y)