#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 14:12:49 2017

@author: pradeep
"""

import numpy as np
import pandas as pd
import matplotlib as plt

cluster_dt = pd.read_stata('/Users/pradeep/Google Drive (pradeep_pachigolla@isb.edu)/Cluster Paper/Data/Data_MAin_v12.dta')
cluster_dt.to_pickle('cluster_dt.pkl')
cluster_dt = pd.read_pickle('cluster_dt.pkl')

#pprint(cluster_dt.columns)
#print(cluster_dt.columns)
#print(pd.get_option("display.max_columns"))
#print(pd.set_option("display.max_columns",999))
#pd.set_option('display.max_columns', None)
#cluster_dt.columns
#pandas.set_option('display.max_rows', None)


cols = list(cluster_dt.columns)

df1 = cluster_dt[['Company_Name',
                          'City', 'PreviousLocation_F1',
                          'PreviousLocation_F2','PreviousLocation_F3',
                          'PreviousLocation_F4','MostExperiencedfounderlocatio']]
                          
df1 = cluster_dt

####################################################
## get people who moved from cluster to non-cluster
####################################################

## get currentcity
df1.City.value_counts()
df1['City_2'] = df1['City'].apply(lambda x: x.split(',')[0])
df1['City_2'] = df1['City'].apply(lambda x: x.strip())
df1['City_3'] = df1['City_2'].apply(lambda x: x.split(',')[0])
df1['City_3'].value_counts()
df1['City'] = df1['City_3']
df1.drop(['City_2','City_3'], axis = 1, inplace = True)

df1['prevlocf1'] = df1['PreviousLocation_F1'].apply(lambda x: x.split('-')[0])
df1['prevlocf2'] = df1['PreviousLocation_F2'].apply(lambda x: x.split('-')[0])
df1['prevlocf3'] = df1['PreviousLocation_F3'].apply(lambda x: x.split('-')[0])
df1['prevlocf4'] = df1['PreviousLocation_F4'].apply(lambda x: x.split('-')[0])
df1['mostexpfloc'] = df1['MostExperiencedfounderlocatio'].apply(lambda x: x.split('-')[0])

df1.drop(['PreviousLocation_F1','PreviousLocation_F2','PreviousLocation_F3','PreviousLocation_F4','MostExperiencedfounderlocatio'], axis = 1, inplace = True)

df1 = df1[df1['Company_Name'] !='']

#### iit iim flag ######
df1['Founder1IIT'] = df1.Founder1educaton.str.contains('IIT', regex = False)
df1['Founder2IIT'] = df1.Founder2education.str.contains('IIT', regex = False)
df1['Founder3IIT'] = df1.Founder3educaton.str.contains('IIT', regex = False)
df1['Founder4IIT'] = df1.Founder4educaton.str.contains('IIT', regex = False)

df1['Founder1IIM'] = df1.Founder1educaton.str.contains('IIM', regex = False)
df1['Founder2IIM'] = df1.Founder2education.str.contains('IIM', regex = False)
df1['Founder3IIM'] = df1.Founder3educaton.str.contains('IIM', regex = False)
df1['Founder4IIM'] = df1.Founder4educaton.str.contains('IIM', regex = False)

df1['founderIIT_flag'] = df1['Founder1IIT']|df1['Founder2IIT']|df1['Founder3IIT']|df1['Founder4IIT']
df1['founders_IITIIM'] = df1['Founder1IIT']|df1['Founder2IIT']|df1['Founder3IIT']|df1['Founder4IIT']|df1['Founder1IIM']|df1['Founder2IIM']|df1['Founder3IIM']|df1['Founder4IIM']



## get companies not in cluster
cluster = ['Bangalore','Mumbai','Delhi','Noida','Pune','Gurgaon','New Delhi','Bengaluru','Bangaluru','Bengalore']
df2 = df1[~df1['City'].isin(cluster)]
## export to csv
#df2.to_csv('movement_clusters.csv')


## get movements from cluster to non-cluster ##
###############################################

# at least one founder moved from cluster to non-cluster
mask = df2['prevlocf1'].isin(cluster)|df2['prevlocf2'].isin(cluster)|df2['prevlocf3'].isin(cluster)|df2['prevlocf4'].isin(cluster)
df2_2 = df2[mask]
df2_3 = df2[~mask]

df2_2['totalMNC'] = df2_2[['Founder1MNCExperience','Founder2MNCExperience','Founder3MNCExperience','Founder4MNCExperience']].sum(axis = 1)
df2_3['totalMNC'] = df2_3[['Founder1MNCExperience','Founder2MNCExperience','Founder3MNCExperience','Founder4MNCExperience']].sum(axis = 1)

len(df2_2[df2_2['totalMNC']>0])
len(df2_3[df2_3['totalMNC']>0])

len(df2_2[df2_2['founders_IITIIM']>0])
len(df2_3[df2_3['founders_IITIIM']>0])


## get people who moved from non-cluster to cluster ##
######################################################

df3 = df1[df1['City'].isin(cluster)]

mask2 = df3['prevlocf1'].isin(cluster)&df3['prevlocf2'].isin(cluster)&df3['prevlocf3'].isin(cluster)&df3['prevlocf4'].isin(cluster)
df3_2 = df3[mask2]
df3_3 = df3[~mask2]

## mask3 = at least one of the founders was in non-cluster before
mask3 = ~df3['prevlocf1'].isin(cluster)|~df3['prevlocf2'].isin(cluster)|~df3['prevlocf3'].isin(cluster)|~df3['prevlocf4'].isin(cluster)
df3_4 = df3[mask3]
df3_5 = df3[~mask3]



df3_2['totalMNC'] = df3_2[['Founder1MNCExperience','Founder2MNCExperience','Founder3MNCExperience','Founder4MNCExperience']].sum(axis = 1)
df3_3['totalMNC'] = df3_3[['Founder1MNCExperience','Founder2MNCExperience','Founder3MNCExperience','Founder4MNCExperience']].sum(axis = 1)
df3_4['totalMNC'] = df3_4[['Founder1MNCExperience','Founder2MNCExperience','Founder3MNCExperience','Founder4MNCExperience']].sum(axis = 1)
df3_5['totalMNC'] = df3_5[['Founder1MNCExperience','Founder2MNCExperience','Founder3MNCExperience','Founder4MNCExperience']].sum(axis = 1)


len(df3_2[df3_2['totalMNC']>0])
len(df3_3[df3_3['totalMNC']>0])

len(df3_4[df3_4['totalMNC']>0])
len(df3_5[df3_5['totalMNC']>0])


len(df3_2[df3_2['founders_IITIIM']>0])
len(df3_3[df3_3['founders_IITIIM']>0])

len(df3_4[df3_4['founders_IITIIM']>0])
len(df3_5[df3_5['founders_IITIIM']>0])


### success failure for founders ###

success = cluster_dt[cluster_dt['Success'] == 1]
failure = cluster_dt[cluster_dt['Failure'] == 1]

columns = ['NewID','Company_Name','City','Year','Success','Failure','Numberoffounders','Founder1_ID',
 'Founder1Name',
 'Workedinafterfailure',
 'Startednewstartupafterfailur',
 'Founder2_ID',
 'Founder2Name',
 'EA',
 'EB',
 'Founder3_ID',
 'Founder3Name',
 'EQ',
 'ER',
 'Founder4_ID',
 'Founder4Name',
 'FG',
 'FH']

success1 = success[columns]
failure1 = failure[columns]

success1.columns = ['NewID','Company_Name','City','Year','Success','Failure','Numberoffounders',
 'FounderID1',
 'FounderName1',
 'WorkedinafterfailureF1',
 'StartednewstartupafterfailurF1',
 'FounderID2',
 'FounderName2',
 'WorkedinafterfailureF2',
 'StartednewstartupafterfailurF2',
 'FounderID3',
 'FounderName3',
 'WorkedinafterfailureF3',
 'StartednewstartupafterfailurF3',
 'FounderID4',
 'FounderName4',
 'WorkedinafterfailureF4',
 'StartednewstartupafterfailurF4']


failure1.columns = ['NewID','Company_Name','City','Year','Success','Failure','Numberoffounders',
 'FounderID1',
 'FounderName1',
 'WorkedinafterfailureF1',
 'StartednewstartupafterfailurF1',
 'FounderID2',
 'FounderName2',
 'WorkedinafterfailureF2',
 'StartednewstartupafterfailurF2',
 'FounderID3',
 'FounderName3',
 'WorkedinafterfailureF3',
 'StartednewstartupafterfailurF3',
 'FounderID4',
 'FounderName4',
 'WorkedinafterfailureF4',
 'StartednewstartupafterfailurF4']


sf1 = success1.append(failure1)


####
linkedinraw = pd.read_excel('Linkedin-Final.xlsx')
####

sf2 = pd.wide_to_long(sf1,  ['FounderID','FounderName','WorkedinafterfailureF','StartednewstartupafterfailurF'], 
                      i = ['NewID', 'Company_Name', 'City', 'Year', 'Success', 'Failure','Numberoffounders'],
                      j = 'Founder')

sf2.reset_index(inplace = True)


sf1lnkdin = pd.merge(sf2, linkedinraw, how = 'left',left_on = ['Company_Name','FounderName'], right_on = ['Startup name',"Founder's name"])

a = sf1lnkdin['WorkedinafterfailureF'].str.split(';', expand = True)

b = sf1lnkdin['StartednewstartupafterfailurF'].str.split(';',expand = True)

company = a[0].str.split('Companyname:', expand = True)
location = a[2].str.split('Location:', expand = True)
newstartupname = b[0].str.split('New_Startup_Name:', expand = True)
newstartuplocation = b[3].str.split('Location:', expand = True)

newstartupname[1]= np.where(pd.isnull(newstartupname[1]), newstartupname[0], newstartupname[1]) # male and sitting in other boards with women

newstartuplocation[1]= np.where(pd.isnull(newstartuplocation[1]), newstartuplocation[0], newstartuplocation[1]) # male and sitting in other boards with women



sf1lnkdin['Companyafter'] = company[1]
sf1lnkdin['Locationafter'] = location[1]
sf1lnkdin['newstartupname'] = newstartupname[1]
sf1lnkdin['newstartuplocation'] = newstartuplocation[1]

sf1lnkdin.to_csv('foundersaftrfailure.csv')


