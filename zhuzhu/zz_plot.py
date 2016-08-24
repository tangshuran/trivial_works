import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data=pd.read_excel("data_SHA.xls")
fig,ax=plt.subplots()
ax.plot(data["Date"],data["HCHFI"],label="HCHFI")
ax.plot(data["Date"],data["SHA"]/2.67547,label="SSE Composite Index")
ax.plot(data["Date"],data["Hushen300 Index"]/3.20393,label="Hushen300 Index")
plt.xlabel("Time/year")
plt.ylabel("Index Point")
plt.title("Comparison of HCHFI,HS300 and SSE Composite Index")
plt.legend(loc='upper right')
plt.ylim(0,7000)
plt.show()