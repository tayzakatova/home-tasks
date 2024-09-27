s = input()
alla = "AHIMOTUVWXY18EJSZ3L25"
f = list(s)
print(s)
b = 1
for i in range(0, len(f)):
    if f[i] not in alla:
        b = 0

if "E" in s:
    s = s.replace("E", "3")
if "J" in s:
    s = s.replace("J", "L")
if "S" in s:
    s = s.replace("S", "2")
if "Z" in s:
    s = s.replace("Z", "5")


if s == s[::-1] and b == 1:
    print(s, "is a mirrored palindrome.")
elif s == s[::-1]:
    print(s, "is a regular palindrome.")
elif s == s[::-1]:
    print(s, "is a mirrored string.")
else:
    print(s, "is not a palindrome.")
