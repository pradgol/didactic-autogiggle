#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 19:52:02 2018

@author: pradeep
"""

import numpy as np
import pandas as pd
import rpy2.robjects as robjects
robjects.r("require(foreign)")

#### input files - csv format####
dirlegacy = pd.read_excel('/Users/pradeep/Workingdirectory/Data/Womboard/Director_legacy_1996_2003_19feb.xlsx') ## source- iss director data 1996-2003 
compustat_cusip = pd.read_excel('compustat_cusip.xlsx') ### cusip from compustat
gender_added = pd.read_csv('/Users/pradeep/Dropbox (Pradeep ISB)/Women board members/Data/genderize_output.csv') ## output from genderize 
patdata = pd.read_stata('/Users/pradeep/Workingdirectory/Data/Womboard/pradeep.dta') ### patent data from saharsh
litg = pd.read_stata('/Users/pradeep/Workingdirectory/Data/forAnandLitigation.dta') ### litigations data from Srivathsan
crsp_permno= pd.read_excel('/Users/pradeep/Workingdirectory/Data/crsp_permno.xlsx') ## get permno to gvkey mapping 
execomp = pd.read_excel('/Users/pradeep/Dropbox (Pradeep ISB)/Women board members/Data/execucomp_24may.xlsx') ## source - compustate capital IQ
firmdata = pd.read_excel('/Users/pradeep/Workingdirectory/Data/firmdata_20feb.xlsx')### get this from compustat
entropy = pd.read_stata('/Users/pradeep/Workingdirectory/Data/entropy_pradeep.dta') ## did not write to pickle
compustat_sahars = pd.read_csv('/Users/pradeep/Workingdirectory/Data/compustatdata_saharsh.csv')
compustat_tobinq = pd.read_excel('/Users/pradeep/Dropbox (Pradeep ISB)/Women board members/Data/compustat_tobinsq.xlsx')

patpermno = pd.read_csv('/Users/pradeep/Google Drive (pradeep_pachigolla@isb.edu)/Women board members/Data/patents.csv')
abandnbr = pd.read_stata('/Users/pradeep/Google Drive (pradeep_pachigolla@isb.edu)/Women board members/Data/abandonmentsdata.dta')
patcitations = pd.read_stata('/Users/pradeep/Workingdirectory/Data/patent_citations.dta')
restot = pd.read_stata('compuvar_restotpretot.dta')
restot.drop_duplicates(inplace = True)


#################### write all csv files to pickle#########################
dirlegacy.to_pickle('/Users/pradeep/Workingdirectory/Data/dirlegacy.pkl')
compustat_cusip.to_pickle('/Users/pradeep/Workingdirectory/Data/compustat_cusip.pkl')

gender_added['genderize_flag'] = 1
gender_added.to_pickle('/Users/pradeep/Workingdirectory/Data/genderize.pkl')

patdata['gvkey']=pd.to_numeric(patdata['gvkey'])  ### change gvkey to numeric
patdata.to_pickle('/Users/pradeep/Workingdirectory/Data/patdata.pkl')

crsp_permno.to_pickle('/Users/pradeep/Workingdirectory/Data/crsp_permno.pkl')
litg.to_pickle('/Users/pradeep/Workingdirectory/Data/litg.pkl')
litgc2.to_pickle('/Users/pradeep/Workingdirectory/Data/litgc2.pkl') ##company level litigation data
execomp.to_pickle('/Users/pradeep/Workingdirectory/Data/execomp.pkl')

firmdata = firmdata[firmdata['Industry Format'] == 'INDL']
firmdata.to_pickle('/Users/pradeep/Workingdirectory/Data/firmdata.pkl')

compustat_sahars.to_pickle('/Users/pradeep/Workingdirectory/Data/compustat_sahars.pkl')

compustat_tobinq['Debt'] = compustat_tobinq['Current Liabilities - Total'] - compustat_tobinq['Current Assets - Total']+compustat_tobinq['Inventories - Total'] + compustat_tobinq['Long-Term Debt - Total']
compustat_tobinq['MVE'] = (compustat_tobinq['Price Close - Annual - Fiscal']*compustat_tobinq['Common Shares Outstanding'])
compustat_tobinq['PS'] = compustat_tobinq['Preferred Stock - Liquidating Value']
compustat_tobinq['tobinq_ab'] = (compustat_tobinq['MVE'] + compustat_tobinq['PS'] + compustat_tobinq['Debt'])/compustat_tobinq['Assets - Total']
compustat_tobinq = compustat_tobinq[compustat_tobinq['Industry Format'] == 'INDL']
tobinqab = compustat_tobinq[['Global Company Key','Data Year - Fiscal','Debt','MVE', 'PS','Assets - Total', 'tobinq_ab']]
tobinqab.to_pickle('/Users/pradeep/Workingdirectory/Data/tobinqab.pkl')


########################### read all pickles ###############################
dirlegacy = pd.read_pickle('/Users/pradeep/Workingdirectory/Data/dirlegacy.pkl')
compustat_cusip = pd.read_pickle('/Users/pradeep/Workingdirectory/Data/compustat_cusip.pkl')
gender_added = pd.read_pickle('/Users/pradeep/Workingdirectory/Data/genderize.pkl')
patdata = pd.read_pickle('/Users/pradeep/Workingdirectory/Data/patdata.pkl') ## read patapp as patdata
crsp_permno = pd.read_pickle('/Users/pradeep/Workingdirectory/Data/crsp_permno.pkl')
litg = pd.read_pickle('/Users/pradeep/Workingdirectory/Data/litg.pkl')
litgc2= pd.read_pickle('/Users/pradeep/Workingdirectory/Data/litgc2.pkl')
execomp = pd.read_pickle('/Users/pradeep/Workingdirectory/Data/execomp.pkl')
firmdata = pd.read_pickle('/Users/pradeep/Workingdirectory/Data/firmdata.pkl')
compustat_sahars = pd.read_pickle('/Users/pradeep/Workingdirectory/Data/compustat_sahars.pkl')
tobinqab = pd.read_pickle('/Users/pradeep/Workingdirectory/Data/tobinqab.pkl')

############################################################################

dirlegacy.drop_duplicates(inplace = True)
dirlegacy['CUSIP - 6 Digit'] = dirlegacy['CUSIP - 6 Digit'].astype(str).apply(lambda x:x.zfill(6))
dirlegacy['cusip'] = dirlegacy['CUSIP - 6 Digit'].str[:6]

dirlegacy.columns = ['year_annualmeet',
'irrc_companyid_legacy',
'irrc_companyid',
'irrc_dirid',
'irrc_dirid_legacy',
'ticker',
'cusip_6dig',
'company_name',
'meeting_date',
'dirname_first',
'dirname_last',
'dir_fullname',
'dir_age',
'female_yn',
'ethnicity',
's_p_index',
'board_affiliation_E_emp_I_indep_L_linked',
'country_employment',
'economic_group',
'other_profession',
'emp_title_if_subsidiaryexec',
'emp_category',
'stock_exchange',
'industry_code_descr',
'person_w_directorship_interlock',
'oth_title_descr',
'oth_employment_title',
'primary_comp_name',
'title_primary_job',
'relation_employee',
'type_services',
'revenue',
'l75_att_yn',
'audit_chair_yn',
'audit_member_yn',
'biz_trans_yn',
'charity_relationship_yn',
'compensation_commitee_chair_yn',
'compensation_committee_member_yn',
'desigdir_yn',
'yr_serv_beg',
'economic_group',
'CEO_exp_yn',
'cfo_yn',
'chairman_yn',
'coo_yn',
'evp_yn',
'prez_yn',
'sec_yn',
'svp_yn',
'treasure_yn',
'vc_yn',
'vp_yn',
'prevemp_yn',
'corp_gov_comm_member_yn',
'grandfathered_retire_tenure',
's_p_index_code',
'industry_grp_code',
'inst_holdings',
'interlock_directorship_yn',
'mth_meeting',
'comm_chair_nominating_yn',
'election_curr_yr_ann_meeting',
'nom_comm_member_yn',
'nonemp_chairman_yn',
'shares_held',
'oth_title_yn',
'oth_affiliation_yn',
'num_otherboards',
'owns_less_1pct_yn',
'pct_votingpower',
'prior_service_on_board_yn',
'prof_services_yn',
'relative_yn',
'substitle_yn',
'common_shares_outstanding',
'total_voting_power',
'year_termination',
'yr_serv_end',
'cusip'
]

dir1 = dirlegacy[['year_annualmeet',
'meeting_date',
'irrc_companyid_legacy',
'irrc_companyid',
'irrc_dirid',
'irrc_dirid_legacy',
'dirname_first',
'dirname_last',
'dir_fullname',
'yr_serv_beg',
'yr_serv_end',
'dir_age',
'female_yn',
'ethnicity',
'board_affiliation_E_emp_I_indep_L_linked',
'grandfathered_retire_tenure',
'primary_comp_name',
'prevemp_yn',
'l75_att_yn',
'desigdir_yn',
'CEO_exp_yn',
'cfo_yn',
'chairman_yn',
'coo_yn',
'evp_yn',
'prez_yn',
'sec_yn',
'svp_yn',
'treasure_yn',
'vc_yn',
'vp_yn',
'audit_chair_yn',
'audit_member_yn',
'compensation_commitee_chair_yn',
'compensation_committee_member_yn',
'corp_gov_comm_member_yn',
'comm_chair_nominating_yn',
'nom_comm_member_yn',
'nonemp_chairman_yn',
'oth_title_yn',
'oth_affiliation_yn',
'owns_less_1pct_yn',
'relative_yn',
'shares_held',
'pct_votingpower',
'total_voting_power',
'revenue',
'num_otherboards',
'ticker',
'company_name',
's_p_index',
's_p_index_code',
'cusip_6dig',
'cusip'
]]

dir1['s_p_index'].replace('S&P 500 (','S&P 500', inplace = True)
dir1['retired'] = dir1['primary_comp_name'].apply(lambda x: 1 if x=='RETIRED' else 0)
dir1['dir_indep']=dir1['board_affiliation_E_emp_I_indep_L_linked'].apply(lambda x: 1 if x== 'I' else 0)
dir1['tenure'] = dir1['yr_serv_end']-dir1['yr_serv_beg']
dir1['tenure'] = dir1['tenure'].apply(lambda x: np.nan if x<0 else x)
dir1['tenure'] = dir1['tenure'].apply(lambda x: np.nan if x>64 else x)
dir1['num_otherboards'] = dir1['num_otherboards'].apply(lambda x: 0 if x =='*' else x)
dir1['num_otherboards']=pd.to_numeric(dir1['num_otherboards'])
dir1['compyr_id'] = dir1['cusip'].map(str) + dir1['year_annualmeet'].map(str)

##**## checkpoint 1 ##**##
dir1.to_pickle('/Users/pradeep/Workingdirectory/Data/dir1.pkl')
dir1 = pd.read_pickle('/Users/pradeep/Workingdirectory/Data/dir1.pkl')
##**##################**##

#################################################################

#################################################################
################# add gender,patent,litg data  ##################
#################################################################

### make cusip into 9 digits and get first 6 digits for merging with noncompustat data
compustat_cusip = compustat_cusip[compustat_cusip['Industry Format'] == 'INDL']## get only indl format
t1= compustat_cusip[['Global Company Key', 'Data Year - Fiscal','CUSIP','Company Name']]
t1['CUSIP'] = t1['CUSIP'].astype(str).apply(lambda x:x.zfill(9))
t1['cusip'] = t1['CUSIP'].str[:6]
t1.drop_duplicates(subset = ['cusip', 'Data Year - Fiscal'], inplace = True) ## not sure why there are duplicates for cusip+fiscal year!!

#### add gvkeys to companies in dir1 ###
dir2 = pd.merge(dir1,t1,how= 'left', left_on = ['cusip','year_annualmeet'] , right_on = ['cusip','Data Year - Fiscal'] )
dir2.drop_duplicates(inplace = True)
dir2['gvkey'] = pd.to_numeric(dir2['Global Company Key'], downcast = 'integer')
del dir2['irrc_dirid']; del dir2['irrc_companyid']

######## add genderize data #############*
d7 = pd.merge(dir2, gender_added, how = 'left', on = 'irrc_dirid_legacy')
d7['genderize_flag'][d7.genderize_flag.isnull()] = 0
d7['female_yn'][d7['Gender'] == 'male'] = 0
d7['female_yn'][d7['Gender'] == 'female'] =1
del d7['Gender']; del d7['Probability']; del d7['Firstname']; del d7['dir_fullname_y']

########## add patent data ##############*
dir96_06 = pd.merge(d7,patdata, how = 'left', left_on = ['gvkey', 'year_annualmeet'], right_on = ['gvkey','fyear']) # with genderize
dir96_06['num_otherboards']=pd.to_numeric(dir96_06['num_otherboards'])

##**## checkpoint 2 ##**##
dir96_06.to_pickle('/Users/pradeep/Workingdirectory/Data/dir96_06.pkl')
dir96_06 = pd.read_pickle('/Users/pradeep/Workingdirectory/Data/dir96_06.pkl')
##**##################**##

##### prepare litigations data ##########*
crsp_permgvkey1 = crsp_permno[["Standard and Poor's Identifier", 'Historical CRSP PERMNO Link to COMPUSTAT Record']] # mapping permno. to gvkey in litigations file
crsp_permgvkey1.columns = ['gvkey','permno']
crsp_permgvkey1.drop_duplicates(subset = ['permno'],inplace= True) # permno to gvkey mapping
crsp_permgvkey1.drop_duplicates(subset = ['gvkey'],inplace= True) # permno to gvkey mapping

litg1 = litg.groupby(['permno','year']).agg({'defendent':np.sum, 'plaintiff':np.sum})
litgc = litg1.reset_index() ## company level litigation data
litgc2 = pd.merge(litgc, crsp_permgvkey1, how = 'left', on = ['permno'] ) # add gvkey to litigations data
litgc2.rename(columns = {'defendent':'defendant'}, inplace = True)
litgc2.drop_duplicates(inplace = True)

#### add litigations data to dir file ####
dir9606lt= pd.merge(dir96_06,litgc2, how='left', left_on = ['gvkey','fyear'], right_on = ['gvkey','year'])
dir9606lt.drop_duplicates(inplace = True)        

############## write director file into stata for stata stats###
dir9606lt.to_csv('directorlevel_data.csv')
robjects.r('x=read.csv("directorlevel_data.csv")')
robjects.r('write.dta(x,"directorlevel_data4Jun.dta")')

######## null value substitution at the last step - so I can generate summary stats at a director level before going for processing/regressions
dir9606lt.defendant.fillna(0, inplace = True)
dir9606lt.plaintiff.fillna(0, inplace = True)
dir9606lt.npat.fillna(0,inplace = True)
dir9606lt.breakthroughs.fillna(0,inplace = True)
dir9606lt.avg_generality.fillna(0,inplace = True)
dir9606lt.median_generality.fillna(0,inplace = True)

del dir9606lt['year']
del dir9606lt['permno']

##**## checkpoint 3 ##**##
dir9606lt.to_pickle('/Users/pradeep/Workingdirectory/Data/dir9606lt2.pkl')### pickle 5 mar
dir9606lt = pd.read_pickle('/Users/pradeep/Workingdirectory/Data/dir9606lt2.pkl')
##**##################**##


#################################################################
############# create instrument and other vars ##################
#################################################################

# companies with female boardmembers flag
cwf = dir9606lt[dir9606lt['female_yn']==1][['year_annualmeet','company_name']]
cwf_nodupes = cwf.drop_duplicates()
cwf_nodupes['womenboard'] = 1

dirfile2 = pd.merge(dir9606lt, cwf_nodupes, how = 'left')
dirfile2.womenboard.fillna(0, inplace = True)

# no. of women board members
nothboards = dirfile2.groupby(['dir_fullname_x','year_annualmeet']).agg({'womenboard':np.sum})
nothboards.reset_index(inplace = True)
nothboards.rename(columns = {'womenboard' : 'otherwomboards_n'}, inplace = True)

#no. of males on other women boards
dirfile3= pd.merge(dirfile2,nothboards, how = 'left')
dirfile3['otherwomboards_n'] = dirfile3.otherwomboards_n - dirfile3.womenboard
dirfile3.otherwomboards_n.value_counts()
dirfile3['male_otherwombrd']=0
dirfile3['male_otherwombrd']= np.where((dirfile3['female_yn'] ==0) & (dirfile3['otherwomboards_n'] > 0), 1,0) # male and sitting in other boards with women

# total external board seats
totexboards = dirfile3.groupby(['dir_fullname_x','year_annualmeet']).agg({'company_name':np.size})
totexboards.reset_index(inplace =True)
totexboards.rename(columns = {'company_name':'tot_boardseats'}, inplace = True)

dirfile3 = pd.merge(dirfile3,totexboards, how = 'left')
dirfile3['ext_boardseats'] = dirfile3['tot_boardseats'] - 1 # total external board seats
dirfile3['male_flag'] = np.where(dirfile3['female_yn'] ==0,1,0) #male flag
dirfile3['tot_male_extboardseats'] = dirfile3['ext_boardseats']*dirfile3['male_flag'] # total male external board seats

## independent directors dummy
dirfile3['dir_indep'] = dirfile3['board_affiliation_E_emp_I_indep_L_linked']
dirfile3['dir_indep']=dirfile3['dir_indep'].apply(lambda x: 1 if x== 'I' else 0)

##**## checkpoint 4 ##**##
dirfile3.to_pickle('/Users/pradeep/Workingdirectory/Data/dirfile3.pkl')
dirfile3 = pd.read_pickle('/Users/pradeep/Workingdirectory/Data/dirfile3.pkl')
##**##################**##


#################################################################
################### merge with execucomp ########################
#################################################################

compyr_exe1 = execomp[['Company ID Number','Fiscal Year','Annual CEO Flag',
                       'Total Current Compensation (Salary + Bonus)', 
                       'Total Compensation (Salary + Bonus + Other Annual + Restriced Stock Grants + LTIP Payouts + All Other + Value of Option Grants)']]
compyr_exe1.drop_duplicates(inplace = True)
compyr_exe1.dropna(inplace = True)
compyr_exe1['execomp_flag']=1

dirfile3_overlap3 = pd.merge(dirfile3, compyr_exe1, how = 'left', left_on = ['gvkey','year_annualmeet'], right_on = ['Company ID Number', 'Fiscal Year'])
dirfile3_overlap3.rename(columns = {'Total Current Compensation (Salary + Bonus)': 'CEO_comp_curr',
                    'Total Compensation (Salary + Bonus + Other Annual + Restriced Stock Grants + LTIP Payouts + All Other + Value of Option Grants)': 'CEO_comp_total'}, inplace = True)
del dirfile3_overlap3['Company ID Number']; del dirfile3_overlap3['Fiscal Year']; del dirfile3_overlap3['Annual CEO Flag']    
dirfile3_overlap3['execomp_flag'][dirfile3_overlap3['execomp_flag'].isnull()] = 0

## export to stat for table 1 replication at director level - not exported yet
dirfile3_overlap3.to_csv("dirfile3_overlap3_24May_2.csv")
robjects.r('x=read.csv("dirfile3_overlap3_24May_2.csv")')
robjects.r('write.dta(x,"dirfile3_overlap3_24May_2.dta")')


#################################################################
###### aggregate director level data to board level data ########
#################################################################

reg1 = dirfile3_overlap3.groupby(['year_annualmeet','gvkey']).agg({'defendant': np.mean,'plaintiff': np.mean, 'breakthroughs':np.mean, 
                        'avg_generality':np.mean,'npat':np.mean,'company_name':np.size, 'female_yn': np.sum, 'dir_age': np.mean, 
                        'l75_att_yn': np.sum, 'CEO_exp_yn': np.sum,
                        'pct_votingpower':np.sum,'num_otherboards':np.mean, 'tenure':np.mean, 'relative_yn':np.sum,
                        'desigdir_yn':np.sum, 'cfo_yn':np.sum, 'chairman_yn':np.sum, 'coo_yn':np.sum, 'evp_yn':np.sum, 
                        'prez_yn':np.sum, 'sec_yn':np.sum, 'svp_yn':np.sum,'treasure_yn':np.sum, 'vc_yn':np.sum, 'vp_yn':np.sum,'prevemp_yn':np.sum,
                        'male_otherwombrd':np.sum,
                        'ext_boardseats':np.sum,
                        'tot_male_extboardseats':np.sum,
                        'otherwomboards_n':np.sum,
                        'dir_indep': np.sum, 
                        'retired':np.sum,
                        'CEO_comp_curr':np.mean,
                        'CEO_comp_total':np.mean
                        })

reg1.num_otherboards.fillna(0,inplace = True)
reg1.treasure_yn.fillna(0,inplace = True)
reg1.pct_votingpower.fillna(0,inplace = True)

reg1.rename(columns = {'company_name': 'board_size', 'female_yn':'female_n', 'dir_age':'avg_age','l75_att_yn':'l75_att_n',
                             'CEO_exp_yn': 'CEO_exp_tot', 'pct_votingpower':'pctvotingpower_boardtot', 'num_otherboards':'notherboards_avg',
                             'tenure':'tenure_avg','relative_yn':'relatives_tot','desigdir_yn': 'desidir_tot', 'cfo_yn': 'cfo_tot', 'chairman_yn': 'chairman_tot', 'coo_yn':'coo_tot', 'evp_yn': 'evp_tot', 
                        'prez_yn':'prez_tot', 'sec_yn':'sec_tot', 'svp_yn':'svp_tot','treasure_yn':'treasurer_tot', 'vc_yn':'vc_tot', 'vp_yn':'vp_tot','prevemp_yn':'prevemployee_tot',
                        'otherwomboards_n': 'extboardseats_womboards_tot','dir_indep':'dirindep_n', 'retired':'retired_n'}, inplace = True)

    
############################variable creation############################
    
reg1.head()

reg1['wom_pct'] = reg1['female_n'] / reg1['board_size']
reg1['attl75_pct'] = reg1['l75_att_n']/reg1['board_size']
reg1['ceoexp_pct'] = reg1['CEO_exp_tot']/reg1['board_size']
reg1['relatives_pct'] = reg1['relatives_tot']/reg1['board_size']
reg1['desigdir_pct'] = reg1['desidir_tot']/reg1['board_size']
reg1['cfo_pct'] = reg1['cfo_tot']/reg1['board_size']
reg1['chairman_pct'] = reg1['chairman_tot']/ reg1['board_size']
reg1['coo_pct'] = reg1['coo_tot']/reg1['board_size']
reg1['evp_pct'] = reg1['evp_tot']/reg1['board_size']
reg1['prez_pct'] = reg1['prez_tot']/ reg1['board_size']
reg1['sec_pct'] = reg1['sec_tot']/ reg1['board_size']
reg1['svp_pct'] = reg1['svp_tot']/ reg1['board_size']
reg1['treasurer_pct'] = reg1['treasurer_tot']/ reg1['board_size']
reg1['vc_pct'] = reg1['vc_tot']/ reg1['board_size']
reg1['vp_pct'] = reg1['vp_tot']/ reg1['board_size']
reg1['prevemp_pct'] = reg1['prevemployee_tot']/reg1['board_size']
reg1['males_onothwomboards_pct'] = reg1['male_otherwombrd']/reg1['board_size']
reg1['extfemboards_extboardseats_pct'] = reg1['extboardseats_womboards_tot']/reg1['ext_boardseats']
reg1['indepdir_frac'] = reg1['dirindep_n']/reg1['board_size']
reg1['males_onothwomboards_pct1'] = reg1['male_otherwombrd']/(reg1['board_size'] - reg1['female_n'])


reg1.drop_duplicates(inplace = True)
reg1.extfemboards_extboardseats_pct.fillna(0, inplace = True)

##**## checkpoint 5 ##**##
reg1.to_pickle('/Users/pradeep/Workingdirectory/Data/reg1.pkl') 
reg1 = pd.read_pickle('/Users/pradeep/Workingdirectory/Data/reg1.pkl')
##**##################**##

##### next set of data manipulations #####
reg2 = reg1.reset_index()
reg2[reg2.duplicated(['year_annualmeet','gvkey'], keep = False)]

reg3 = pd.merge(reg2, firmdata, how='left', left_on = ['gvkey','year_annualmeet'], right_on = ['Global Company Key','Data Year - Fiscal'])
reg3.drop_duplicates(inplace = True)

#########add new company vars ############
reg3['rnd_sales_ratio'] = reg3['Research and Development Expense']/reg3['Sales/Turnover (Net)']
reg3['adv_sales_ratio'] = reg3['Advertising Expense']/reg3['Sales/Turnover (Net)']
reg3.rename(columns = {'Sales/Turnover (Net)': 'sales','Assets - Total':'total_assets',
                       'Active/Inactive Status Marker':'active_inactive_status',
                       'Advertising Expense':'adv_expense','Research and Development Expense':'rnd_expense',
                       'Standard Industry Classification Code':'sic'}, inplace = True)

##**## checkpoint 6 ##**##
reg3.to_pickle('/Users/pradeep/Workingdirectory/Data/reg3.pkl') 
reg3= pd.read_pickle('/Users/pradeep/Workingdirectory/Data/reg3.pkl') 
##**##################**##

### clean up ###########
reg4 = reg3[['year_annualmeet', 'gvkey', 'defendant','plaintiff', 'breakthroughs',
       'avg_generality', 'npat', 'board_size', 'female_n', 'avg_age',
       'l75_att_n', 'CEO_exp_tot', 'pctvotingpower_boardtot',
       'notherboards_avg', 'tenure_avg', 'relatives_tot', 'desidir_tot',
       'cfo_tot', 'chairman_tot', 'coo_tot', 'evp_tot', 'prez_tot', 'sec_tot',
       'svp_tot', 'treasurer_tot', 'vc_tot', 'vp_tot', 'prevemployee_tot',
       'male_otherwombrd', 'ext_boardseats', 'tot_male_extboardseats',
       'extboardseats_womboards_tot', 'wom_pct', 'attl75_pct', 'ceoexp_pct',
       'relatives_pct', 'desigdir_pct', 'cfo_pct', 'chairman_pct', 'coo_pct',
       'evp_pct', 'prez_pct', 'sec_pct', 'svp_pct', 'treasurer_pct', 'vc_pct',
       'vp_pct', 'prevemp_pct', 'males_onothwomboards_pct','males_onothwomboards_pct1','extfemboards_extboardseats_pct',
       'indepdir_frac','rnd_sales_ratio','adv_sales_ratio', 'sic','Employees',
       'total_assets','Cash',
       'active_inactive_status','sales',
       'adv_expense','rnd_expense','CEO_comp_curr','CEO_comp_total'
        ]]

###### add entropy #########
entropy['year'] = entropy['datadate'].dt.year
entropy['gvkey'] =pd.to_numeric(entropy['gvkey'])
reg5 = pd.merge(reg4,entropy, how = 'left', left_on = ['gvkey','year_annualmeet'],right_on = ['gvkey','year'])
reg5.drop_duplicates(['gvkey','year_annualmeet'], keep = 'last', inplace = True)
comp_roa = compustat_sahars[['gvkey','fyear','tobinQ_def','tobinQ','roa','sic2dig']]
reg5 = pd.merge(reg5,comp_roa, how = 'left', left_on = ['gvkey','year_annualmeet'],right_on = ['gvkey','fyear'])

### add new tobinsq ###
reg6 = pd.merge(reg5, tobinqab, how = 'left', left_on = ['gvkey','year_annualmeet'], right_on = ['Global Company Key','Data Year - Fiscal'])

##**## checkpoint 7 ##**##
reg6.to_pickle('/Users/pradeep/Workingdirectory/Data/reg6.pkl')
##**##################**##

## writing reg6 into stata 
reg6.to_csv('bdata_4June.csv')
robjects.r('x=read.csv("bdata_4June.csv")')
robjects.r('write.dta(x,"bdata_4June.dta")')

########################################################
##### add patents data, abandonments and restot  #######
########################################################

####### abandonments #####

ptpermnonomiss = patpermno[~patpermno['permno'].isnull()]
abandgvkey = pd.merge(patdata,abandperm, how = 'left', left_on = 'permnocrsp', right_on = 'permno')
cit = pd.merge(ptpermnonomiss,patcitations, how = 'left', left_on = 'patnum', right_on = 'patent')# citations data
abpt = pd.merge(cit, abandnbr, how = 'left', left_on = 'patnum',right_on = 'patent')# abandonments data

# create abandonment variables 
abpt['abd_aft12yr'] = np.where(((abpt['PaidYr12'] >0) & (abpt['expired'] >0 )), 1, 0)
abpt['abd_12yr'] = np.where(((abpt['PaidYr8']>0) & (abpt['PaidYr12'] == 0) & (abpt['expired'] >0)),1,0 )
abpt['abd_8yr'] = np.where(((abpt['PaidYr4']>0) & (abpt['PaidYr8'] == 0) & (abpt['expired'] >0)),1,0 )
abpt['abd_4yr'] = np.where(((abpt['PaidYr4'] == 0) & (abpt['expired'] >0)),1,0 )

# create variables at permno level
ptdf1 = abpt.groupby(['permno','appyear']).agg({'abd_aft12yr': np.sum, 'abd_12yr':np.sum, 'abd_8yr':np.sum,
                        'abd_4yr':np.sum, 'expired':np.sum, 'failure':np.sum, 'fw_cites_bs':np.sum, 'fw_cites_bs_adj':np.sum, 'permno':np.size })
ptdf1.rename(columns = {'permno':'ngrants'}, inplace = True)
ptdf1.reset_index(inplace = True)

## agg by permno and abandon year
abptclvl_abyr = abpt.groupby(['permno','abandon']).agg({'expired':np.sum })
abptclvl_abyr.reset_index(inplace = True)
abptclvl_abyr.columns = ['permno','abandon_yr','nabandoned_focusyr']

# add gvkey
patdata2 = pd.merge(patdata, ptdf1, how = 'left', left_on = ['permnocrsp','fyear'], right_on = ['permno','appyear'])
patdata2 = pd.merge(patdata2, abptclvl_abyr, how = 'left', left_on =['permnocrsp','fyear'], right_on = ['permno','abandon_yr'] )

#add abandonments data to reg6
x = pd.merge(reg6, patdata2, how = 'left', left_on = ['gvkey','year_annualmeet'], right_on = ['gvkey','fyear'])

#add restot and pretot
y = pd.merge(x, restot, how = 'left', left_on = ['gvkey','year_annualmeet'], right_on = ['gvkey','gyear'])
y.drop_duplicates(inplace = True)

# add nick bloom tq
rdx_nbtq_4Jun = pd.read_stata('rdx_nbtq_4Jun.dta')
rdx_nbtq_4Jun['gvkey_num']=rdx_nbtq_4Jun['gvkey'].astype(float)
rdx_nbtq_4Jun.drop_duplicates(inplace = True)
rdx_nbtq_4Jun = rdx_nbtq_4Jun[rdx_nbtq_4Jun['indfmt'] == 'INDL']

reg7 = pd.merge(y, rdx_nbtq_4Jun, how= 'left', left_on =['gvkey', 'year_annualmeet'], right_on = ['gvkey_num', 'fyear'])

##**## checkpoint 8 ##**##
reg7.to_pickle('/Users/pradeep/Workingdirectory/Data/reg7.pkl')
##**##################**##


## writing y into stata 
reg7.to_csv('bdata_4June.csv')
robjects.r('x=read.csv("bdata_4June.csv")')
robjects.r('write.dta(x,"bdata_4June.dta")')


y.info()
y.dtypes
