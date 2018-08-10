use "cscdata_11June.dta"
destring earnings_cscservices ,replace force

** destring **
destring statedig_topup_amt csc_topup_amt 


** earnings **
reg earnings_cscservices vle_age children hrs_perday_csc vle_training_dur investment_amt_cscsetup csc_opendays_perweek csc_area distance_csc_csc distance_csc_town distance_csc_distrhq csc_electricity_hrs csc_elecbill_mthly char_achvment_mot char_locus_control char_meta_cog char_self_efficacy 
outreg2 using "csc_13June.doc",append

** investment amount **
reg investment_amt_cscsetup vle_age children distance_csc_csc distance_csc_town distance_csc_distrhq csc_electricity_hrs char_achvment_mot char_locus_control char_meta_cog char_self_efficacy 
outreg2 using "csc_13June.doc",append

** time spent at csc **
reg hrs_perday_csc vle_age children distance_csc_csc distance_csc_town distance_csc_distrhq csc_electricity_hrs char_achvment_mot char_locus_control char_meta_cog char_self_efficacy 
reg hrs_perday_csc vle_age children distance_csc_csc distance_csc_town distance_csc_distrhq csc_electricity_hrs char_achvment_mot char_locus_control char_meta_cog char_self_efficacy paid_fulltime_emp paid_parttime_emp family_fulltime family_parttime emp_training_dur investment_amt_cscsetup internet_usage_home_hrspweek 
outreg2 using "csc_13June.doc",append

** Vle training duration **
reg vle_training_dur vle_age children investment_amt_cscsetup distance_csc_csc distance_csc_town distance_csc_distrhq csc_electricity_hrs char_achvment_mot char_locus_control char_meta_cog char_self_efficacy paid_fulltime_emp paid_parttime_emp family_fulltime family_parttime internet_usage_home_hrspweek emp_training_dur 
outreg2 using "csc_13June.doc",append

** Employee training duration **
reg emp_training_dur  vle_age children investment_amt_cscsetup distance_csc_csc distance_csc_town distance_csc_distrhq csc_electricity_hrs char_achvment_mot char_locus_control char_meta_cog char_self_efficacy family_fulltime family_parttime internet_usage_home_hrspweek  
outreg2 using "csc_13June.doc",append

** CSC open days per week **
reg csc_opendays_perweek  vle_age children investment_amt_cscsetup distance_csc_csc distance_csc_town distance_csc_distrhq csc_electricity_hrs char_achvment_mot char_locus_control char_meta_cog char_self_efficacy family_fulltime  familypartflag internet_usage_home_hrspweek empfullflag emppartflag 
outreg2 using "csc_13June.doc",append

** No. of funding sources **
reg no_fundsources  vle_age investment_amt_cscsetup distance_csc_csc distance_csc_town distance_csc_distrhq  char_achvment_mot char_locus_control char_meta_cog char_self_efficacy family_fulltime  familypartflag internet_usage_home_hrspweek nearningmembers  
outreg2 using "csc_13June.doc",append

** No. of income sources **
destring incomesource_self_Agriculture incomesource_self_CSCGovernment incomesource_self_CSCNonGovern incomesource_self_InterestDep incomesource_self_Other incomesource_self_OtherBusiness incomesource_self_RentLease incomesource_self_SalaryPension, replace force
egen nsources_income = rowtotal(incomesource_self_Agriculture incomesource_self_CSCGovernment incomesource_self_CSCNonGovern incomesource_self_InterestDep incomesource_self_Other incomesource_self_OtherBusiness incomesource_self_RentLease incomesource_self_SalaryPension)
reg nsources_income  vle_age investment_amt_cscsetup distance_csc_csc distance_csc_town distance_csc_distrhq  char_achvment_mot char_locus_control char_meta_cog char_self_efficacy family_fulltime  familypartflag internet_usage_home_hrspweek nearningmembers  

** number of employees **
egen total_emp = rowtotal( paid_fulltime_emp paid_parttime_emp family_fulltime family_parttime )

** employee flag**
egen total_emp = rowtotal( paid_fulltime_emp paid_parttime_emp family_fulltime family_parttime )
replace emp_yn =0 if total_emp == 0

** drop useless variables **
drop X1 new_col_names username blank1 start_survey blank2 mobile email blank3 timestamp2 blank4 blank5 blank6 blank7 blank8 blank9 blank10 photo_csc_interior photo_csc_exterior photo_csc_20m factors_betterbiz_  apps_used_ workingat_csc_NoneNoEmployees workingat_csc_Others familyfullflag familypartflag empfullflag emppartflag next_section_yn

** new variables gerry george **
gen graduate_flag = 1 if education == "Graduate"
*education 6 = Post Graduate
recode graduate_flag .= 1 if education == 6 
recode graduate_flag .=0
gen communitycredit_flag = 1 if chits_cc_pct >0 
gen commcredit_flag2 = 1 if loans_coopsbanks_pct >0
recode communitycredit_flag .=0
recode commcredit_flag2 .=0
gen priorbizexp_flag = 1 if occupation_beforecsc == "Businessman/ Self-Employed Professional"
gen future_outlook = 1 if csc_usage_future == "Pick Up / Grow"
recode priorbizexp_flag .=0

** rename vars **
rename csc_govtservice_freqperperson_to cscgovt_formsperperson1
rename csc_govtservice_freqperperson_to cscgovt_formsperperson1
rename csc_govtservice_revenuecontribut cscgovt_revenuecontri1
rename FD cscgovt_formsperperson2
rename FE cscgovt_revenuecontri2
rename FH cscgovt_formsperperson3
rename FI cscgovt_revenuecontri3
rename FL cscgovt_formsperperson4
rename FM cscgovt_revenuecontri4
rename FP cscgovt_formsperperson5
rename FQ cscgovt_revenuecontri5
rename csc_nongovtservice_uniquecitizen cscnongovt_uniquecitpm
rename cscnongovt_uniquecitpm cscnongovt_uniquecitpm1
rename csc_nongovtservice_revenuecontri cscnongovt_revcontripm1
rename FV cscnongovt_uniquecitpm2
rename FW cscnongovt_revcontripm2
rename FY cscnongovt_uniquecitpm3
rename FZ cscnongovt_revcontrip3
rename GB cscnongovt_uniquecitpm4
rename GC cscnongovt_revcontrip4
rename GE cscnongovt_uniquecitpm5
rename GF cscnongovt_revcontrip5
rename farmer_earnings_pd farmer_earnings_pm

** label vars **

label  var new_col_names New Column

label  var state "State"
label  var username "User Name"
label  var district "District"
label  var blank1 "Turn on the audio and read out the Respondent Information Form. Wait for respondent to agree and then start the survey"
label  var start_survey "Can we start the survey?"
label  var gps_location "GPS Location"
label  var time "Date and Time"
label  var date "Date and Time"
label  var csc_name "Name of CSC"
label  var vle_name "Name of VLE"
label  var vle_id "VLE ID"
label  var respondent_name "Name of respondent"
label  var blank2 "Can you please tell me your name and address please;"
label  var csc_startdate "When did you start this CSC centre?   MM / YYYY"
label  var influencer "Who was the main influencer in your decision to start a CSC?  TICK ALL THAT APPLY"
label  var gender "Gender (DO NOT ASK)"
label  var vle_age "Your age please? (COMPLETED YEARS)"
label  var mobile "Your mobile number please;  (CAREFUL)"
label  var email "Your email id please; (CAREFUL)"
label  var agri_labourer_earnings_pd "How much does an average agri labourer in this village earn PER DAY?"
label  var farmer_earnings_pm "How much does an average farmer in this village earn PER MONTH?"
label  var marital_status "Marital Status"
label  var children "How many children? (accurate one)"
label  var services_provided_types "Which of the following services do you provide here?"
label  var csc_service_top1 "Of the many services you provide at the CSC, which ONE is the most utilized by the public? CAN BE ANY SERVICE, G2C, B2C  Next?"
label  var csc_service_top2 "Second most used CSC service?"
label  var csc_service_top3 "Third most used CSC service?"
label  var csc_service_top4 "Fourth most used CSC service?"
label  var csc_service_top5 "Fifth most used CSC service?"
label  var csc_topup_amt "On an average, how much do you top-up for CSC services? 	Rs. ____ / per week"""
label  var statedig_service_top1 "Of the many services you provide using the State Digital Service (MENTION RELEVANT NAME), which ONE is the most utilized by the public? CAN BE ANY SERVICE, G2C, B2C  Next?"
label  var statedig_service_top2 "Second most used State Digital Service?"
label  var statedig_service_top3 "Third most used State Digital Service?"
label  var statedig_service_top4 "Fourth most used State Digital Service?"
label  var statedig_service_top5 "Fifth most used State Digital Service?"
label  var statedig_topup_amt "On an average, how much do you top-up for _____ (State Digital) services? 	Rs. ______ / per week"""
label  var directdig_service_top1 "Of the many digital services you provide using the Direct Service (Insurance, Recharge etc), which ONE is the most utilized by the public?"
label  var directdig_service_top2 "Second most used Direct Digital Service?"
label  var directdig_service_top3 "Third most used Direct Digital Service?"
label  var directdig_service_top4 "Fourth most used Direct Digital Service?"
label  var directdig_service_top5 "Fifth most used Direct Digital Service?"
label  var csc_open_freq "How often is the CSC open?"
label  var hrs_perday_csc "How many hours do you spend per day at CSC? 	Normal Day, Average number of hours?"""
label  var persons_workingat_csc "Please pick all the persons who work here at your CSC;"
label  var paid_fulltime_emp "Paid Full-time Employees (More than 6 Hours per day)"
label  var paid_parttime_emp "Paid Part-time Employees (Less than 6 Hours per day)"
label  var family_fulltime "Full-time Family Members"
label  var family_parttime "Part-time Family Members"
label  var other_workers "Other workers"
label  var avg_emp_pay "How much do you pay to the employee on average?"
label  var familyhelp_relationship "Family members' relationship with you;"
label  var employee_training_yn "Is your employee / Are the employees trained on CSC operations?"
label  var emp_training_location "Where was the training held?"
label  var emp_training_type "What was the nature of this training?"
label  var emp_training_dur "What is the total training duration you received? 	______ hours since start of CSC"""
label  var csc_setup_time_sinceapp "How long did it take to set up the CSC after formally putting an online application?"
label  var vle_training_yn "Were you trained on CSC operations?"
label  var vle_training_location "Where was the training held?"
label  var vle_training_type "What was the nature of this training?"
label  var vle_training_dur "What is the total training duration you received? 	______ hours since starting CSC"""
label  var person_at_csc_daytoday "Who sits at the CSC and operates it on a daily basis?"
label  var person_at_csc_other "Other - Please specify:"
label  var investment_amt_cscsetup "How much funds did you invest for setting up the CSC?"
label  var source_of_funds_investmentcapita "Source of funds for you for setting up CSC (Please tick all the options applicable and respective % of total setup costs) PICK ALL THAT APPLY"
label  var source_of_funds_other "Other sources (please specify)"
label  var own_savings_pct "Own savings  ________ %"
label  var chits_cc_pct "Chits/Credit Cards  _______%"
label  var loans_familyfrnds_pct "Loans from Family members/ Friends/ Relatives _____ %"
label  var loans_moneylender_pct "Loans from Money lender"
label  var loans_coopsbanks_pct "Loans from Co-op society/ Banks/ Financial Institutions ______%"
label  var othr_sources_pct "Other sources    _______%"
label  var interest_pct "What was the interest rate?  ( % Example:  10%, 12.5%, 14% etc)"
label  var family_earningmembers "How many people earn in your family? It can be salary, agriculture, rent, etc."
label  var earnings_cscservices "What was your total earnings from providing CSC services during the last month?"
label  var income_before_csc "What was your average monthly income before setting up the CSC?"
label  var income_sources_self_all "Please pick all the sources of your income;"
label  var income_sources_self_oth "Other income sources(Please specify)"
label  var income_csc_govt_services_self "Income from CSC government services"
label  var income_csc_nongovt_services_self "Income from CSC non-government services"
label  var income_oth_biz_self "Income from Any other business"
label  var income_rent_lease_self "Income from Rent/Lease"
label  var income_agri_farm_self "Income from Agriculture / Farm"
label  var income_interests_deposits_self "Income from Interest / Deposits"
label  var income_salary_pension_self "Income from Salary / Pension"
label  var income_other_self "Income from Other"
label  var income_sources_fam_all "Please pick all the sources of income for your family, all family members;"
label  var income_sources_fam_oth "Other income sources for family (Please specify)"
label  var income_csc_govt_services_fam "Income from CSC government services - Annual Income (family)"
label  var income_csc_nongovt_services_fam "CSC non-government services - Annual Income (family)"
label  var income_oth_biz_fam "Any other business - Annual Income (family)"
label  var income_rent_lease_fam "Rent / Lease - Annual Income (family)"
label  var income_agri_farm_fam "Agriculture / Farm Income - Annual Income (family)"
label  var income_interests_deposits_fam "Interest / Deposits - Annual Income (family)"
label  var income_salary_pension_fam "Salary / Pension  - Annual Income (family)"
label  var income_other_fam "Other - Annual Income (family)"
label  var permissions_setup_total "Apart from signing agreement with CSC e-Governance Services, how many additional permissions, licenses, approvals, authorizations, etc., did you have to take from the relevant authorities to start the CSC?"
label  var permissions_setup_political "Local political leadership"
label  var permissions_district "District administration / Revenue officials"
label  var permissions_panchayat "Village Panchayat"
label  var permissions_police "Police Department"
label  var permissions_electric "Electricity Dept"
label  var permissions_tele "Telephone dept./ Agency"
label  var permissions_internet "Internet Service Provider"
label  var permissions_oth "Others"
label  var csc_opendays_perweek "For how many days a week is the CSC open?"
label  var csc_opentime "Opening Time     (Ex. 0900  / 1000 etc)"
label  var csc_closetime "Closing Time   (Ex. 1800 / 1900 / 2000 etc)"
label  var csc_closedays_yr "For how many days in a year (approx.) is the CSC closed due to unexpected reasons?"
label  var csc_nvillages "No of villages covered by CSC (including the village in which CSC is located):"
label  var csc_area "CSC floor area:   (Ex. 100 SFt, 120 SFt, 400 SFt etc)"
label  var csc_electricity_hrs "On a normal day, how many hours do you have electricity?"
label  var unusualworkinghrs_pwr_yn "Do you have to work during mid-night / early morning due to power availability?  Explain: Mid-night/ early morning or other unusual hours due to power being available only at that time?"
label  var internet_speed_perception "Perception of internet speed"
label  var movie_download_time "Time taken to download a movie (in minutes)"
label  var counters_n "No. of counters in the CSC"
label  var computers_n "Number of computers in working condition"
label  var printers_n "Number of Printers in working condition"
label  var printer_scanner_n "Number of Printers-Scanner in working condition"
label  var printer_scanner_copier_n "Number of Printers-Scanner-Copier in working condition"
label  var xerox_coppier_n "Number of Xerox / Copier in working condition"
label  var biometric_iris_scanner_n "Number of Bio-Metric / Iris Scanners in working condition"
label  var invertor_ups_n "Number of Inverters / UPS in working condition"
label  var digicam_webcam_n "Number of Digital / Web Camera in working condition"
label  var lamination_n "Number of Lamination Machine in working condition"
label  var oth_equip_n "Number of any OTHER in working condition"
label  var oth_equip_specify "Other equipment - Please specify"
label  var computer_use_customers_yn "Do you allow customers to access/ use computers by themselves?"
label  var computer_use_education_yn "Are the computers used for education/ training services?"
label  var computer_use_jobsearch_yn "Are computers used for job search?"
label  var computer_use_doctor_yn "Are computers used for consulting a doctor?"
label  var computer_use_other_purpose "Any other purpose that computers are used for;"
label  var distance_csc_town "CSC - Distance from Nearest town"
label  var distance_csc_postoffice "CSC - Distance from nearest Post Office"
label  var distance_csc_distrhq "CSC - Distance from nearest District Headquarters"
label  var distance_csc_bank "CSC - Distance from nearest Bank"
label  var distance_csc_csc "CSC - Distance from nearest CSC"
label  var entre_conditions "Please indicate your opinion on the conditions for entrepreneurship in your district."
label  var entre_public_attitude "Public attitude toward entrepreneurship"
label  var entre_success_promo "Promotion of entrepreneurship success"
label  var entre_skills_training "Training of entrepreneurial skills"
label  var entre_success_recognition "Recognition of entrepreneurial success"
label  var entre_marketops_growth "Economic growth and market opportunity for entrepreneurs"
label  var csc_totalexpenses_mthly "What are the different expenses you have at the CSC every month?"
label  var csc_rent_mthly "Monthly Rent"
label  var csc_elecbill_mthly "Monthly Electricity Charges"
label  var csc_phinternetbill_mthly "Monthly - Telephone + Internet Charges"
label  var csc_interestexpense_mthly "Monthly Interest - Bank Charges, Interest on Loans"
label  var csc_salaries_mthly "Monthly Employee Salaries/Wages"
label  var csc_training_mthly "Monthly Training Expenses"
label  var csc_expenseitems_othr "Other (Please specify)"
label  var csc_expenseother_mthly "Other - Monthly Expense"
label  var csc_govtservice_top1 "Using CSC, of all the Government services you provide, which ONE is the most utilized?"
label  var csc_govtservice_formspm_top1 "Usual number of forms/applications processed per month?"
label  var cscgovt_formsperperson1 "Of these, how many are from the same person? That is one person, many applications."
label  var cscgovt_revenuecontri1 "How much does the service contribute to your CSC business / revenue?"
label  var csc_govtservice_top2 "Using CSC, of all the Government services you provide, which ONE is the next most utilized? Second"
label  var csc_govtservice_formspm_top2 "Usual number of forms/applications processed per month?"
label  var cscgovt_formsperperson2 "Of these, how many are from the same person? That is one person, many applications."
label  var cscgovt_revenuecontri2 "How much does the service contribute to your CSC business / revenue?"
label  var csc_govtservice_top3 "Using CSC, of all the Government services you provide, which ONE is the next most utilized? Third"
label  var csc_govtservice_formspm_top3 "Usual number of forms/applications processed per month?"
label  var cscgovt_formsperperson3 "Of these, how many are from the same person? That is one person, many applications."
label  var cscgovt_revenuecontri3 "How much does the service contribute to your CSC business / revenue?"
label  var csc_govtservice_top4 "Using CSC, of all the Government services you provide, which ONE is the next most utilized? Fourth"
label  var csc_govtservice_formspm_top4 "Usual number of forms/applications processed per month?"
label  var cscgovt_formsperperson4 "Of these, how many are from the same person? That is one person, many applications."
label  var cscgovt_revenuecontri4 "How much does the service contribute to your CSC business / revenue?"
label  var csc_govtservice_top5 "Using CSC, of all the Government services you provide, which ONE is the next most utilized? Fifth"
label  var csc_govtservice_formspm_top5 "Usual number of forms/applications processed per month?"
label  var cscgovt_formsperperson5 "Of these, how many are from the same person? That is one person, many applications."
label  var cscgovt_revenuecontri5 "How much does the service contribute to your CSC business / revenue?"
label  var csc_nongovtservice_top1 "Using CSC, of all the Non-Government services you provide, which ONE is the most utilized?"
label  var cscnongovt_uniquecitpm1 "Usual number of unique citizens served per month?"
label  var cscnongovt_revcontripm1 "How much does the service contribute to your CSC business / revenue?"
label  var csc_nongovtservice_top2 "Using CSC, of all the Non-Government services you provide, which ONE is the next most utilized? Second"
label  var cscnongovt_uniquecitpm2 "Usual number of unique citizens served per month?"
label  var cscnongovt_revcontripm2 "How much does the service contribute to your CSC business / revenue?"
label  var csc_nongovtservice_top3 "Using CSC, of all the Non-Government services you provide, which ONE is the next most utilized? Third"
label  var cscnongovt_uniquecitpm3 "Usual number of unique citizens served per month?"
label  var cscnongovt_revcontrip3 "How much does the service contribute to your CSC business / revenue?"
label  var csc_nongovtservice_top4 "Using CSC, of all the Non-Government services you provide, which ONE is the next most utilized? Fourth"
label  var cscnongovt_uniquecitpm4 "Usual number of unique citizens served per month?"
label  var cscnongovt_revcontrip4 "How much does the service contribute to your CSC business / revenue?"
label  var csc_nongovtservice_top5 "Using CSC, of all the Non-Government services you provide, which ONE is the next most utilized? Fifth"
label  var cscnongovt_uniquecitpm5 "Usual number of unique citizens served per month?"
label  var cscnongovt_revcontrip5 "How much does the service contribute to your CSC business / revenue?"
label  var skilltraining_progs_12m_n "Number of local skill development trainings provided by the CSC in the last 12 months? Like vocational trainings, distant learning courses, spoken English courses, interviewing, personality development etc."
label  var skilltraining_villager_attendanc "What is the total number of villagers who have attended the skill development training programs in the last 12 months?"
label  var mkting_campaigns_yn "Do you undertake marketing / promotional campaigns for popularizing the CSC services?"
label  var mkting_campaign_typesused "What is the nature of these campaigns?"
label  var mkting_campaign_othr "Others (Please specify)"
label  var csc_usage_future "Do you think that the usage of CSC services;"
label  var continue_w_csc_yn "Would you like to continue with the CSC business in the future?"
label  var csc_newsletter_receive_freq "How often do you receive newsletters about the CSC program?"
label  var csc_newsletter_read_freq "How often do you read the newsletters about the CSC program?"
label  var email_check_freq "How often do you check the CSC emails?"
label  var reason_for_usingcsc1 "What is the reason why CSC services are frequented by people in the village? Next?"
label  var reason_for_usingcsc2 "What is the reason why CSC services are frequented by people in the village? Next?"
label  var reason_notusingcsc1 "What do you think is the TOP reason why some villagers do not come more frequently to the CSC? Next?"
label  var reason_notusingcsc2 "What do you think is the TOP reason why some villagers do not come more frequently to the CSC? Next?"
label  var serv_reqd_for_csc_growth1 "In your opinion, what other services are needed to expand / increase business of CSCs?"
label  var serv_reqd_for_csc_growth2 "In your opinion, what other services are needed to expand / increase business of CSCs?"
label  var csc_skill_acq_channels "How do you acquire new skills / knowledge on CSC services?"
label  var skillacq_video_usage "Have you learnt / used video for learning new things about CSC / Services?"
label  var skillacq_video_platform "You watch these CSC videos on;"
label  var factors_betterbiz_csc "What do you think are the key factors for better business of CSCs? PICK ALL THAT APPLY"
label  var factors_betterbiz_csc_oth "Others (please specify)"
label  var csc_backend_downtime_dayspweek "On average what is the downtime (not working) of the CSC backend/ IT system?   Number of Days / Week"
label  var csc_backend_downtime_hrspday "On average what is the downtime (not working) of the CSC backend/ IT system?   Number of Hours / Day"
label  var nfamilymembers "In total, how many members are there in your family? (Living under one roof)"
label  var nadults "Number of Adults (18 +)"
label  var nchildren "Number of Children (backup nchildren)"
label  var nearningmembers "How many are earning members? Working, Salary, Agriculture, Labour, Business etc.,"
label  var housetype "What type of house do you live in?   (Main portion / Living Area)"
label  var housetype_oth_spec "Other - Please specify"
label  var immovable_assets_owned "Which of the following immovable assets do you own? I mean  owned by the family."
label  var products_owned "Which of the following products do you own?"
label  var education "Your education please? (Completed)"
label  var blank3 "Which of the following products do you own?"
label  var computer_acq_date "When did you get this computer?   MM / YYYY"
label  var internet_access_home_yn "Do you have Internet access at home?"
label  var internet_usage_home_hrspweek "How long do you use the internet at home? Number of hours / week"
label  var smartphone_usage_yn "Do you use a Smart Phone?"
label  var apps_used_commonly "Which apps do you most commonly use?"
label  var apps_used_other "Other - Please specify"
label  var relatives_frnds_involved_yn "Are any of your relatives or close friends involved in a business?"
label  var fathers_occupation "What is your father's occupation?"
label  var njobs_beforecsc "How many jobs have you done before starting the CSC? (Salaried / Own Business / Etc)"
label  var occupation_beforecsc "Just before starting the CSC, were you;"
label  var lastjob "Please look at this card and indicate in which field was your last business/job?"
label  var lastjob_role "How were you involved?"
label  var lastjob_length "How long did you run this / were you employed?"
label  var lastjob_type_ftpt "Were you ?"
label  var lastjob2 "Before this, what were you doing?"
label  var lastjob2_role "How were you involved?"
label  var lastjob2_length "How long did you run this / were you employed?"
label  var lastjob2_type_ftpt "Were you ?"
label  var lastjob3 "Before this, what were you doing?"
label  var lastjob3_role "How were you involved?"
label  var lastjob3_length "How long did you run this / were you employed?"
label  var lastjob3_type_ftpt "Were you ?"
label  var csc_setup_plan_time "When did you first think of setting up a CSC? And, who all, what all, helped you convert your wish to reality?"
label  var timestamp2 "Date and Time"
label  var next_section_yn "Shall we proceed to the next section?"
label  var blank4 "User Name"
label  var blank5 "Event Name"
label  var blank6 "Name of CSC"
label  var blank7 "Name of VLE"
label  var blank8 "How often do you meet other CSC/VLE's?  And, where do you usually meet them?"
label  var ncustomers_csc_duringsurvey "How many walk-in customers did you notice during the survey?"
label  var blank9 "Date and Time"
label  var blank10 "Notes and Images"
label  var char_like_workinghard "Working hard is something I like doing very much"
label  var char_personaldemand "When I am working, the demands I make upon myself are pretty high"
label  var char_othppl_perception_dontworkh "Other people think I don’t work very hard"
label  var char_numfriends_fate "It is chiefly a matter of fate whether or not I have few friends or many friends"
label  var char_workaccomplishment_lovejob "I accomplish a lot at work because I love my job"
label  var char_getwhatiwant_workhard "When I get what I want, it is usually because I worked hard for it"
label  var char_planahead_unwise_fortune "It is not always wise to plan too far ahead since many things turn out to be a matter of good or bad fortune"
label  var char_leaders_reason_rightplaceti "Most leaders have reached their positions because they were lucky enough to be in the right place at the right time"
label  var char_unsucessfulbizstrategy_expe "When my way of running the business is not successful, I experiment with new different ways of running the business"
label  var char_monitor_areasneedmorepracti "I closely monitor the areas where I need more practice"
label  var char_goalsetting_direction_succe "I set goals for myself in order to direct my activities for making the business a success"
label  var char_thingsdontunderstand_adj_st "I figure out which things I do not understand well and adjust my strategies accordingly"
label  var char_sticktoaims_accomplishgoals "It is usually easy for me to stick to my aims and accomplish my goals"
label  var char_unexpectedevents_conf "I am confident that I could deal efficiently with unexpected events"
label  var char_calm_difficulties_copingabi "I can remain calm when facing difficulties because I can rely on my coping abilities"
label  var char_problem_manysolns "When confronted with a problem, I can usually find several solutions"
label  var char_mostppl_trusted "Most people can be trusted"
label  var char_unselfishcause_exploited "Those devoted to unselfish causes are often exploited by others"
label  var char_freqcontact_diffppl "I frequently come in contact with people that are different from me"
label  var char_comfort_diffppl "I feel comfortable to talk to people that are different from me"
label  var char_time_to_trust "How long does it typically take you to generate a basic level of trust from a person you just met?"
label  var advice_frndsfamily "What are your suggestions to any friend or family member who wishes to open an CSC Centre?"
label  var photo_csc_interior "CSC Photo - Inside View"
label  var photo_csc_exterior "CSC Photo - Outside View"
label  var photo_csc_20m "CSC Photo - From 20 Metres Far"
label  var state2 "State"
label  var district2 "District"
label  var gram_panchayat "Gram Panchayat"
label  var csc_visible_yn "Is CSC prominently visible / noticeable with clear logo, sign boards etc?   - OBSERVE, DO NOT ASK"
label  var csc_accessible_yn "Is the CSC location easily accessible?   - OBSERVE, DO NOT ASK"
label  var csc_leftwing_area_yn "Is the region/ area where CSC is located generally affected by Left- Wing Extremism?    - OBSERVE, DO NOT ASK"
label  var csc_existingcybercafe_yn "Is CSC an existing cyber cafe or other shop which was converted into a CSC?"
label  var source_CreditCardChit "Flag - Credit cards or chit funds is a source of Funding capital"
label  var source_FamilyMemberFriendRe "Flag - Family or friends  is a source of Funding capital"
label  var source_LoansfromCoopsociety "Flag - Loans from Coop-Society is a source of Funding capital"
label  var source_LoansfromMoneyLender "Flag - Loans from Money Lender is a source of Funding capital"
label  var source_Other "Flag -  is a source of Funding capital"
label  var source_Othersourcespleasespe "Flag - Credit cards or chit funds is a source of Funding capital"
label  var source_OwnSavings "Flag - Credit cards or chit funds is a source of Funding capital"
label  var no_fundsources "Number of funding sources"
label  var influencer_FamilymemberRelat "Flag - Family member /Relative was a main influencer for starting CSC"
label  var influencer_FriendColleague "Flag - Friend/ Colleague was a main influencer for starting CSC"
label  var influencer_GovtOfficial "Flag - Govt. Official was a main influencer for starting CSC"
label  var influencer_NGOOtherInstituti "Flag - NGO/ Oth. Institute was a main influencer for starting CSC"
label  var influencer_Other "Flag - Friend/ Colleague was a main influencer for starting CSC"
label  var influencer_Self "Flag -  Him/Herself was a main influencer for starting CSC"
label  var incomesource_self_Agriculture "Flag - Agriculture is an income source for VLE"
label  var incomesource_self_CSCGovernment "Flag - CSC Govt. Services is an income source for VLE"
label  var incomesource_self_CSCNonGovern "Flag - CSC Non Govt. Services is an income source for VLE"
label  var incomesource_self_InterestDep "Flag - Interest from deposits is an income source for VLE"
label  var incomesource_self_Other "Flag - Any other income sources for VLE"
label  var incomesource_self_OtherBusiness "Flag - Other Business is an income source for VLE"
label  var incomesource_self_RentLease "Flag - Rent or Lease is an income source for VLE"
label  var incomesource_self_SalaryPension "Flag - Salary or pension is an income source for VLE"
label  var factors_betterbiz_ ""
label  var factors_betterbiz_Additionalsha "Flag for Better business (VLE opinion)- Additional share of income for VLEs involved in the marketing of services"
label  var factors_betterbiz_Betterinterne "Flag for Better business (VLE opinion)- Better internet connectivity"
label  var factors_betterbiz_Closingdownt "Flag for Better business (VLE opinion)- Closing down traditional modes"
label  var factors_betterbiz_Highershareo "Flag for Better business (VLE opinion)- Higher share of revenue in services"
label  var factors_betterbiz_Lowerdeposit "Flag for Better business (VLE opinion)- Lower deposit requirements to register CSC"
label  var factors_betterbiz_Morefreedomi "Flag for Better business (VLE opinion)- More freedom in offering products and services"
label  var factors_betterbiz_Other "Flag for Better business (VLE opinion)- other"
label  var factors_betterbiz_Reducedintere "Flag for Better business (VLE opinion)- Reduced interest on loans / Better and easier credit facilities"
label  var factors_betterbiz_Reductionins "Flag for Better business (VLE opinion)- Reduction in service charges"
label  var factors_betterbiz_Subsidyinope "Flag for Better business (VLE opinion)- Subsidy in operational costs"
label  var apps_used_ ""
label  var apps_used_Facebook "Flag- Uses Facebook"
label  var apps_used_Other "Flag- Uses apps other than FB, whatsapp Youtube"
label  var apps_used_Whatsapp "Flag - Uses Whatsapp"
label  var apps_used_Youtube "Flag - Uses Youtube"
label  var skilvid_platform_Other "Flag - Uses platforms other than youtube, whatsapp for skills acquisition"
label  var skilvid_platform_Whatsapp "Flag - Uses Whatsapp for watching skills acquisition videos"
label  var skilvid_platform_Youtube "Flag - Uses Youtube for watching skills acquisition videos"
label  var skill_acq_channels_CSCStaff "Flag - CSC Staff are a channel for skill acquisition"
label  var skill_acq_channels_Newsletter "Flag - Newsletter is a channel for skill acquisition "
label  var skill_acq_channels_OtherVLEs "Flag - Other VLEs are a channel for skill acquisition"
label  var skill_acq_channels_WatchingVide "Flag - Watchign Videos is a channel for skill acquisition"
label  var skill_acq_channels_WorkshopTr "Flag - Workshop Training is a channel for skill acquisition"
label  var workingat_csc_FulltimeFamilyMem "Flag - Fulltime Family members are working at CSC"
label  var workingat_csc_NoneNoEmployees "Flag - No Employees"
label  var workingat_csc_Others "Flag - People other than family and employees are working at CSC"
label  var workingat_csc_PaidFulltimeEmplo "Flag - Paid Fulltime Employees are working at CSC"
label  var workingat_csc_PaidParttimeEmplo "Flag - Paid Partime Employees are working at CSC"
label  var workingat_csc_ParttimeFamilyMem "Flag - Partime Family members are working at CSC"
label  var familyfullflag ""
label  var familypartflag ""
label  var empfullflag ""
label  var emppartflag ""
label  var formspm_total "Total Forms processed per month (sum of top 5 forms processed per month)"
label  var farmer_earnings_pm2 "Farmer earnings per month (2)"
label  var mthly_expenses2 "monthly expenses for VLE"
label  var csc_openhrs "Number of hours CSC is open"
label  var char_achvment_mot "VLE Characteristic - Achievement Motivation"
label  var char_locus_control "VLE Characteristic - Locus of Control"
label  var char_meta_cog "VLE Characteristic - Metacognitive Ability"
label  var char_self_efficacy "VLE Characteristic - Self Efficacy"
label  var flipcharothpplworkhard "Rereversed - Charac. Other ppl work hard"
label  var nsources_income "Number of sources of income"


label  var username "User Name"
label  var state "State"
label  var district "District"
label  var date "Date and Time"
label  var Timestamp "Date and Time"
label  var gpslocation "GPS Location"
label  var cscname "CSC Name (Where survey conducted)"
label  var cscid "CSC Sl No."
label  var district2 "District"
label  var villagename "Village Name"
label  var panchayat "Gram Panchayat Name"
label  var respondentname "Respondent Name (Citizen)"
label  var code "Code"
label  var maritalstatus "Marital Status:"
label  var children "How many children?"
label  var education "Your education? (Highest level completed)"
label  var occupation "Your occupation;"
label  var top5products "Many services are provided at the CSC. This includes Government Services, Certificates, Schemes, Forms etc, and it also includes Business services like Mobile Recharge, Rail Booking etc. Considering all the services together, which ONE have you used the most? Next? Next? (Upto 5)"
label  var topreason_link "What is the main reason you use the CSC / Jan Seva Kendra / Mee Sewa?  GET TOP 5 REASONS"
label  var topreason_text "What is the main reason you use the CSC / Jan Seva Kendra / Mee Sewa?  GET TOP 5 REASONS"
label  var newservices "What new services (government or private) do you believe must be added to CSC?  GET UPTO 5"
label  var newservices "What new services (government or private) do you believe must be added to CSC?  GET UPTO 5"
label  var schemeenrolled_link "Please list the schemes for which you have enrolled/ registered through the CSC?"
label  var csc_alt "Other than CSC, what are the alternative service providers in your village?"
label  var csc_alt_oth "Other"
label  var intro1 "I will now read out some statements. Please tell me, to what extent you agree / disagree with..."
label  var continuebuying_clv "I will continue buying the products/services at CSC / e-seva centre in the near future"
label  var contenttrans_clv "Am content with my transactions through the CSC/ e-seva centre"
label  var moneysworth_clv "I do not get my money’s worth when I transact through the CSC e-seva"
label  var happyrefer_crv "I am happy to refer the CSC/ e-seva centre to my friends and relatives"
label  var refercsc_crv "Given that I use the CSC, I refer my friends and relatives to the the CSC/ e-seva centre"
label  var activelydiscuss_civ "I do not actively discuss about the CSC/ e-seva centre"
label  var cscexp_civ "I love talking about my CSC/ e-seva experience"
label  var discussbenefits_civ "I discuss the beneﬁts that I get from the CSC/ e-seva centre with others"
label  var feedbackexp_ckv "I provide feedback about my experiences with the CSC/ e-seva centre to the VLE"
label  var suggimprove_ckv "I provide suggestions for improving the performance of the CSC/ e-seva centre"
label  var suggnewprods_ckv "I provide suggestions/feedback about new product/service that can be provided by the CSC"
label  var ntrips_govtoff "Number of trips you made in the last one year to any Government Offices; (ALL Govt Offices, Total Number of Trips)"
label  var ntrips_cscs "Number of trips you made in the last one year to CSC's;   (Total Number of Trips)"
label  var distptrans_govtoff "What is the average distance (in Kms) you travel for each transaction - Government Office  (Any Govt Office, Average)"
label  var distptrans_csc "What is the average distance (in Kms) you travel for each transaction - CSC  (Any CSC, Average)"
label  var trvltime_govtoff "What is the average time taken (in Minutes) for each trip to Government Office (Any Govt Office, Average time for travel)"
label  var trvltime_csc "What is the average time taken (in Minutes) for each trip to CSC (Any CSC, Average time for travel)"
label  var cost_govtoff "What is the average cost (in Rupees) for each trip to Government Office (Any Govt Office, Average time for travel)"
label  var cost_csc "What is the average cost (in Rupees) for each trip to CSC (Any CSC, Average time for travel)"
label  var waittime_govtoff "What is the usual waiting time (in Minutes) for each transaction at Government office  (Any Govt Office, Average time you have to wait)"
label  var waittime_csc "What is the usual waiting time (in Minutes) for each transaction at CSC (Any CSC, Average time you have to wait)"
label  var nintermediaries_govtoff "What is the average number of intermediaries/counters you had to go through to successfully complete each transaction at Govt office"
label  var nintermediaries_csc "What is the average number of intermediaries/counters you had to go through to successfully complete each transaction at CSC"
label  var wageloss_govtoff "What was the average wage loss (in rupees) for each transaction attempted at Government office"
label  var wageloss_csc "What was the average wage loss (in rupees) for each transaction attempted at CSC"
label  var nedlays_govt "Out of 10 works that you needed to get done, how many would be delayed at Government Office?  (By Delay, I mean, it took more time than it should have taken)"
label  var ndelays_csc "Out of 10 works that you needed to get done, how many would be delayed at CSC?  (By Delay, I mean, it took more time than it should have taken)"
label  var ndenied_govt "Out of 10 works that you needed to get done, how many would be DENIED at Government Office?  (By Denied, I mean, it is not done)"
label  var ndeined_csc "Out of 10 works that you needed to get done, how many would be DENIED at CSC?  (By Denied, I mean, it is not done)"
label  var allodoccons_yn "Please tell me whether - Consulting an Allopathic Doctor - is available at CSC?"
label  var nconsallodocs_l3m "How many times have you used - Consult Allopathic Doctor - in the past 3 months?"
label  var homeodoccons_yn "Please tell me whether - Consulting an Homeopathic Doctor - is available at CSC?"
label  var nconshomeodocs_l3m "How many times have you used - Consult Homeo Doctor - in the past 3 months?"
label  var ayurveddocs_yn "Please tell me whether - Consulting an Ayurvedic Doctor - is available at CSC?"
label  var naurveddocs_l3m "How many times have you used - Consult Ayurvedic Doctor - in the past 3 months?"
label  var mobiledth_yn "Please tell me whether - Mobile and DTH payments, recharge  - is available at CSC?"
label  var nmobiledth_l3m "How many times have you used - Mobile and DTH payments, recharge  - in the past 3 months?"
label  var schlunivenrl_yn "Please tell me whether - Enrol and Study in School / University - is available at CSC?"
label  var nschlunivenrl_l3m "How many times have you used - Enrol and Study in School / University - in the past 3 months?"
label  var iitiasstudy_yn "Please tell me whether - Enrol and Study for IIT/ IAS coaching - is available at CSC?"
label  var niitiasstudyused_l3m "How many times have you used - Enrol and Study for IIT/ IAS coaching - in the past 3 months?"
label  var skilltraining_yn "Please tell me whether - Enrol and Study for Skill Training - is available at CSC?"
label  var nskilltrainingused_l3m "How many times have you used - Enrol and Study for Skill Training - in the past 3 months?"
label  var adhar_yn "Please tell me whether - Apply for Aadhar Card - is available at CSC?"
label  var nadharused_l3m "How many times have you used - Apply for Aadhar Card - in the past 3 months?"
label  var pancard_yn "Please tell me whether - Apply for Pan Card - is available at CSC?"
label  var npancard_l3m "How many times have you used - Apply for Pan Card - in the past 3 months?"
label  var passport_yn "Please tell me whether - Apply for Passport - is available at CSC?"
label  var applypassport_l3m "How many times have you used - Apply for Passport - in the past 3 months?"
label  var bankacct_yn "Please tell me whether - Open and use bank accounts- is available at CSC?"
label  var bankacct_l3m "How many times have you used - Open and use bank accounts - in the past 3 months?"
label  var insurance_yn "Please tell me whether - Purchase Insurance policies (life, health, others) - is available at CSC?"
label  var insurance_l3m "How many times have you used - Purchase Insurance policies (life, health, others) - in the past 3 months?"
label  var pensionpl_yn "Please tell me whether - Enroll in Pension plans (Atal PY, NPS, PMSBY) - is available at CSC?"
label  var npensionpl_l3m "How many times have you used - Enroll in Pension plans (Atal PY, NPS, PMSBY) - in the past 3 months?"
label  var upifundtrfr_yn "Please tell me whether - Online transfer of funds, UPI - is available at CSC?"
label  var upifundtrfr_l3m "How many times have you used - Online transfer of funds, UPI - in the past 3 months?"
label  var digitalpayewallets_yn "Please tell me whether - Training on digital payments, e-wallets - is available at CSC?"
label  var digitalpayewallet_l3m "How many times have you used - Training on digital payments, e-wallets - in the past 3 months?"
label  var otherserv_yn "Any other service available at the CSC;"
label  var otherserv_l3m "How often have you used ........... in the last 3 months?"
label  var suggestions_link "Your suggestions for making CSC more relevant for your needs"


** variables **

drop state2 State


** destring **

destring csc_topup_amt statedig_topup_amt avg_emp_pay csc_totalexpenses_mthly csc_govtservice_formspm_top1 cscgovt_revenuecontri1 csc_govtservice_formspm_top2 csc_govtservice_formspm_top3 csc_govtservice_formspm_top4 csc_govtservice_formspm_top5 cscgovt_formsperperson2 cscgovt_formsperperson3 cscgovt_formsperperson4 cscgovt_formsperperson5 cscgovt_revenuecontri2 cscgovt_revenuecontri3 cscgovt_revenuecontri4 cscgovt_revenuecontri5 cscnongovt_uniquecitpm1 cscnongovt_uniquecitpm2 cscnongovt_uniquecitpm3 cscnongovt_uniquecitpm4 cscnongovt_uniquecitpm5 cscnongovt_revcontripm2 cscnongovt_revcontrip3 cscnongovt_revcontrip4 cscnongovt_revcontrip5 skilltraining_villager_attendanc csc_backend_downtime_dayspweek csc_backend_downtime_hrspday nadults ncustomers_csc_duringsurvey apps_used_Facebook apps_used_Other apps_used_Whatsapp apps_used_Youtube skilvid_platform_Other skilvid_platform_Whatsapp skilvid_platform_Youtube cscnongovt_revcontripm1, replace force

** y/n to 1-0 **

foreach x in employee_training_yn vle_training_yn unusualworkinghrs_pwr_yn computer_use_customers_yn computer_use_education_yn computer_use_jobsearch_yn computer_use_doctor_yn mkting_campaigns_yn continue_w_csc_yn internet_access_home_yn smartphone_usage_yn relatives_frnds_involved_yn csc_visible_yn csc_accessible_yn csc_leftwing_area_yn csc_existingcybercafe_yn {
replace `x' = "1" if `x' == "Yes" 
replace `x' = "0" if `x' == "No"
}

destring employee_training_yn vle_training_yn unusualworkinghrs_pwr_yn computer_use_customers_yn computer_use_education_yn computer_use_jobsearch_yn computer_use_doctor_yn mkting_campaigns_yn continue_w_csc_yn internet_access_home_yn smartphone_usage_yn relatives_frnds_involved_yn csc_visible_yn csc_accessible_yn csc_leftwing_area_yn csc_existingcybercafe_yn , replace force

** factor variables for charactoristics based on EFA **
egen char_factor1 = rmean(char_like_workinghard  char_personaldemand  char_goalsetting_direction_succe  char_thingsdontunderstand_adj_st char_sticktoaims_accomplishgoals char_unexpectedevents_conf char_calm_difficulties_copingabi char_problem_manysolns )
egen char_factor2 = rmean(flipcharothpplworkhard char_workaccomplishment_lovejob char_getwhatiwant_workhard char_unsucessfulbizstrategy_expe char_monitor_areasneedmorepracti )
egen char_factor3 = rmean(char_numfriends_fate char_planahead_unwise_fortune char_leaders_reason_rightplaceti )


** entre coding **

foreach x in entre_public_attitude entre_success_promo entre_skills_training entre_success_recognition entre_marketops_growth{
tab `x'
}

foreach x in entre_public_attitude entre_success_promo entre_skills_training entre_success_recognition entre_marketops_growth {
replace `x' = "4" if `x' == "Good" 
replace `x' = "3" if `x' == "Average"
replace `x' = "2" if `x' == "Fair"
replace `x' = "1" if `x' == "Must be improved"
destring `x', replace force
}

** code marital status **
replace marital_status = "0" if marital_status == "Single / Unmarried"
replace marital_status = "1" if marital_status == "Married"
replace marital_status = "2" if marital_status == "Divorced"
replace marital_status = "3" if marital_status == "Widow"
destring marital_status , replace

** code gender **
replace gender = "1" if gender == "Female"
replace gender = "0" if gender == "Male"
destring gender ,replace

*******************************
*** VLE chars shaped by env ***
*******************************
/* 
dvs :achievement motivation, locus of control, metacognitive, self efficacy
ivs :entrepreneurship public attitude, success promotion, skills training, sucess recognition, marketops and growth
controls: VLE age, marital status, number of children, family size, gender
*/

foreach y in char_achvment_mot char_locus_control char_meta_cog char_self_efficacy{
foreach x in entre_public_attitude entre_success_promo entre_skills_training entre_success_recognition entre_marketops_growth {
reg `y' vle_age  children nfamilymembers i.marital_status i.gender i.`x'
}
}

foreach y in char_achvment_mot char_locus_control char_meta_cog char_self_efficacy{
reg `y' vle_age  children nfamilymembers i.marital_status i.gender i.entre_public_attitude i.entre_success_promo i.entre_skills_training i.entre_success_recognition i.entre_marketops_growth 
}


*****************************************
** vle performance and characteristics **

** EARNINGS ** 
reg earnings_cscservices vle_age vle_training_dur distance_csc_csc distance_csc_distrhq csc_electricity_hrs agri_labourer_earnings_pd i.viralkm_clus3 
** earnings controlled for environment **
reg earnings_cscservices vle_age vle_training_dur distance_csc_csc distance_csc_distrhq csc_electricity_hrs agri_labourer_earnings_pd i.viralkm_clus3 i.entre_marketops_growth i.entre_public_attitude i.entre_skills_training i.entre_success_promo i.entre_success_recognition 

* additional controls - education, gender , access to community credit - chitfunds

**** VLE segmentation exercise *******
sort viralkm_clus3 
by viralkm_clus3 :summarize vle_age earnings_cscservices gender marital_status children investment_amt_cscsetup csc_topup_amt statedig_topup_amt csc_open_freq hrs_perday_csc persons_workingat_csc paid_fulltime_emp paid_parttime_emp family_fulltime family_parttime other_workers familyhelp_relationship avg_emp_pay employee_training_yn emp_training_dur vle_training_yn vle_training_dur char_achvment_mot char_locus_control char_meta_cog char_self_efficacy 


*** Raw variables to drop ***
drop persons_workingat_csc 

*** funding and investment ***
/*
number of sources of funds 
Amount invested to setup CSC
*/


*** operational expenses - CSC characteristics? ***
/*
total monthly expenses
rent
electricity
interest
internet
salary
training
*/

/*
'distance_csc_town',
 'distance_csc_postoffice',
 'distance_csc_distrhq',
 'distance_csc_bank',
 'distance_csc_csc'
 number of employees
 average salary of employees
 
 */
 

by viralkm_clus3 : summarize  internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn hrs_perday_csc employee_training_yn  vle_training_yn vle_training_dur investment_amt_cscsetup no_fundsources nsources_income csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn continue_w_csc_yn csc_usage_future csc_openhrs emp_yn total_emp
 

*** new char **
egen char_gritpr = rmean(char_like_workinghard char_personaldemand char_goalsetting_direction_succe char_thingsdontunderstand_adj_st char_sticktoaims_accomplishgoals char_unexpectedevents_conf char_calm_difficulties_copingabi char_problem_manysolns)

******************
**** new clus ****
******************

** recode agree disagree variables into likert scale **
foreach x in mostppl_trusted unselfishcause_exploited freqcontact_diffppl comfort_diffppl{
gen `x'_lkrt = "5" if `x' == "Strongly Agree"
replace `x'_lkrt = "4" if `x' == "Agree"
replace `x'_lkrt = "3" if `x' == "Neutral/ Don’t know"
replace `x'_lkrt = "3" if `x' == "Neutral/Don't Know"
replace `x'_lkrt = "2" if `x' == "Disagree"
replace `x'_lkrt = "1" if `x' == "Strongly Disagree"
destring `x'_lkrt, replace force
}

* time to trust char **
gen time_to_trust_lkrt = 5 if  time_to_trust == "It happens over a year or more"
replace time_to_trust_lkrt =4 if time_to_trust == "It takes at least 3 or 4 months"
replace time_to_trust_lkrt =3 if time_to_trust == "About month of working together/ Don’t know"
replace time_to_trust_lkrt =2 if time_to_trust == "After about 2 or 3 meetings"
replace time_to_trust_lkrt =1 if time_to_trust == "First meeting"
replace time_to_trust_lkrt = 2 if time_to_trust == "???? 2 ?? 3 ??????????"
replace time_to_trust_lkrt = 4 if time_to_trust == "?? ?????? ??? ? ?? 4 ????? ????"
replace time_to_trust_lkrt = 3 if time_to_trust == "???? ????? ???? ??? ???? / ??? ?????"

*** remove prefix ***
foreach x in char_like_workinghard char_personaldemand char_othppl_perception_dontworkh char_numfriends_fate char_workaccomplishment_lovejob char_getwhatiwant_workhard char_planahead_unwise_fortune char_leaders_reason_rightplaceti char_unsucessfulbizstrategy_expe char_monitor_areasneedmorepracti char_goalsetting_direction_succe char_thingsdontunderstand_adj_st char_sticktoaims_accomplishgoals char_unexpectedevents_conf char_calm_difficulties_copingabi char_problem_manysolns char_mostppl_trusted char_unselfishcause_exploited char_freqcontact_diffppl char_comfort_diffppl char_time_to_trust{
renpfix char_
}

/*
foreach x in like_workinghard personaldemand prcptn_dntworkhard numfriends_fate workacc_lovejob getwhatiwant_workhard plnahead_unwise leaders_rtplacetime biznosuccess_expmt monitor_practiceareas goalsetting adjstrat stickaimsgoals unexpectedevents_conf calm_copingablty problem_manysolns mostppl_trusted unselfishcause_exploited freqcontact_diffppl comfort_diffppl time_to_trust{
rensfix `x' _c
}
*/

*** flip characteris
gen pln_unwise_flip  = -char_planahead_unwise_fortune
gen leaders_placntime_flip = -char_leaders_reason_rightplaceti
gen prcptn_dntworkhard_flip = -prcptn_dntworkhard 

pln_unwise_flip 
leaders_placntime_flip
numfrnds_fate_flip
prcptn_dntworkhard_flip


** transform 11 point likert to 5 point likert **

foreach x in like_workinghard personaldemand prcptn_dntworkhard_flip numfrnds_fate_flip workacc_lovejob getwhatiwant_workhard pln_unwise_flip leaders_placntime_flip biznosuccess_expmt monitor_practiceareas goalsetting adjstrat stickaimsgoals unexpectedevents_conf calm_copingablty problem_manysolns{

gen `x'_lkrt = (`x' - (-5))/(5 - (-5)) * (5-1) + 1

}

** factor analysis **

factor mostppl_trusted_lkrt unselfishcause_exploited_lkrt freqcontact_diffppl_lkrt comfort_diffppl_lkrt time_to_trust_lkrt like_workinghard_lkrt personaldemand_lkrt prcptn_dntworkhard_flip_lkrt numfrnds_fate_flip_lkrt workacc_lovejob_lkrt getwhatiwant_workhard_lkrt pln_unwise_flip_lkrt leaders_placntime_flip_lkrt biznosuccess_expmt_lkrt monitor_practiceareas_lkrt goalsetting_lkrt adjstrat_lkrt stickaimsgoals_lkrt unexpectedevents_conf_lkrt calm_copingablty_lkrt problem_manysolns_lkrt
screeplot
graph save Graph "/Users/pradeep/Workingdirectory/Data/CSC analysis/screeplot_26June.gph"

factor mostppl_trusted_lkrt unselfishcause_exploited_lkrt freqcontact_diffppl_lkrt comfort_diffppl_lkrt time_to_trust_lkrt like_workinghard_lkrt personaldemand_lkrt prcptn_dntworkhard_flip_lkrt numfrnds_fate_flip_lkrt workacc_lovejob_lkrt getwhatiwant_workhard_lkrt pln_unwise_flip_lkrt leaders_placntime_flip_lkrt biznosuccess_expmt_lkrt monitor_practiceareas_lkrt goalsetting_lkrt adjstrat_lkrt stickaimsgoals_lkrt unexpectedevents_conf_lkrt calm_copingablty_lkrt problem_manysolns_lkrt, factors(4)
rotate, kaiser



** create factor / construct variables **
/* old cluster 
** grit and persistence **
egen gritty_factorchar = rmean(char_like_workinghard char_personaldemand char_goalsetting_direction_succe char_thingsdontunderstand_adj_st char_sticktoaims_accomplishgoals char_unexpectedevents_conf char_calm_difficulties_copingabi char_problem_manysolns)
egen driveachmot_factorchar = rmean(char_workaccomplishment_lovejob char_getwhatiwant_workhard char_monitor_areasneedmorepracti )
***** locus of contrl  ***
egen locusctrl_factorchar = rmean(char_numfriends_fate planning_unwise_flipchar leaders_placntime_flipchar ) 
*/

** create constructs (means)**
egen GritPersistCnstr_mean = rmean(like_workinghard_lkrt personaldemand_lkrt goalsetting_lkrt adjstrat_lkrt stickaimsgoals_lkrt unexpectedevents_conf_lkrt calm_copingablty_lkrt problem_manysolns_lkrt)
egen BlfSelfFateCnstr_mean = rmean(numfrnds_fate_flip_lkrt pln_unwise_flip_lkrt leaders_placntime_flip_lkrt)
egen DrvAchmtCnstr_mean = rmean(workacc_lovejob_lkrt getwhatiwant_workhard_lkrt biznosuccess_expmt_lkrt monitor_practiceareas_lkrt)
egen DiverseNtwrk_mean = rmean(freqcontact_diffppl_lkrt comfort_diffppl_lkrt)

** create viral constructs (means) **
egen AchvmtMot_meanV = rmean(like_workinghard_lkrt personaldemand_lkrt)
egen LocusCtrl_meanV = rmean(numfrnds_fate_flip_lkrt workacc_lovejob_lkrt getwhatiwant_workhard_lkrt pln_unwise_flip_lkrt leaders_placntime_flip_lkrt)
egen MetacogAb_meanV = rmean(biznosuccess_expmt_lkrt monitor_practiceareas_lkrt goalsetting_lkrt adjstrat_lkrt)
egen SelfEffcy_meanV = rmean(stickaimsgoals_lkrt unexpectedevents_conf_lkrt calm_copingablty_lkrt problem_manysolns_lkrt)
egen FrndFoe_meanV = rmean(mostppl_trusted_lkrt unselfishcause_exploited_lkrt time_to_trust_lkrt)
egen NtwrkDiv_meanV = rmean(freqcontact_diffppl_lkrt comfort_diffppl_lkrt)


** create constructs (factors) **
*step 1 factor with only useful vars *
factor freqcontact_diffppl_lkrt comfort_diffppl_lkrt like_workinghard_lkrt personaldemand_lkrt numfrnds_fate_flip_lkrt workacc_lovejob_lkrt getwhatiwant_workhard_lkrt pln_unwise_flip_lkrt leaders_placntime_flip_lkrt biznosuccess_expmt_lkrt monitor_practiceareas_lkrt goalsetting_lkrt adjstrat_lkrt stickaimsgoals_lkrt unexpectedevents_conf_lkrt calm_copingablty_lkrt problem_manysolns_lkrt, factors(4)
rotate, kaiser
predict GritPersistCnstr_f1 DrvAchmtCnstr_f2 BlfSelfFateCnstr_f3  DiverseNtwrk_f4

**** environment variables **
factor entre_public_attitude entre_success_promo entre_skills_training entre_success_recognition entre_marketops_growth
screeplot
graph save Graph "/Users/pradeep/Google Drive (pradeep_pachigolla@isb.edu)/CSC/Funal report/screeplot_entreenv_26June.gph"
rotate,kaiser
factor entre_public_attitude entre_success_promo entre_skills_training entre_success_recognition entre_marketops_growth, factors(1)
rotate,kaiser
predict EntreEnv_f1


******************************************************************************
******************************* Segmentation *********************************
******************************************************************************


*** clusters  using factor vars ***

cluster singlelinkage GritPersistCnstr_f1 DrvAchmtCnstr_f2 BlfSelfFateCnstr_f3 DiverseNtwrk_f4, measure(L2) name(Ftr4ClusHier_v1)
cluster dendrogram Ftr4ClusHier_v1
cluster dendrogram Ftr4ClusHier_v1, cutnumber(20)
graph save Graph "/Users/pradeep/Google Drive (pradeep_pachigolla@isb.edu)/CSC/Funal report/FtrClusHier_v1.gph"
cluster stop

cluster kmeans GritPersistCnstr_f1 DrvAchmtCnstr_f2 BlfSelfFateCnstr_f3 DiverseNtwrk_f4, k(4) measure(L2) name(Ftr4ClusKM_v1) start(krandom)


**** Profiling *******
sort ClusFtr4KM_v1
by ClusFtr4KM_v1 : summarize earnings_cscservices Sales_AMT Sales_Count formspm_total2 Sales_AMT_pm abnormal_inc HHI GritPersistCnstr_f1 DrvAchmtCnstr_f2 BlfSelfFateCnstr_f3 DiverseNtwrk_f4 GritPersistCnstr_mean   DrvAchmtCnstr_mean BlfSelfFateCnstr_mean DiverseNtwrk_mean vle_age gender marital_status children nfamilymembers nearningmembers priorbizexp_flag graduate_flag internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn vle_training_dur emp_yn employee_training_yn emp_training_dur total_emp csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn future_outlook  commcredit_flag2 communitycredit_flag 

*by Ftr4ClusKM_v1 : summarize GritPersistCnstr_f1 DrvAchmtCnstr_f2 BlfSelfFateCnstr_f3 DiverseNtwrk_f4
*by Ftr4ClusKM_v1 : summarize GritPersistCnstr_mean BlfSelfFateCnstr_mean DrvAchmtCnstr_mean DiverseNtwrk_mean
*by Ftr4ClusKM_v1 : summarize earnings_cscservices 

reg earnings_cscservices i.ClusFtr4KM_v1 

reg earnings_cscservices vle_age vle_training_dur distance_csc_csc distance_csc_distrhq csc_electricity_hrs agri_labourer_earnings_pd gender graduate_flag  commcredit_flag2  i.ClusFtr4KM_v1 EntreEnv_f1 

** summaries **
* table 1 *

*by Ftr4ClusKM_v1 : summarize vle_age gender marital_status children nfamilymembers nearningmembers  internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn vle_training_dur emp_yn employee_training_yn emp_training_dur csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn future_outlook  priorbizexp_flag graduate_flag total_emp commcredit_flag2 communitycredit_flag

foreach x in  vle_age gender marital_status children nfamilymembers nearningmembers  internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn vle_training_dur emp_yn employee_training_yn emp_training_dur csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn future_outlook  priorbizexp_flag graduate_flag total_emp commcredit_flag2 communitycredit_flag {
ttest `x', by(ClusFtr4KM_v1)
}

foreach x in  vle_age gender marital_status children nfamilymembers nearningmembers  internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn vle_training_dur emp_yn employee_training_yn emp_training_dur csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn future_outlook  priorbizexp_flag graduate_flag total_emp commcredit_flag2 communitycredit_flag {
display `x'
anova `x' ClusFtr4KM_v1
}

*** cluster v2 ***
*factors
sort ClusFtr4KM3_v2 
by ClusFtr4KM3_v2 : summarize earnings_cscservices Sales_AMT Sales_Count formspm_total2 Sales_AMT_pm abnormal_inc HHI GritPersistCnstr_f1 DrvAchmtCnstr_f2 BlfSelfFateCnstr_f3 DiverseNtwrk_f4 GritPersistCnstr_mean   DrvAchmtCnstr_mean BlfSelfFateCnstr_mean DiverseNtwrk_mean vle_age gender marital_status children nfamilymembers nearningmembers priorbizexp_flag graduate_flag internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn vle_training_dur emp_yn employee_training_yn emp_training_dur total_emp csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn future_outlook  commcredit_flag2 communitycredit_flag 
*means
sort ClusMn4KM3_v2 
by ClusMn4KM3_v2 : summarize earnings_cscservices Sales_AMT Sales_Count formspm_total2 Sales_AMT_pm abnormal_inc HHI GritPersistCnstr_f1 DrvAchmtCnstr_f2 BlfSelfFateCnstr_f3 DiverseNtwrk_f4 GritPersistCnstr_mean   DrvAchmtCnstr_mean BlfSelfFateCnstr_mean DiverseNtwrk_mean vle_age gender marital_status children nfamilymembers nearningmembers priorbizexp_flag graduate_flag internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn vle_training_dur emp_yn employee_training_yn emp_training_dur total_emp csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn future_outlook  commcredit_flag2 communitycredit_flag 




*******************************
*** clusters using mean vars ***
cluster singlelinkage GritPersistCnstr_mean BlfSelfFateCnstr_mean DrvAchmtCnstr_mean DiverseNtwrk_mean, measure(L2) name(ClusHierMn4_v1)
cluster stop
cluster kmeans GritPersistCnstr_mean BlfSelfFateCnstr_mean DrvAchmtCnstr_mean DiverseNtwrk_mean, k(4) measure(L2) name(ClusMn4KM_v1) start(krandom)


**** Profiling *******
sort ClusFtr4KM_v1
by ClusFtr4KM_v1 : summarize earnings_cscservices Sales_AMT Sales_Count formspm_total2 Sales_AMT_pm abnormal_inc HHI GritPersistCnstr_f1 DrvAchmtCnstr_f2 BlfSelfFateCnstr_f3 DiverseNtwrk_f4 GritPersistCnstr_mean   DrvAchmtCnstr_mean BlfSelfFateCnstr_mean DiverseNtwrk_mean vle_age gender marital_status children nfamilymembers nearningmembers priorbizexp_flag graduate_flag internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn vle_training_dur emp_yn employee_training_yn emp_training_dur total_emp csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn future_outlook  commcredit_flag2 communitycredit_flag 



reg Sales_AMT i.ClusMn4KM_v1 
reg Sales_AMT vle_age vle_training_dur distance_csc_csc distance_csc_distrhq csc_electricity_hrs agri_labourer_earnings_pd gender graduate_flag  commcredit_flag2  i.ClusMn4KM_v1 EntreEnv_f1 

** summaries **
* table 1 *
*by ClusMn4KM_v1 : summarize 

foreach x in Sales_AMT Sales_Count earnings_cscservices {
gen ln`x' = ln(1+`x')
}

**** t test *********

drop if ClusMn4KM_v1 == 2
drop if ClusMn4KM_v1 == 3
*ttest lnSalesAmt , by(ClusMn4KM_v1 )

foreach x in earnings_cscservices Sales_AMT lnSalesAmt Sales_Count formspm_total2 Sales_AMT_pm abnormal_inc HHI GritPersistCnstr_f1 DrvAchmtCnstr_f2 BlfSelfFateCnstr_f3 DiverseNtwrk_f4 GritPersistCnstr_mean   DrvAchmtCnstr_mean BlfSelfFateCnstr_mean DiverseNtwrk_mean vle_age gender marital_status children nfamilymembers nearningmembers priorbizexp_flag graduate_flag internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn vle_training_dur emp_yn employee_training_yn emp_training_dur total_emp csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn future_outlook  commcredit_flag2 communitycredit_flag {
display "`x'"
ttest `x', by(ClusMn4KM_v1)
}

use "cscdata_26Jun.dta", clear


drop if ClusMn4KM_v1 == 2
drop if ClusMn4KM_v1 == 4
foreach x in earnings_cscservices Sales_AMT lnSalesAmt Sales_Count formspm_total2 Sales_AMT_pm abnormal_inc HHI GritPersistCnstr_f1 DrvAchmtCnstr_f2 BlfSelfFateCnstr_f3 DiverseNtwrk_f4 GritPersistCnstr_mean   DrvAchmtCnstr_mean BlfSelfFateCnstr_mean DiverseNtwrk_mean vle_age gender marital_status children nfamilymembers nearningmembers priorbizexp_flag graduate_flag internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn vle_training_dur emp_yn employee_training_yn emp_training_dur total_emp csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn future_outlook  commcredit_flag2 communitycredit_flag {
display "`x'"
ttest `x', by(ClusMn4KM_v1)
}

use "cscdata_26Jun.dta", clear

drop if ClusMn4KM_v1 == 3
drop if ClusMn4KM_v1 == 4
foreach x in earnings_cscservices Sales_AMT lnSalesAmt Sales_Count formspm_total2 Sales_AMT_pm abnormal_inc HHI GritPersistCnstr_f1 DrvAchmtCnstr_f2 BlfSelfFateCnstr_f3 DiverseNtwrk_f4 GritPersistCnstr_mean   DrvAchmtCnstr_mean BlfSelfFateCnstr_mean DiverseNtwrk_mean vle_age gender marital_status children nfamilymembers nearningmembers priorbizexp_flag graduate_flag internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn vle_training_dur emp_yn employee_training_yn emp_training_dur total_emp csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn future_outlook  commcredit_flag2 communitycredit_flag {
display "`x'"
ttest `x', by(ClusMn4KM_v1)
}

use "cscdata_26Jun.dta", clear

drop if ClusMn4KM_v1 == 1
drop if ClusMn4KM_v1 == 3
foreach x in earnings_cscservices Sales_AMT lnSalesAmt Sales_Count formspm_total2 Sales_AMT_pm abnormal_inc HHI GritPersistCnstr_f1 DrvAchmtCnstr_f2 BlfSelfFateCnstr_f3 DiverseNtwrk_f4 GritPersistCnstr_mean   DrvAchmtCnstr_mean BlfSelfFateCnstr_mean DiverseNtwrk_mean vle_age gender marital_status children nfamilymembers nearningmembers priorbizexp_flag graduate_flag internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn vle_training_dur emp_yn employee_training_yn emp_training_dur total_emp csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn future_outlook  commcredit_flag2 communitycredit_flag {
display "`x'"
ttest `x', by(ClusMn4KM_v1)
}

use "cscdata_26Jun.dta", clear


drop if ClusMn4KM_v1 == 1
drop if ClusMn4KM_v1 == 4
foreach x in earnings_cscservices Sales_AMT lnSalesAmt Sales_Count formspm_total2 Sales_AMT_pm abnormal_inc HHI GritPersistCnstr_f1 DrvAchmtCnstr_f2 BlfSelfFateCnstr_f3 DiverseNtwrk_f4 GritPersistCnstr_mean   DrvAchmtCnstr_mean BlfSelfFateCnstr_mean DiverseNtwrk_mean vle_age gender marital_status children nfamilymembers nearningmembers priorbizexp_flag graduate_flag internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn vle_training_dur emp_yn employee_training_yn emp_training_dur total_emp csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn future_outlook  commcredit_flag2 communitycredit_flag {
display "`x'"
ttest `x', by(ClusMn4KM_v1)
}

use "cscdata_26Jun.dta", clear

drop if ClusMn4KM_v1 == 1
drop if ClusMn4KM_v1 == 2
foreach x in earnings_cscservices Sales_AMT lnSalesAmt Sales_Count formspm_total2 Sales_AMT_pm abnormal_inc HHI GritPersistCnstr_f1 DrvAchmtCnstr_f2 BlfSelfFateCnstr_f3 DiverseNtwrk_f4 GritPersistCnstr_mean   DrvAchmtCnstr_mean BlfSelfFateCnstr_mean DiverseNtwrk_mean vle_age gender marital_status children nfamilymembers nearningmembers priorbizexp_flag graduate_flag internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn vle_training_dur emp_yn employee_training_yn emp_training_dur total_emp csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn future_outlook  commcredit_flag2 communitycredit_flag {
display "`x'"
ttest `x', by(ClusMn4KM_v1)
}

use "cscdata_26Jun.dta", clear


foreach x in earnings_cscservices Sales_AMT lnSalesAmt Sales_Count formspm_total2 Sales_AMT_pm abnormal_inc HHI GritPersistCnstr_f1 DrvAchmtCnstr_f2 BlfSelfFateCnstr_f3 DiverseNtwrk_f4 GritPersistCnstr_mean   DrvAchmtCnstr_mean BlfSelfFateCnstr_mean DiverseNtwrk_mean  internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn emp_yn employee_training_yn emp_training_dur total_emp csc_nvillages mkting_campaigns_yn future_outlook {
reg `x' i.ClusMn4KM_v1 
reg `x' i.ClusMn4KM_v1 vle_age gender graduate_flag priorbizexp_flag nfamilymembers nearningmembers vle_training_dur distance_csc_csc distance_csc_distrhq csc_electricity_hrs agri_labourer_earnings_pd commcredit_flag2 communitycredit_flag EntreEnv_f1 
}


/*
foreach x in  vle_age gender marital_status children nfamilymembers nearningmembers  internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn vle_training_dur emp_yn employee_training_yn emp_training_dur csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn future_outlook  priorbizexp_flag graduate_flag total_emp commcredit_flag2 communitycredit_flag {
display `x'
anova `x' ClusMn4KM_v1
}
*/

** other regressions **

foreach x in commcredit_flag2 communitycredit_flag {
reg `x' smartphone_usage_yn internet_access_home_yn internet_usage_home_hrspweek i.ClusMn4KM_v1 vle_age gender graduate_flag priorbizexp_flag nfamilymembers nearningmembers vle_training_dur distance_csc_csc distance_csc_distrhq csc_electricity_hrs agri_labourer_earnings_pd  EntreEnv_f1 
}

** standard deviations **

foreach x in vle_age nfamilymembers children nearningmembers distance_csc_town distance_csc_postoffice distance_csc_distrhq distance_csc_bank distance_csc_csc GritPersistCnstr_mean DrvAchmtCnstr_mean BlfSelfFateCnstr_mean DiverseNtwrk_mean internet_usage_home_hrspweek investment_amt_cscsetup no_fundsources{
egen s`x' = std(`x')
}


foreach x in svle_age snfamilymembers schildren snearningmembers sdistance_csc_town sdistance_csc_postoffice sdistance_csc_distrhq sdistance_csc_bank sdistance_csc_csc sGritPersistCnstr_mean sDrvAchmtCnstr_mean sBlfSelfFateCnstr_mean sDiverseNtwrk_mean sinternet_usage_home_hrspweek sinvestment_amt_cscsetup no_fundsources{
gen `x'_lh = 1 if `x' >= 0
recode `x'_lh .=0
}

egen std_salesamt = std(Sales_AMT )
egen std_salescount = std(Sales_Count )
egen std_earnings = std(earnings_cscservices )
egen sincome_abnrml = std(income_abnrml )

foreach x in std_salesamt std_salescount std_earnings sincome_abnrml{
gen `x'_lh = 1 if `x' >= 0
recode `x'_lh .=0
}

*** create environment standard deviation variables ***

foreach x in entre_public_attitude entre_success_promo entre_skills_training entre_success_recognition entre_marketops_growth{
egen s`x' = std(`x')
}

*** create low high dummies for environment variables ***

foreach x in entre_public_attitude entre_success_promo entre_skills_training entre_success_recognition entre_marketops_growth{
gen `x'_lh = 1 if s`x' >= 0
recode `x'_lh .=0
}




**** low-high analysis ***
sort sGritPersistCnstr_mean_lh 
by sGritPersistCnstr_mean_lh : summarize svle_age_lh  snfamilymembers_lh  schildren_lh snearningmembers_lh  graduate_flag priorbizexp_flag sdistance_csc_town_lh sdistance_csc_postoffice_lh sdistance_csc_distrhq_lh sdistance_csc_bank_lh sdistance_csc_csc_lh smartphone_usage_yn internet_access_home_yn sinternet_usage_home_hrspweek_lh sinvestment_amt_cscsetup_lh commcredit_flag2 communitycredit_flag source_FamilyMemberFriendRe sno_fundsources_lh mkting_campaigns_yn 

sort sDrvAchmtCnstr_mean_lh
by sDrvAchmtCnstr_mean_lh: summarize svle_age_lh  snfamilymembers_lh  schildren_lh snearningmembers_lh  graduate_flag priorbizexp_flag sdistance_csc_town_lh sdistance_csc_postoffice_lh sdistance_csc_distrhq_lh sdistance_csc_bank_lh sdistance_csc_csc_lh smartphone_usage_yn internet_access_home_yn sinternet_usage_home_hrspweek_lh sinvestment_amt_cscsetup_lh commcredit_flag2 communitycredit_flag source_FamilyMemberFriendRe sno_fundsources_lh mkting_campaigns_yn 

sort sBlfSelfFateCnstr_mean_lh 
by sBlfSelfFateCnstr_mean_lh: summarize svle_age_lh  snfamilymembers_lh  schildren_lh snearningmembers_lh  graduate_flag priorbizexp_flag sdistance_csc_town_lh sdistance_csc_postoffice_lh sdistance_csc_distrhq_lh sdistance_csc_bank_lh sdistance_csc_csc_lh smartphone_usage_yn internet_access_home_yn sinternet_usage_home_hrspweek_lh sinvestment_amt_cscsetup_lh commcredit_flag2 communitycredit_flag source_FamilyMemberFriendRe sno_fundsources_lh mkting_campaigns_yn

sort sDiverseNtwrk_mean_lh 
by sDiverseNtwrk_mean_lh: summarize svle_age_lh  snfamilymembers_lh  schildren_lh snearningmembers_lh  graduate_flag priorbizexp_flag sdistance_csc_town_lh sdistance_csc_postoffice_lh sdistance_csc_distrhq_lh sdistance_csc_bank_lh sdistance_csc_csc_lh smartphone_usage_yn internet_access_home_yn sinternet_usage_home_hrspweek_lh sinvestment_amt_cscsetup_lh commcredit_flag2 communitycredit_flag source_FamilyMemberFriendRe sno_fundsources_lh mkting_campaigns_yn



sort std_salesamt_lh 
by std_salesamt_lh : summarize svle_age_lh  snfamilymembers_lh  schildren_lh snearningmembers_lh  graduate_flag priorbizexp_flag sdistance_csc_town_lh sdistance_csc_postoffice_lh sdistance_csc_distrhq_lh sdistance_csc_bank_lh sdistance_csc_csc_lh smartphone_usage_yn internet_access_home_yn sinternet_usage_home_hrspweek_lh sinvestment_amt_cscsetup_lh commcredit_flag2 communitycredit_flag source_FamilyMemberFriendRe sno_fundsources_lh mkting_campaigns_yn

sort std_salescount_lh 
by std_salescount_lh : summarize svle_age_lh  snfamilymembers_lh  schildren_lh snearningmembers_lh  graduate_flag priorbizexp_flag sdistance_csc_town_lh sdistance_csc_postoffice_lh sdistance_csc_distrhq_lh sdistance_csc_bank_lh sdistance_csc_csc_lh smartphone_usage_yn internet_access_home_yn sinternet_usage_home_hrspweek_lh sinvestment_amt_cscsetup_lh commcredit_flag2 communitycredit_flag source_FamilyMemberFriendRe sno_fundsources_lh mkting_campaigns_yn

sort std_earnings_lh
by std_earnings_lh : summarize svle_age_lh  snfamilymembers_lh  schildren_lh snearningmembers_lh  graduate_flag priorbizexp_flag sdistance_csc_town_lh sdistance_csc_postoffice_lh sdistance_csc_distrhq_lh sdistance_csc_bank_lh sdistance_csc_csc_lh smartphone_usage_yn internet_access_home_yn sinternet_usage_home_hrspweek_lh sinvestment_amt_cscsetup_lh commcredit_flag2 communitycredit_flag source_FamilyMemberFriendRe sno_fundsources_lh mkting_campaigns_yn






********* descriptives by low- high ***

sort std_salesamt_lh 
by std_salesamt_lh : summarize vle_age  nfamilymembers  children nearningmembers  graduate_flag priorbizexp_flag distance_csc_town distance_csc_postoffice distance_csc_distrhq distance_csc_bank distance_csc_csc smartphone_usage_yn internet_access_home_yn internet_usage_home_hrspweek investment_amt_cscsetup commcredit_flag2 communitycredit_flag source_FamilyMemberFriendRe no_fundsources mkting_campaigns_yn GritPersistCnstr_mean DrvAchmtCnstr_mean BlfSelfFateCnstr_mean DiverseNtwrk_mean vle_training_yn vle_training_dur employee_training_yn emp_training_dur clv_mean crv_mean civ_mean ckv_mean

sort std_salescount_lh 
by std_salescount_lh : summarize vle_age  nfamilymembers  children nearningmembers  graduate_flag priorbizexp_flag distance_csc_town distance_csc_postoffice distance_csc_distrhq distance_csc_bank distance_csc_csc smartphone_usage_yn internet_access_home_yn internet_usage_home_hrspweek investment_amt_cscsetup commcredit_flag2 communitycredit_flag source_FamilyMemberFriendRe no_fundsources mkting_campaigns_yn GritPersistCnstr_mean DrvAchmtCnstr_mean BlfSelfFateCnstr_mean DiverseNtwrk_mean vle_training_yn vle_training_dur employee_training_yn emp_training_dur clv_mean crv_mean civ_mean ckv_mean

sort std_earnings_lh
by std_earnings_lh : summarize vle_age  nfamilymembers  children nearningmembers  graduate_flag priorbizexp_flag distance_csc_town distance_csc_postoffice distance_csc_distrhq distance_csc_bank distance_csc_csc smartphone_usage_yn internet_access_home_yn internet_usage_home_hrspweek investment_amt_cscsetup commcredit_flag2 communitycredit_flag source_FamilyMemberFriendRe no_fundsources mkting_campaigns_yn GritPersistCnstr_mean DrvAchmtCnstr_mean BlfSelfFateCnstr_mean DiverseNtwrk_mean vle_training_yn vle_training_dur employee_training_yn emp_training_dur clv_mean crv_mean civ_mean ckv_mean

sort sGritPersistCnstr_mean_lh 
by sGritPersistCnstr_mean_lh : summarize vle_age  nfamilymembers  children nearningmembers  graduate_flag priorbizexp_flag distance_csc_town distance_csc_postoffice distance_csc_distrhq distance_csc_bank distance_csc_csc smartphone_usage_yn internet_access_home_yn internet_usage_home_hrspweek investment_amt_cscsetup commcredit_flag2 communitycredit_flag source_FamilyMemberFriendRe no_fundsources mkting_campaigns_yn Sales_AMT Sales_Count earnings_cscservices clv_mean crv_mean civ_mean ckv_mean

sort sDrvAchmtCnstr_mean_lh
by sDrvAchmtCnstr_mean_lh: summarize vle_age  nfamilymembers  children nearningmembers  graduate_flag priorbizexp_flag distance_csc_town distance_csc_postoffice distance_csc_distrhq distance_csc_bank distance_csc_csc smartphone_usage_yn internet_access_home_yn internet_usage_home_hrspweek investment_amt_cscsetup commcredit_flag2 communitycredit_flag source_FamilyMemberFriendRe no_fundsources mkting_campaigns_yn Sales_AMT Sales_Count earnings_cscservices clv_mean crv_mean civ_mean ckv_mean

sort sBlfSelfFateCnstr_mean_lh 
by sBlfSelfFateCnstr_mean_lh: summarize vle_age  nfamilymembers  children nearningmembers  graduate_flag priorbizexp_flag distance_csc_town distance_csc_postoffice distance_csc_distrhq distance_csc_bank distance_csc_csc smartphone_usage_yn internet_access_home_yn internet_usage_home_hrspweek investment_amt_cscsetup commcredit_flag2 communitycredit_flag source_FamilyMemberFriendRe no_fundsources mkting_campaigns_yn Sales_AMT Sales_Count earnings_cscservices clv_mean crv_mean civ_mean ckv_mean

sort sDiverseNtwrk_mean_lh 
by sDiverseNtwrk_mean_lh: summarize vle_age  nfamilymembers  children nearningmembers  graduate_flag priorbizexp_flag distance_csc_town distance_csc_postoffice distance_csc_distrhq distance_csc_bank distance_csc_csc smartphone_usage_yn internet_access_home_yn internet_usage_home_hrspweek investment_amt_cscsetup commcredit_flag2 communitycredit_flag source_FamilyMemberFriendRe no_fundsources mkting_campaigns_yn Sales_AMT Sales_Count earnings_cscservices clv_mean crv_mean civ_mean ckv_mean

sort sincome_abnrml_lh  
by sincome_abnrml_lh  : summarize vle_age  nfamilymembers  children nearningmembers  graduate_flag priorbizexp_flag distance_csc_town distance_csc_postoffice distance_csc_distrhq distance_csc_bank distance_csc_csc smartphone_usage_yn internet_access_home_yn internet_usage_home_hrspweek investment_amt_cscsetup commcredit_flag2 communitycredit_flag source_FamilyMemberFriendRe no_fundsources mkting_campaigns_yn GritPersistCnstr_mean DrvAchmtCnstr_mean BlfSelfFateCnstr_mean DiverseNtwrk_mean vle_training_yn vle_training_dur employee_training_yn emp_training_dur clv_mean crv_mean civ_mean ckv_mean


gen salescnt_abnrml= Sales_Count - SalesCntDistr

sort ssalescnt_abnrml_lh  
by ssalescnt_abnrml_lh  : summarize vle_age  nfamilymembers  children nearningmembers  graduate_flag priorbizexp_flag distance_csc_town distance_csc_postoffice distance_csc_distrhq distance_csc_bank distance_csc_csc smartphone_usage_yn internet_access_home_yn internet_usage_home_hrspweek investment_amt_cscsetup commcredit_flag2 communitycredit_flag source_FamilyMemberFriendRe no_fundsources mkting_campaigns_yn GritPersistCnstr_mean DrvAchmtCnstr_mean BlfSelfFateCnstr_mean DiverseNtwrk_mean vle_training_yn vle_training_dur employee_training_yn emp_training_dur clv_mean crv_mean civ_mean ckv_mean

*** low high descriptives for environment variables **

entre_public_attitude_lh entre_success_promo_lh entre_skills_training_lh entre_success_recognition_lh entre_marketops_growth_lh

sort entre_public_attitude_lh  
by entre_public_attitude_lh  : summarize vle_age  nfamilymembers  children nearningmembers  graduate_flag priorbizexp_flag distance_csc_town distance_csc_postoffice distance_csc_distrhq distance_csc_bank distance_csc_csc smartphone_usage_yn internet_access_home_yn internet_usage_home_hrspweek investment_amt_cscsetup commcredit_flag2 communitycredit_flag source_FamilyMemberFriendRe no_fundsources mkting_campaigns_yn vle_training_yn vle_training_dur employee_training_yn emp_training_dur GritPersistCnstr_mean DrvAchmtCnstr_mean BlfSelfFateCnstr_mean DiverseNtwrk_mean  clv_mean crv_mean civ_mean ckv_mean

sort entre_public_attitude_lh  
by entre_public_attitude_lh  : summarize earnings_cscservices Sales_AMT Sales_Count income_abnrml salescnt_abnrml



sort entre_success_promo_lh  
by entre_success_promo_lh  : summarize vle_age  nfamilymembers  children nearningmembers  graduate_flag priorbizexp_flag distance_csc_town distance_csc_postoffice distance_csc_distrhq distance_csc_bank distance_csc_csc smartphone_usage_yn internet_access_home_yn internet_usage_home_hrspweek investment_amt_cscsetup commcredit_flag2 communitycredit_flag source_FamilyMemberFriendRe no_fundsources mkting_campaigns_yn vle_training_yn vle_training_dur employee_training_yn emp_training_dur GritPersistCnstr_mean DrvAchmtCnstr_mean BlfSelfFateCnstr_mean DiverseNtwrk_mean clv_mean crv_mean civ_mean ckv_mean

sort entre_success_promo_lh  
by entre_success_promo_lh  : summarize earnings_cscservices Sales_AMT Sales_Count income_abnrml salescnt_abnrml

sort entre_skills_training_lh  
by entre_skills_training_lh  : summarize vle_age  nfamilymembers  children nearningmembers  graduate_flag priorbizexp_flag distance_csc_town distance_csc_postoffice distance_csc_distrhq distance_csc_bank distance_csc_csc smartphone_usage_yn internet_access_home_yn internet_usage_home_hrspweek investment_amt_cscsetup commcredit_flag2 communitycredit_flag source_FamilyMemberFriendRe no_fundsources mkting_campaigns_yn vle_training_yn vle_training_dur employee_training_yn emp_training_dur GritPersistCnstr_mean DrvAchmtCnstr_mean BlfSelfFateCnstr_mean DiverseNtwrk_mean clv_mean crv_mean civ_mean ckv_mean

sort entre_skills_training_lh  
by entre_skills_training_lh  : summarize earnings_cscservices Sales_AMT Sales_Count income_abnrml salescnt_abnrml

sort entre_success_recognition_lh  
by entre_success_recognition_lh  : summarize vle_age  nfamilymembers  children nearningmembers  graduate_flag priorbizexp_flag distance_csc_town distance_csc_postoffice distance_csc_distrhq distance_csc_bank distance_csc_csc smartphone_usage_yn internet_access_home_yn internet_usage_home_hrspweek investment_amt_cscsetup commcredit_flag2 communitycredit_flag source_FamilyMemberFriendRe no_fundsources mkting_campaigns_yn vle_training_yn vle_training_dur employee_training_yn emp_training_dur GritPersistCnstr_mean DrvAchmtCnstr_mean BlfSelfFateCnstr_mean DiverseNtwrk_mean clv_mean crv_mean civ_mean ckv_mean

sort entre_success_recognition_lh  
by entre_success_recognition_lh  : summarize earnings_cscservices Sales_AMT Sales_Count income_abnrml salescnt_abnrml

sort entre_marketops_growth_lh  
by entre_marketops_growth_lh  : summarize vle_age  nfamilymembers  children nearningmembers  graduate_flag priorbizexp_flag distance_csc_town distance_csc_postoffice distance_csc_distrhq distance_csc_bank distance_csc_csc smartphone_usage_yn internet_access_home_yn internet_usage_home_hrspweek investment_amt_cscsetup commcredit_flag2 communitycredit_flag source_FamilyMemberFriendRe no_fundsources mkting_campaigns_yn vle_training_yn vle_training_dur employee_training_yn emp_training_dur GritPersistCnstr_mean DrvAchmtCnstr_mean BlfSelfFateCnstr_mean DiverseNtwrk_mean clv_mean crv_mean civ_mean ckv_mean

sort entre_marketops_growth_lh  
by entre_marketops_growth_lh  : summarize earnings_cscservices Sales_AMT Sales_Count income_abnrml salescnt_abnrml

*** state vs entrepreneurial opportunities **

tab state entre_public_attitude_lh 
tab state entre_success_promo_lh 
tab state entre_skills_training_lh 
tab state entre_success_recognition_lh 
tab state entre_marketops_growth_lh 



** outcomes **

foreach x in lnSales_AMT lnSales_Count lnearnings_cscservices{
reg `x' sGritPersistCnstr_mean_lh sDrvAchmtCnstr_mean_lh sBlfSelfFateCnstr_mean_lh sDiverseNtwrk_mean_lh
}

foreach x in lnSales_AMT lnSales_Count lnearnings_cscservices{
reg `x' sGritPersistCnstr_mean sDrvAchmtCnstr_mean sBlfSelfFateCnstr_mean sDiverseNtwrk_mean
}

** Analysis part 1 ***

tab sDrvAchmtCnstr_mean_lh , gen(drivedummy)
tab sGritPersistCnstr_mean_lh, generate(gritdummy)
tab sBlfSelfFateCnstr_mean_lh, generate(selfbeliefdummy)
tab sDiverseNtwrk_mean_lh, generate(diversenetworksdummy) 
tab std_salesamt_lh, gen(salesamtdummy)
tab std_salescount_lh , gen(salescountdummy)
tab std_earnings_lh , gen(earningsdummy)
tab sincome_abnrml_lh, gen(abnrmlsalesincmedummy)
tab ssalescnt_abnrml_lh, gen(abnrmlsalescntdummy)

** generate environment dummies **

tab entre_public_attitude_lh, gen (entrepubattdum)
tab entre_success_promo_lh, gen(entresuccpromdum)
tab entre_skills_training_lh, gen(entreskiltrdum)
tab entre_success_recognition_lh, gen(entresuccrecogdum)
tab entre_marketops_growth_lh, gen(marketopsgrwthdum)




*** location **
display "location"
foreach x in gritdummy drivedummy selfbeliefdummy diversenetworksdummy salesamtdummy salescountdummy earningsdummy{
foreach y in distance_csc_town distance_csc_postoffice distance_csc_distrhq distance_csc_bank distance_csc_csc {
reg `y' `x'1 `x'2, noconstant
lincom `x'1-`x'2
}
}


foreach x in abnrmlsalesincmedummy abnrmlsalescntdummy {
foreach y in distance_csc_town distance_csc_postoffice distance_csc_distrhq distance_csc_bank distance_csc_csc {
reg `y' `x'1 `x'2, noconstant
lincom `x'1-`x'2
}
}

foreach x in entrepubattdum entresuccpromdum entreskiltrdum entresuccrecogdum marketopsgrwthdum{
foreach y in distance_csc_town distance_csc_postoffice distance_csc_distrhq distance_csc_bank distance_csc_csc {
reg `y' `x'1 `x'2, noconstant
lincom `x'1-`x'2
}
}


*** dems **
display "demographics"
foreach x in gritdummy drivedummy selfbeliefdummy diversenetworksdummy salesamtdummy salescountdummy earningsdummy{
foreach y in vle_age nfamilymembers children nearningmembers graduate_flag priorbizexp_flag {
reg `y' `x'1 `x'2, noconstant
lincom `x'2-`x'1
}
}

display "demographics"
foreach x in abnrmlsalesincmedummy abnrmlsalescntdummy {
foreach y in vle_age nfamilymembers children nearningmembers graduate_flag priorbizexp_flag {
reg `y' `x'1 `x'2, noconstant
lincom `x'2-`x'1
}
}

display "demographics"
foreach x in entrepubattdum entresuccpromdum entreskiltrdum entresuccrecogdum marketopsgrwthdum{
foreach y in vle_age nfamilymembers children nearningmembers graduate_flag priorbizexp_flag {
reg `y' `x'1 `x'2, noconstant
lincom `x'2-`x'1
}
}



** strategies **
** digital literacy **
display "digital literacy"
foreach x in gritdummy drivedummy selfbeliefdummy diversenetworksdummy salesamtdummy salescountdummy earningsdummy{
foreach y in smartphone_usage_yn internet_access_home_yn internet_usage_home_hrspweek {
reg `y' `x'1 `x'2, noconstant
lincom `x'2-`x'1
}
}

display "digital literacy"
foreach x in abnrmlsalesincmedummy abnrmlsalescntdummy{
foreach y in smartphone_usage_yn internet_access_home_yn internet_usage_home_hrspweek {
reg `y' `x'1 `x'2, noconstant
lincom `x'2-`x'1
}
}

display "digital literacy"
foreach x in entrepubattdum entresuccpromdum entreskiltrdum entresuccrecogdum marketopsgrwthdum{
foreach y in smartphone_usage_yn internet_access_home_yn internet_usage_home_hrspweek {
reg `y' `x'1 `x'2, noconstant
lincom `x'2-`x'1
}
}



** seeking capital **
display "seeking capital"
foreach x in gritdummy drivedummy selfbeliefdummy diversenetworksdummy salesamtdummy salescountdummy earningsdummy{
foreach y in investment_amt_cscsetup no_fundsources commcredit_flag2 communitycredit_flag source_FamilyMemberFriendRe {
reg `y' `x'1 `x'2, noconstant
lincom `x'2-`x'1
}
}

display "seeking capital"
foreach x in abnrmlsalesincmedummy abnrmlsalescntdummy{
foreach y in investment_amt_cscsetup no_fundsources commcredit_flag2 communitycredit_flag source_FamilyMemberFriendRe {
reg `y' `x'1 `x'2, noconstant
lincom `x'2-`x'1
}
}

display "seeking capital"
foreach x in entrepubattdum entresuccpromdum entreskiltrdum entresuccrecogdum marketopsgrwthdum{
foreach y in investment_amt_cscsetup no_fundsources commcredit_flag2 communitycredit_flag source_FamilyMemberFriendRe {
reg `y' `x'1 `x'2, noconstant
lincom `x'2-`x'1
}
}


** engage in marketing **
display "marketing"
foreach x in gritdummy drivedummy selfbeliefdummy diversenetworksdummy salesamtdummy salescountdummy earningsdummy{
foreach y in mkting_campaigns_yn {
reg `y' `x'1 `x'2, noconstant
lincom `x'2-`x'1
}
}

display "marketing"
foreach x in abnrmlsalesincmedummy abnrmlsalescntdummy{
foreach y in mkting_campaigns_yn {
reg `y' `x'1 `x'2, noconstant
lincom `x'2-`x'1
}
}

display "marketing"
foreach x in entrepubattdum entresuccpromdum entreskiltrdum entresuccrecogdum marketopsgrwthdum{
foreach y in mkting_campaigns_yn {
reg `y' `x'1 `x'2, noconstant
lincom `x'2-`x'1
}
}



** outcomes **
display "outcomes"
foreach x in gritdummy drivedummy selfbeliefdummy diversenetworksdummy {
foreach y in earnings_cscservices Sales_AMT Sales_Count {
reg `y' `x'1 `x'2, noconstant
lincom `x'2-`x'1
}
}

display "outcomes"
foreach x in abnrmlsalesincmedummy abnrmlsalescntdummy {
foreach y in earnings_cscservices Sales_AMT Sales_Count {
reg `y' `x'1 `x'2, noconstant
lincom `x'2-`x'1
}
}

display "outcomes"
foreach x in entrepubattdum entresuccpromdum entreskiltrdum entresuccrecogdum marketopsgrwthdum{
foreach y in earnings_cscservices Sales_AMT Sales_Count income_abnrml salescnt_abnrml {
reg `y' `x'1 `x'2, noconstant
lincom `x'2-`x'1
}
}




** customer engagement **
foreach x in gritdummy drivedummy selfbeliefdummy diversenetworksdummy salesamtdummy salescountdummy earningsdummy {
foreach y in clv_mean crv_mean civ_mean ckv_mean {
reg `y' `x'1 `x'2, noconstant
lincom `x'2-`x'1
}
}

foreach x in abnrmlsalesincmedummy abnrmlsalescntdummy {
foreach y in clv_mean crv_mean civ_mean ckv_mean {
reg `y' `x'1 `x'2, noconstant
lincom `x'2-`x'1
}
}

foreach x in entrepubattdum entresuccpromdum entreskiltrdum entresuccrecogdum marketopsgrwthdum {
foreach y in clv_mean crv_mean civ_mean ckv_mean {
reg `y' `x'1 `x'2, noconstant
lincom `x'2-`x'1
}
}


** performance vs characteristics **
display "performance"
foreach x in salesamtdummy salescountdummy earningsdummy {
foreach y in  GritPersistCnstr_mean DrvAchmtCnstr_mean BlfSelfFateCnstr_mean DiverseNtwrk_mean {
reg `y' `x'1 `x'2, noconstant
lincom `x'2-`x'1
}
}

display "performance"
foreach x in abnrmlsalesincmedummy abnrmlsalescntdummy  {
foreach y in  GritPersistCnstr_mean DrvAchmtCnstr_mean BlfSelfFateCnstr_mean DiverseNtwrk_mean {
reg `y' `x'1 `x'2, noconstant
lincom `x'2-`x'1
}
}

display "performance"
foreach x in entrepubattdum entresuccpromdum entreskiltrdum entresuccrecogdum marketopsgrwthdum {
foreach y in  GritPersistCnstr_mean DrvAchmtCnstr_mean BlfSelfFateCnstr_mean DiverseNtwrk_mean {
reg `y' `x'1 `x'2, noconstant
lincom `x'2-`x'1
}
}



** performance vs training **
display "performance"
foreach x in salesamtdummy salescountdummy earningsdummy {
foreach y in  vle_training_yn vle_training_dur employee_training_yn emp_training_dur {
reg `y' `x'1 `x'2, noconstant
lincom `x'2-`x'1
}
}

display "performance"
foreach x in abnrmlsalesincmedummy abnrmlsalescntdummy {
foreach y in  vle_training_yn vle_training_dur employee_training_yn emp_training_dur {
reg `y' `x'1 `x'2, noconstant
lincom `x'2-`x'1
}
}

display "training"
foreach x in entrepubattdum entresuccpromdum entreskiltrdum entresuccrecogdum marketopsgrwthdum {
foreach y in  vle_training_yn vle_training_dur employee_training_yn emp_training_dur {
reg `y' `x'1 `x'2, noconstant
lincom `x'2-`x'1
}
}



foreach x in  vle_age gender marital_status children nfamilymembers nearningmembers  internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn vle_training_dur emp_yn employee_training_yn emp_training_dur csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn future_outlook  priorbizexp_flag graduate_flag total_emp commcredit_flag2 communitycredit_flag {
display "`x'"
ttest `x', by(std_salesamt_lh)
}

foreach x in  vle_age gender marital_status children nfamilymembers nearningmembers  internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn vle_training_dur emp_yn employee_training_yn emp_training_dur csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn future_outlook  priorbizexp_flag graduate_flag total_emp commcredit_flag2 communitycredit_flag {
display "`x'"
ttest `x', by(std_salescount_lh)
}

foreach x in  vle_age gender marital_status children nfamilymembers nearningmembers  internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn vle_training_dur emp_yn employee_training_yn emp_training_dur csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn future_outlook  priorbizexp_flag graduate_flag total_emp commcredit_flag2 communitycredit_flag {
display "`x'"
ttest `x', by(std_earnings_lh)
}

foreach x in  vle_age gender marital_status children nfamilymembers nearningmembers  internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn vle_training_dur emp_yn employee_training_yn emp_training_dur csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn future_outlook  priorbizexp_flag graduate_flag total_emp commcredit_flag2 communitycredit_flag {
display "`x'"
ttest `x', by(sDrvAchmtCnstr_mean_lh)
}
foreach x in  vle_age gender marital_status children nfamilymembers nearningmembers  internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn vle_training_dur emp_yn employee_training_yn emp_training_dur csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn future_outlook  priorbizexp_flag graduate_flag total_emp commcredit_flag2 communitycredit_flag {
display "`x'"
ttest `x', by(sGritPersistCnstr_mean_lh)
}
foreach x in  vle_age gender marital_status children nfamilymembers nearningmembers  internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn vle_training_dur emp_yn employee_training_yn emp_training_dur csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn future_outlook  priorbizexp_flag graduate_flag total_emp commcredit_flag2 communitycredit_flag {
display "`x'"
ttest `x', by(sBlfSelfFateCnstr_mean_lh)
}

foreach x in  vle_age gender marital_status children nfamilymembers nearningmembers  internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn vle_training_dur emp_yn employee_training_yn emp_training_dur csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn future_outlook  priorbizexp_flag graduate_flag total_emp commcredit_flag2 communitycredit_flag {
display "`x'"
ttest `x', by(sDiverseNtwrk_mean_lh)
}


tab sDrvAchmtCnstr_mean_lh , gen(drivedummy)
tab sGritPersistCnstr_mean_lh, generate(gritdummy)
tab sBlfSelfFateCnstr_mean_lh, generate(selfbeliefdummy)
tab sDiverseNtwrk_mean_lh, generate(diversenetworksdummy) 
tab std_salesamt_lh, gen(salesamtdummy)
tab std_salescount_lh , gen(salescountdummy)
tab std_earnings_lh , gen(earningsdummy)


** high low **
*** ttests by state ***



by state, sort: ttest investment_amt_cscsetup, by( std_salesamt_lh)
by state, sort: ttest investment_amt_cscsetup, by( std_salescount_lh)
by state, sort: ttest investment_amt_cscsetup, by( std_earnings_lh)
by state, sort: ttest investment_amt_cscsetup, by( sDrvAchmtCnstr_mean_lh)
by state, sort: ttest investment_amt_cscsetup, by( sGritPersistCnstr_mean_lh)
by state, sort: ttest investment_amt_cscsetup, by( sBlfSelfFateCnstr_mean_lh)
by state, sort: ttest investment_amt_cscsetup, by( sDiverseNtwrk_mean_lh)


foreach x in   internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn vle_training_dur emp_yn employee_training_yn emp_training_dur csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn future_outlook  priorbizexp_flag graduate_flag total_emp commcredit_flag2 communitycredit_flag {
display "`x' by std_salesamt_lh "
by state, sort: ttest `x', by(std_salesamt_lh)
}

foreach x in   internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn vle_training_dur emp_yn employee_training_yn emp_training_dur csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn future_outlook  priorbizexp_flag graduate_flag total_emp commcredit_flag2 communitycredit_flag {
display "`x' by std_salescount_lh"
by state, sort: ttest `x', by(std_salescount_lh)
}

foreach x in   internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn vle_training_dur emp_yn employee_training_yn emp_training_dur csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn future_outlook  priorbizexp_flag graduate_flag total_emp commcredit_flag2 communitycredit_flag {
display "`x' by std_earnings_lh"
by state, sort: ttest `x', by(std_earnings_lh)
}

foreach x in   internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn vle_training_dur emp_yn employee_training_yn emp_training_dur csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn future_outlook  priorbizexp_flag graduate_flag total_emp commcredit_flag2 communitycredit_flag {
display "`x' by sDrvAchmtCnstr_mean_lh"
by state, sort: ttest `x', by(sDrvAchmtCnstr_mean_lh)
}

foreach x in   internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn vle_training_dur emp_yn employee_training_yn emp_training_dur csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn future_outlook  priorbizexp_flag graduate_flag total_emp commcredit_flag2 communitycredit_flag {
display "`x' by sGritPersistCnstr_mean_lh"
by state, sort: ttest `x', by(sGritPersistCnstr_mean_lh)
}

foreach x in   internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn vle_training_dur emp_yn employee_training_yn emp_training_dur csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn future_outlook  priorbizexp_flag graduate_flag total_emp commcredit_flag2 communitycredit_flag {
display "`x' by sBlfSelfFateCnstr_mean_lh"
by state, sort: ttest `x', by(sBlfSelfFateCnstr_mean_lh)
}

foreach x in   internet_access_home_yn internet_usage_home_hrspweek smartphone_usage_yn nsources_income no_fundsources investment_amt_cscsetup hrs_perday_csc vle_training_yn vle_training_dur emp_yn employee_training_yn emp_training_dur csc_nvillages distance_csc_distrhq distance_csc_csc mkting_campaigns_yn future_outlook  priorbizexp_flag graduate_flag total_emp commcredit_flag2 communitycredit_flag {
display "`x' by sDiverseNtwrk_mean_lh"
by state, sort: ttest `x', by(sDiverseNtwrk_mean_lh)
}

********** code archive ******************
/*
** chars and environment **
foreach y in gritty_factorchar driveachmot_factorchar locusctrl_factorchar{
reg `y' vle_age  children nfamilymembers i.marital_status i.gender i.entre_public_attitude i.entre_success_promo i.entre_skills_training i.entre_success_recognition i.entre_marketops_growth 
}

** cluster check - calinski harabasz statistic optimal clusters **
cluster singlelinkage char_factor1 char_factor2 char_factor3, measure(L2)
cluster stop

*/

********** Socio Economic Impact ***********

foreach x in ntrips_govtoff distptrans_govtoff
foreach y in ntrips_cscs distptrans_csc


    trvltime_govtoff trvltime_csc cost_govtoff cost_csc waittime_govtoff waittime_csc nintermediaries_govtoff nintermediaries_csc wageloss_govtoff wageloss_csc nedlays_govt ndelays_csc ndenied_govt ndeined_csc



** customer engagement **
egen clv_mean = rmean(continuebuying_clv contenttrans_clv moneysworth_clv)
egen crv_mean = rmean(happyrefer_crv refercsc_crv)
egen civ_mean = rmean(activelydiscuss_civ cscexp_civ discussbenefits_civ)
egen ckv_mean = rmean(feedbackexp_ckv suggimprove_ckv suggnewprods_ckv)


** misc checks ***

gen govt_bldng = 1 if csc_rent_mthly ==0
recode govt_bldng .=0 
tab govt_bldng 

**** income before csc replacement ****
gen income_beforecsc_num =  1 if inc_bef_csc_str == "1"
recode income_beforecsc_num .= 2 if inc_bef_csc_str == "15"
recode income_beforecsc_num .= 3 if inc_bef_csc_str == "19"
recode income_beforecsc_num .= 3 if inc_bef_csc_str == "17"
recode income_beforecsc_num .= 4 if inc_bef_csc_str == "5"
recode income_beforecsc_num .= 5 if inc_bef_csc_str == "8"
recode income_beforecsc_num .= 6 if inc_bef_csc_str == "11"
recode income_beforecsc_num .= 2 if inc_bef_csc_str == "16"
recode income_beforecsc_num .= 7 if inc_bef_csc_str == "4"
recode income_beforecsc_num .= 4 if inc_bef_csc_str == "7"
recode income_beforecsc_num .= 5 if inc_bef_csc_str == "10"
recode income_beforecsc_num .= 6 if inc_bef_csc_str == "13"
recode income_beforecsc_num .= 7 if inc_bef_csc_str == "20"
recode income_beforecsc_num .= 3 if inc_bef_csc_str == "18"
recode income_beforecsc_num .= 7 if inc_bef_csc_str == "3"
recode income_beforecsc_num .= 2 if inc_bef_csc_str == "14"
recode income_beforecsc_num .= 4 if inc_bef_csc_str == "6"
recode income_beforecsc_num .= 6 if inc_bef_csc_str == "12"
recode income_beforecsc_num .= 1 if inc_bef_csc_str == "2"
recode income_beforecsc_num .= 5 if inc_bef_csc_str == "9"

*** variables ***
egen comps_mode = mode(computers_n ), by(state) maxmode
gen portalintegrationflag = 1 if state == 1
recode portalintegrationflag .= 1 if state == 4
recode portalintegrationflag .= 1 if state == 5
recode portalintegrationflag .= 1 if state == 6
recode portalintegrationflag .= 1 if state == 7
recode portalintegrationflag .= 1 if state == 10
recode portalintegrationflag .=0



egen digital_eqpmt = rsum(digicam_webcam_n printer_scanner_copier_n printer_scanner_n biometric_iris_scanner_n)


gen GDP = 51 if state == 1
recode GDP .= 80 if state ==2
recode GDP .= 230 if state == 3
recode GDP .= 217 if state == 4
recode GDP .= 430 if state == 5
recode GDP .= 70 if state == 6
recode GDP .= 80 if state == 7
recode GDP .= 130 if state == 8
recode GDP .= 230 if state == 9
recode GDP .= 160 if state == 10

gen population = 31 if state  == 1
recode population .= 103 if state  == 2
recode population .= 60 if state  == 3
recode population .= 61 if state  == 4
recode population .= 112 if state  == 5
recode population .= 42 if state  == 6
recode population .= 27 if state  == 7
recode population .= 35 if state  == 8
recode population .= 207 if state  == 9
recode population .= 91 if state  == 10

gen literacy = 0.73 if state  == 1
recode literacy .= 0.64 if state  == 2
recode literacy .= 0.79 if state  == 3
recode literacy .= 0.75 if state  == 4
recode literacy .= 0.83 if state  == 5
recode literacy .= 0.73 if state  == 6
recode literacy .= 0.77 if state  == 7
recode literacy .= 0.67 if state  == 8
recode literacy .= 0.70 if state  == 9
recode literacy .= 0.77 if state  == 10

gen lGDP = log(GDP)
gen lpopulation = log(1+population) 
gen lagriLabourerInc = log(1+ agri_labourer_earnings_pd )
gen lfarmerEarningspm = log(1+ farmer_earnings_pm )
gen GDPperCap = GDP / population 


************************

reg highDrive  GDPperCap highAgri highFInc  entre_success_promo entre_success_recognition entre_public_attitude entre_skills_training
outreg2 using "csc_24Jul2.doc",append
reg highGrit  GDPperCap highAgri highFInc  entre_success_promo entre_success_recognition entre_public_attitude entre_skills_training
outreg2 using "csc_24Jul2.doc",append
reg highDiverse  GDPperCap highAgri highFInc entre_success_promo entre_success_recognition entre_public_attitude entre_skills_training
outreg2 using "csc_24Jul2.doc",append
reg highBelief2 GDPperCap highAgri highFInc entre_success_promo entre_success_recognition entre_public_attitude entre_skills_training
outreg2 using "csc_24Jul2.doc",append



/*
reg highDrive  lGDPperCapita lagriLabourerInc lfarmerEarningspm  
outreg2 using "csc_24Jul4.doc",append
reg highGrit  lGDPperCapita lagriLabourerInc lfarmerEarningspm  
outreg2 using "csc_24Jul4.doc",append
reg highDiverse  lGDPperCapita lagriLabourerInc lfarmerEarningspm 
outreg2 using "csc_24Jul4.doc",append
reg highBelief2 lGDPperCapita lagriLabourerInc lfarmerEarningspm 
outreg2 using "csc_24Jul4.doc",append

reg highDrive  lGDPperCapita lagriLabourerInc lfarmerEarningspm  entre_success_promo entre_success_recognition entre_public_attitude entre_skills_training
outreg2 using "csc_24Jul4.doc",append
reg highGrit  lGDPperCapita lagriLabourerInc lfarmerEarningspm  entre_success_promo entre_success_recognition entre_public_attitude entre_skills_training
outreg2 using "csc_24Jul4.doc",append
reg highDiverse  lGDPperCapita lagriLabourerInc lfarmerEarningspm entre_success_promo entre_success_recognition entre_public_attitude entre_skills_training
outreg2 using "csc_24Jul4.doc",append
reg highBelief2 lGDPperCapita lagriLabourerInc lfarmerEarningspm entre_success_promo entre_success_recognition entre_public_attitude entre_skills_training
outreg2 using "csc_24Jul4.doc",append
*/


reg sDrvAchmtCnstr_mean lGDPperCapita lagriLabourerInc lfarmerEarningspm 
outreg2 using "csc_24Jul5.doc",append
reg sGritPersistCnstr_mean lGDPperCapita lagriLabourerInc lfarmerEarningspm 
outreg2 using "csc_24Jul5.doc",append
reg sDiverseNtwrk_mean lGDPperCapita lagriLabourerInc  lfarmerEarningspm 
outreg2 using "csc_24Jul5.doc",append
reg sBlfSelfFateCnstr_mean lGDPperCapita lagriLabourerInc lfarmerEarningspm 
outreg2 using "csc_24Jul5.doc",append

reg sDrvAchmtCnstr_mean lGDPperCapita lagriLabourerInc lfarmerEarningspm entre_success_promo entre_success_recognition entre_public_attitude entre_skills_training
outreg2 using "csc_24Jul5.doc",append
reg sGritPersistCnstr_mean lGDPperCapita lagriLabourerInc lfarmerEarningspm entre_success_promo entre_success_recognition entre_public_attitude entre_skills_training
outreg2 using "csc_24Jul5.doc",append
reg sDiverseNtwrk_mean lGDPperCapita lagriLabourerInc  lfarmerEarningspm entre_success_promo entre_success_recognition entre_public_attitude entre_skills_training
outreg2 using "csc_24Jul5.doc",append
reg sBlfSelfFateCnstr_mean lGDPperCapita lagriLabourerInc lfarmerEarningspm entre_success_promo entre_success_recognition entre_public_attitude entre_skills_training
outreg2 using "csc_24Jul5.doc",append

reg priorbizexp_flag lGDPperCapita lagriLabourerInc lfarmerEarningspm 
outreg2 using "csc_24Jul5.doc",append
reg priorbizexp_flag lGDPperCapita lagriLabourerInc lfarmerEarningspm entre_success_promo entre_success_recognition entre_public_attitude entre_skills_training
outreg2 using "csc_24Jul5.doc",append
reg priorbizexp_flag lGDPperCapita lagriLabourerInc lfarmerEarningspm sDrvAchmtCnstr_mean sGritPersistCnstr_mean sDiverseNtwrk_mean sBlfSelfFateCnstr_mean entre_success_promo entre_success_recognition entre_public_attitude entre_skills_training
outreg2 using "csc_24Jul5.doc",append



/*
reg sDrvAchmtCnstr_mean lGDPperCapita highAgri highFInc entre_success_promo entre_success_recognition entre_public_attitude entre_skills_training
outreg2 using "csc_24Jul3.doc",append
reg sGritPersistCnstr_mean lGDPperCapita highAgri highFInc entre_success_promo entre_success_recognition entre_public_attitude entre_skills_training
outreg2 using "csc_24Jul3.doc",append
reg sDiverseNtwrk_mean lGDPperCapita highAgri  highFInc entre_success_promo entre_success_recognition entre_public_attitude entre_skills_training
outreg2 using "csc_24Jul3.doc",append
reg sBlfSelfFateCnstr_mean lGDPperCapita highAgri highFInc entre_success_promo entre_success_recognition entre_public_attitude entre_skills_training
outreg2 using "csc_24Jul3.doc",append

*/

*** archival data***
gen GDP = 51 if State  == "Assam"
recode GDP .= 80 if State  == "Bihar"
recode GDP .= 230 if State  == "Gujarat"
recode GDP .= 217 if State  == "Karnataka"
recode GDP .= 430 if State  == "Maharashtra"
recode GDP .= 70 if State  == "Odisha"
recode GDP .= 80 if State  == "Punjab"
recode GDP .= 130 if State  == "Telangana"
recode GDP .= 230 if State  == "Uttar Pradesh"
recode GDP .= 160 if State  == "West Bengal"



