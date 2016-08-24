# -*- coding: utf-8 -*-
import pandas as pd
import os
import glob
import math
import numpy as np
data=pd.read_excel("new_new_data.xls")
SHA=[]
for index1,row1 in data.iterrows():
    date1=row1["Date"]
    file="SHA data.xls"
    temp=pd.read_excel(file)
    for index2,row2 in temp.iterrows():
        date2=row2["date"]
        if date1.date()==date2.date():
            SHA.append(row2["SHA"])
    if len(SHA) !=index1+1:
        SHA.append(np.nan)
        print date1
data['SHA'] = pd.Series(SHA, index=data.index)
writer = pd.ExcelWriter('data_SHA.xls')
data.to_excel(writer, sheet_name='Sheet1')
writer.save()