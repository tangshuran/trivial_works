import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_excel("data_SHA.xls")
R_Ft_list=[]
R_Mt_list=[]
for i in range(data.shape[0]-1):
    R_Ft=(data.ix[i+1]["HCHFI"]-data.ix[i]["HCHFI"])/data.ix[i]["HCHFI"]*100
    R_Mt=(data.ix[i+1]["SHA"]-data.ix[i]["SHA"])/data.ix[i]["SHA"]*100
    R_Ft_list.append(R_Ft)
    R_Mt_list.append(R_Mt)
R_Ft_list.append(np.nan)
R_Mt_list.append(np.nan)
data['R_Ft'] = pd.Series(R_Ft_list, index=data.index)
data['R_Mt'] = pd.Series(R_Mt_list, index=data.index)
y_hat=data["R_Ft"]-data["SHIBOR"]
x_hat=data["R_Mt"]-data["SHIBOR"]
data['y'] = pd.Series(y_hat, index=data.index)
data['x'] = pd.Series(x_hat, index=data.index)
new_data=data.drop(len(data)-1)
beta,alpha=np.polyfit(list(new_data['x']),list(new_data['y']),1)
fig1, ax1 = plt.subplots()
ax1.scatter(new_data['x'], new_data['y'])
ax1.plot(new_data['x'], new_data['x']*beta+alpha, c='r')
plt.xlabel("Excess return on the SSE Composite Index")
plt.ylabel("Excess return on the Howbuy China Hedge Fund Index")
plt.title("Linear Regression based on CAPM : SSE Composite Index")
plt.show()
sharp_ratio=(np.mean(data["R_Ft"])-np.mean(data["SHIBOR"]))/np.std(data["R_Ft"])
treynor_ratio=(np.mean(data["R_Ft"])-np.mean(data["SHIBOR"]))/beta
writer = pd.ExcelWriter('new_new_data2.xls')
data.to_excel(writer, sheet_name='Sheet1')
writer.save()
print "np.std(data['R_Ft'])"
print np.std(data["R_Ft"])
print "np.mean(data['R_Ft'])"
print np.mean(data["R_Ft"])
print "np.std(data['R_Mt'])"
print np.std(data["R_Mt"])
print "np.mean(data['R_Mt'])"
print np.mean(data["R_Mt"])
print "beta,alpha"
print beta,alpha
