#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 17:48:50 2018

@author: pradeep
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bokeh.plotting import figure
import rpy2.robjects as robjects
robjects.r("require(foreign)")


##################################################################
         ########### data columns start ###############
##################################################################

import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bokeh.plotting import figure


colnames =['new_col_names',
 'state',
 'username',
 'district',
 'blank1',
 'start_survey?',
 'gps_location',
 'time',
 'date',
 'csc_name',
 'vle_name',
 'vle_id',
 'respondent_name',
 'blank2',
 'csc_startdate',
 'influencer',
 'gender',
 'vle_age',
 'mobile',
 'email',
 'agri_labourer_earnings_pd',
 'farmer_earnings_pd',
 'marital_status',
 'children',
 'services_provided_types',
 'csc_service_top1',
 'csc_service_top2',
 'csc_service_top3',
 'csc_service_top4',
 'csc_service_top5',
 'csc_topup_amt',
 'statedig_service_top1',
 'statedig_service_top2',
 'statedig_service_top3',
 'statedig_service_top4',
 'statedig_service_top5',
 'statedig_topup_amt',
 'directdig_service_top1',
 'directdig_service_top2',
 'directdig_service_top3',
 'directdig_service_top4',
 'directdig_service_top5',
 'csc_open_freq',
 'hrs_perday_csc',
 'persons_workingat_csc',
 'paid_fulltime_emp',
 'paid_parttime_emp',
 'family_fulltime',
 'family_parttime',
 'other_workers',
 'avg_emp_pay',
 'familyhelp_relationship',
 'employee_training_yn',
 'emp_training_location',
 'emp_training_type',
 'emp_training_dur',
 'csc_setup_time_sinceapp',
 'vle_training_yn',
 'vle_training_location',
 'vle_training_type',
 'vle_training_dur',
 'person_at_csc_daytoday',
 'person_at_csc_other',
 'investment_amt_cscsetup',
 'source_of_funds_investmentcapital',
 'source_of_funds_other',
 'own_savings_pct',
 'chits_cc_pct',
 'loans_familyfrnds_pct',
 'loans_moneylender_pct',
 'loans_coopsbanks_pct',
 'othr_sources_pct',
 'interest_pct',
 'family_earningmembers',
 'earnings_cscservices',
 'income_before_csc',
 'income_sources_self_all',
 'income_sources_self_oth',
 'income_csc_govt_services_self',
 'income_csc_nongovt_services_self',
 'income_oth_biz_self',
 'income_rent_lease_self',
 'income_agri_farm_self',
 'income_interests_deposits_self',
 'income_salary_pension_self',
 'income_other_self',
 'income_sources_fam_all',
 'income_sources_fam_oth',
 'income_csc_govt_services_fam',
 'income_csc_nongovt_services_fam',
 'income_oth_biz_fam',
 'income_rent_lease_fam',
 'income_agri_farm_fam',
 'income_interests_deposits_fam',
 'income_salary_pension_fam',
 'income_other_fam',
 'permissions_setup_total',
 'permissions_setup_political',
 'permissions_district',
 'permissions_panchayat',
 'permissions_police',
 'permissions_electric',
 'permissions_tele',
 'permissions_internet',
 'permissions_oth',
 'csc_opendays_perweek',
 'csc_opentime',
 'csc_closetime',
 'csc_closedays_yr',
 'csc_nvillages',
 'csc_area',
 'csc_electricity_hrs',
 'unusualworkinghrs_pwr_yn',
 'internet_speed_perception',
 'movie_download_time',
 'counters_n',
 'computers_n',
 'printers_n',
 'printer_scanner_n',
 'printer_scanner_copier_n',
 'xerox_coppier_n',
 'biometric_iris_scanner_n',
 'invertor_ups_n',
 'digicam_webcam_n',
 'lamination_n',
 'oth_equip_n',
 'oth_equip_specify',
 'computer_use_customers_yn',
 'computer_use_education_yn',
 'computer_use_jobsearch_yn',
 'computer_use_doctor_yn',
 'computer_use_other_purpose',
 'distance_csc_town',
 'distance_csc_postoffice',
 'distance_csc_distrhq',
 'distance_csc_bank',
 'distance_csc_csc',
 'entre_conditions',
 'entre_public_attitude',
 'entre_success_promo',
 'entre_skills_training',
 'entre_success_recognition',
 'entre_marketops_growth',
 'csc_totalexpenses_mthly',
 'csc_rent_mthly',
 'csc_elecbill_mthly',
 'csc_phinternetbill_mthly',
 'csc_interestexpense_mthly',
 'csc_salaries_mthly',
 'csc_training_mthly',
 'csc_expenseitems_othr',
 'csc_expenseother_mthly',
 'csc_govtservice_top1',
 'csc_govtservice_formspm_top1',
 'csc_govtservice_freqperperson_top1',
 'csc_govtservice_revenuecontribution_top1',
 'csc_govtservice_top2',
 'csc_govtservice_formspm_top2',
 'csc_govtservice_freqperperson_top2',
 'csc_govtservice_revenuecontribution_top2',
 'csc_govtservice_top3',
 'csc_govtservice_formspm_top3',
 'csc_govtservice_freqperperson_top3',
 'csc_govtservice_revenuecontribution_top3',
 'csc_govtservice_top4',
 'csc_govtservice_formspm_top4',
 'csc_govtservice_freqperperson_top4',
 'csc_govtservice_revenuecontribution_top4',
 'csc_govtservice_top5',
 'csc_govtservice_formspm_top5',
 'csc_govtservice_freqperperson_top5',
 'csc_govtservice_revenuecontribution_top5',
 'csc_nongovtservice_top1',
 'csc_nongovtservice_uniquecitizens_top1',
 'csc_nongovtservice_revenuecontribution_top1',
 'csc_nongovtservice_top2',
 'csc_nongovtservice_uniquecitizens_top2',
 'csc_nongovtservice_revenuecontribution_top2',
 'csc_nongovtservice_top3',
 'csc_nongovtservice_uniquecitizens_top3',
 'csc_nongovtservice_revenuecontribution_top3',
 'csc_nongovtservice_top4',
 'csc_nongovtservice_uniquecitizens_top4',
 'csc_nongovtservice_revenuecontribution_top4',
 'csc_nongovtservice_top5',
 'csc_nongovtservice_uniquecitizens_top5',
 'csc_nongovtservice_revenuecontribution_top5',
 'skilltraining_progs_12m_n',
 'skilltraining_villager_attendance',
 'mkting_campaigns_yn',
 'mkting_campaign_typesused',
 'mkting_campaign_othr',
 'csc_usage_future',
 'continue_w_csc_yn',
 'csc_newsletter_receive_freq',
 'csc_newsletter_read_freq',
 'email_check_freq',
 'reason_for_usingcsc1',
 'reason_for_usingcsc2',
 'reason_notusingcsc1',
 'reason_notusingcsc2',
 'serv_reqd_for_csc_growth1',
 'serv_reqd_for_csc_growth2',
 'csc_skill_acq_channels',
 'skillacq_video_usage',
 'skillacq_video_platform',
 'factors_betterbiz_csc',
 'factors_betterbiz_csc_oth',
 'csc_backend_downtime_dayspweek',
 'csc_backend_downtime_hrspday',
 'nfamilymembers',
 'nadults',
 'nchildren',
 'nearningmembers',
 'housetype',
 'housetype_oth_spec',
 'immovable_assets_owned',
 'products_owned',
 'education',
 'blank3',
 'computer_acq_date',
 'internet_access_home_yn',
 'internet_usage_home_hrspweek',
 'smartphone_usage_yn',
 'apps_used_commonly',
 'apps_used_other',
 'relatives_frnds_involved_yn',
 'fathers_occupation',
 'njobs_beforecsc',
 'occupation_beforecsc',
 'lastjob',
 'lastjob_role',
 'lastjob_length',
 'lastjob_type_ftpt',
 'lastjob2',
 'lastjob2_role',
 'lastjob2_length',
 'lastjob2_type_ftpt',
 'lastjob3',
 'lastjob3_role',
 'lastjob3_length',
 'lastjob3_type_ftpt',
 'csc_setup_plan_time',
 'timestamp2',
 'next_section_yn',
 'blank4',
 'blank5',
 'blank6',
 'blank7',
 'blank8',
 'ncustomers_csc_duringsurvey',
 'blank9',
 'blank10',
 'char_like_workinghard',
 'char_personaldemand',
 'char_othppl_perception_dontworkhard',
 'char_numfriends_fate',
 'char_workaccomplishment_lovejob',
 'char_getwhatiwant_workhard',
 'char_planahead_unwise_fortune',
 'char_leaders_reason_rightplacetime',
 'char_unsucessfulbizstrategy_experiment',
 'char_monitor_areasneedmorepractice',
 'char_goalsetting_direction_success',
 'char_thingsdontunderstand_adj_strat',
 'char_sticktoaims_accomplishgoals_easy',
 'char_unexpectedevents_conf',
 'char_calm_difficulties_copingabilities',
 'char_problem_manysolns',
 'char_mostppl_trusted',
 'char_unselfishcause_exploited',
 'char_freqcontact_diffppl',
 'char_comfort_diffppl',
 'char_time_to_trust',
 'advice_frndsfamily',
 'photo_csc_interior',
 'photo_csc_exterior',
 'photo_csc_20m',
 'state2',
 'district2',
 'gram_panchayat',
 'csc_visible_yn',
 'csc_accessible_yn',
 'csc_leftwing_area_yn',
 'csc_existingcybercafe_yn'
  ]



cscdata_part1 = pd.read_excel('VLE Data File April 810.xlsx')
cscdata_part2 = pd.read_excel('VLE Data File May 206.xlsx')
cscdata_part1.columns = colnames
cscdata_part2.columns = colnames

csc_master = cscdata_part1.append(cscdata_part2)

#csc_master = pd.read_excel('VLE Data File April 810_pp.xlsx')

nines = [999,9999,99999,999999,9999999,99999999,999999999,9999999999,99999999999,999999999999,9999999999999,99999999999999,999999999999999]
csc_master.replace(nines, np.NaN, inplace = True)


csc_master.describe(include = 'all')
csc_master.info()
csc_master.state.value_counts()


csc_master.to_pickle('csc_master_7June.pkl')
csc_master = pd.read_pickle('csc_master_7June.pkl')

csc_master.to_csv('csc_master_7June.csv')
csc_master.to_feather('csc_master')

c2 = csc_master.drop_duplicates(subset = 'vle_id')

###############################################################################
                     ### group columns question wise ####
###############################################################################


ids = ['state',
 'username',
 'district','gps_location',
 'time',
 'date',
 'csc_name',
 'vle_name',
 'vle_id',
 'respondent_name',
 'mobile',
 'email', 'state2',
 'district2',
 'gram_panchayat'
 ]


demographics = ['gender',
 'vle_age', 'marital_status',
 'education',
 'children',
 'family_earningmembers',
 'nfamilymembers',
 'nadults',
 'nchildren',
 'nearningmembers',
 'housetype',
 'housetype_oth_spec',
 'immovable_assets_owned',
 'products_owned',
 'computer_acq_date',
 'internet_access_home_yn',
 'internet_usage_home_hrspweek',
 'smartphone_usage_yn',
 'apps_used_commonly',
 'apps_used_other', 'email_check_freq']


income_chars =[
 'agri_labourer_earnings_pd',
 'farmer_earnings_pd',
 'csc_topup_amt',
 'statedig_topup_amt', 
 'earnings_cscservices',
 'income_before_csc',
 'income_sources_self_all',
 'income_sources_self_oth',
 'income_csc_govt_services_self',
 'income_csc_nongovt_services_self',
 'income_oth_biz_self',
 'income_rent_lease_self',
 'income_agri_farm_self',
 'income_interests_deposits_self',
 'income_salary_pension_self',
 'income_other_self',
 'income_sources_fam_all',
 'income_sources_fam_oth',
 'income_csc_govt_services_fam',
 'income_csc_nongovt_services_fam',
 'income_oth_biz_fam',
 'income_rent_lease_fam',
 'income_agri_farm_fam',
 'income_interests_deposits_fam',
 'income_salary_pension_fam',
 'income_other_fam'
        ]

capital[
 'investment_amt_cscsetup',
 'source_of_funds_investmentcapital',
 'source_of_funds_other',
 'own_savings_pct',
 'chits_cc_pct',
 'loans_familyfrnds_pct',
 'loans_moneylender_pct',
 'loans_coopsbanks_pct',
 'othr_sources_pct',
 'interest_pct'
        ]


csc_expenses = [
         'csc_totalexpenses_mthly',
 'csc_rent_mthly',
 'csc_elecbill_mthly',
 'csc_phinternetbill_mthly',
 'csc_interestexpense_mthly',
 'csc_salaries_mthly',
 'csc_training_mthly',
 'csc_expenseitems_othr',
 'csc_expenseother_mthly',
        ]

csc_chars = ['csc_startdate', 'csc_open_freq',
 'hrs_perday_csc']

csc_infra = [ 'internet_speed_perception',
 'movie_download_time',
 'counters_n',
 'computers_n',
 'printers_n',
 'printer_scanner_n',
 'printer_scanner_copier_n',
 'xerox_coppier_n',
 'biometric_iris_scanner_n',
 'invertor_ups_n',
 'digicam_webcam_n',
 'lamination_n',
 'oth_equip_n',
 'oth_equip_specify',
 'computer_use_customers_yn',
 'computer_use_education_yn',
 'computer_use_jobsearch_yn',
 'computer_use_doctor_yn',
 'computer_use_other_purpose',
 'skilltraining_progs_12m_n',
 'skilltraining_villager_attendance',
 'csc_newsletter_receive_freq',
 'csc_newsletter_read_freq'
]

csc_coverage = [
         'csc_opendays_perweek',
 'csc_opentime',
 'csc_closetime',
 'csc_closedays_yr',
 'csc_nvillages',
 'csc_area',
 'csc_electricity_hrs',
 'unusualworkinghrs_pwr_yn',
 'distance_csc_town',
 'distance_csc_postoffice',
 'distance_csc_distrhq',
 'distance_csc_bank',
 'distance_csc_csc'
        ]

csc_employees =[
 'persons_workingat_csc',
 'paid_fulltime_emp',
 'paid_parttime_emp',
 'family_fulltime',
 'family_parttime',
 'other_workers',
 'avg_emp_pay',
 'familyhelp_relationship',
 'person_at_csc_daytoday',
 'person_at_csc_other'
       ]



skills = [
 'employee_training_yn',
 'emp_training_location',
 'emp_training_type',
 'emp_training_dur',
 'vle_training_yn',
 'vle_training_location',
 'vle_training_type',
 'vle_training_dur',
 'csc_skill_acq_channels',
 'skillacq_video_usage',
 'skillacq_video_platform'
 ]



services = [
 'services_provided_types',
 'csc_service_top1',
 'csc_service_top2',
 'csc_service_top3',
 'csc_service_top4',
 'csc_service_top5',
 'statedig_service_top1',
 'statedig_service_top2',
 'statedig_service_top3',
 'statedig_service_top4',
 'statedig_service_top5',
 'directdig_service_top1',
 'directdig_service_top2',
 'directdig_service_top3',
 'directdig_service_top4',
 'directdig_service_top5',
 'csc_govtservice_top1',
 'csc_govtservice_formspm_top1',
 'csc_govtservice_freqperperson_top1',
 'csc_govtservice_revenuecontribution_top1',
 'csc_govtservice_top2',
 'csc_govtservice_formspm_top2',
 'csc_govtservice_freqperperson_top2',
 'csc_govtservice_revenuecontribution_top2',
 'csc_govtservice_top3',
 'csc_govtservice_formspm_top3',
 'csc_govtservice_freqperperson_top3',
 'csc_govtservice_revenuecontribution_top3',
 'csc_govtservice_top4',
 'csc_govtservice_formspm_top4',
 'csc_govtservice_freqperperson_top4',
 'csc_govtservice_revenuecontribution_top4',
 'csc_govtservice_top5',
 'csc_govtservice_formspm_top5',
 'csc_govtservice_freqperperson_top5',
 'csc_govtservice_revenuecontribution_top5',
 'csc_nongovtservice_top1',
 'csc_nongovtservice_uniquecitizens_top1',
 'csc_nongovtservice_revenuecontribution_top1',
 'csc_nongovtservice_top2',
 'csc_nongovtservice_uniquecitizens_top2',
 'csc_nongovtservice_revenuecontribution_top2',
 'csc_nongovtservice_top3',
 'csc_nongovtservice_uniquecitizens_top3',
 'csc_nongovtservice_revenuecontribution_top3',
 'csc_nongovtservice_top4',
 'csc_nongovtservice_uniquecitizens_top4',
 'csc_nongovtservice_revenuecontribution_top4',
 'csc_nongovtservice_top5',
 'csc_nongovtservice_uniquecitizens_top5',
 'csc_nongovtservice_revenuecontribution_top5'
        ]



csc_setupease = [
         'csc_setup_time_sinceapp',
 'permissions_setup_total',
 'permissions_setup_political',
 'permissions_district',
 'permissions_panchayat',
 'permissions_police',
 'permissions_electric',
 'permissions_tele',
 'permissions_internet',
 'permissions_oth',
]

csc_growth = ['mkting_campaigns_yn',
 'mkting_campaign_typesused',
 'mkting_campaign_othr',
 'csc_usage_future',
 'continue_w_csc_yn',
 'factors_betterbiz_csc',
 'factors_betterbiz_csc_oth']



environment = [
 'entre_conditions',
 'entre_public_attitude',
 'entre_success_promo',
 'entre_skills_training',
 'entre_success_recognition',
 'entre_marketops_growth',
 'csc_visible_yn',
 'csc_accessible_yn',
 'csc_leftwing_area_yn',
 'csc_existingcybercafe_yn'
 'csc_backend_downtime_dayspweek',
 'csc_backend_downtime_hrspday'
        ]



vle_history = [ 'influencer','relatives_frnds_involved_yn',
 'fathers_occupation',
 'njobs_beforecsc',
 'occupation_beforecsc',
 'lastjob',
 'lastjob_role',
 'lastjob_length',
 'lastjob_type_ftpt',
 'lastjob2',
 'lastjob2_role',
 'lastjob2_length',
 'lastjob2_type_ftpt',
 'lastjob3',
 'lastjob3_role',
 'lastjob3_length',
 'lastjob3_type_ftpt',
 'char_like_workinghard',
 'char_personaldemand',
 'char_othppl_perception_dontworkhard',
 'char_numfriends_fate',
 'char_workaccomplishment_lovejob',
 'char_getwhatiwant_workhard',
 'char_planahead_unwise_fortune',
 'char_leaders_reason_rightplacetime',
 'char_unsucessfulbizstrategy_experiment',
 'char_monitor_areasneedmorepractice',
 'char_goalsetting_direction_success',
 'char_thingsdontunderstand_adj_strat',
 'char_sticktoaims_accomplishgoals_easy',
 'char_unexpectedevents_conf',
 'char_calm_difficulties_copingabilities',
 'char_problem_manysolns',
 'char_mostppl_trusted',
 'char_unselfishcause_exploited',
 'char_freqcontact_diffppl',
 'char_comfort_diffppl',
 'char_time_to_trust']
 

#voice   
 csc_voice = ['advice_frndsfamily',
 'csc_setup_plan_time',
  'reason_for_usingcsc1',
 'reason_for_usingcsc2',
 'reason_notusingcsc1',
 'reason_notusingcsc2',
 'serv_reqd_for_csc_growth1',
 'serv_reqd_for_csc_growth2']


#photos

csc_pics = [ 'photo_csc_interior',
 'photo_csc_exterior',
 'photo_csc_20m']


##split_sep 

split_sep = ['services_provided_types', 'source_of_funds_investmentcapital','income_sources_self_all',
             'income_sources_self_oth','income_sources_fam_all',
 'mkting_campaign_typesused','factors_betterbiz_csc',
 'factors_betterbiz_csc_oth', 'immovable_assets_owned',
 'products_owned','apps_used_commonly']

## factor

factor_num = ['own_savings_pct',
 'chits_cc_pct',
 'loans_familyfrnds_pct',
 'loans_moneylender_pct',
 'loans_coopsbanks_pct',
 'othr_sources_pct',
 'income_csc_govt_services_self',
 'income_csc_nongovt_services_self',
 'income_oth_biz_self',
 'income_rent_lease_self',
 'income_agri_farm_self',
 'income_interests_deposits_self',
 'income_salary_pension_self',
 'income_other_self',
 'income_csc_govt_services_fam',
 'income_csc_nongovt_services_fam',
 'income_oth_biz_fam',
 'income_rent_lease_fam',
 'income_agri_farm_fam',
 'income_interests_deposits_fam',
 'income_salary_pension_fam',
 'income_other_fam',]

factor_char = ['person_at_csc_daytoday', 'family_earningmembers',
               'income_before_csc', 'income_sources_fam_all',
 'income_sources_fam_oth',
 'permissions_setup_political',
 'permissions_district',
 'permissions_panchayat',
 'permissions_police',
 'permissions_electric',
 'permissions_tele',
 'permissions_internet',
 'permissions_oth',
        'unusualworkinghrs_pwr_yn','internet_speed_perception',
       'computer_use_customers_yn',
 'computer_use_education_yn',
 'computer_use_jobsearch_yn',
 'computer_use_doctor_yn','entre_public_attitude',
 'entre_success_promo',
 'entre_skills_training',
 'entre_success_recognition',
 'entre_marketops_growth','skilltraining_progs_12m_n',
 'mkting_campaigns_yn', 'csc_usage_future','continue_w_csc_yn',
 'csc_newsletter_receive_freq',
 'csc_newsletter_read_freq',
 'email_check_freq', 'csc_skill_acq_channels',
 'skillacq_video_usage','skillacq_video_usage',
 'skillacq_video_platform','housetype',
 'education','internet_access_home_yn','smartphone_usage_yn','relatives_frnds_involved_yn',
 'fathers_occupation', 'njobs_beforecsc', 'occupation_beforecsc',
 'lastjob',
 'lastjob_role',
 'lastjob_length',
 'lastjob_type_ftpt',
 'lastjob2',
 'lastjob2_role',
 'lastjob2_length',
 'lastjob2_type_ftpt',
 'lastjob3',
 'lastjob3_role',
 'lastjob3_length',
 'lastjob3_type_ftpt', 'csc_visible_yn',
 'csc_accessible_yn',
 'csc_leftwing_area_yn',
 'csc_existingcybercafe_yn','counters_n'
]


freetext = ['mkting_campaign_othr', 'factors_betterbiz_csc_oth',
            'housetype_oth_spec','apps_used_other',  'income_sources_fam_oth',

########### missing treatment #########

xzero = ['children', 'paid_fulltime_emp',
 'paid_parttime_emp',
 'family_fulltime',
 'family_parttime',
 'other_workers','emp_training_dur','vle_training_dur',
 'own_savings_pct', 
 'chits_cc_pct',
 'loans_familyfrnds_pct',
 'loans_moneylender_pct',
 'loans_coopsbanks_pct',
 'othr_sources_pct',
 'interest_pct',
 'income_csc_govt_services_self',
 'income_csc_nongovt_services_self',
 'income_oth_biz_self',
 'income_rent_lease_self',
 'income_agri_farm_self',
 'income_interests_deposits_self',
 'income_salary_pension_self',
 'income_other_self',
# 'income_sources_fam_all',
# 'income_sources_fam_oth',
 'income_csc_govt_services_fam',
 'income_csc_nongovt_services_fam',
 'income_oth_biz_fam',
 'income_rent_lease_fam',
 'income_agri_farm_fam',
 'income_interests_deposits_fam',
 'income_salary_pension_fam',
 'income_other_fam',
 'computers_n',
 'printers_n',
 'printer_scanner_n',
 'printer_scanner_copier_n',
 'xerox_coppier_n',
 'biometric_iris_scanner_n',
 'invertor_ups_n',
 'digicam_webcam_n',
 'lamination_n',
 'oth_equip_n',
 'csc_rent_mthly',
 'csc_phinternetbill_mthly',
 'csc_salaries_mthly',
 'csc_expenseother_mthly',
 #'skilltraining_villager_attendance',
 #'csc_backend_downtime_dayspweek',
 #'csc_backend_downtime_hrspday', 
 #'nfamilymembers',
 #'nadults',
 'nchildren',
 'nearningmembers',
 'investment_amt_cscsetup',
 'internet_usage_home_hrspweek',
 #'avg_emp_pay'
 ]



means_districtwise = ['agri_labourer_earnings_pd','farmer_earnings_pd',
                      'hrs_perday_csc', 'csc_opendays_perweek','csc_closedays_yr',
                      'csc_nvillages','csc_area',
                      'csc_electricity_hrs','movie_download_time',
                      'distance_csc_town',
 'distance_csc_postoffice',
 'distance_csc_distrhq',
 'distance_csc_bank',
 'distance_csc_csc', 'csc_totalexpenses_mthly','csc_elecbill_mthly',
 'csc_interestexpense_mthly', 'csc_training_mthly','csc_govtservice_freqperperson_top1']


### missing replacement numeric.

csc_master[xzero] = csc_master[xzero].fillna(0)
csc_master[means_districtwise]= csc_master[['district']+means_districtwise].groupby('district').transform(lambda x: x.fillna(x.median()))

#### ignore ############
#e = csc_master[means_districtwise]
#e = csc_master[['district']+means_districtwise].groupby('district').median()
#csc_master['csc_totalexpenses_mthly'] = pd.to_numeric(csc_master['csc_totalexpenses_mthly'], errors = 'coerce')
#g = csc_master[['district']+means_districtwise]
#g[means_districtwise]= g.groupby('district').transform(lambda x: x.fillna(x.median()))
##
#csc_master[means_districtwise] = csc_master[means_districtwise].fillna(csc_master[['district']+means_districtwise].groupby('district').transform('median'))
##
########################

## text cleaning

csc_master['education'].replace('Intermediate or diploma','Intermediate or Diploma', inplace = True)

csc_master['email_check_freq'].replace('Once a fortnight','Once a Fortnight', inplace = True)
csc_master['email_check_freq'].replace('Once a week','Once a Week', inplace = True)
csc_master['email_check_freq'].replace(' Once a week','Once a Week', inplace = True)
csc_master.email_check_freq.value_counts()

csc_master.family_earningmembers.replace('Myself only', 'Myself Only', inplace = True)
csc_master.family_earningmembers.replace('Self and spouse ', 'Self and Spouse', inplace = True)
csc_master.family_earningmembers.value_counts()

csc_master.lastjob_type_ftpt.value_counts()
csc_master.lastjob_type_ftpt.replace('Only investor', 'Only Investor', inplace = True)

csc_master.lastjob_length.replace('1 to 2 years', '1 to 2 Years', inplace = True)
csc_master.lastjob_length.replace('More than 3 years', 'More than 3 Years', inplace = True )
csc_master.lastjob_length.replace('2 to 3 years', '2 to 3 Years' , inplace = True)
csc_master.lastjob_length.replace('1 Year or less', '1 Year or Less' , inplace = True)
csc_master.lastjob_length.replace('3 + Years', 'More than 3 Years' , inplace = True)
csc_master.lastjob_length.value_counts()

csc_master.occupation_beforecsc.value_counts()
csc_master.occupation_beforecsc.replace('Salaried/ Service/ employee (e.g. Financial Services, Pharma, IT, etc.)', 'Salaried / Service / Employee', inplace = True)

csc_master.fathers_occupation = csc_master.fathers_occupation.str.strip()
csc_master.fathers_occupation.value_counts()
csc_master.fathers_occupation.replace('Agri laborer', 'Agriculture Labourer', inplace = True)
csc_master.fathers_occupation.replace('Salaried employee – Govt', 'Salaried Employee - Govt', inplace = True)
csc_master.fathers_occupation.replace('Salaried employee – Private', 'Salaried Employee - Private', inplace = True)
csc_master.fathers_occupation.replace('Contractor / Mason etc.,', 'Contractor / Mason etc', inplace = True)
csc_master.fathers_occupation.replace('Contractor / Mason etc.,', 'Contractor / Mason etc', inplace = True)
csc_master.fathers_occupation.replace('Casual laborer / Coolie / Daily wage earner', 'Daily Wage Earner / Coolie', inplace = True)

csc_master.influencer = csc_master.influencer.str.strip()
csc_master.influencer.value_counts()


csc_master.skilltraining_progs_12m_n.value_counts()
csc_master.skilltraining_progs_12m_n.replace('0()',0,inplace = True)

csc_master.computer_use_doctor_yn.value_counts()
csc_master.computer_use_doctor_yn.replace('no','No', inplace = True)


csc_master.to_csv('csc_master_7june.csv')

###############################################################################
################          expand text fields          #########################
###############################################################################


############################ source of funds ##################################

####### text fields flags 

#csc_master[['influencer_1', 'influencer_2', 'influencer_3']] = pd.DataFrame(csc_master.influencer.str.split('|', expand = True))

sourceoffunds = csc_master.source_of_funds_investmentcapital.str.split('|', expand = True)
sourceoffunds['state'] = csc_master.state
sourceoffunds['vleid'] = csc_master.vle_id

a = pd.melt(sourceoffunds, id_vars = ['vleid', 'state'])

a.value = a.value.str.strip()

a.value.replace('Family member, Friend, Relative', 'Family Member, Friend, Relative', inplace = True)
a.value.replace('Loans from Family members/ Friends/ Relatives', 'Family Member, Friend, Relative', inplace = True)
a.value.replace('Chits/Credit Cards', 'Credit Card / Chit', inplace = True)
a.value.replace('Loans from Money lender', 'Loans from Money Lender', inplace = True )
a.value.replace('Money Lender', 'Loans from Money Lender', inplace = True)
a.value.replace('Loans from Money lender ', 'Loans from Money Lender', inplace = True )
a.value.replace('Loans from Co-op society/ Banks','Loans from Co-op society/ Banks/ Financial Institutions', inplace = True )
a.value.replace('Co-op, Bank, Institution','Loans from Co-op society/ Banks/ Financial Institutions', inplace = True )
a.value.replace('Own savings','Own Savings', inplace = True)

a.value.unique()
a.variable.unique()
a.vleid.unique()

b = a.dropna()
b.variable = 1
b= b.drop_duplicates(['vleid','value'],keep = 'first')
c= b.pivot(columns = 'value', values = 'variable', index = 'vleid')
c.columns = ['source_'+ str(i) for i in c.columns]

c.fillna(0, inplace = True)

c['no_fundsources'] = c.sum(axis = 1)

csc_master2 = pd.merge(csc_master, c, how = 'left', left_on = 'vle_id', right_index = True)

## try plotting ##

plt.plot(b.state, b.variable)


######################### influencer #######################

influencer = csc_master.influencer.str.split('|', expand = True)
influencer['vleid'] = csc_master.vle_id

a = pd.melt(influencer, id_vars = 'vleid')
a.variable = 1
a.value.replace('', np.nan,inplace = True)
a.dropna( inplace = True)

a.value = a.value.str.strip()

a.value.unique()

a.replace('Govt Officer','Govt Official', inplace = True )
a.replace('Govt Officer, Other', 'Govt Official', inplace = True )
a.replace('NGO / Other institution','NGO / Other Institution', inplace = True )
a.replace('family member / Relative','Family member / Relative', inplace = True)

a.value.unique()

a.drop_duplicates(inplace = True)

b = a.pivot(index = 'vleid', columns = 'value', values = 'variable')

b.fillna(0, inplace = True)

b.columns = ['influencer_'+i for i in  b.columns]

csc_master2 = pd.merge(csc_master2, b, how = 'left', left_on = 'vle_id', right_index = True)


##############################################################

################### income sources  ########## 

# function part 1 = split by separator and expand and give out unique values, melt, removenas, spaces, display values that need replacing #

a = csc_master2.income_sources_self_all.str.split('|', expand = True)
a['vleid'] = csc_master2.vle_id
b = pd.melt(a, id_vars = 'vleid')
b.dropna(inplace = True)
b.value = b.value.str.strip()
b.variable = 1
b.value.unique()


# part 2 = replace text strings with whatever 
govtserv = ['CSC Government Services', 'CSC government services']
nongovtserv = ['CSC Non-Government Services','CSC Non Government Services', 'CSC non-government services  / Private Services', 'CSC non-government services']
rent = ['CSC Government Services','Rent' ]
agri = ['Agriculture / Farm Income', 'Agriculture' ]
salary= ['Salary/Pension', 'Salary / Pension']
oth_biz = ['Other Business', 'Other business', 'Any other business']
deposits = [ 'Interest / Deposits','ब्याज़/फिक्स डिपोसिट']

b.value.replace(govtserv, govtserv[0], inplace = True)
b.value.replace(nongovtserv, nongovtserv[0], inplace = True)
b.value.replace(rent, rent[0], inplace = True)
b.value.replace(agri, agri[0], inplace = True)
b.value.replace(salary, salary[0], inplace = True)
b.value.replace(oth_biz, oth_biz[0], inplace = True)
b.value.replace(deposits, deposits[0], inplace = True)
b.value.unique()



# part 3 =  pivot, rename ##

b.drop_duplicates(inplace= True)
c = b.pivot(index = 'vleid', columns ='value', values = 'variable')
c.fillna(0, inplace = True)
c.columns = ['incomesource_self_'+i for i in c.columns]

csc_master2 = pd.merge(csc_master2, c, how = 'left', left_on = 'vle_id',right_index = True)

#csc_master2.drop(csc_master2.iloc[:,-8:], axis =1, inplace = True)

#pd.get_dummies(b['value'], prefix = 'incomesources_self', prefix_sep = '_')


csc_master2.to_csv('csc_master2_7may.csv')


##################### factors for doing business ###########

csc_master2 = pd.read_excel('csc_master2_7may.xlsx')

factors_betterbiz_csc

# function part 1 = split by separator and expand and give out unique values, melt, removenas, spaces, display values that need replacing #

a = csc_master2.factors_betterbiz_csc.str.split('|', expand = True)
a['vleid'] = csc_master2.vle_id
b = pd.melt(a, id_vars = 'vleid')
b.dropna(inplace = True)
b.value = b.value.str.strip()
b.variable = 1
b.value.unique()


# part 2 = replace text strings with whatever 


share = ['Higher share of revenue in services','Higher share of revenue']
charges = ['Reduction in service charges', 'Reduction']
trad = ['Closing down traditional modes', 'Traditional','Closing down traditional modes* of delivery of services']
subsidy = ['Subsidy in operational costs', 'Subsidy in operational costs ?','Subsidy','Subsidy in operational costs (incurred on maintenance, electricity, internet connection etc.)', 'Subsidy in operational costs ీ']
credit = ['Reduced interest on loans / Better and easier credit facilities','Reduced interest & Credit facilities','Reduced interest on loans', 'Credit']
internet= ['Better internet connectivity','Better Internet Connectivity']
freedom = ['More freedom in offering products and services','More freedom']
addinc = ['Additional share of income for VLEs involved in the marketing of services','Additional share of income', 'Additional share of income', 'Marketing']
#mkting = ['Marketing']
depositreq = ['Lower deposit requirements to register CSC', 'Lower deposit','Deposit']
othr = ['Other','Others (please specify)', 'Others']



b.value.replace(share, share[0], inplace = True)
b.value.replace(charges, charges[0], inplace = True)
b.value.replace(trad, trad[0], inplace = True)
b.value.replace(subsidy, subsidy[0], inplace = True)
b.value.replace(credit, credit[0], inplace = True)
b.value.replace(internet, internet[0], inplace = True)
b.value.replace(freedom, freedom[0], inplace = True)
#b.value.replace(mkting, mkting[0], inplace = True)
b.value.replace(othr, othr[0], inplace = True)
b.value.replace(addinc, addinc[0], inplace = True)
b.value.replace(depositreq, depositreq[0], inplace = True)

b.value.unique()



# part 3 =  pivot, rename ##

b.drop_duplicates(inplace= True)
c = b.pivot(index = 'vleid', columns ='value', values = 'variable')
c.fillna(0, inplace = True)
c.columns = ['factors_betterbiz_'+i for i in c.columns]

#csc_master2.drop()

#csc_master2.drop(csc_master2.iloc[:,-23:], axis =1, inplace = True)

csc_master2 = pd.merge(csc_master2, c, how = 'left', left_on = 'vle_id',right_index = True)

dups= csc_master2.drop_duplicates()

#csc_master2.drop(csc_master2.iloc[:,-8:], axis =1, inplace = True)

#pd.get_dummies(b['value'], prefix = 'incomesources_self', prefix_sep = '_')


csc_master2.to_excel('csc_master2_7may2.xlsx')

###########################################
############# apps used by VLEs ###########
###########################################


#csc_master2['apps_used_commonly']

# function part 1 = split by separator and expand and give out unique values, melt, removenas, spaces, display values that need replacing #

a = csc_master2.apps_used_commonly.str.split('|', expand = True)
a['vleid'] = csc_master2.vle_id
b = pd.melt(a, id_vars = 'vleid')
b.dropna(inplace = True)
b.value = b.value.str.strip()
b.variable = 1
b.value.unique()


# part 2 = replace text strings with whatever 


#share = ['Higher share of revenue in services','Higher share of revenue']
#charges = ['Reduction in service charges', 'Reduction']
#trad = ['Closing down traditional modes', 'Traditional']
#subsidy = ['Subsidy in operational costs', 'Subsidy in operational costs ?','Subsidy']
#credit = ['Reduced interest on loans / Better and easier credit facilities','Reduced interest & Credit facilities','Reduced interest on loans', 'Credit']
#internet= ['Better internet connectivity','Better Internet Connectivity']
#freedom = ['More freedom in offering products and services','More freedom']
#addinc = ['Additional share of income for VLEs involved in the marketing of services','Additional share of income', 'Additional share of income', 'Marketing']
#mkting = ['Marketing']
#depositreq = ['Lower deposit requirements to register CSC', 'Lower deposit','Deposit']
#othr = ['Other','Others (please specify)']

random = ['','Refrigerator','Two Wheeler', 'Two-wheeler', 'Washing Machine']

b.value.replace(random,random[0], inplace = True)

b.value.unique()



# part 3 =  pivot, rename ##

b.drop_duplicates(inplace= True)
c = b.pivot(index = 'vleid', columns ='value', values = 'variable')
c.fillna(0, inplace = True)
c.columns = ['apps_used_'+i for i in c.columns]

#csc_master2.drop()


#csc_master2.drop(csc_master2.iloc[:,-23:], axis =1, inplace = True)

csc_master2 = pd.merge(csc_master2, c, how = 'left', left_on = 'vle_id',right_index = True)

dups= csc_master2.drop_duplicates()

#csc_master2.drop(csc_master2.iloc[:,-8:], axis =1, inplace = True)

#pd.get_dummies(b['value'], prefix = 'incomesources_self', prefix_sep = '_')

###
###### skill acq video platofrm ########
###

# function part 1 = split by separator and expand and give out unique values, melt, removenas, spaces, display values that need replacing #

'skillacq_video_platform',

a = csc_master2.skillacq_video_platform.str.split('|', expand = True)
a['vleid'] = csc_master2.vle_id
b = pd.melt(a, id_vars = 'vleid')
b.dropna(inplace = True)
b.value = b.value.str.strip()
b.variable = 1
b.value.unique()


# part 2 = replace text strings with whatever 

youtube = ['Youtube','Youtube / Youtube']
whatsapp = ['Whatsapp','Whatsapp / Whatsapp']
other = ['Other','Other / Other']


b.value.replace(youtube,youtube[0], inplace = True)
b.value.replace(whatsapp,whatsapp[0], inplace = True)
b.value.replace(other,other[0], inplace = True)


b.value.unique()


# part 3 =  pivot, rename ##

b.drop_duplicates(inplace= True)
c = b.pivot(index = 'vleid', columns ='value', values = 'variable')
c.fillna(0, inplace = True)
c.columns = ['skilvid_platform_'+i for i in c.columns]

csc_master2 = pd.merge(csc_master2, c, how = 'left', left_on = 'vle_id',right_index = True)

dups= csc_master2.drop_duplicates()

###
### skill acq channel
###

# function part 1 = split by separator and expand and give out unique values, melt, removenas, spaces, display values that need replacing #

a = csc_master2.csc_skill_acq_channels.str.split('|', expand = True)
a['vleid'] = csc_master2.vle_id
b = pd.melt(a, id_vars = 'vleid')
b.dropna(inplace = True)
b.value = b.value.str.strip()
b.variable = 1
b.value.unique()


# part 2 = replace text strings with whatever 

newsletter = ['Newsletter / Email','Newsletter / e-mail','Two Wheeler', 'Two-wheeler', 'Washing Machine']
videos = ['Watching Videos','By watching video materials']
oth_vle = ['Other VLEs','From other VLE']
wkrship = ['Workshop / Training','Workshops / Trainings' ]
csc_staff = ['CSC Staff','Speaking to CSC staff']

b.value.replace(newsletter,newsletter[0], inplace = True)
b.value.replace(videos,videos[0], inplace = True)
b.value.replace(oth_vle,oth_vle[0], inplace = True)
b.value.replace(wkrship,wkrship[0], inplace = True)
b.value.replace(csc_staff,csc_staff[0], inplace = True)


b.value.unique()


# part 3 =  pivot, rename ##

b.drop_duplicates(inplace= True)
c = b.pivot(index = 'vleid', columns ='value', values = 'variable')
c.fillna(0, inplace = True)
c.columns = ['skill_acq_channels_'+i for i in c.columns]

csc_master2 = pd.merge(csc_master2, c, how = 'left', left_on = 'vle_id',right_index = True)

dups= csc_master2.drop_duplicates()



### 
### persons working at csc ###
###
'persons_workingat_csc',

# function part 1 = split by separator and expand and give out unique values, melt, removenas, spaces, display values that need replacing #

a = csc_master2.persons_workingat_csc.str.split('|', expand = True)
a['vleid'] = csc_master2.vle_id
b = pd.melt(a, id_vars = 'vleid')
b.dropna(inplace = True)
b.value = b.value.str.strip()
b.variable = 1
b.value.unique()


# part 2 = replace text strings with whatever 

fullfam = ['Full-time Family Members', 'Full Time Family Member','Full-time Family Member (s)','Full-time Family member','Full-time Family Member' ]
partfam = ['Part-time Family Members', 'Part Time Family Member','Part-time Family Member']
fullemp = ['Paid Full-time Employees', 'Paid Full Time Employee']
partemp = ['Paid Part-time Employees', 'Paid Part Time Employee','Paid Part-time Employees']
noemp   = ['None / No Employees', 'No one / No employees']
others  = ['Others','Other' ]

b.value.replace(fullfam,fullfam[0], inplace = True)
b.value.replace(partfam,partfam[0], inplace = True)
b.value.replace(fullemp,fullemp[0], inplace = True)
b.value.replace(partemp,partemp[0], inplace = True)
b.value.replace(noemp,noemp[0], inplace = True)
b.value.replace(others,others[0], inplace = True)

b.value.unique()


# part 3 =  pivot, rename ##

b.drop_duplicates(inplace= True)
c = b.pivot(index = 'vleid', columns ='value', values = 'variable')
c.fillna(0, inplace = True)
c.columns = ['workingat_csc_'+i.replace(" ","") for i in c.columns]

csc_master2 = pd.merge(csc_master2, c, how = 'left', left_on = 'vle_id',right_index = True)

dups= csc_master2.drop_duplicates()

##########################
##### worker flags #######
##########################
csc_master2['familyfullflag'] =0
csc_master2['familyfullflag'][csc_master2['family_fulltime'] > 0] = 1

csc_master2['familypartflag'] =0
csc_master2['familypartflag'][csc_master2['family_parttime'] > 0] = 1

csc_master2['empfullflag'] =0
csc_master2['empfullflag'][csc_master2['paid_fulltime_emp'] > 0] = 1
csc_master2['emppartflag'] =0
csc_master2['emppartflag'][csc_master2['paid_parttime_emp'] > 0] = 1

csc_master2[['family_fulltime','familyfullflag','family_parttime','familypartflag','paid_fulltime_emp',
             'empfullflag','paid_parttime_emp','emppartflag']]


### total forms ###
a= csc_master2[['csc_govtservice_formspm_top1','csc_govtservice_formspm_top2','csc_govtservice_formspm_top3', 'csc_govtservice_formspm_top4','csc_govtservice_formspm_top5','formspm_total']]
csc_master2['formspm_total']  = csc_master2[['csc_govtservice_formspm_top1','csc_govtservice_formspm_top2','csc_govtservice_formspm_top3', 'csc_govtservice_formspm_top4','csc_govtservice_formspm_top5']].sum(axis =1)

csc_master2[['csc_govtservice_formspm_top1','csc_govtservice_formspm_top2','csc_govtservice_formspm_top3', 'csc_govtservice_formspm_top4','csc_govtservice_formspm_top5','formspm_total']]

#csc_master2.to_csv('csc_master2_30may.csv')

csc_master2.to_csv('csc_master2_7June.csv')

############ other 

influencer_cols = ['source_Credit Card / Chit',
 'source_Family Member, Friend, Relative',
 'source_Loans from Co-op society/ Banks/ Financial Institutions',
 'source_Loans from Money Lender',
 'source_Other',
 'source_Other sources (please specify)',
 'source_Own Savings','no_fundsources']


##### cluster analysis variable transformation ! ###############

df = pd.read_stata('cscdata_11June.dta')

df.loc[df['district'] == 'Ahmedabad', 'district' ] = 'Ahmadabad'
df.loc[df['district'] == 'pune', 'district' ] = 'Pune'
df.loc[df['district'] == 'balasore', 'district' ] = 'Balasore'
df.loc[df['district'] == 'Tarn taran', 'district' ] = 'Tarn Taran'


a = list(df.district.unique())
b = list(csc_archiv.District.unique())

csc_archiv = pd.read_excel('CSC_Archival_Data.xlsx')

cscmah = csc_archiv[csc_archiv['State'] == 'Maharashtra']

district_data =csc_archiv.groupby('District').agg({'Sales AMT':np.mean,'Sales Count':np.mean})

district_data.rename(columns ={'Sales AMT': 'SalesAmtDistr', 'Sales Count':'SalesCntDistr'}, inplace = True)

csc_archiv = pd.merge(csc_archiv, district_data, left_on = 'District', right_index = True)


df['vle_id_num'] = pd.to_numeric(df['vle_id'], errors = 'coerce')

df2 = pd.merge(df, csc_archiv, how = 'left', left_on = 'vle_id_num', right_on = 'CSC_Ids')



df2['formspm_total2'] =df2['csc_govtservice_formspm_top1']+df2['csc_govtservice_formspm_top2']+df2['csc_govtservice_formspm_top3']+df2['csc_govtservice_formspm_top4']+df2['csc_govtservice_formspm_top5']

df2['share1'] = round(df2['csc_govtservice_formspm_top1']/df2['formspm_total2']*100)
df2['share2'] = round(df2['csc_govtservice_formspm_top2']/df2['formspm_total2']*100)
df2['share3'] = round(df2['csc_govtservice_formspm_top3']/df2['formspm_total2']*100)
df2['share4'] = round(df2['csc_govtservice_formspm_top4']/df2['formspm_total2']*100)
df2['share5'] = round(df2['csc_govtservice_formspm_top5']/df2['formspm_total2']*100)

d1 = df2[['csc_govtservice_formspm_top1', 'csc_govtservice_formspm_top2', 'csc_govtservice_formspm_top3', 'csc_govtservice_formspm_top4' ,'csc_govtservice_formspm_top5', 'formspm_total']]

df2['HHI'] = df2['share1']**2+ df2['share2']**2+ df2['share3']**2+ df2['share4']**2+ df2['share5']**2

#df2['income_agrilabourer_pm'] = df2['agri_labourer_earnings_pd']*25

df2['Sales_AMT_pm'] = df2['Sales AMT']/12
df2['abnormal_inc'] = df2['csc_sales_pm'] - df2['farmer_earnings_pm']

d1 = df2[['farmer_earnings_pm','earnings_cscservices','Sales AMT', 'csc_sales_pm','abnormal_inc']]


df2.to_csv('cscdata_26Jun.csv')
robjects.r('x=read.csv("cscdata_26Jun.csv")')
robjects.r('write.dta(x,"cscdata_26Jun.dta")')

########################################################



####### citizen data analysis ################

cit = pd.read_excel('Citizen Datafile 1058v2.xlsx', sheetname = 'The export' )

cit.columns = ['username',
'state',
'district',
'date',
'Timestamp',
'gpslocation',
'cscname',
'cscid',
'district2',
'villagename',
'panchayat',
'respondentname',
'code',
'maritalstatus',
'children',
'education',
'occupation',
'top5products',
'topreason_link',
'topreason_text',
'newservices',
'newservices',
'schemeenrolled_link',
'csc_alt',
'csc_alt_oth',
'intro1',
'continuebuying_clv',
'contenttrans_clv',
'moneysworth_clv',
'happyrefer_crv',
'refercsc_crv',
'activelydiscuss_civ',
'cscexp_civ',
'discussbenefits_civ',
'feedbackexp_ckv',
'suggimprove_ckv',
'suggnewprods_ckv',
'ntrips_govtoff',
'ntrips_cscs',
'distptrans_govtoff',
'distptrans_csc',
'trvltime_govtoff',
'trvltime_csc',
'cost_govtoff',
'cost_csc',
'waittime_govtoff',
'waittime_csc',
'nintermediaries_govtoff',
'nintermediaries_csc',
'wageloss_govtoff',
'wageloss_csc',
'nedlays_govt',
'ndelays_csc',
'ndenied_govt',
'ndeined_csc',
'allodoccons_yn',
'nconsallodocs_l3m',
'homeodoccons_yn',
'nconshomeodocs_l3m',
'ayurveddocs_yn',
'naurveddocs_l3m',
'mobiledth_yn',
'nmobiledth_l3m',
'schlunivenrl_yn',
'nschlunivenrl_l3m',
'iitiasstudy_yn',
'niitiasstudyused_l3m',
'skilltraining_yn',
'nskilltrainingused_l3m',
'adhar_yn',
'nadharused_l3m',
'pancard_yn',
'npancard_l3m',
'passport_yn',
'applypassport_l3m',
'bankacct_yn',
'bankacct_l3m',
'insurance_yn',
'insurance_l3m',
'pensionpl_yn',
'npensionpl_l3m',
'upifundtrfr_yn',
'upifundtrfr_l3m',
'digitalpayewallets_yn',
'digitalpayewallet_l3m',
'otherserv_yn',
'otherserv_l3m',
'suggestions_link']

custeng = ['continuebuying_clv',
'contenttrans_clv',
'moneysworth_clv',
'happyrefer_crv',
'refercsc_crv',
'activelydiscuss_civ',
'cscexp_civ',
'discussbenefits_civ',
'feedbackexp_ckv',
'suggimprove_ckv',
'suggnewprods_ckv']

cit[custeng]


for x in custeng:
    cit.loc[cit[x] == 'Strongly Agree',x]= 5
    cit.loc[cit[x] == 'Agree',x]= 4
    cit.loc[cit[x] == 'Neutral',x]= 3
    cit.loc[cit[x] == 'Disagree',x]= 2
    cit.loc[cit[x] == 'Strongly Disagree',x]= 1

for x in custeng:
    cit[x] = pd.to_numeric(cit[x])

 
serviceqs = ['allodoccons_yn','homeodoccons_yn','ayurveddocs_yn','mobiledth_yn','schlunivenrl_yn',
'iitiasstudy_yn','skilltraining_yn','adhar_yn','pancard_yn','passport_yn','bankacct_yn','insurance_yn',
'pensionpl_yn','upifundtrfr_yn','digitalpayewallets_yn']

#cit['pensionpl_yn']= pd.to_numeric(cit['pensionpl_yn'])

for x in serviceqs:
    print(cit[x].unique())    
    cit.loc[cit[x]=="No, don't know if it is available", x] = 0
    cit.loc[cit[x]=='Yes, know it is available',x] = 1

for x in serviceqs:
    cit[x] = pd.to_numeric(cit[x])

impactvars = ['ntrips_govtoff',
'ntrips_cscs',
'distptrans_govtoff',
'distptrans_csc',
'trvltime_govtoff',
'trvltime_csc',
'cost_govtoff',
'cost_csc',
'waittime_govtoff',
'waittime_csc',
'nintermediaries_govtoff',
'nintermediaries_csc',
'wageloss_govtoff',
'wageloss_csc',
'nedlays_govt',
'ndelays_csc',
'ndenied_govt',
'ndeined_csc']

df2 = cit[['username',
'state',
'district',
'cscid',
'district2',
'maritalstatus',
'children',
'education',
'occupation',
'top5products',
'csc_alt',
'continuebuying_clv',
'contenttrans_clv',
'moneysworth_clv',
'happyrefer_crv',
'refercsc_crv',
'activelydiscuss_civ',
'cscexp_civ',
'discussbenefits_civ',
'feedbackexp_ckv',
'suggimprove_ckv',
'suggnewprods_ckv',
'ntrips_govtoff',
'ntrips_cscs',
'distptrans_govtoff',
'distptrans_csc',
'trvltime_govtoff',
'trvltime_csc',
'cost_govtoff',
'cost_csc',
'waittime_govtoff',
'waittime_csc',
'nintermediaries_govtoff',
'nintermediaries_csc',
'wageloss_govtoff',
'wageloss_csc',
'nedlays_govt',
'ndelays_csc',
'ndenied_govt',
'ndeined_csc',
'allodoccons_yn',
'nconsallodocs_l3m',
'homeodoccons_yn',
'nconshomeodocs_l3m',
'ayurveddocs_yn',
'naurveddocs_l3m',
'mobiledth_yn',
'nmobiledth_l3m',
'schlunivenrl_yn',
'nschlunivenrl_l3m',
'iitiasstudy_yn',
'niitiasstudyused_l3m',
'skilltraining_yn',
'nskilltrainingused_l3m',
'adhar_yn',
'nadharused_l3m',
'pancard_yn',
'npancard_l3m',
'passport_yn',
'applypassport_l3m',
'bankacct_yn',
'bankacct_l3m',
'insurance_yn',
'insurance_l3m',
'pensionpl_yn',
'npensionpl_l3m',
'upifundtrfr_yn',
'upifundtrfr_l3m',
'digitalpayewallets_yn',
'digitalpayewallet_l3m',
'otherserv_yn',
'otherserv_l3m']]

df2.replace(999, np.NaN, inplace = True)


df2[df2['ntrips_govtoff'] < 0]['ntrips_govtoff'] = 0
df2[df2['ntrips_cscs'] < 0]['ntrips_cscs'] = 0
df2.loc[df2['nedlays_govt'] > 10,'nedlays_govt'] = 10
df2[df2['ndelays_csc'] > 10]['ndelays_csc'] = 10
df2[df2['ndenied_govt'] > 10]['ndenied_govt'] = 10
df2[df2['ndeined_csc'] > 10]['ndeined_csc'] = 10

df3 = pd.DataFrame()


df3 = df2.groupby('cscid').agg({'continuebuying_clv':np.mean,
                 'contenttrans_clv':np.mean,
                 'moneysworth_clv':np.mean,
                 'happyrefer_crv':np.mean,
                 'refercsc_crv':np.mean,
                 'activelydiscuss_civ':np.mean,
                 'cscexp_civ':np.mean,
                 'discussbenefits_civ':np.mean,
                 'feedbackexp_ckv':np.mean,
                 'suggimprove_ckv':np.mean,
                 'suggnewprods_ckv':np.mean,
                 'ntrips_govtoff':np.mean ,
                 'ntrips_cscs':np.mean,
                 'distptrans_govtoff':np.mean,
                 'distptrans_csc':np.mean,
                 'trvltime_govtoff':np.mean,
                 'trvltime_csc':np.mean,
                 'cost_govtoff':np.mean,
                 'cost_csc':np.mean,
                 'waittime_govtoff':np.mean,
                 'waittime_csc':np.mean,
                 'nintermediaries_govtoff':np.mean,
                 'nintermediaries_csc':np.mean,
                 'wageloss_govtoff':np.mean,
                 'wageloss_csc':np.mean,
                 'nedlays_govt':np.mean,
                 'ndelays_csc':np.mean,
                 'ndenied_govt':np.mean,
                 'ndeined_csc':np.mean,
                 'allodoccons_yn':np.sum,
                 'homeodoccons_yn':np.sum,
                 'ayurveddocs_yn':np.sum,
                 'mobiledth_yn':np.sum,
                 'schlunivenrl_yn':np.sum,
                 'iitiasstudy_yn':np.sum,
                 'skilltraining_yn':np.sum,
                 'adhar_yn':np.sum,
                 'pancard_yn':np.sum,
                 'passport_yn':np.sum,
                 'bankacct_yn':np.sum,
                 'insurance_yn':np.sum,
                 'pensionpl_yn':np.sum,
                 'upifundtrfr_yn':np.sum,
                 'digitalpayewallets_yn':np.sum,
                 'state':np.size})

    
    
df3.reset_index(inplace = True)

df3.rename(columns = {'state':'customercount'}, inplace = True)
    
df3['allpthydoccons_awreness'] = df3['allodoccons_yn']/ df3['customercount']
df3['homeodoccons_awreness'] = df3['homeodoccons_yn']/ df3['customercount']
df3['ayurveddocs_awreness'] = df3['ayurveddocs_yn']/ df3['customercount']
df3['mobiledth_awreness'] = df3['mobiledth_yn']/ df3['customercount']
df3['schlunivenrl_awreness'] = df3['schlunivenrl_yn']/ df3['customercount']
df3['iitiasstudy_awreness'] = df3['iitiasstudy_yn']/ df3['customercount']
df3['skilltraining_awreness'] = df3['skilltraining_yn']/ df3['customercount']
df3['adhar_awreness'] = df3['adhar_yn']/ df3['customercount']
df3['pancard_awreness'] = df3['pancard_yn']/ df3['customercount']
df3['passport_awreness'] = df3['passport_yn']/ df3['customercount']
df3['bankacct_awreness'] = df3['bankacct_yn']/ df3['customercount']
df3['insurance_awreness'] = df3['insurance_yn']/ df3['customercount']
df3['pensionpl_awreness'] = df3['pensionpl_yn']/ df3['customercount']
df3['upifundtrfr_awreness'] = df3['upifundtrfr_yn']/ df3['customercount']
df3['digitalpayewallets_awreness'] = df3['digitalpayewallets_yn']/ df3['customercount']


cscdf = pd.read_stata('cscdata_woc5Jul.dta')

df4 = pd.merge(cscdf, df3, how = 'left', left_on = 'vle_id_num', right_on = 'cscid')

df4.to_csv('cscdata_9Jul.csv')
robjects.r('x=read.csv("cscdata_9Jul.csv")')
robjects.r('write.dta(x,"cscdata_9Jul.dta")')


###****** services *******#######

df_19Jul = pd.read_stata('cscdata_10Jul_v2st13.dta')


services = df_19Jul[['state','csc_govtservice_top1','csc_govtservice_top2','csc_govtservice_top3', 'csc_govtservice_top4', 'csc_govtservice_top5', 'csc_nongovtservice_top1', 'csc_nongovtservice_top2', 'csc_nongovtservice_top3', 'csc_nongovtservice_top4', 'csc_nongovtservice_top5']]
services.set_index('state',inplace = True)
a = pd.melt(services, id_vars = 'state')
serv2 = services.stack(dropna = True)
s3 = serv2.reset_index()
    
    
    
gserv = df4[['state','csc_govtservice_top1','csc_govtservice_top2','csc_govtservice_top3', 'csc_govtservice_top4', 'csc_govtservice_top5']]

a = pd.melt(gserv, id_vars = 'state')

## no matchi wth archiva data. Sent to Sriram ##miss

miss = df4[pd.isnull(df4['CSC_Ids'])][['vle_id','state','district','gps_location','time','date','csc_name','vle_name','respondent_name','csc_startdate']]


miss.to_csv('cscidarchiv_nomatch.csv')

##### cleaning up product labels ########


Adhar = ['Aaadhar',
'Aaadhar',
'Aadhaar',
'Aadhaar',
'Aadhaar',
'Aadhaar Card',
'Aadhar',
'Aadhar',
'Aadhar',
'Aadhar',
'Aadhar card',
'Aadhar Card',
'Aadhar card',
'Aadhar Card',
'Aadhar card',
'Aadhar Card',
'Aadhar card',
'Aadhar Card',
'Aadhar Card',
'Aadhar Card (cirrection',
'Aadhar Card attachment and Correction',
'Aadhar Card cilling',
'Aadhar printing',
'Aadhar screening',
'Aadhar Verification',
'Aadhar,smartcard',
'AADHARCARD',
'Aadharcard print',
'Aadharcard print',
'Adahr card',
'Addhar',
'Addhar',
'Adhar',
'Adhar',
'Adhar',
'Adhar  card',
'Adhar attachment',
'Adhar attachments',
'Adhar cads new',
'Adhar card',
'Adhar Card',
'Adhar card',
'Adhar card',
'Adhar card',
'Adhar card verification',
'Adhar correction',
'Adhar dpwn loding',
'Adhar link',
'Adhar linking',
'Adhar new',
'Adhar new',
'Adhar print',
'Adhar print',
'Adhar printing',
'Adhar printing',
'Adhar printing',
'Adhar printing',
'Adhar update service',
'Adhar updation',
'Adhar, sevasindu',
'Adharcard',
'andhar card',
'Andhar card',
'Andhar card',
'Aaadhar',
'Aadhaar',
'Aadhar',
'Aadhar',
'Aadhar',
'Aadhar Card',
'Aadhar Card',
'Aadhar Card',
'Aadhar.pvc',
'AadharCard',
'Adaracard',
'Adhar',
'Adhar',
'Adhar',
'Adhar',
'adhar card',
'Adhar card',
'Adhar card',
'Adhar card',
'Adhar card',
'Adhar card new',
'Adhar cards',
'Adhar cards',
'Adhar correctin',
'Adhar correction,',
'Adhar print',
'Adhar printing',
'Adhar printing',
'Adhara download',
'Adharcard',
'Adharcard']
    
plt.scatter(df_19Jul.distance_csc_distrhq,df_19Jul.Sales_AMT)

### data collection ####



##################################

df_19Jul[df_19Jul['vle_id_num'] == 75317700015]['vle_id']
df_19Jul[df_19Jul['vle_id_num'] == 75317700015]['vle_id']

df_19Jul.to_csv('df_19Jul.csv')



df5 = pd.merge(cscdf,df3, how = 'right', left_on = 'vle_id_num', right_on = 'cscid')

df5.to_csv('csciderrors2.csv')
    
['nconsallodocs_l3m',
'nconshomeodocs_l3m',
'naurveddocs_l3m',
'nmobiledth_l3m',
'nschlunivenrl_l3m',
'niitiasstudyused_l3m',
'nskilltrainingused_l3m',
'nadharused_l3m',
'npancard_l3m',
'applypassport_l3m',
'bankacct_l3m',
'bankacct_l3m',
'insurance_l3m',
'npensionpl_l3m',
'upifundtrfr_l3m',
'digitalpayewallet_l3m',
'otherserv_l3m']


data10jul = pd.read_stata('cscdata_10Jul_v13.dta')

## no. of VLEs paying rent ##
mask = data10jul['csc_rent_mthly']>0
len(data10jul[mask])



m1 = csc_archiv[['CSC_Ids','SalesAmtDistr','SalesCntDistr']]

m2 = pd.merge(data10jul,m1, how = 'left', left_on = 'vle_id_num', right_on = 'CSC_Ids')

del m2['CSC_Ids_y']

m2['income_abnrml'] = m2['Sales_AMT'] - m2['SalesAmtDistr']

m2.to_csv('cscdata_10Jul.csv')
robjects.r('x=read.csv("cscdata_10Jul.csv")')
robjects.r('write.dta(x,"cscdata_10Jul.dta")')



################## end #########################




################################################################################
##########               rest of code                    #######################
################################################################################


#################### get master data and clean up #########

#csc_master = pd.read_excel('CSC_survey_14Jan_2.xlsx')

## data dump 2
#csc_master = pd.read_excel('CSC Impact Assessment Survey Data VLE Feb 7.xlsx')

## data karnataka
#csc_master = pd.read_excel('CSC Karnataka Datafile.xlsx')

## data interim 1
csc_master = pd.read_excel('VLE Data File 22 March Part 1 Interim Delivery Revised_pradeep.xlsx')

csc_master.replace(999,np.NaN, inplace = True)
csc_master.replace(999999,np.NaN, inplace = True)

csc_master.describe(include = 'all')

csc_master.replace('Karanataka','Karnataka', inplace = True)
csc_master.replace('Karantaka','Karnataka', inplace = True)
csc_master.replace('Uttar pradesh','Uttarpradesh', inplace = True)
csc_master.replace('UP','Uttarpradesh', inplace = True)
csc_master.replace('Up','Uttarpradesh', inplace = True)
csc_master.replace('Utttar pradeah','Uttarpradesh', inplace = True)
#csc_master['State (CSC Location)'].replace(np.NaN,'Uttarpradesh', inplace = True)


csc_master.replace('Karanataka','Karnataka', inplace = True)
csc_master.replace('Karantaka','Karnataka', inplace = True)
csc_master.replace('Uttar pradesh','Uttarpradesh', inplace = True)

csc_master.replace('Uttarprafesh','Uttarpradesh', inplace = True)
csc_master.replace('Blhar','Bihar', inplace = True)
csc_master.replace('Patna','Bihar', inplace = True)
csc_master.replace('Telengana','Telangana', inplace = True)


csc_master.replace('ODISHA','Odisha', inplace = True)


#csc_master.iloc[:,-7]

################ means ######################

csc_means = csc_master[[
        'Name of CSC',
'Name of VLE',
'VLE ID',
'What is your age? (Completed years)',
'How much does an average agri labourer in this village earn per day?',
'How much does an average farmer in this village earn per month?',
'How many children do you have?',
'How many hours do you spend per day at CSC? 	Normal Day, Average number of hours?',
'How many PAID FULL TIME Employees are there in the CSC?  I mean who work here for more than 6 hours per day',
'How many PAID PART TIME Employees are there in the CSC?',
'How many FULL TIME FAMILY MEMBER are there in the CSC?',
'How many PART TIME FAMILY MEMBER are there in the CSC?',
#'Other workers',
'How much do you pay to the employee on an average?',
'What is the total duration of training they received?  Example: 2 Hours, 4 Hours, 10 Hours, 20 Hour etc',
'What is the total duration of training you received?  Example: 2 Hours, 4 Hours, 10 Hours, 20 Hour etc',
'How much funds did you invest for setting up the CSC?',
'% of total setup costs - From Own Savings',
'% of total setup costs - From Chits/Credit Card',
'% of total setup costs - Loan from Family Members / Friends',
'% of total setup costs - From Money Lender',
'% of total setup costs - Loans from Co-op society/ Banks/ Financial Institutions',
'% of total setup costs - From Other Source',
'What is the interest rate?',
'What was your total earnings from providing CSC services during the last month?',
'What was your average monthly income before setting up the CSC? Income from all sources',
'Annual income from CSC - Govt Services',
'Annual income from CSC - Non-Govt Services',
'Annual income from Other Business',
'Annual income from Rent / Lease',
'Annual income from Farm / Agriculture',
'Annual income from Deposit / Interest / Dividend',
'Annual income from Salary / Pension',
'Annual income from Other Source',
'Apart from signing agreement with CSC e-Governance Services, how many additional permissions, licenses, approvals, authorizations, etc., did you have to take from ________ to start the CSC?',
'For how many days a week is the CSC open?',
'What time do you usually OPEN?',
'What time do you usually CLOSE?',
'For how many days in a year (approx.) is the CSC closed due to unexpected reasons?',
'Number of villages covered by CSC (including the village in which CSC is located)',
'CSC Floor Area  (in SFT....Approximate will do)',
'On a normal day, how many hours do you have electricity (from the board/government)',
'What is the Time taken to download a movie (in mins)',
'Number of COMPUTERS available and working condition at CSC;',
'Number of PRINTERS available and working condition at CSC;',
'Number of PRINTER cum SCANNER available and working condition at CSC;',
'Number of PRINTER, SCANNER, COPIER available and working condition at CSC;',
'Number of COPY / XEROX machines available and working condition at CSC;',
'Number of BIOMETRIC /IRIS Scanner available and working condition at CSC;',
'Number of INVERTOR / UPS available and working condition at CSC;',
'Number of DIGITAL CAMERA/WEB CAM available and working condition at CSC;',
'Number of LAMINATION MACHINE available and working condition at CSC;',
'Number of any other equipment available and working condition at CSC;',
'Distance of CSC from the NEAREST TOWN (in kms);',
'Distance of CSC from the NEAREST POST OFFICE (in kms);',
'Distance of CSC from the NEAREST DISTRICT HEADQUARTERS (in kms);',
'Distance of CSC from the NEAREST BANK (in kms);',
'Distance of CSC from the NEAREST CSC (in kms);',
'Rent per Month;',
'Electricity per Month;',
'Phone & Internet per Month;',
'Debt / Loan, Interest etc',
'Employee Salaries;',
'Training expenses;',
'Other expenses (above) per Month;',
'Of all the Government services you provide, which ONE is the most utilized?',
'What is the average number of forms/applications processed per month?',
'What is the average number of unique citizens served per month?',
'How much does it contribute to your CSC business / revenue?   (In % of total)',
'Of all the Government services you provide, which ONE is the next most utilized?',
'What is the average number of forms/applications processed per month?',
'What is the average number of unique citizens served per month?',
'How much does it contribute to your CSC business / revenue?   (In % of total)',
'Of all the Government services you provide, which ONE is the next most utilized?',
'What is the average number of forms/applications processed per month?',
'What is the average number of unique citizens served per month?',
'How much does it contribute to your CSC business / revenue?   (In % of total)',
'Of all the Government services you provide, which ONE is the next most utilized?',
'What is the average number of forms/applications processed per month?',
'What is the average number of unique citizens served per month?',
'How much does it contribute to your CSC business / revenue?   (In % of total)',
'Of all the Government services you provide, which ONE is the most utilized?',
'What is the average number of forms/applications processed per month?',
'What is the average number of unique citizens served per month?',
'How much does it contribute to your CSC business / revenue?   (In % of total)',
'Of all the Non - Government services you provide, which ONE is the most utilized?',
'What is the average number of unique citizens served per month?',
'How much does it contribute to your CSC business / revenue?   (In % of total)',
'Of all the Non - Government services you provide, which ONE is the next most utilized?',
'What is the average number of unique citizens served per month?',
'How much does it contribute to your CSC business / revenue?   (In % of total)',
'Of all the Non - Government services you provide, which ONE is the next most utilized?',
'What is the average number of unique citizens served per month?',
'How much does it contribute to your CSC business / revenue?   (In % of total)',
'Of all the Non - Government services you provide, which ONE is the next most utilized?',
'What is the average number of unique citizens served per month?',
'How much does it contribute to your CSC business / revenue?   (In % of total)',
'Of all the Non - Government services you provide, which ONE is the next most utilized?',
'What is the average number of unique citizens served per month?',
'How much does it contribute to your CSC business / revenue?   (In % of total)',
'What is the total number of villagers who have attended the skill development training programs in the last 12 months?',
'On average what is the downtime (not working) of the CSC backend/ IT system?   ____ hours/ day',
'On average what is the downtime (not working) of the CSC backend/ IT system?   days / Week',
'In total, how many members are there in your family?  (Staying with you / Single kitchen)',
'How many adults?',
'How many children?',
'How many are earning members? Working, Salary, Agriculture, Labour, Business etc.',
'How long do you use the internet at home? Number of hours / week',
'Do you use a Smart Phone?',
#'Name of CSC',
#'Name of VLE',
#'State (CSC Location)',
'State'
]]


#csc_means = pd.read_excel('CSC_survey_14Jan_2_means.xlsx')


csc_means.columns = ['csc_name',
'vle_name',
'vle_id',
'vle_age',
'income_agrilabourer',
'income_farmer',
'nchildren',
'hrsatcsc',
'emp_fulltime_paid',
'emp_parttime_paid',
'fam_fulltime',
'fam_parttime',
#'emp_others',
'sal_emp',
'trainhrs_emp',
'trainhrs_vle',
'investmentamt',
'investment_savings',
'investment_chitcc',
'investment_famfrnds',
'investment_moneylender',
'investment_banks',
'investment_other',
'intrate',
'earningspermonth',
'earnings_befcsc',
'income_govtservices',
'income_nongovservices',
'income_otherbus',
'income_rent',
'income_farm',
'income_interest',
'income_salarypension',
'income_oth',
'num_permissions',
'n_opendays',
'opentime',
'closetime',
'closedays',
'villages_covered',
'floor_area',
'elec_nhours',
'downloadtime_movie',
'computers',
'printers',
'scanner_printer',
'scanner_printer_copier',
'xerox',
'biometricscanner',
'invertor',
'digicam_webcam',
'lamination_machine',
'oth_equipment',
'distance_town',
'distance_postoffice',
'distance_districthq',
'distance_bank',
'distance_nextcsc',
'rentamt',
'electricity_pm',
'internet_phone_pm',
'interest_expense_pm',
'salaries_expense_pm',
'training_pm',
'otherexpense_pm',
'govtserv1',
'govtserv1_nformspm',
'govtserv1_uniquectznpm',
'govtserv1_revenuepm',
'govtserv2',
'govtserv2_nformspm',
'govtserv2_uniquectznpm',
'gotserv2_revenuepm',
'govtserv3',
'govtserv3_nformspm',
'govtserv3_uniquectznpm',
'govtserv3_revenuepm',
'govtserv4',
'govtserv4_nformspm',
'govtserv4_uniquectznpm',
'govtserv4_revenuepm',
'govtserv5',
'govtserv5_nformspm',
'govtserv5_uniquectznpm',
'govtserv5_revenuepm',
'nongovtserv1',
'nongovtserv1_uniquectznpm',
'nongovtserv1_revenuepm',
'nongovtserv2',
'nongovtserv2_uniquectznpm',
'nongovtserv2_revenuepm',
'nongovtserv3',
'nongovtserv3_uniquectznpm',
'nongovtserv3_revenuepm',
'nongovtserv4',
'nongovtserv4_uniquectznpm',
'nongovtserv4_revenuepm',
'nongovtserv5',
'nongovtserv5_uniquectznpm',
'nongovtserv5_revenuepm',
'skilldevprog_villagersattended',
'Itdowntime_hrsperday',
'Itdowntime_daysperweek',
'familysize',
'familysize_adults',
'familysize_children',
'family_earningmembers',
'internet_usage_hrs',
'smartphone_yn',
#'csc_name2',
#'vle_name2',
'state']

csc_means = csc_means[~csc_means['csc_name'].isnull()]


#a = csc_means['familysize_children'].apply(lambda x: x[:,1])

csc_means['income_agrilabourer'] = csc_means['income_agrilabourer']*20

csc_means.state.value_counts()


csc_mean2= csc_means[[
#'csc_name',
#'vle_name',
#'vle_id',
'vle_age',
'income_agrilabourer',
'income_farmer',
'nchildren',
'hrsatcsc',
'emp_fulltime_paid',
'emp_parttime_paid',
'fam_fulltime',
'fam_parttime',
#'emp_others',
'sal_emp',
'trainhrs_emp',
'trainhrs_vle',
'investmentamt',
'investment_savings',
'investment_chitcc',
'investment_famfrnds',
'investment_moneylender',
'investment_banks',
'investment_other',
'intrate',
'earningspermonth',
#'earnings_befcsc',
'income_govtservices',
'income_nongovservices',
'income_otherbus',
'income_rent',
'income_farm',
'income_interest',
'income_salarypension',
'income_oth',
'num_permissions',
'n_opendays',
#'opentime',
#'closetime',
'closedays',
'villages_covered',
'floor_area',
'elec_nhours',
'downloadtime_movie',
'computers',
'printers',
'scanner_printer',
'scanner_printer_copier',
'xerox',
'biometricscanner',
'invertor',
'digicam_webcam',
'lamination_machine',
'oth_equipment',
'distance_town',
'distance_postoffice',
'distance_districthq',
'distance_bank',
'distance_nextcsc',
'rentamt',
'electricity_pm',
'internet_phone_pm',
'interest_expense_pm',
'salaries_expense_pm',
'training_pm',
'otherexpense_pm',
#'govtserv1',
'govtserv1_nformspm',
'govtserv1_uniquectznpm',
'govtserv1_revenuepm',
#'govtserv2',
'govtserv2_nformspm',
'govtserv2_uniquectznpm',
'gotserv2_revenuepm',
#'govtserv3',
'govtserv3_nformspm',
'govtserv3_uniquectznpm',
'govtserv3_revenuepm',
#'govtserv4',
'govtserv4_nformspm',
'govtserv4_uniquectznpm',
'govtserv4_revenuepm',
#'govtserv5',
'govtserv5_nformspm',
'govtserv5_uniquectznpm',
'govtserv5_revenuepm',
#'nongovtserv1',
'nongovtserv1_uniquectznpm',
'nongovtserv1_revenuepm',
#'nongovtserv2',
'nongovtserv2_uniquectznpm',
'nongovtserv2_revenuepm',
#'nongovtserv3',
'nongovtserv3_uniquectznpm',
'nongovtserv3_revenuepm',
#'nongovtserv4',
'nongovtserv4_uniquectznpm',
'nongovtserv4_revenuepm',
#'nongovtserv5',
'nongovtserv5_uniquectznpm',
'nongovtserv5_revenuepm',
'skilldevprog_villagersattended',
'Itdowntime_hrsperday',
'Itdowntime_daysperweek',
'familysize',
'familysize_adults',
'familysize_children',
'family_earningmembers',
'internet_usage_hrs',
#'smartphone_yn',
'state'
]]

csc_mean2.replace(999999,np.NaN, inplace = True)

csc_mean3 = csc_mean2[csc_mean2['state'] != 'Telangana']

################### dataset for avg plots#####

csc_mean3.to_csv('csc_means3.csv')

#########################################################

#for i in csc_mean3.columns:
#    print(i)
#    csc_mean3[csc_mean3['i']>1e6][i] = np.NaN


csc_avg = csc_mean3.groupby('state').mean()
csc_avg.columns # some columns haven't featured... check later...
csc_avg.to_csv('avgplots_26Mar.csv')

csc_countryavg = csc_mean3.mean()
csc_countryavg.to_csv('avgplots_country_26Mar.csv')

telangana = csc_mean2[csc_mean2['state'] == 'Telangana']


#### csc text descriptives###

csc_text = csc_master[['What have you studied? (Please share highest level completed)']]

csc_text.columns = ['vle_education']


########## stats for state reports ###
csc_means.vle_age.describe()
csc_counts.gender.value_counts()
csc_text.vle_education.value_counts()
csc_means.familysize.describe()
csc_means.earningspermonth.describe()

a = csc_means[['emp_fulltime_paid',
 'emp_parttime_paid',
 'fam_fulltime',
 'fam_parttime',
 'emp_others']]

a.replace(np.NaN,0, inplace = True)

a['total_employees'] = a['emp_fulltime_paid']+a['emp_parttime_paid']+a['fam_fulltime']+ a['fam_parttime']+ a['emp_others']

a.total_employees.describe()
csc_means.elec_nhours.describe()

## it downtime
a = csc_means[['Itdowntime_hrsperday','Itdowntime_daysperweek']]
a.replace(30,3, inplace = True)
a['itdowntime_hrsperweek'] = a['Itdowntime_hrsperday']*a['Itdowntime_daysperweek']
a.itdowntime_hrsperweek.describe()

##
csc_means.intrate

##
csc_means.villages_covered.describe()
csc_means.distance_districthq.describe()

##distances

a = csc_means[['distance_town',
 'distance_postoffice',
 'distance_districthq',
 'distance_bank',
 'distance_nextcsc']]

a.describe()
csc_means.floor_area.describe()

### incomes

a = csc_means[['income_govtservices',
'income_nongovservices',
'income_otherbus',
'income_rent',
'income_farm',
'income_interest',
'income_salarypension',
'income_oth']]

a.replace(np.NaN,0, inplace = True)

a['total_income_csc'] = a['income_govtservices']+a['income_nongovservices']

a.describe()

a.drop(a.columns[[1]], axis =1, inplace = True )

##
csc_means.earningspermonth.describe()

### monthly operational cost and investment amount

csc_means.investmentamt.describe()

a = csc_means[['state','rentamt','electricity_pm',
               'internet_phone_pm','interest_expense_pm','salaries_expense_pm','training_pm',
               'otherexpense_pm']]

a.replace(np.NaN, 0,inplace = True)

a['total_expense'] = a.rentamt+a.electricity_pm+a.internet_phone_pm+ a.interest_expense_pm+a.salaries_expense_pm+a.training_pm+a.otherexpense_pm

a.total_expense.describe()

## training
csc_means.trainhrs_vle.describe()





#####################################################
####################### counts ######################


csc_counts = csc_master[['Gender (Record, Do not ask)',
'Your marital status;',
'How often is the CSC open?',
'How long did it take to set up the CSC after formally putting an online application?',
'Were you trained on CSC operations?',
'Local political leadership',
'District administration / Revenue officials',
'Village panchayat',
'Police department',
'Electricity department',
'Telephone dept./ Agency',
'Internet Service Provider',
'Other service provider',
'Do you have to work during mid-night / early morning due to power availability?  Explain: Mid-night/ early morning or other unusual hours due to power being available only at that time?',
'Do you allow customers to access/ use computers by themselves?',
'Are the computers used for education/ training services?',
'Are computers used for job search?',
'Are computers used for consulting a doctor?',
'Number of local skill development trainings provided by the CSC in the last 12 months? Like vocational trainings, distant learning courses, spoken English courses, interviewing, personality development etc',
'Would you like to continue with the CSC business in the future?',
#'Is the CSC location easily accessible?',
#'Is the region/ area where CSC is located generally affected by Left- Wing Extremism?',
#'Is CSC an existing cyber café or other shop which was converted into a CSC?',
'State']]




csc_counts.columns = ['gender',
'maritalstatus',
'csc_open_howoften',
'timeto_setup',
'trained_yn',
'npermissions_political_leadership',
'npermissions_distr_admin',
'npermisions_panchayat',
'npermissions_police',
'npermissions_electric',
'npermissions_phone',
'npermissions_internet',
'npermissions_others',
'odd_working_hrs_dueto_pwr',
'customers_allwd_to_use_comps',
'comps_usedfor_train_edu_servs',
'comps_usedfor_job_search',
'comps_usedfor_docs',
'nskilltrainings_l12m',
'continue_w_csc_yn',
#'location_visible',
#'leftwing_extremism',
#'csc_convertedfrm_cybercafe',
'state']


################ csc counts dataset #############
csc_counts.to_csv('csc_counts.csv')
#################################################




################ some trials ####################

####### number of permissions ###

csc_counts = csc_counts[~csc_counts['gender'].isnull()]

a = csc_counts[['npermissions_political_leadership',
               'npermissions_distr_admin',
               'npermisions_panchayat',
               'npermissions_police',
               'npermissions_electric',
               'npermissions_phone',
               'npermissions_internet',
               'npermissions_others']]

a.npermissions_political_leadership.value_counts()

describe()

a.groupby(['state','npermissions_political_leadership']).size()
csc_counts.groupby(['state','npermissions_distr_admin']).size()
csc_counts.groupby(['state','npermisions_panchayat']).size()
csc_counts.groupby(['state','npermissions_police']).size()
csc_counts.groupby(['state','npermissions_electric']).size()
csc_counts.groupby(['state','npermissions_phone']).size()
csc_counts.groupby(['state','npermissions_internet']).size()
csc_counts.groupby(['state','npermissions_others']).size()





counts = csc_counts.apply(pd.Series.value_counts)


cscounts = csc_counts.groupby('state').size()
csc_counts.groupby('state').size()
csc_counts['state'].value_counts()


for i in csc_counts.columns:
    print(csc_counts.loc[i])
    csc_counts.groupby(['state',i]).size()

csc_counts.groupby(['state',])

csc_counts2 = csc_counts.set_index('state')



csc_counts.pivot_table(index = 'state',  aggfunc = len)

#### metrics for plots

pd.crosstab(index = csc_counts['state'], columns = csc_counts['gender'])
pd.crosstab(index = csc_counts['state'], columns = csc_counts['maritalstatus'])
pd.crosstab(index = csc_counts['state'], columns = csc_counts['csc_open_howoften'])
#pd.crosstab(index = csc_counts['state'], columns = csc_counts['timeto_setup'])
pd.crosstab(index = csc_counts['state'], columns = csc_counts['trained_yn'])
#pd.crosstab(index = csc_counts['state'], columns = csc_counts['npermissions_political_leadership'])
#pd.crosstab(index = csc_counts['state'], columns = csc_counts['npermissions_distr_admin'])
#pd.crosstab(index = csc_counts['state'], columns = csc_counts['npermisions_panchayat'])
#pd.crosstab(index = csc_counts['state'], columns = csc_counts['npermissions_police'])
#pd.crosstab(index = csc_counts['state'], columns = csc_counts['npermissions_electric'])
#pd.crosstab(index = csc_counts['state'], columns = csc_counts['npermissions_phone'])
#pd.crosstab(index = csc_counts['state'], columns = csc_counts['npermissions_internet'])
#pd.crosstab(index = csc_counts['state'], columns = csc_counts['npermissions_others'])
#pd.crosstab(index = csc_counts['state'], columns = csc_counts['odd_working_hrs_dueto_pwr'])
pd.crosstab(index = csc_counts['state'], columns = csc_counts['customers_allwd_to_use_comps'])
pd.crosstab(index = csc_counts['state'], columns = csc_counts['comps_usedfor_train_edu_servs'])
pd.crosstab(index = csc_counts['state'], columns = csc_counts['comps_usedfor_job_search'])
pd.crosstab(index = csc_counts['state'], columns = csc_counts['comps_usedfor_docs'])
pd.crosstab(index = csc_counts['state'], columns = csc_counts['continue_w_csc_yn'])
pd.crosstab(index = csc_counts['state'], columns = csc_counts['location_visible'])
pd.crosstab(index = csc_counts['state'], columns = csc_counts['leftwing_extremism'])
pd.crosstab(index = csc_counts['state'], columns = csc_counts['csc_convertedfrm_cybercafe'])


csc_counts['nskilltrainings_l12m'] = csc_counts['nskilltrainings_l12m'].astype('str')
csc_counts['nskilltrainings_l12m'].replace('0()','0',inplace = True)
pd.crosstab(index = csc_counts['state'], columns = csc_counts['nskilltrainings_l12m']) ### redo

#csc_counts['nskilltrainings_l12m'].value_counts()
#csc_counts.value_counts()

#### not sure what these are
print(csc_counts.groupby(['state','gender']).size())
csc_counts.groupby(['state','maritalstatus']).size()
csc_counts.groupby(['state','csc_open_howoften']).size()
csc_counts.groupby(['state','timeto_setup']).size()
csc_counts.groupby(['state','trained_yn']).size()
csc_counts.groupby(['state','npermissions_political_leadership']).size()
csc_counts.groupby(['state','npermissions_distr_admin']).size()
csc_counts.groupby(['state','npermisions_panchayat']).size()
csc_counts.groupby(['state','npermissions_police']).size()
csc_counts.groupby(['state','npermissions_electric']).size()
csc_counts.groupby(['state','npermissions_phone']).size()
csc_counts.groupby(['state','npermissions_internet']).size()
csc_counts.groupby(['state','npermissions_others']).size()
csc_counts.groupby(['state','odd_working_hrs_dueto_pwr']).size()
csc_counts.groupby(['state','customers_allwd_to_use_comps']).size()
csc_counts.groupby(['state','comps_usedfor_train_edu_servs']).size()
csc_counts.groupby(['state','comps_usedfor_job_search']).size()
csc_counts.groupby(['state','comps_usedfor_docs']).size()
csc_counts.groupby(['state','nskilltrainings_l12m']).size()
csc_counts.groupby(['state','continue_w_csc_yn']).size()
csc_counts.groupby(['state','location_visible']).size()
csc_counts.groupby(['state','leftwing_extremism']).size()
csc_counts.groupby(['state','csc_convertedfrm_cybercafe']).size()



####################### freqs #####################################


top_services = csc_means[['govtserv1',
'govtserv1_nformspm',
'govtserv1_uniquectznpm',
'govtserv1_revenuepm',
'govtserv2',
'govtserv2_nformspm',
'govtserv2_uniquectznpm',
'gotserv2_revenuepm',
'govtserv3',
'govtserv3_nformspm',
'govtserv3_uniquectznpm',
'govtserv3_revenuepm',
'govtserv4',
'govtserv4_nformspm',
'govtserv4_uniquectznpm',
'govtserv4_revenuepm',
'govtserv5',
'govtserv5_nformspm',
'govtserv5_uniquectznpm',
'govtserv5_revenuepm',
'nongovtserv1',
'nongovtserv1_uniquectznpm',
'nongovtserv1_revenuepm',
'nongovtserv2',
'nongovtserv2_uniquectznpm',
'nongovtserv2_revenuepm',
'nongovtserv3',
'nongovtserv3_uniquectznpm',
'nongovtserv3_revenuepm',
'nongovtserv4',
'nongovtserv4_uniquectznpm',
'nongovtserv4_revenuepm',
'nongovtserv5',
'nongovtserv5_uniquectznpm',
'nongovtserv5_revenuepm', 'state']]


######################################################
#### get all services under one column################
######################################################

top_services = csc_means[['govtserv1',
'govtserv1_nformspm',
'govtserv1_uniquectznpm',
'govtserv1_revenuepm',
'govtserv2',
'govtserv2_nformspm',
'govtserv2_uniquectznpm',
'gotserv2_revenuepm',
'govtserv3',
'govtserv3_nformspm',
'govtserv3_uniquectznpm',
'govtserv3_revenuepm',
'govtserv4',
'govtserv4_nformspm',
'govtserv4_uniquectznpm',
'govtserv4_revenuepm',
'govtserv5',
'govtserv5_nformspm',
'govtserv5_uniquectznpm',
'govtserv5_revenuepm',
'nongovtserv1',
'nongovtserv1_uniquectznpm',
'nongovtserv1_revenuepm',
'nongovtserv2',
'nongovtserv2_uniquectznpm',
'nongovtserv2_revenuepm',
'nongovtserv3',
'nongovtserv3_uniquectznpm',
'nongovtserv3_revenuepm',
'nongovtserv4',
'nongovtserv4_uniquectznpm',
'nongovtserv4_revenuepm',
'nongovtserv5',
'nongovtserv5_uniquectznpm',
'nongovtserv5_revenuepm', 'state']]


top_services.groupby(['state','govtserv1']).sum()
top_services.to_csv('top_services.csv')


govt1 = pd.melt(top_services, id_vars = ['state','govtserv1'], value_vars=['nongovtserv1_revenuepm'], value_name = 'revenue_pm' )
govt2 = pd.melt(top_services, id_vars = ['state','govtserv2'], value_vars=['nongovtserv2_revenuepm'], value_name = 'revenue_pm' )
govt3 = pd.melt(top_services, id_vars = ['state','govtserv3'], value_vars=['nongovtserv3_revenuepm'], value_name = 'revenue_pm' )
govt4 = pd.melt(top_services, id_vars = ['state','govtserv4'], value_vars=['nongovtserv4_revenuepm'], value_name = 'revenue_pm' )
govt5 = pd.melt(top_services, id_vars = ['state','govtserv5'], value_vars=['nongovtserv5_revenuepm'], value_name = 'revenue_pm' )


govt1.columns = ['state','govtserv','variable','revenue_pct']
govt2.columns = ['state','govtserv','variable','revenue_pct']
govt3.columns = ['state','govtserv','variable','revenue_pct']
govt4.columns = ['state','govtserv','variable','revenue_pct']
govt5.columns = ['state','govtserv','variable','revenue_pct']


govt = govt1.append(govt2)
govt = govt.append(govt3)
govt = govt.append(govt4)
govt = govt.append(govt5)

govt = govt.reset_index()

cards = govt.groupby(['state','govtserv'])['revenue_pct'].count()

print(cards)

#######################################
#### data corrections in master dataset####
########################################


Adhar = ["Aadhar Card",
"Adhar",
"Aadar",
"Adhar",
"Aadhar Card",
"Adhar",
"Aadhar Card",
"Aadhar Verification",
"Aadharcard print",
"Adhar",
"Adhar, sevasindu",
"Aadhar Card",
"Aadhar Card (cirrection",
"Aadhar printing",
"Adaracard",
"Adhar",
"Aadhar Card",
"Adhar",
"Adhar print",
"Adhar printing",
"Aadhaar",
"Aadhaar Card",
"Aadhar Card",
"Aadhar Card attachment and Correction",
"AadharCard",
"Adhar",
"Adhar attachments"]

govt.govtserv.replace(Adhar,'Adhar',inplace = True)


birthc= ["Birth  certificate",
"Birth certi",
"Birth certif",
"Birth certifi",
"Birth certifi.",
"Birth certificate",
"Birth certificet"]

govt.govtserv.replace(birthc,'Birth Certificate',inplace = True)

panc = ["Pan Card",
"Pan Card",
"Pan Card",
"Pam card",
"Pan Card",
"Pen card",
"Pan Card",
"Pancrd",
"pancrd",
"pancsrd",
"Pancard",
"PN card",
"Pan Card",
"Only Pan Card service provided",
"Pan Card",
"Pan Card,",
"Pan Card"]

govt.govtserv.replace(panc,'Pan Card',inplace = True)


pmg = ["PMG Disha",
"PMGDSA",
"PMG disha",
"Pmg disha",
"Pradhan mantri gramin digital sak",
"P m g",
"P.m.g disha",
"P.m.g disha",
"Pmg",
"Pmg disha",
"PMG Disa",
"PM DIsha",
"Pmgdisah"]

govt.govtserv.replace(pmg,'PMG Disha',inplace = True)

passport = ["Assport",
"Passport",
"Pass port",
"Passport",
"Passport",
"Passport",
"Pass port",
"Passport",
"passport"]

govt.govtserv.replace(passport,'Passport',inplace = True)

castc = ["Caste certificate",
"Caste",
"Caste Certificate",
"Caste certificate",
"Caste certificate",
"Caste",
"Caste and income",
"Caste certificate",
"Caste",
"Caste Certificate"]

digipay = ["Digi Pay",
"Digi pay",
"Digi pay",
"Digi Pay",
"Digi pay",
"DGPay",
"Digi Pay"]

elecbill = ["E bill",
"Light  bill",
"Light bil",
"Light bill",
"Light bll",
"Electricity bill",
"Electricity bill",
"Electric bill payment",
"Electricity bill",
"Electricity bill",
"Bijali bil",
"Electricity Bill",
"Light bill",
"light bill",
"E bill",
"Electricity bill",
"Electricity bills"]


dindayal = ["Pandit Din Dayal",
"Pandit Din Dayal Grahak Bhandar",
"Pandit din dayal grahak bhandar",
"Pandit din dyal grahak bhandar"]

lifec  = ["Life",
"Life cerificate",
"Life certificate",
"Life certyficate",
"Living certificate",
"Lifecertifcate",
"P, live certificate"]

incomec = ["Income cert",
"Income certificate",
"Income certificate",
"Income certificata",
"Income certificate"]

insurance = ["Incurence",
"Inshuraince",
"Inshurance",
"Insurance",
"Insurance",
"insurance",
"Insurance",
"Life incurence",
"Lic",
"Insurence"]

rationc = ["Rashan card",
"Rashtion card"]

mobrecharge = ["mobile & DTH Recharge",
"mobile & DTH recharge",
"mobile & DTH rechrrge",
"Mobil & DTH Recharge",
"Mobile & DTH Recharge"]


xzeros = []


govt.govtserv.replace(castc,'Caste Certificate',inplace = True)
govt.govtserv.replace(digipay,'Digipay',inplace = True)
govt.govtserv.replace(elecbill,'Electricity Bill',inplace = True)
govt.govtserv.replace(dindayal,'Pandit Din Dayal Bhandar',inplace = True)
govt.govtserv.replace(lifec,'Life Certificate',inplace = True)
govt.govtserv.replace(incomec,'Income Certificate',inplace = True)
govt.govtserv.replace(insurance,'Insurance',inplace = True)
govt.govtserv.replace(rationc,'Ration Card',inplace = True)
govt.govtserv.replace(mobrecharge,'Mobile & DTH Recharge',inplace = True)




cards = govt.groupby(['state','govtserv'])['revenue_pct'].count()
print(cards)



#### regressions

cscreg = csc_means[['earningspermonth',
                   'vle_age','income_agrilabourer','income_farmer',
                   'nchildren','hrsatcsc','emp_fulltime_paid',
                   'emp_parttime_paid','fam_fulltime',
                   'fam_parttime',
                   'sal_emp',
                   'trainhrs_emp', 'trainhrs_vle', 'investmentamt',
                   'n_opendays','villages_covered','floor_area','elec_nhours',
                   'computers','biometricscanner','invertor', 'digicam_webcam',
                   'distance_town' ,'distance_postoffice', 'distance_districthq',
                   'distance_bank', 'distance_nextcsc','rentamt', 'electricity_pm',
                   'internet_phone_pm', 'interest_expense_pm', 'salaries_expense_pm',
                   'training_pm', 'otherexpense_pm',
                   'skilldevprog_villagersattended', 'Itdowntime_hrsperday',
                   'Itdowntime_daysperweek', 'familysize','familysize_adults',
                   'familysize_children' ,'family_earningmembers', 'internet_usage_hrs',
                   'smartphone_yn'
                   ]]

cscreg['smartphone_yn'] = cscreg['smartphone_yn'].astype('category')

###################### without missing fill #############
cscreg.to_csv('cscreg.csv')
#########################################################


## missing value subs##

##means

cscreg[['earningspermonth','income_agrilabourer','income_farmer','hrsatcsc','investmentamt',
        'n_opendays','villages_covered',
 'floor_area',
 'elec_nhours','distance_town',
 'distance_postoffice',
 'distance_districthq',
 'distance_bank',
 'distance_nextcsc', 'Itdowntime_hrsperday',
 'Itdowntime_daysperweek', 'internet_usage_hrs',]].fillna

        


##zeros



cscreg[['nchildren','emp_fulltime_paid','emp_parttime_paid','fam_fulltime','fam_parttime',
        'sal_emp','trainhrs_emp',
        'trainhrs_vle','computers',
        'biometricscanner','invertor','digicam_webcam','rentamt','electricity_pm',
        'internet_phone_pm',
        'interest_expense_pm',
        'salaries_expense_pm','training_pm',
        'otherexpense_pm']].fillna(0,inplace = True)

cscmeans4 = cscmeans3[['nchildren','emp_fulltime_paid','emp_parttime_paid','fam_fulltime','fam_parttime',
        'sal_emp','trainhrs_emp',
        'trainhrs_vle','computers',
        'biometricscanner','invertor','digicam_webcam','rentamt','electricity_pm',
        'internet_phone_pm',
        'interest_expense_pm',
        'salaries_expense_pm','training_pm',
        'otherexpense_pm']].fillna(0)

###not substituted

#'skilldevprog_villagersattended',

# 'familysize',
# 'familysize_adults',
# 'familysize_children',
# 'family_earningmembers',

# 'smartphone_yn'

#### capping###
cscreg.loc[cscreg['emp_fulltime_paid'] > 10, 'emp_fulltime_paid'] = 1
cscreg.loc[cscreg['emp_parttime_paid'] > 10, 'emp_parttime_paid'] = 1
cscreg.loc[cscreg['fam_fulltime'] > 10, 'fam_fulltime'] = 1
cscreg.loc[cscreg['fam_parttime'] > 10, 'fam_parttime'] = 1
#cscreg.loc[cscreg['emp_others'] > 10, 'emp_others'] = 1
#cscreg.loc[cscreg['Itdowntime_hrsperday'] > 24, 'Itdowntime_hrsperday'] = cscreg['Itdowntime_hrsperday'].mean()
#cscreg.loc[cscreg['internet_usage_hrs'] > 24, 'internet_usage_hrs'] = cscreg['internet_usage_hrs'].mean()
cscreg.loc[cscreg['investmentamt'] <0, 'investmentamt'] =0 ## na = mean? 0?

#cscreg.loc[cscreg['investmentamt'] >7000000, 'investmentamt'].apply(lambda x: x/10) ## na = mean? 0?

cscreg['investmentamt']=cscreg['investmentamt'].apply(lambda x: x if x<= 700000 else x/10)

################# export reg data ##################
cscreg.to_csv('cscreg2.csv')
####################################################

################plots################################

plt.hist(cscreg['investmentamt'], bins = 100)
plt.hist(cscreg['trainhrs_vle'], bins = 50)
cscreg.trainhrs_vle.describe()


#####################################################


import statsmodels.api as sm
import statsmodels.formula.api as smf

cscinc = smf.ols('earningspermonth ~ vle_age + income_agrilabourer+ income_farmer +nchildren + hrsatcsc + emp_fulltime_paid+ fam_fulltime+fam_parttime + investmentamt+ familysize+ internet_usage_hrs+ smartphone_yn + trainhrs_vle', data = cscreg).fit()

print(cscinc.summary())



#type(top_services.govtserv1.value_counts()) + top_services.govtserv2.value_counts()

#zip(top_services.govtserv1.value_counts(), top_services.govtserv2.value_counts())



########################################################################
############################## citizens ##########################################

citizen_master = pd.read_excel('CSC Impact Assessment Survey Data Citizen Jan 29.xlsx')

cit_anal = citizen_master[['What is the main reason you use the CSC / Jan Seva Kendra / Mee Sewa?  GET TOP 5 REASONS text',
                           'What new services (government or private) do you believe must be added to CSC?  GET UPTO 5',
                           'Number of trips you made in the last one year to any Government Offices; (ALL Govt Offices, Total Number of Trips)',
                           "Number of trips you made in the last one year to CSC's;   (Total Number of Trips)",
                           'What is the average distance (in Kms) you travel for each transaction - Government Office  (Any Govt Office, Average)',
                           'What is the average distance (in Kms) you travel for each transaction - CSC  (Any CSC, Average)',
                           'What is the average time taken (in Minutes) for each trip to Government Office (Any Govt Office, Average time for travel)', 
                           'What is the average time taken (in Minutes) for each trip to CSC (Any CSC, Average time for travel)',
                           'What is the average cost (in Rupees) for each trip to Government Office (Any Govt Office, Average time for travel)',	
                           'What is the average cost (in Rupees) for each trip to CSC (Any CSC, Average time for travel)',
                           'What is the usual waiting time (in Minutes) for each transaction at Government office  (Any Govt Office, Average time you have to wait)',
                           'What is the usual waiting time (in Minutes) for each transaction at CSC (Any CSC, Average time you have to wait)',
                           'What is the average number of intermediaries/counters you had to go through to successfully complete each transaction at Govt office',
                           'What is the average number of intermediaries/counters you had to go through to successfully complete each transaction at CSC',
                           'What was the average wage loss (in rupees) for each transaction attempted at Government office',
                           'What was the average wage loss (in rupees) for each transaction attempted at CSC',
                           'Out of 10 works that you needed to get done, how many would be delayed at Government Office?  (By Delay, I mean, it took more time than it should have taken)',
                           'Out of 10 works that you needed to get done, how many would be delayed at CSC?  (By Delay, I mean, it took more time than it should have taken)',	
                           'Out of 10 works that you needed to get done, how many would be denied at Govt Office?  ',
                           'Out of 10 works that you needed to get done, how many would be denied at CSC?  ']]

cit_anal.columns = ['reasons_usingcsc','new_services_wanted',
                    'trips_govtoffice_1yr','trips_csc_1yr',
'distance_govtoffice',
'distance_csc',
'traveltime_govtoffice',
'traveltime_csc',
'costoftrip_govtoffice',
'costoftrip_csc',
'waitingtime_govtoffice',
'waitingtime_csc',
'intermediaries_govtoffice',
'intermediaries_csc',
'wageloss_govtoffice',
'wageloss_csc',
'ndelaysoutof10_govtoffice',
'ndelaysoutof10_csc',
'ndeniedoutof10_govtoffice',
'ndeniedoutof10_csc',]

cit_anal.replace(999,np.nan, inplace = True)

cit_anal[['prod_1','prod_2','prod_3','prod_4','prod_5']] = cit_anal['reasons_usingcsc'].str.split(",", expand = True)
cit_anal[['need_1','need_2','need_3','need_4','need_5']] = cit_anal['new_services_wanted'].str.split(",", expand = True)


cit_means = cit_anal[['trips_govtoffice_1yr','trips_csc_1yr',
'distance_govtoffice',
'distance_csc',
'traveltime_govtoffice',
'traveltime_csc',
'costoftrip_govtoffice',
'costoftrip_csc',
'waitingtime_govtoffice',
'waitingtime_csc',
'intermediaries_govtoffice',
'intermediaries_csc',
'wageloss_govtoffice',
'wageloss_csc',
'ndelaysoutof10_govtoffice',
'ndelaysoutof10_csc',
'ndeniedoutof10_govtoffice',
'ndeniedoutof10_csc']]

cit_means.replace(3000,np.nan, inplace = True)
cit_means.intermediaries_govtoffice.replace(1300,np.nan, inplace= True)
cit_means.intermediaries_csc.replace(500,np.nan, inplace= True)



cit_means.mean()

############## citizens misc graphs#######

citizens_products = cit_anal[['prod_1','prod_2','prod_3','prod_4','prod_5','need_1','need_2','need_3','need_4','need_5']]

p1 = citizens_products.prod_1
p = p1.append(citizens_products.prod_2)
p = p.append(citizens_products.prod_3)
p = p.append(citizens_products.prod_4)
p = p.append(citizens_products.prod_5)

p.value_counts()
count()


cprod1 = pd.melt(citizens_products, id_vars = ['state','prod_1'], value_vars=['nongovtserv1_revenuepm'], value_name = 'revenue_pm' )
cprod2 = pd.melt(citizens_products, id_vars = ['state','prod_2'], value_vars=['nongovtserv2_revenuepm'], value_name = 'revenue_pm' )
cprod3 = pd.melt(citizens_products, id_vars = ['state','prod_3'], value_vars=['nongovtserv3_revenuepm'], value_name = 'revenue_pm' )
cprod4 = pd.melt(citizens_products, id_vars = ['state','prod_4'], value_vars=['nongovtserv4_revenuepm'], value_name = 'revenue_pm' )
cprod5 = pd.melt(citizens_products, id_vars = ['state','prod_5'], value_vars=['nongovtserv5_revenuepm'], value_name = 'revenue_pm' )


govt1.columns = ['state','govtserv','variable','revenue_pct']
govt2.columns = ['state','govtserv','variable','revenue_pct']
govt3.columns = ['state','govtserv','variable','revenue_pct']
govt4.columns = ['state','govtserv','variable','revenue_pct']
govt5.columns = ['state','govtserv','variable','revenue_pct']


govt = govt1.append(govt2)
govt = govt.append(govt3)
govt = govt.append(govt4)
govt = govt.append(govt5)

govt = govt.reset_index()

govt.groupby(['state','govtserv'])['revenue_pct'].count()







####################################old code###########################


csc_new = csc_master[['State','District','GPS Location', ## location
                      'Name of VLE','VLE ID','Name of CSC','Name of VLE','VLE ID', ##ID
                      'Gender (DO NOT ASK)',	'Your age please? (COMPLETED YEARS)', ,'How many children?', 'Are you;', ##demographics

'When did you start this CSC centre?   MM / YYYY' #(time since operation)

## income benchmarks
'How much does an average agri labourer in this village earn PER DAY?',
'How much does an average farmer in this village earn PER MONTH?',
'How many hours do you spend per day at CSC? 	Normal Day, Average number of hours?',
"On an average, how much do you top-up for CSC services? 	Rs. ____ / per week"

## employees
'How many PAID FULL TIME Employees are there in the CSC?  I mean who work here for more than 6 hours per day',
'How many PAID PART TIME Employees are there in the CSC?',
'How many FULL TIME FAMILY MEMBER are there in the CSC?',
'How many PART TIME FAMILY MEMBER are there in the CSC?',
#'Other workers',
'How much do you pay to the employee on an average?',
'What is the total duration of training they received?  Example: 2 Hours, 4 Hours, 10 Hours, 20 Hour etc',
'What is the total duration of training you received?  Example: 2 Hours, 4 Hours, 10 Hours, 20 Hour etc',
'How much funds did you invest for setting up the CSC?',
'% of total setup costs - From Own Savings',
'% of total setup costs - From Chits/Credit Card',
'% of total setup costs - Loan from Family Members / Friends',
'% of total setup costs - From Money Lender',
'% of total setup costs - Loans from Co-op society/ Banks/ Financial Institutions',
'% of total setup costs - From Other Source',
'What is the interest rate?',
'What was your total earnings from providing CSC services during the last month?',
'What was your average monthly income before setting up the CSC? Income from all sources',
'Annual income from CSC - Govt Services',
'Annual income from CSC - Non-Govt Services',
'Annual income from Other Business',
'Annual income from Rent / Lease',
'Annual income from Farm / Agriculture',
'Annual income from Deposit / Interest / Dividend',
'Annual income from Salary / Pension',
'Annual income from Other Source',
'Apart from signing agreement with CSC e-Governance Services, how many additional permissions, licenses, approvals, authorizations, etc., did you have to take from ________ to start the CSC?',
'For how many days a week is the CSC open?',
'What time do you usually OPEN?',
'What time do you usually CLOSE?',
'For how many days in a year (approx.) is the CSC closed due to unexpected reasons?',
'Number of villages covered by CSC (including the village in which CSC is located)',
'CSC Floor Area  (in SFT....Approximate will do)',
'On a normal day, how many hours do you have electricity (from the board/government)',
'What is the Time taken to download a movie (in mins)',
'Number of COMPUTERS available and working condition at CSC;',
'Number of PRINTERS available and working condition at CSC;',
'Number of PRINTER cum SCANNER available and working condition at CSC;',
'Number of PRINTER, SCANNER, COPIER available and working condition at CSC;',
'Number of COPY / XEROX machines available and working condition at CSC;',
'Number of BIOMETRIC /IRIS Scanner available and working condition at CSC;',
'Number of INVERTOR / UPS available and working condition at CSC;',
'Number of DIGITAL CAMERA/WEB CAM available and working condition at CSC;',
'Number of LAMINATION MACHINE available and working condition at CSC;',
'Number of any other equipment available and working condition at CSC;',
'Distance of CSC from the NEAREST TOWN (in kms);',
'Distance of CSC from the NEAREST POST OFFICE (in kms);',
'Distance of CSC from the NEAREST DISTRICT HEADQUARTERS (in kms);',
'Distance of CSC from the NEAREST BANK (in kms);',
'Distance of CSC from the NEAREST CSC (in kms);',
'Rent per Month;',
'Electricity per Month;',
'Phone & Internet per Month;',
'Debt / Loan, Interest etc',
'Employee Salaries;',
'Training expenses;',
'Other expenses (above) per Month;',
'Of all the Government services you provide, which ONE is the most utilized?',
'What is the average number of forms/applications processed per month?',
'What is the average number of unique citizens served per month?',
'How much does it contribute to your CSC business / revenue?   (In % of total)',
'Of all the Government services you provide, which ONE is the next most utilized?',
'What is the average number of forms/applications processed per month?',
'What is the average number of unique citizens served per month?',
'How much does it contribute to your CSC business / revenue?   (In % of total)',
'Of all the Government services you provide, which ONE is the next most utilized?',
'What is the average number of forms/applications processed per month?',
'What is the average number of unique citizens served per month?',
'How much does it contribute to your CSC business / revenue?   (In % of total)',
'Of all the Government services you provide, which ONE is the next most utilized?',
'What is the average number of forms/applications processed per month?',
'What is the average number of unique citizens served per month?',
'How much does it contribute to your CSC business / revenue?   (In % of total)',
'Of all the Government services you provide, which ONE is the most utilized?',
'What is the average number of forms/applications processed per month?',
'What is the average number of unique citizens served per month?',
'How much does it contribute to your CSC business / revenue?   (In % of total)',
'Of all the Non - Government services you provide, which ONE is the most utilized?',
'What is the average number of unique citizens served per month?',
'How much does it contribute to your CSC business / revenue?   (In % of total)',
'Of all the Non - Government services you provide, which ONE is the next most utilized?',
'What is the average number of unique citizens served per month?',
'How much does it contribute to your CSC business / revenue?   (In % of total)',
'Of all the Non - Government services you provide, which ONE is the next most utilized?',
'What is the average number of unique citizens served per month?',
'How much does it contribute to your CSC business / revenue?   (In % of total)',
'Of all the Non - Government services you provide, which ONE is the next most utilized?',
'What is the average number of unique citizens served per month?',
'How much does it contribute to your CSC business / revenue?   (In % of total)',
'Of all the Non - Government services you provide, which ONE is the next most utilized?',
'What is the average number of unique citizens served per month?',
'How much does it contribute to your CSC business / revenue?   (In % of total)',
'What is the total number of villagers who have attended the skill development training programs in the last 12 months?',
'On average what is the downtime (not working) of the CSC backend/ IT system?   ____ hours/ day',
'On average what is the downtime (not working) of the CSC backend/ IT system?   days / Week',
'In total, how many members are there in your family?  (Staying with you / Single kitchen)',
'How many adults?',
'How many children?',
'How many are earning members? Working, Salary, Agriculture, Labour, Business etc.',
'How long do you use the internet at home? Number of hours / week',
'Do you use a Smart Phone?',
#'Name of CSC',
#'Name of VLE',
#'State (CSC Location)',
#csc_means = pd.read_excel('CSC_survey_14Jan_2_means.xlsx')
### count ###
'How often is the CSC open?',
'How long did it take to set up the CSC after formally putting an online application?',
'Were you trained on CSC operations?',
'Local political leadership',
'District administration / Revenue officials',
'Village panchayat',
'Police department',
'Electricity department',
'Telephone dept./ Agency',
'Internet Service Provider',
'Other service provider',
'Do you have to work during mid-night / early morning due to power availability?  Explain: Mid-night/ early morning or other unusual hours due to power being available only at that time?',
'Do you allow customers to access/ use computers by themselves?',
'Are the computers used for education/ training services?',
'Are computers used for job search?',
'Are computers used for consulting a doctor?',
'Number of local skill development trainings provided by the CSC in the last 12 months? Like vocational trainings, distant learning courses, spoken English courses, interviewing, personality development etc',
'Would you like to continue with the CSC business in the future?',
#'Is the CSC location easily accessible?',
#'Is the region/ area where CSC is located generally affected by Left- Wing Extremism?',
#'Is CSC an existing cyber café or other shop which was converted into a CSC?',



'Who was the main influencer in your decision to start a CSC?  TICK ALL THAT APPLY' ## influence network
'Which of the following services do you provide here?',	'Of the many services you provide at the CSC, which ONE is the most utilized by the public? CAN BE ANY SERVICE, G2C, B2C  Next?','Second most used service?',	'Next? Third',	'Next? Fourth',	'Next? Fifth',
'Of the many services you provide using the State Digital Service (MENTION RELEVANT NAME), which ONE is the most utilized by the public? CAN BE ANY SERVICE, G2C, B2C  Next?',	'Second most used State Digital Service?','Next? Third',	'Next? Fourth',	'Next? Fifth'



]]



csc_new.columns = ['csc_name',
'vle_name',
'vle_id',
'vle_age',
'income_agrilabourer',
'income_farmer',
'nchildren',
'hrsatcsc',
'emp_fulltime_paid',
'emp_parttime_paid',
'fam_fulltime',
'fam_parttime',
#'emp_others',
'sal_emp',
'trainhrs_emp',
'trainhrs_vle',
'investmentamt',
'investment_savings',
'investment_chitcc',
'investment_famfrnds',
'investment_moneylender',
'investment_banks',
'investment_other',
'intrate',
'earningspermonth',
'earnings_befcsc',
'income_govtservices',
'income_nongovservices',
'income_otherbus',
'income_rent',
'income_farm',
'income_interest',
'income_salarypension',
'income_oth',
'num_permissions',
'n_opendays',
'opentime',
'closetime',
'closedays',
'villages_covered',
'floor_area',
'elec_nhours',
'downloadtime_movie',
'computers',
'printers',
'scanner_printer',
'scanner_printer_copier',
'xerox',
'biometricscanner',
'invertor',
'digicam_webcam',
'lamination_machine',
'oth_equipment',
'distance_town',
'distance_postoffice',
'distance_districthq',
'distance_bank',
'distance_nextcsc',
'rentamt',
'electricity_pm',
'internet_phone_pm',
'interest_expense_pm',
'salaries_expense_pm',
'training_pm',
'otherexpense_pm',
'govtserv1',
'govtserv1_nformspm',
'govtserv1_uniquectznpm',
'govtserv1_revenuepm',
'govtserv2',
'govtserv2_nformspm',
'govtserv2_uniquectznpm',
'gotserv2_revenuepm',
'govtserv3',
'govtserv3_nformspm',
'govtserv3_uniquectznpm',
'govtserv3_revenuepm',
'govtserv4',
'govtserv4_nformspm',
'govtserv4_uniquectznpm',
'govtserv4_revenuepm',
'govtserv5',
'govtserv5_nformspm',
'govtserv5_uniquectznpm',
'govtserv5_revenuepm',
'nongovtserv1',
'nongovtserv1_uniquectznpm',
'nongovtserv1_revenuepm',
'nongovtserv2',
'nongovtserv2_uniquectznpm',
'nongovtserv2_revenuepm',
'nongovtserv3',
'nongovtserv3_uniquectznpm',
'nongovtserv3_revenuepm',
'nongovtserv4',
'nongovtserv4_uniquectznpm',
'nongovtserv4_revenuepm',
'nongovtserv5',
'nongovtserv5_uniquectznpm',
'nongovtserv5_revenuepm',
'skilldevprog_villagersattended',
'Itdowntime_hrsperday',
'Itdowntime_daysperweek',
'familysize',
'familysize_adults',
'familysize_children',
'family_earningmembers',
'internet_usage_hrs',
'smartphone_yn',
#'csc_name2',
#'vle_name2',
'gender',
'maritalstatus',
'csc_open_howoften',
'timeto_setup',
'trained_yn',
'npermissions_political_leadership',
'npermissions_distr_admin',
'npermisions_panchayat',
'npermissions_police',
'npermissions_electric',
'npermissions_phone',
'npermissions_internet',
'npermissions_others',
'odd_working_hrs_dueto_pwr',
'customers_allwd_to_use_comps',
'comps_usedfor_train_edu_servs',
'comps_usedfor_job_search',
'comps_usedfor_docs',
'nskilltrainings_l12m',
'continue_w_csc_yn',
#'location_visible',
#'leftwing_extremism',
#'csc_convertedfrm_cybercafe',
'state']


csc_new.to_csv('csvnew.csv')




###############################################################################
########################old code/ old data ############# not needed ############



csc_surv = pd.read_excel('CSC_survey_14Jan.xlsx')
csc_col_old = pd.DataFrame(csc_surv.columns)
csc_surv.shape


cscdf = csc_surv[['GPS Location','Date and Time', 'Date and Time.1',
                  'Name of CSC','VLE ID','Name of respondent','What is your age? (Completed years)',
                  'How much does an average agri labourer in this village earn per day?',
                  'How much does an average farmer in this village earn per month?',
                  'How many children do you have?', 'Of the many services you provide at the CSC, which ONE is the most utilized by the public? EXPLAIN - CAN BE ANY SERVICE, G2C, B2C',
                  'SECOND most utilized by the public?','Next?','Next?.1','Next?.2',
                  'How many hours do you spend per day at CSC? 	Normal Day, Average number of hours?',
                  'How many PAID FULL TIME Employees are there in the CSC?  I mean who work here for more than 6 hours per day',
                  'How many PAID PART TIME Employees are there in the CSC?',
                  'How many FULL TIME FAMILY MEMBER are there in the CSC?',
                  'How many PART TIME FAMILY MEMBER are there in the CSC?',
                  'Other workers','How much do you pay to the employee on an average?',
                  'Please pick the family members who support you, the VLE, in running the CSC;',
                  'Were your employees trained on CSC operations?',
                  'What is the total duration of training they received?  Example: 2 Hours, 4 Hours, 10 Hours, 20 Hour etc',
                  'Were you trained on CSC operations?',
                  'What is the total duration of training you received?  Example: 2 Hours, 4 Hours, 10 Hours, 20 Hour etc',
                  'How much funds did you invest for setting up the CSC?',
                  '% of total setup costs - From Own Savings',
                  '% of total setup costs - From Chits/Credit Card',
                  '% of total setup costs - Loan from Family Members / Friends',
                  '% of total setup costs - From Money Lender',
                  '% of total setup costs - Loans from Co-op society/ Banks/ Financial Institutions',
                  '% of total setup costs - From Other Source',
                  'What is the interest rate?',
                  'What was your total earnings from providing CSC services during the last month?',
                  'What was your average monthly income before setting up the CSC? Income from all sources',
#                  'Annual income from CSC - Govt Services',
#                  'Annual income from CSC - Non-Govt Services',
#                  'Annual income from Other Business',
#                  'Annual income from Rent / Lease',
#                  'Annual income from Deposit / Interest / Dividend',
#                  'Annual income from Salary / Pension',
#                  'Annual income from Other Source',
                  'For how many days a week is the CSC open?',
                  'What time do you usually OPEN?',
                  'What time do you usually CLOSE?'
                  ]]

cscdf.columns = ['gps_loc','timestamp','date','csc_name','vle_id','name_resp',
                 'age','wage_lab_pd','income_farmer_pm','nchild','no_1_serv',
                 'no_2_serv','no_3_serv','no_4_serv','no_5_serv','hrs_at_csc',
                 'fulltime_emp','parttime_emp','fulltime_family','part_family','other_emp',
                 'avg_emp_pay','supporting_family_list','emp_training_yn','emp_training_hrs',
                 'vle_training_yn','vle_training_hrs', 'investment_total',
                 'inv_ownsavings','inv_chit_cc','inv_fam_frnds','inv_moneylender', 
                 'inv_bank_coop','inv_others','int_rate','csc_earnings_lmth','vle_previnc_total',
                 'cscopendays_perweek','open_time','close_time']


cscdf.to_pickle('csc_data.pkl')
cscdf= pd.read_pickle('csc_data.pkl')

cscdf['age'].max()
cscdf['age'].value_counts()
cscdf['no_1_serv'].value_counts()

cscnew_col = pd.DataFrame(cscdf.columns)

#################### plots######################

cscdf['age'].plot(kind ='hist')
plt.show()

cscdf['wage_lab_pd'].plot(kind = 'hist')
cscdf['income_farmer_pm'].plot(kind = 'hist')
cscdf['nchild'].plot(kind = 'hist')
cscdf['no_1_serv'].value_counts().plot()
cscdf['no_2_serv'].value_counts().plot()
cscdf['hrs_at_csc'].plot(kind = 'hist')

cscdf['fulltime_emp'].hist() # error
cscdf['parttime_emp'].hist() #### error
cscdf[['fulltime_emp','parttime_emp','fulltime_family','part_family','other_emp']].hist()

cscdf['avg_emp_pay'].hist()

cscdf[['emp_training_hrs','vle_training_hrs']].hist()

cscdf[['vle_training_yn','emp_training_yn']].value_counts().hist()### separate both

cscdf[['investment_total']].plot()

cscdf[['inv_ownsavings','inv_chit_cc','inv_fam_frnds','inv_moneylender','inv_bank_coop','inv_others']].mean().plot() ### fill 0 for NaNs and plot again

cscdf['int_rate'].hist() 
cscdf[['csc_earnings_lmth']].plot()

cscdf['vle_previnc_total'].value_counts().plot()

cscdf['cscopendays_perweek'].hist()

####(cscdf['open_time'] - cscdf['close_time']).plot()


csc_surv.columns =[]

print(csc_surv.columns)
print(csc_col_old)
csc_surv.plot()

#############################old code for reference ################################

govt.govtserv.replace('Pan card','Pancard', inplace =True )
govt.govtserv.replace('PAN CARD','Pancard', inplace =True )
govt.govtserv.replace('Pan','Pancard', inplace =True )
govt.govtserv.replace('pancard','Pancard', inplace =True )
govt.govtserv.replace('Pancard,','Pancard', inplace =True )



### adhar card
govt.govtserv.replace('Aadhar','Adhar', inplace =True )
govt.govtserv.replace('Adhar card','Adhar', inplace =True )
govt.govtserv.replace('aadhar card','Adhar', inplace =True )
govt.govtserv.replace('Adharcard','Adhar', inplace =True )
govt.govtserv.replace('Adhar correction,','Adhar', inplace =True )



#### seva sindu###
govt.govtserv.replace('Seva sindu','Sevasindu', inplace =True )
govt.govtserv.replace('Seva sindhu','Sevasindu', inplace =True )


### caste and income certificate
govt.govtserv.replace('Coste and income','Caste and income', inplace =True )
govt.govtserv.replace('Caste income','Caste and income', inplace =True )
govt.govtserv.replace('Caste amd income','Caste and income', inplace =True )


### life certificate##
govt.govtserv.replace('Life certiifcate','Life Certificate', inplace =True )
govt.govtserv.replace('Life certiifcate','Life Certificate', inplace =True )

## electricity bill###
govt.govtserv.replace('Elec bill','Electricity bill', inplace =True )


## income certificate##
govt.govtserv.replace('Income','Income certificate', inplace =True )


govt.govtserv.value_counts()
govt.govtserv.value_counts()
govt.govtserv.replace('Pan card','Pancard', inplace =True )
govt.govtserv.replace('PAN CARD','Pancard', inplace =True )
govt.govtserv.replace('Pan','Pancard', inplace =True )

govt.govtserv.replace('Aadhar','Adhar', inplace =True )
govt.govtserv.replace('Aaadhar','Adhar', inplace =True )

govt.govtserv.replace('Seva sindu','Sevasindu', inplace =True )
govt.govtserv.replace('Seva sindhu','Sevasindu', inplace =True )

govt.govtserv.replace('Coste and income','Caste and income', inplace =True )
govt.govtserv.replace('Caste income','Caste and income', inplace =True )
govt.govtserv.replace('Caste amd income','Caste and income', inplace =True )
govt.govtserv.replace('Income and cast','Caste and income', inplace =True )


govt.govtserv.replace('Caste certifcate','Caste certificate', inplace =True )

govt.govtserv.replace('Income','Income certificate', inplace =True )
govt.govtserv.replace('Incomecertifcate','Income certificate', inplace =True )

govt.govtserv.replace('Life certifcate','Life Certificate', inplace =True )
govt.govtserv.replace('Life certiifcate','Life Certificate', inplace =True )

govt.govtserv.replace('Electricity','Electricity bill', inplace =True )



govt.govtserv.value_counts()
govt.govtserv.replace('Pan card','Pancard', inplace =True )
govt.govtserv.replace('PAN CARD','Pancard', inplace =True )
govt.govtserv.replace('Pan','Pancard', inplace =True )

govt.govtserv.replace('Aadhar','Adhar', inplace =True )
govt.govtserv.replace('Aaadhar','Adhar', inplace =True )

govt.govtserv.replace('Seva sindu','Sevasindu', inplace =True )
govt.govtserv.replace('Seva sindhu','Sevasindu', inplace =True )

govt.govtserv.replace('Coste and income','Caste and income', inplace =True )
govt.govtserv.replace('Caste income','Caste and income', inplace =True )
govt.govtserv.replace('Caste amd income','Caste and income', inplace =True )
govt.govtserv.replace('Income and cast','Caste and income', inplace =True )


govt.govtserv.replace('Caste certifcate','Caste certificate', inplace =True )
govt.govtserv.replace('Cast certificate','Caste certificate', inplace =True )


govt.govtserv.replace('Income','Income certificate', inplace =True )
govt.govtserv.replace('Incomecertifcate','Income certificate', inplace =True )

govt.govtserv.replace('Life certifcate','Life Certificate', inplace =True )
govt.govtserv.replace('Life certiifcate','Life Certificate', inplace =True )

govt.govtserv.replace('Electricity','Electricity bill', inplace =True )


govt.govtserv.value_counts()

govt.govtserv.replace('Pan card','Pancard', inplace =True )
govt.govtserv.replace('PAN CARD','Pancard', inplace =True )
govt.govtserv.replace('Pan','Pancard', inplace =True )

govt.govtserv.replace('Aadhar','Adhar', inplace =True )
govt.govtserv.replace('Aaadhar','Adhar', inplace =True )

govt.govtserv.replace('Seva sindu','Sevasindu', inplace =True )
govt.govtserv.replace('Seva sindhu','Sevasindu', inplace =True )

govt.govtserv.replace('Coste and income','Caste and income', inplace =True )
govt.govtserv.replace('Caste income','Caste and income', inplace =True )
govt.govtserv.replace('Caste amd income','Caste and income', inplace =True )
govt.govtserv.replace('Income and cast','Caste and income', inplace =True )


govt.govtserv.replace('Caste certifcate','Caste certificate', inplace =True )
govt.govtserv.replace('Cast certificate','Caste certificate', inplace =True )


govt.govtserv.replace('Income','Income certificate', inplace =True )
govt.govtserv.replace('Incomecertifcate','Income certificate', inplace =True )

govt.govtserv.replace('Life certifcate','Life Certificate', inplace =True )
govt.govtserv.replace('Life certiifcate','Life Certificate', inplace =True )

govt.govtserv.replace('Electricity','Electricity bill', inplace =True )



govt.govtserv.value_counts()
govt.govtserv.replace('Pan card','Pancard', inplace =True )
govt.govtserv.replace('PAN CARD','Pancard', inplace =True )
govt.govtserv.replace('Pan','Pancard', inplace =True )

govt.govtserv.replace('Aadhar','Adhar', inplace =True )
govt.govtserv.replace('Aaadhar','Adhar', inplace =True )

govt.govtserv.replace('Seva sindu','Sevasindu', inplace =True )
govt.govtserv.replace('Seva sindhu','Sevasindu', inplace =True )

govt.govtserv.replace('Coste and income','Caste and income', inplace =True )
govt.govtserv.replace('Caste income','Caste and income', inplace =True )
govt.govtserv.replace('Caste amd income','Caste and income', inplace =True )
govt.govtserv.replace('Income and cast','Caste and income', inplace =True )


govt.govtserv.replace('Caste certifcate','Caste certificate', inplace =True )
govt.govtserv.replace('Cast certificate','Caste certificate', inplace =True )


govt.govtserv.replace('Income','Income certificate', inplace =True )
govt.govtserv.replace('Incomecertifcate','Income certificate', inplace =True )
govt.govtserv.replace('Income certifcate','Income certificate', inplace =True )

govt.govtserv.replace('Life certifcate','Life Certificate', inplace =True )
govt.govtserv.replace('Life certiifcate','Life Certificate', inplace =True )


govt.govtserv.replace('Electricity','Electricity bill', inplace =True )
govt.govtserv.replace('Elec bill','Electricity bill', inplace =True )

govt.govtserv.replace('Incomecost','Caste and income', inplace =True )

govt.govtserv.replace('Dg pay','Digi pay', inplace =True )
govt.govtserv.replace('Electric bill','Electricity bill', inplace =True )
govt.govtserv.replace('Niwas','Niwas certificate', inplace =True )

govt.govtserv.replace('Olge age','Old age', inplace =True )
govt.govtserv.replace('Niwas','Niwas certificate', inplace =True )


###########missing capping ###################



cscreg['earningspermonth'].fillna(cscreg['earningspermonth'].mean(), inplace = True)
cscreg['income_agrilabourer'].fillna(cscreg['income_agrilabourer'].mean(), inplace = True)
cscreg['income_farmer'].fillna(cscreg['income_farmer'].mean(), inplace = True)
cscreg.nchildren.fillna(0, inplace = True)

cscreg.emp_fulltime_paid.fillna(0,inplace = True)
cscreg.emp_parttime_paid.fillna(0,inplace = True)
cscreg.fam_fulltime.fillna(0,inplace = True)
cscreg.fam_parttime.fillna(0,inplace = True)
#cscreg.emp_others.fillna(0,inplace = True)
cscreg.sal_emp.fillna(0,inplace = True) ## na = mean? 0?
cscreg.trainhrs_emp.fillna(0,inplace = True) ## na = mean? 0?
cscreg.trainhrs_vle.fillna(0,inplace = True) ## na = mean? 0?
cscreg.investmentamt.fillna(0,inplace = True) ## na = mean? 0?

cscreg['villages_covered'].fillna(cscreg['villages_covered'].mean(), inplace = True)
cscreg['floor_area'].fillna(cscreg['floor_area'].mean(), inplace = True)

cscreg.biometricscanner.fillna(0,inplace = True) ## na = mean? 0?
cscreg.invertor.fillna(0,inplace = True) ## na = mean? 0?
cscreg.digicam_webcam.fillna(0,inplace = True) ## na = mean? 0?

cscreg['distance_nextcsc'].fillna(cscreg['distance_nextcsc'].mean(), inplace = True)

cscreg['rentamt'].fillna(cscreg['rentamt'].mean(), inplace = True)
cscreg['interest_expense_pm'].fillna(cscreg['interest_expense_pm'].mean(), inplace = True)
cscreg.salaries_expense_pm.fillna(0,inplace = True) ## na = mean? 0?
cscreg.training_pm.fillna(0,inplace = True) ## na = mean? 0?
cscreg.otherexpense_pm.fillna(0,inplace = True) ## na = mean? 0?

cscreg.skilldevprog_villagersattended.fillna(0,inplace = True) 


cscreg.Itdowntime_hrsperday.fillna(0,inplace = True) ## na = mean? 0?
cscreg.familysize_children.fillna(0,inplace = True) 
cscreg.family_earningmembers.fillna(0,inplace = True) 

cscreg.internet_usage_hrs.fillna(cscreg.internet_usage_hrs.mean(),inplace = True) ## na = mean? 0?


