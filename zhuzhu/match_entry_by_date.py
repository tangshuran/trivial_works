# -*- coding: utf-8 -*-
import pandas as pd
import os
import glob
import math
cwd=os.getcwd()
os.chdir(cwd)
data=pd.read_excel("data.xls")
for index1,row1 in data.iterrows():
    date1=row1["Date"]
    row1["Date"]=date1.date()
    for file in glob.glob(u"S*.xls"):
        temp=pd.read_excel(file)
        for index2,row2 in temp.iterrows():
            date2=row2[u"日期"]
            if date1.date()==date2.date():
                row1["SHIBOR"]=row2[u"1M"]
                data.ix[index1]=row1
    if math.isnan(row1["SHIBOR"]):
        print date1.date()
writer = pd.ExcelWriter('new_data.xls')
data.to_excel(writer, sheet_name='Sheet1')
writer.save()

