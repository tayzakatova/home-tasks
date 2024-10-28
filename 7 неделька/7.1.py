class Vector:
    def __init__(self, x, y, z):
        assert isinstance(x, (int, float)) and not isinstance(x, bool)
        assert isinstance(y, (int, float)) and not isinstance(y, bool)
        assert isinstance(z, (int, float)) and not isinstance(z, bool)
        self.x = x
        self.y = y
        self.z = z
    def __abs__(self):
        return(self.x**2 + self.y**2 + self.z**2)**0.5
    def __add__(self, other):
        assert isinstance(other, Vector)
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z,)
    def __sub__(self, other):
        assert isinstance(other, Vector)
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z,)
    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x*other.x + self.y*other.y + self.z*other.z
        if isinstance(other, (int, float)):
            return Vector(self.x*other, self.y*other, self.z*other)
        else:
            raise AssertionError    #выдаст ошибку
    def __str__(self):
        return f'x = {self.x}, y = {self.y}, z = {self.z}'

V1 = Vector(0, 1 ,0) 
V2 = Vector(1, 1 ,0) 
V3 = Vector(1, 0 ,0) 
V4 = Vector(0, 0, 0)
a = [V1, V2, V3] #использую этот список и для 1 и для 2 пункта задания
def mass_center(l):
    res = Vector(0, 0, 0)
    for i in l:
        res += i
    return res*(1/len(l))
print(mass_center(a))

s = []

def pl(k):
    for i in range(1, len(k)):
        c = k[i-1] - k[i]
        s.append(c)
    s.append(k[1] - k[len(k)-1])
    return s

def vec(self,other):
    assert isinstance(other, Vector)
    return Vector(self.y*other.z-self.z*other.y,self.x*other.z-self.z*other.x,self.y*other.x-self.x*other.y)

b = []
g = (pl(a))
for i in range(0, len(g)):
        for f in range(0, len(g)):
            c = vec(g[i], g[f])
            b.append(c)
#print(b)
p = []
for i in b:
    p.append(abs(i))
print(p)
print(max(p)/2)#это максимальная площадь

q = Vector(0, 0, 0)
v = 1/len(a)
for i in a:
    q += i
print(q*v)