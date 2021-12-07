import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('/home/esther/Documents/airplane_trajectories/20-20_plain_2.csv')

t = df.loc[:,'0']
x = df.loc[:,'1']
y = df.loc[:,'2']

plt.plot(x, y, '--ro', label='Airplane Path')
plt.legend()
plt.show()