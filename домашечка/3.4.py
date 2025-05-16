def prefix(pref):
    n = len(pref)
    s = ['a'] * n
    for i in range(1, n):
        if pref[i] > 0:
            s[i] = s[pref[i] - 1]
        else:
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c != s[pref[i - 1]]:
                    s[i] = c
                    break
    return ''.join(s)

pr = [0, 0, 1, 2, 3, 4, 0, 1]
res = prefix(pr)
print(res)
