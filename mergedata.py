# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 11:57:14 2020

@author: bogdan
"""

import pandas as pd



# goods in stock at 1 store
df = pd.read_csv('elomsk/elomsknal.csv')

# goods in stock at 2 store
df2 = pd.read_csv('elomsk/sknal.csv')



# goods in stock at 1 and 2 stores together
df4 = pd.merge(df, df2, on='product', how='inner')
df4.to_excel('elomsk/restdm.xlsx')
df4 = df4.fillna(0)

# get goods that are more in the first store
el = df4.query('count_x > count_y')
# get goods that are more in the second store
sk = df4.query('count_y > count_x')
print('el =',len(el))
print('sk =',len(sk))
print(el)

# write result to Excel 
el.to_excel('elomsk/elbig.xlsx')
sk.to_excel('elomsk/skbig.xlsx')
          
