import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_excel("data_SHA.xls")
data2=data.loc[:,["Date","SHA","SHIBOR","HCHFI"]]
R_Ft_list=[]
R_Mt_list=[]
for i in range(data2.shape[0]-1):
    R_Ft=(data2.ix[i+1]["HCHFI"]-data2.ix[i]["HCHFI"])/data2.ix[i]["HCHFI"]
    R_Mt=(data2.ix[i+1]["SHA"]-data2.ix[i]["SHA"])/data2.ix[i]["SHA"]
    R_Ft_list.append(R_Ft)
    R_Mt_list.append(R_Mt)
R_Ft_list.append(np.nan)
R_Mt_list.append(np.nan)
data2['R_Ft'] = pd.Series(R_Ft_list, index=data2.index)
data2['R_Mt'] = pd.Series(R_Mt_list, index=data2.index)
y_hat=data2['R_Ft']-data2["SHIBOR"]/100
x_hat=data2['R_Mt']-data2["SHIBOR"]/100
data2['X=R_Mt-r_ft'] = pd.Series(x_hat, index=data2.index)
data2['Y=R_Ft-r_ft'] = pd.Series(y_hat, index=data2.index)
new_data=data2.drop(len(data2)-1).loc[:,["Date",'R_Ft','R_Mt','X=R_Mt-r_ft','Y=R_Ft-r_ft']]
writer = pd.ExcelWriter('table.xls')
new_data.to_excel(writer, sheet_name='Sheet1')
writer.save()