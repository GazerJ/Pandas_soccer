# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 15:32:49 2021

@author: 姜高晓
"""

import pandas as pd

n=15
soc=pd.read_excel('./zy'+str(n//1)+'.xlsx')
dataSheet=pd.read_excel('./计算物理作业out.xlsx')

for i in soc['姓名']:
    dataSheet.loc[dataSheet['姓名']==i,n]=soc.loc[soc['姓名']==i,"成绩"].values
    if len(dataSheet.loc[dataSheet['姓名']==i,n])==0:
        print(i)
dataSheet.to_excel('./计算物理作业out.xlsx',na_rep='',header=True,index=True, index_label=None,encoding='utf-8')
