import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('BTC_data.csv')
print(df)
fig = plt.figure(figsize=(12,7), dpi=100)

clos = list(df['close'])
tim = list(df['time'])
for i in range(len(tim)):
    tim[i] = tim[i][0:10]
    tim[i]= tim[i][8:10] + tim[i][4:8] + tim[i][0:4]
tim_first = tim[0]
tim_last = tim[-1]
plt.plot(tim, clos, 'r')

plt.xlabel('Date', fontsize = 16)
plt.ylabel('Cost', fontsize = 16, loc = "center")

ticks_tim = [tim[i] for i in range(len(tim)) if i%50 == 0]


plt.xticks(ticks_tim, fontsize = 8)
plt.xticks(rotation=50)
plt.grid()
plt.tight_layout()
plt.show()
#cоседка очень помогла с количеством и наложением меток друг на друга