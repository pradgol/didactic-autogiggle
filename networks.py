#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 13:41:43 2017

@author: pradeep
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr
import networkx as nx



######################linkedin data prep##################
##########################################################

linkedin_dt = pd.read_excel('Linkedin-Final.xlsx',na_values = ['NA'])

linkedin_dt.describe()
linkedin_dt.columns

linkedin_workingdt = pd.DataFrame(linkedin_dt, columns =["Founder's name",'Startup name','Location',
                                   'Companies','Position held','Experience Dates ',
                                   'University','Courses','College timeline',
                                   'Connection'])

linkedin_workingdt.to_pickle('/Users/pradeep/Workingdirectory/Data/linkedinnt.pkl')
linkedin_workingdt = pd.read_pickle('/Users/pradeep/Workingdirectory/Data/linkedinnt.pkl')


#linkedin_workingdt.index = 1:16167
#index = list(range(1000000,1016167,1)),


#linkedin_workingdt.shape
#linkedin_workingdt.describe()
#linkedin_workingdt.columns
#linkedin_workingdt.index

#linkedin_workingdt.columns.str.strip()

founders = linkedin_workingdt["Founder's name"]

linkeidn_dict= {founders: linkedin_workingdt["Courses"]}


####split companies data and get a cell for each company, pos, date###

companies_test= linkedin_workingdt['Companies'].str.split('\(\&\)',expand = True)
position_held = linkedin_workingdt['Position held'].str.split('\(\&\)', expand = True)
exp_dates = linkedin_workingdt['Experience Dates '].str.split('\(\&\)', expand = True)

######strip spaces########
companies_obj = companies_test.select_dtypes(['object'])
companies_test[companies_obj.columns] = companies_obj.apply(lambda x: x.str.strip())

pos_obj = position_held.select_dtypes(['object'])
position_held[pos_obj.columns] = pos_obj.apply(lambda x:x.str.strip())

exp_obj = exp_dates.select_dtypes(['object'])
exp_dates[exp_obj.columns] = pos_obj.apply(lambda x:x.str.strip())

####split universities data and get a cell for each Uni, course, date###

unis = linkedin_workingdt['University'].str.split('\(\&\)',expand = True)
courses = linkedin_workingdt['Courses'].str.split('\(\&\)',expand = True)
college_dates = linkedin_workingdt['College timeline'].str.split('\(\&\)',expand = True)

######strip spaces#########

unis_obj = unis.select_dtypes(['object'])
unis[unis_obj.columns] = unis_obj.apply(lambda x:x.str.strip())

courses_obj = courses.select_dtypes(['object'])
courses[courses_obj.columns] = courses_obj.apply(lambda x:x.str.strip())

coll_obj = college_dates.select_dtypes(['object'])
college_dates[coll_obj.columns] = coll_obj.apply(lambda x:x.str.strip())


######### add data to nd array########

linkedin_test=linkedin_workingdt

l4=xr.Dataset({
              'unis':unis, 'courses': courses,'collegedates': college_dates,
              'companies':companies_test,'position':position_held, 'expdates':exp_dates,
              'raw':linkedin_workingdt})

######### iterate over unis of all entrepreneurs and see if there is a common key###########

unistack = unis.stack() ## create stack of unis variable

i = 0
j = 0

for i in unis.rows:
    for j in unis.columns:
        if unis.iloc[i,j] != "":
            print(i,j)
    tuple1 = unistack[unistack == unis.iloc[1,0]].index.get_level_values(0)

unistack[4,2]

unistack.index.get_level_values(0)

unis.iloc[1,0]

unis.stack()[unis.stack() ==unis.iloc[1,0]]


unis[unis == unis.iloc[1,0]]

###The most unoptimal code possible!!!###########


unis_edges = pd.DataFrame(columns = ['E1','E2'])

unis[1][4]

unis = unis.replace(np.nan, '', regex=True)

for j in range(0,len(unis)-1):
    for i in unis.columns:
        for l in range(j+1,len(unis)-1):
            for k in unis.columns:
                if unis[i][j] != "":
                    if unis[i][j] == unis[k][l]:
                        df = pd.DataFrame([[j,l]], columns = ['E1','E2'])
                        unis_edges = unis_edges.append(df) 
                        print(l)
                        

unis_edges.to_csv('/Users/pradeep/Google Drive (pradeep_pachigolla@isb.edu)/Entrepreneur network/unis_edges.csv')


#####test - to try later###

######## try creating edges from unis######33

unis = linkedin_workingdt['University'].str.split('\(\&\)')
unis2 = linkedin_workingdt['University'].str.split('\(\&\)',expand = True)

if pd.notnull(unis.iloc[1]).any(): ###boolean for rowvalue 
    mask = [unis2.stack().str.contains(a) for a in unis.iloc[1]]


tup = unis2.stack()[mask[0]]


test = pd.DataFrame(columns= ['Node1','Node2']) ### initialize empty dataframe

test['Node1'] = 1
test['Node2'] = tup.index.get_level_values(0)

test['Node2'].append(tup.index.get_level_values(0))


######
arb = []

arb.append(tup.index.values)

abc = pd.DataFrame(arb).stack()

d['edge1'] = e.values[0]

#e= abc.reset_index(level = 1, drop = True)

#e.index = range(len(abc))

### function to get edges


df = []
test = pd.DataFrame(columns= ['Node1','Node2'])
test2 = pd.DataFrame(columns = ['Node1','Node2'])

insti = unis.iloc[1]


def func(insti):    
    mask = [unis2.stack().str.contains(y) for y in insti]            
    for a in range(len(mask)):
        test = pd.DataFrame(columns= ['Node1','Node2'])
        print(1)
        tup = unis2.stack()[mask[a]]
        test['Node2']= tup.index.get_level_values(0)
        test2.append(test)
 
func(insti)

test2 = pd.DataFrame([])


######################################################################
############Function to calculate nodes##############################

def func(i,insti):    
    test2 = pd.DataFrame([])
    mask = [unis2.stack().str.contains(y) for y in insti]    
    for a in mask:
        tup = unis2.stack()[a]
        test= pd.DataFrame(tup.index.get_level_values(0), columns = ['Node2'])
        test2 = test2.append(test)
        test2['Node1']= i
#    print(test2)
    return test2


############## testing##########

#### universities####

unis = linkedin_workingdt['University'].str.split('\(\&\)')
unis2 = linkedin_workingdt['University'].str.split('\(\&\)',expand = True)

unis_notnull = unis[unis.notnull()]

nodelist = pd.DataFrame([], columns = ['Node1','Node2']) 
for i,j in unis_notnull.iteritems(): ##calling function to create nodes
    print(i)
    nodelist = nodelist.append(func(i,j))
 
unis_nodes_nodupes = nodelist.drop_duplicates()



#####################################
#####################################
#####################################

################

##########test function 2#########


subset = unis.iloc[1:5]
subset1 = subset[subset.notnull()]

list(subset1.items())


func(subset)

mask1 = subset.notnull()

subset1 = subset[mask1]

output = subset1.apply(func) ##### calling function - working !!!
    

######## capturing output########

subset1.apply(func1) 

nodes = pd.DataFrame([])

nodes = list(zip(subset[subset.notnull()].apply(func)))

nodes

node2 = pd.DataFrame.from_items(nodes)

nodes.merge(subset[subset.notnull()].apply(func),left_index = True, right_index = True)




insti = unis.iloc[1]

mask = [unis2.stack().str.contains(y) for y in insti]
for a in mask:
    tup = unis2.stack()[a]
    print(tup)
    test = pd.DataFrame(tup.index.get_level_values(0), columns = ['Node2'])
    test2 = test2.append(test)



pd.DataFrame([['a','b']], columns=['Node1','Node2'])

a= pd.DataFrame([insti.index,tup.index.get_level_values(0)],columns = ['Node1','Node2'])




unis2 = unis.dropna(how= 'all')  


###
unis2 = unis.stack().str.strip()
###
courses2= courses.stack()
###
coldates2=college_dates.stack()
###
edutime = pd.concat(unis2,courses2,coldates2)
###
edu= pd.merge(unis,courses,college_dates)

####

unis2 = unis2.dropna()

unis2.to_csv('/Users/pradeep/Google Drive (pradeep_pachigolla@isb.edu)/Entrepreneur network/unis_list.csv')

unis2.shape

len(unis2)

unis_edges2 = pd.DataFrame(columns = ['E1','E2'])

i=0
j=0

un2= unis2.sort_index


un2==un2

for i in range(0,len(unis2)-1):
    for j in range(i+1, len(unis2)-1):
        if unis2.values[i] == unis2.values[j]:
            ag= pd.DataFrame([unis2.index.values[i],unis2.index.values[j]],columns = ['E1','E2'])
            unis_edges2 = unis_edges2.append(ag)
            print(unis2.values[j])

print(unis2[unis2==unis2.iloc[j]].index.values)

print(unis2.iloc[[j]].index.values)

for index, uni in enumerate(unis2):
abc= unis2.iloc[[j]].index.values,unis2[unis2==unis2.iloc[j]].index.values

abc

                       
###############prepare network nodes file##########

unis_test = unis_edges.stack()
unis_nodes = unis_test.copy(deep=True)



unis_nodes2 = unis_nodes.drop_duplicates(keep= 'first')

unis_nodes2.to_csv('/Users/pradeep/Google Drive (pradeep_pachigolla@isb.edu)/Entrepreneur network/unis_nodes.csv')



#####################Draw networks#################





#####################################################################
#########################Test########################################
#####################################################################



################### networkx##############

g= nx.Graph()
g.add_edges_from(unis_edges)
g.add_nodes_from(unis_nodes2)

type(g.nodes())
g.edges()[-1]


h=nx.path_graph(10)

nx.draw(g)
plt.show()



print(nx.shortest_path(g,'a','b'))


petersen=nx.petersen_graph()

nx.draw(petersen) 

nx.draw_random(g)



########################

for i in range(1,10):
    if i == 3:
        continue
    print(i)
    if i != 3:
        print('holala')


xyz_tuple = pd.DataFrame(columns = ['E1','E2'])
df2.columns = ['E1','E2']

xyz_tuple=xyz_tuple.append(df2)


xyz = pd.DataFrame(data = [['a','b'],['b','a'],['a','a'],['b','c']])

xyz[1][3]

for a in range(0,len(xyz)-1):
    for b in xyz.columns:
        for c in range(a+1,len(xyz)-1):
            for d in xyz.columns:
                if xyz[b][a] == xyz[d][c]:                    
                    df2 = pd.DataFrame([[a,c]],columns = ['E1','E2'])
                    xyz_tuple=xyz_tuple.append(df2) 


###########################################
#################cheatsheet################
###########################################

linkedin_test=linkedin_workingdt
linkedin_test.columns
linkedin_test.shapes 
linkedin_test.index

linkedin_test.describe()
linkedin_test.describe().index
linkedin_test.describe().columns

linkedin_test.index.name = 'id'
linkedin_test.columns.name= 'attr'
linkedin_test.head()

linkedin_test['Location']

linkedin_test['Companies'] = linkedin_workingdt['Companies'].str.split('\(\&\)').str.strip()

linkedin_test['Companies'].str.strip()



linkedin_test.loc[0:5]

linkedin_test[linkedin_test['Location']== 'Noida Area, India']

new_link = linkedin_test.dropna()
new_link.shape

new_link = linkedin_test.dropna(how = 'all')
new_link.shape

ix= new_link.index

new_link = new_link.set_index("Founder's name")
 
new_link.loc['Kushagra Sinha']

new_link.iloc[16166]

new_link.T

new_link.shape

linkedin_test.describe()
linkedin_test.cov()
linkedin_test.corr()
linkedin_test.rank()
linkedin_test.cumsum()
linkedin_test.plot()

linkedin_test.info()

linkedin_test.columns

######create xr data array from linkedin_test panda data frame#####
l3 = xr.DataArray(linkedin_test, dims= ('Founder','Attributes' ))


####add unis etc split columns as coordinates for each dimension#####

l3.attrs

linkedin_test=linkedin_workingdt

l4=xr.Dataset({
              'unis':unis, 'courses': courses,'collegedates': college_dates,
              'companies':companies_test,'position':position_held, 'expdates':exp_dates,
              'raw':linkedin_test})

l4['companies'].stack()

l4['raw']
l4['companies']
l4['unis']

l4['unis'].str.strip()

for l4


companies_test.head(4)
companies_test.stack()


companies_test[companies_test]







l4.info


l4.shape

unis.shape

l3.dims
l3.shape
l3.coords


, dims=("Founder's name", 'Startup name', 'Location', 'Companies',
       'Position held', 'Experience Dates ', 'University', 'Courses',
       'College timeline', 'Connection') )



xr.DataArray()

linkedin_test["Founder's name", 'Startup name', 'Location', 'Companies',
       'Position held', 'Experience Dates ', 'University', 'Courses',
       'College timeline', 'Connection']


xr.DataArray(np.random.randn(2,3))

data= xr.DataArray(np.random.randn(2,3),dims= ('x','y'), coords= {'x':['a','b']})

data.dims
data.values
data.coords

data_test= xr.DataArray(linkedin_workingdt, dims= ('Founders','Details'), coords)

linkedin_dt[5:100:5]


data_test.coords['unis']

data_test.dims
data_test.values
data_test.coords

s=pd.Series(np.random.randn(10))

######### check among colleges each person to see if there is a common key and code#####



##### get the final dataset with the common keys#######




linkedin_3d.dims

companies_t2= companies_test.astype(str)

companies_t2.dtype
str.strip()

unis_test= unis.astype(str)

unis_test.dtypes

unis_test.columns.str.strip()


#unis_test.columns.dtype

#index = linkedin_dt["Founder's name",'Startup name'].str.join("_")

s=pd.Series(np.random.randn(10))


#########test############
s= pd.Series(np.random.randn(5),index= ['a', 'b', 'c', 'd', 'e'])

s

pd.Series(np.random.randn(5))

s.index

d= {'a':0., 'b':1., 'c':2.}

pd.Series(d)

pd.Series(d,index = ['a','b','d','c'])

pd.Series(s,index =['a'])

s[:4]

s['e']
###########end test########


for row in companies_test.rows.values:
    for row2 in companies_test.iterrows():
        company_tuple[m][0]= companies_test[row] and company_tuple[n][0] = company_test[row2]

help(str)
print(companies_test.columns)
print(companies_test.index+1)


company_tuple = pd.DataFrame(columns =['E1','E2'] )

company_tuple.shape

companies_test[:,3]


print(companies_test[0][1])



