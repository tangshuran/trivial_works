import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import defaultdict
data=pd.read_excel("data_SHA.xls")
fig,ax=plt.subplots()
year_list=range(2007,2016)
yield_ratio_HCHFI_list=[]
yield_ratio_HS300_list=[]
yield_ratio_SHA_list=[]
for i in range(data.shape[0]-1):
    yield_ratio_HCHFI=(data.ix[i+1]["HCHFI"]-data.ix[i]["HCHFI"])/data.ix[i]["HCHFI"]
    yield_ratio_HS300=(data.ix[i+1]["Hushen300 Index"]-data.ix[i]["Hushen300 Index"])/data.ix[i]["Hushen300 Index"]
    yield_ratio_SHA=(data.ix[i+1]["SHA"]-data.ix[i]["SHA"])/data.ix[i]["SHA"]
    yield_ratio_HCHFI_list.append(yield_ratio_HCHFI)
    yield_ratio_HS300_list.append(yield_ratio_HS300)
    yield_ratio_SHA_list.append(yield_ratio_SHA)
yield_ratio_HCHFI_list.append(np.nan)
yield_ratio_HS300_list.append(np.nan)
yield_ratio_SHA_list.append(np.nan)
data['yield_ratio_HCHFI'] = pd.Series(yield_ratio_HCHFI_list, index=data.index)
data['yield_ratio_HS300'] = pd.Series(yield_ratio_HS300_list, index=data.index)
data['yield_ratio_SHA'] = pd.Series(yield_ratio_SHA_list, index=data.index)
new_data=data.drop(len(data)-1)
result=pd.DataFrame()
result["year"]=year_list
yield_ratio_HCHFI_dct= defaultdict(list)
yield_ratio_SHA_dct= defaultdict(list)
yield_ratio_HS300_dct= defaultdict(list)
for index,row in new_data.iterrows():
    year=str(row["Date"].year)
    yield_ratio_HCHFI_dct[year].append(row["yield_ratio_HCHFI"])
    yield_ratio_SHA_dct[year].append(row["yield_ratio_SHA"])
    yield_ratio_HS300_dct[year].append(row["yield_ratio_HS300"])
for i in yield_ratio_HCHFI_dct:
    result.loc[result["year"]==int(i),"yield_ratio_HCHFI"]=sum(yield_ratio_HCHFI_dct[i])
for i in yield_ratio_HCHFI_dct:
    result.loc[result["year"]==int(i),"yield_ratio_SHA"]=sum(yield_ratio_SHA_dct[i])
for i in yield_ratio_HCHFI_dct:
    result.loc[result["year"]==int(i),"yield_ratio_HS300"]=sum(yield_ratio_HS300_dct[i])
writer = pd.ExcelWriter('yield_ratio.xls')
result.to_excel(writer, sheet_name='Sheet1')
writer.save()