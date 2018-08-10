#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 14:42:40 2018

@author: pradeep
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

startupround_v14 = pd.read_stata('startupround_v14.dta')
startupround_v14.to_feather('startupround14')
startupround_v14= pd.read_feather('startupround14')



angelovx = pd.read_excel('Angelo_VX.xlsx')
angelovx.to_feather('angelovx')
angelovx = pd.read_feather('angelovx')

founderdata = pd.read_excel('linkedin_export_Race_Exp_Gender_22Dec.xlsx')
founderdata.to_pickle('founderdata.pkl')
founderdata = pd.read_pickle('founderdata.pkl')

successfailure = pd.read_excel('Success failure definition2.2_Master_15nov.xlsx')
successfailure.to_pickle('successfailure.pkl')

### dataprep

del founderdata['gender match']

ex1= founderdata
ex1['cumcount'] = ex1.groupby('StartUp').cumcount()

del ex1['firstname']
del ex1['Url']
del ex1['Demographics']


ex1 = ex1.drop(['Tags', 'summary','Experience date','Experience company','School','School Years'], axis = 1)

columns = ['cumcount']

values = [ 'Name', 'Top card title',
       'Locality', 'Demographics', 'Tags', 'summary', 'Experience',
       'Experience date', 'Experience company', 'Experience role', 'School',
       'School Name', 'School Years', 'School Course', 'Connections',
       'entre_exp', 'tech_edu', 'mgmt_edu', 'edulvl_phd', 'edulvl_masters',
       'edulvl_bachelors', 'edulvl_dropout', 'education', 'gradyr',
       'yrs_since_grad', 'age', 'Probability', 'race', 'Experience Years_New',
       'fdc' ]


index = ['StartUp']

ex1.rename(columns = {'fdc':'gender'}, inplace = True)

ex1.loc[ex1['race'] == 'api(Asian percentage chance)', 'race'] = 'Asian'

fd2 = ex1.set_index(['StartUp', 'cumcount'])
fd2 = fd2.unstack()

#fd2.reset_index(inplace = True)

colnames1 = [i+str(j) for i, j in fd2.columns]

fd2.columns = colnames1

## pivot table that worked
##fd2 = pd.pivot_table(founderdata, values = values , columns = columns, index = index  )


#successfailure['startup_caps']= successfailure.Startups.str.upper()

###1. for each startup take the founder row and concatenate ii
###2. transopose it so that for each startup there is a column for a founder
###3. count max columns required and put it under that


#### add fields to df1 #####
df = startupround_v14
df1_2 = pd.merge(df,successfailure,how = 'left', left_on = 'CompanyName',right_on = 'Startups' )
df1_3 = pd.merge(df1_2, fd2, how = 'left', left_on = 'CompanyName', right_index = True )

df1_3.to_csv('startupround_v14_6May.csv')

import rpy2.robjects as robjects
robjects.r("require(foreign)")
robjects.r('x=read.csv("startupround_v14_6May.csv")')
robjects.r('write.dta(x,"startupround_v14_6May.dta")')


#### add fields to df2 #####
df2 = angelovx
df2_2 = pd.merge(df2, successfailure, how = 'left', left_on = 'ID', right_on = 'ID')
df2_3 = pd.merge(df2_2, fd2, how = 'left', left_on = 'Startups_y', right_index = True)


df2_3.to_csv('angelovx_6may.csv')
robjects.r('x=read.csv("angelovx_6may.csv")')
robjects.r('write.dta(x,"angelovx_6may.dta")')



