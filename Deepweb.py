#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 17:30:41 2018

@author: pradeep
"""
import numpy as np
import pandas as pd
import glob



######### store wise ##########
PATH = '/Users/pradeep/Workingdirectory/Data/DNM Files/Evolution/store listings/'

df = pd.DataFrame(columns = ['storename','product','price','vendor','rating','level','date'])

df = []

a= pd.DataFrame()


for glo in glob.glob(f'{PATH}/*.*'):
#    print(glo)
    a = pd.read_csv(glo, names = ['storename','product','price','vendor','rating','level'])
    a['date']= glo[72:82]
    df.append(a)
    
df1 = pd.concat([df[i] for i in range(len(df))], ignore_index = True)


len(df1.date.unique())

df2 = df1.groupby(['storename','date']).agg({'product': np.size })
df2.reset_index(inplace = True)
df2.columns = ['storename','date','nproducts']

df3 = df2.groupby(['date']).agg({'storename':np.size})
df3.to_csv('nstores.csv')

df4 = df2.groupby(['date']).agg({'nproducts':np.mean})
df4.to_csv('avgproducts.csv')

df5 = df2.groupby(['date']).agg({'nproducts':np.sum})
df5.to_csv('totproducts.csv')

currency= pd.DataFrame(df1['price'].str.strip())['price'].str.split(" ", expand = True)
currency.columns = ['currency_type','price_value']
currency.currency_type.unique()

df1['currency_type'] = currency['currency_type']
df1['price_value'] = currency['price_value']

rating = pd.DataFrame(df1['rating'].str.strip())

rating = pd.DataFrame(rating['rating'].str.replace("(",""))
rating = pd.DataFrame(rating['rating'].str.replace(")",""))

df1['rating_new'] = rating['rating']

level = df1['level'].str.strip().str.split("(", expand = True)
level.columns = ['level','nratings']
level['nratings'] = level['nratings'].str.replace(")","")
level['level'] = level['level'].str.strip()
level['nratings'] = level['nratings'].str.strip()
level.level.unique()

df1['level_new'] = level['level']
df1['nratings'] = level['nratings']

del df1['rating']

storepanel = df1[['date','storename','product','vendor','currency_type','price_value','rating_new','level_new','nratings']]

storepanel.drop_duplicates(inplace= True)

storepanel.to_pickle('storepanel.pkl')
storepanel = pd.read_pickle('storepanel.pkl')

storepanel.to_csv('storepaneldata_31Oct.csv')
storepanel.to_excel('storepaneldata_31Oct.xlsx')

####### product wise #######

PATH = '/Users/pradeep/Workingdirectory/Data/DNM Files/Evolution/Category listings/'

ef = []
a= pd.DataFrame()

glo[75:85]

for glo in glob.glob(f'{PATH}/*.*'):
#    print(glo)
    a = pd.read_csv(glo, names = ['prod_category','product','price','vendor','rating','level'])
    a['date']= glo[75:85]
    ef.append(a)
    
ef1 = pd.concat([ef[i] for i in range(len(ef))], ignore_index = True)

ef1.date.unique()
len(ef1.date.unique())

ef1['prod_category'] = ef1['prod_category'].str.strip()

ef2 = ef1.groupby(['prod_category','date']).agg({'product': np.size })
ef2.reset_index(inplace = True)
ef2.columns = ['prod_category','date','nproducts']


ef3 = ef2.groupby(['date']).agg({'prod_category':np.size})
ef3.to_csv('nprod_category.csv')

ef4 = ef2.groupby(['date']).agg({'nproducts':np.mean})
ef4.to_csv('avgproducts_cat.csv')

ef5 = ef2.groupby(['date']).agg({'nproducts':np.sum})
ef5.to_csv('totproducts_cat.csv')

currency= pd.DataFrame(ef1['price'].str.strip())['price'].str.split(" ", expand = True)
currency.columns = ['currency_type','price_value']
currency.currency_type.unique()

ef1['currency_type'] = currency['currency_type']
ef1['price_value'] = currency['price_value']

rating = pd.DataFrame(ef1['rating'].str.strip())

rating = pd.DataFrame(rating['rating'].str.replace("(",""))
rating = pd.DataFrame(rating['rating'].str.replace(")",""))

ef1['rating_new'] = rating['rating']

level = ef1['level'].str.strip().str.split("(", expand = True)
level.columns = ['level','nratings']
level['nratings'] = level['nratings'].str.replace(")","")
level['level'] = level['level'].str.strip()
level['nratings'] = level['nratings'].str.strip()
level.level.unique()

ef1['level_new'] = level['level']
ef1['nratings'] = level['nratings']

#del df1['rating']

productcatpanel = ef1[['date','prod_category','product','vendor','currency_type','price_value','rating_new','level_new','nratings']]


productcatpanel['prod_category'] = productcatpanel.prod_category.str.strip()
productcatpanel['date']= productcatpanel.date.str.strip()
productcatpanel['product'] = productcatpanel['product'].str.strip()
productcatpanel['vendor'] = productcatpanel['vendor'].str.strip()
productcatpanel['currency_type']= productcatpanel['currency_type'].str.strip()
productcatpanel['price_value'] = productcatpanel['price_value'].str.strip()
productcatpanel['rating_new'] = productcatpanel['rating_new'].str.strip()
productcatpanel['level_new'] = productcatpanel['level_new'].str.strip()
productcatpanel['nratings'] = productcatpanel['nratings'].str.strip()

productcatpanel.drop_duplicates(inplace= True)


l = list(productcatpanel.prod_category.unique())

l = pd.DataFrame(l)

l.to_csv('productcategory.csv')

productcatpanel.to_pickle('categorypanel.pkl')
productcatpanel= pd.read_pickle('categorypanel.pkl')


productcatpanel.to_csv('categorypanel_31Oct.csv')
productcatpanel.to_excel('categorypanel_31Oct.xlsx')


####### get silkroad vendors #########

PATH = '/Users/pradeep/Workingdirectory/Data/DNM Files/SilkRoad2/Vendor ratings/'

ff = []
a= pd.DataFrame()

PATH[72:82]

glo[75:85]

for glo in glob.glob(f'{PATH}/*.*'):
#    print(glo)
    a = pd.read_csv(glo, names = ['product','price','shipping','ratingcnt','vendor','ratinggood'])
    a['date']= glo[72:82]
    ff.append(a)
   
ff1 = pd.concat([ff[i] for i in range(len(ff))], ignore_index = True)

ff2 = ff1[['vendor','date']]

ff3 = ff2.drop_duplicates()

ff1.date.unique()
len(ff1.date.unique())
ff3['silk'] = 1
ff3['month']= ff3['date'].apply(lambda x: x[5:7])
ff3['year']= ff3['date'].apply(lambda x: x[0:4])


import datetime

efvendor = ef1[['vendor','date']]
efvendor['evol']=1
efvendor['month'] = efvendor['date'].apply(lambda x: x[5:7])
efvendor['year'] = efvendor['date'].apply(lambda x: x[0:4])


efvendor = efvendor.drop_duplicates()


len(efvendor.vendor.unique())

cmnv = pd.merge(efvendor, ff3, on = ['vendor','month','year'], how = 'left')

cmnv.drop_duplicates()

np.sum(cmnv['silk'])

commonv = cmnv[['vendor','evol','silk','month','year']]

commonv = commonv.drop_duplicates()

c = commonv[['vendor','silk']]
len(c)

c = c.drop_duplicates()
len(c)

d = c[c['silk']==1]
len(d)

e = ef1[['vendor']]
e = e.drop_duplicates()
len(e)

## test how many evolution vendors were on silkroad ##

f = ff1[['vendor']]
f = f.drop_duplicates()
len(f)

e['evol'] = 1
f['silk'] = 1

###### list of evolution vendors also present on silkroad
g = pd.merge(e,f, how = 'left', on = 'vendor')

h = g[g['silk']==1] # check how many on silkroad

g['vendor'] = g['vendor'].str.strip()

categorypanel2 = pd.merge(productcatpanel, g, how= 'left', on = 'vendor')


np.sum(categorypanel2['silk'])

## category panel data with silkroad flag added ####
categorypanel2.to_pickle('categorypanel3_31Oct.pkl')
categorypanel2.to_csv('categorypanel3_31Oct.csv')


############# rough work ###############


for x in df:
    df1.append(x)

df1 = pd.DataFrame(columns = ['storename','product','price','vendor','rating','level','date'])
for a in df:
    df1.append(a)

df1 = pd.DataFrame(columns = ['storename','product','price','vendor','rating','level','date'])

del df1

glo[72:82]





##### extract from webpages - moved to Jupyter ! #######
from bs4 import BeautifulSoup
import json
import codecs

PATH = '/Users/pradeep/Workingdirectory/Data/DNM Files/2014-11-06/'

soup = BeautifulSoup(open('index.php?topic=515.0;all'), 'html.parser')

print(soup.prettify())

a = soup.prettify()

soup.li
soup.li['class']
soup.li.next_element

soup.h3
soup.h3.span.next_element.next_element

soup.head
soup.body
soup.contents

soup.find_all('Price')

soup.find_all('span')

## member karma posts
for x in soup.find_all('li'):
    print(x.next_element.string)


####################

#Forum title
soup.title.string

#topic

# member name
for profile in soup.find_all('h4'):
    print(profile.get_text())


#Reply no./ message no. and timestamp
for strong in soup2.find_all('strong'):
    print(strong.string) 
    print(strong.next_element.next_element)

# edit to post
soup.em.string

for em in soup.find_all('em'):
    timestamp = em.next_element
    print(timestamp)


#text of the post
for inner in soup.find_all('div','inner'):
    innerelement = inner.next_element
    print(innerelement)

#username
for profile in soup2.find_all('h4'):
    print(profile.get_text())

#Member type
for postgroup in soup.find_all('li','postgroup'):
    memberlevel = postgroup.next_element

#no. of posts
for postcount in soup.find_all('li','postcount'):
    nposts  = postcount.next_element
    
#karma
for karma in soup.find_all('li','karma'):
    karmalvl = karma.next_element
#quote
for blurb in soup.find_all('li','blurb'):
    blurbquote = blurb.next_element





Things I want

Username
text posted
moderator flag
in reply to flag
member type
no. of posts
karma
blurb?
topic
message no.
signature



