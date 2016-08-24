import pandas as pd
import numpy as np
from collections import defaultdict
import scipy.stats
import matplotlib.pyplot as plt
data=pd.read_excel("new_new_data2.xls")
new_data=data.drop(len(data)-1)
x=new_data["x"]
y=new_data["y"]
slope, intercept, r, prob2, see = scipy.stats.linregress(x, y)
y_hat=x*slope+intercept
SSE=np.sum((y-y_hat)**2)
MSE=SSE/(len(y)-2)
SEPE_intercept=np.sqrt(MSE)*np.sqrt(1/len(y)+(np.mean(x)**2)/np.sum((x-np.mean(x))**2))
T=intercept/SEPE_intercept
fig1, ax1 = plt.subplots()
ax1.scatter(x, y)
ax1.plot(x, x*slope+intercept, c='r')
plt.show()