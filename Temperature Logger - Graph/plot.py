import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("temps.txt")
df.columns = ['Seconds','Temperature']

x = df['Seconds']
y = df['Temperature']

plt.scatter(x,y)
#plt.plot(x,y)
plt.show()
