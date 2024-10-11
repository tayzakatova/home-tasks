import matplotlib.pyplot as plt 
import pandas as pd 
import scipy as sp
from scipy.optimize import fsolve
import numpy as np
from statistics import mean

def MNK(x_axis,y_axis):
    def Cov(x_axis, y_axis):
        xy = mean(x_axis * y_axis)
        return xy - mean(x_axis) * mean(y_axis)
    k = Cov(x_axis, y_axis) / Cov(x_axis, x_axis)
    b = mean(y_axis) - k * mean(x_axis)
    return k, b


file = pd.read_excel('20_1.xlsx') 
x_axis = file['I']
y_axis = file['U']
k, b = MNK(x_axis, y_axis) 
fig,ax = plt.subplots()
plt.xlim([0, 150])
plt.ylim([0, 200])
ax.scatter(x_axis, y_axis, s=5)
X=[]
for i in range(500):
    X.append(i)
Y=[]
for i in range(500):
    Y.append(i * k + b) 
ax.plot(X,Y)
plt.errorbar(x_axis, y_axis, xerr=0.01, yerr=2.5, fmt='none',ecolor='red')
plt.xlabel("I, мА", loc='right')
plt.ylabel("V, мВ", loc='top', rotation=0)
plt.grid(which='major')
plt.grid(which='minor', linestyle=':')
plt.tight_layout()

plt.minorticks_on()


file = pd.read_excel('30_1.xlsx') 
x_axis = file['I']
y_axis = file['U']
k, b = MNK(x_axis, y_axis) 
plt.xlim([0, 150])
plt.ylim([0, 200])
ax.scatter(x_axis, y_axis, s=5)
X=[]
for i in range(500):
    X.append(i)
Y=[]
for i in range(500):
    Y.append(i * k + b) 
ax.plot(X,Y)
plt.errorbar(x_axis, y_axis, xerr=0.01, yerr=2.5, fmt='none',ecolor='red')
plt.xlabel("I, мА", loc='right')
plt.ylabel("V, мВ", loc='top', rotation=0)
plt.grid(which='major')
plt.grid(which='minor', linestyle=':')
plt.tight_layout()

plt.minorticks_on()


file = pd.read_excel('50_1.xlsx') 
x_axis = file['I']
y_axis = file['U']
k, b = MNK(x_axis, y_axis) 
plt.xlim([0, 150])
plt.ylim([0, 200])
ax.scatter(x_axis, y_axis, s=5)
X=[]
for i in range(220):
    X.append(i)
Y=[]
for i in range(220):
    Y.append(i * k + b) 
ax.plot(X,Y)
plt.errorbar(x_axis, y_axis, xerr=0.01, yerr=2.5, fmt='none',ecolor='red')
plt.xlabel("I, мА", loc='right')
plt.ylabel("V, мВ", loc='top', rotation=0)
plt.grid(which='major')
plt.grid(which='minor', linestyle=':')
plt.tight_layout()
plt.minorticks_on()
plt.show()