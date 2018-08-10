###### summary stats - dir level #####

drop if female_yn == .

summarize female_yn l75_att_yn num_otherboards tenure dir_age retired  audit_member_yn compensation_committee_membr_yn nom_comm_member_yn corp_gov_comm_member_yn


**### generate code - board level data ###

 gen single_femaledir = 1 if female_n ==1 
 recode single_femaledir .=0
 gen female_dummy = 0 if female_n ==0
 recode female_dummy .=1

gen lntobinsq = ln(1+ tobinQ )
gen lnsales = ln(1+sales)
gen lntobinsq_ab = ln(1+ tobinq_ab )
gen lnboardsize = ln(1+board_size)
gen lnceocomp_tot = ln(1+CEO_comp_total)
gen lnceocomp_cur = ln(1+ CEO_comp_curr)
gen lntobinq_nb = ln(1+ tq_nickbloom )

gen CEO_frac_inc = 1 - (CEO_comp_curr / CEO_comp_total )

*drop if sales == .
*drop if tobinQ == .
*drop if lntobinsq_ab == .

** summary stats board level ###

summarize board_size indepdir_frac female_dummy single_femaledir wom_pct CEO_comp_total CEO_frac_inc 


** summary stats - firm level ###
summarize sales lnsales tobinQ roa  tobinq_ab


**##### replication regression ###

 xtivreg lntobinsq (wom_pct =  males_onothwomboards_pct1 ) board_size indepdir_frac lnsales sales_entropy i.year_annualmeet , fe i(gvkey) first
 
 xtivreg lntobinsq_ab (wom_pct =  males_onothwomboards_pct1 ) board_size indepdir_frac lnsales sales_entropy i.year_annualmeet , fe i(gvkey) first




*### patent variables ###

foreach x in breakthroughs plaintiff defendant avg_generality npat{
  recode `x' .=0
   }
  
 
foreach x in board_size avg_age pctvotingpower_boardtot tenure_avg breakthroughs plaintiff defendant avg_generality npat total_assets Cash {
gen ln`x' = ln(1+`x')
}

foreach x in breakthroughs plaintiff defendant avg_generality npat{
  egen s`x'=std(`x')
  }
  




*### generate new vars for regression
bysort gvkey: egen asales=mean(sales)
gen salesEff = sales/total_assets
gen lnpat= ln(1+npat)
egen spat= std(npat)
gen rndmissing = 1 if rnd_sales_ratio ==.
recode rndmissing .=0
gen rnd_sales_ratio1= rnd_sales_ratio
replace rnd_sales_ratio1 = 0 if rnd_sales_ratio ==.
gen advmissing = 1 if adv_sales_ratio==.
recode advmissing .=0
gen adv_sales_ratio1=adv_sales_ratio
replace adv_sales_ratio1=0 if adv_sales_ratio==.
gen salesmissing = 1 if sales ==.
recode salesmissing .=0
gen cashmissing = 1 if Cash ==.
recode cashmissing .=0
gen assetsmissing =1 if total_assets ==.
recode assetsmissing .=0
gen salesentropymissing = 1 if sales_entropy ==.
recode salesentropymissing .=0



*#### generate 
*reg avg_generality   i._traj_Group  board_size avg_age  tenure_avg total_assets Cash salesEff  rnd_sales_ratio1 rndmissing   i.year_annualmeet
*sum adv_sales_ratio

*egen sbreakthroughs=std(breakthroughs)

######### test instrument ####



#### patent regressions ######

 foreach x in lnbreakthroughs lnpat lnavg_generality lnplaintiff lndefendant{
  ivreg2 `x' (wom_pct= males_onothwomboards_pct1 )  board_size avg_age  tenure_avg total_assets Cash salesEff  rnd_sales_ratio1 rndmissing advmissing adv_sales_ratio1  i.year_annualmeet, ffirst
  }

 foreach x in lnbreakthroughs lnpat lnavg_generality lnplaintiff lndefendant{
  ivreg2 `x' (wom_pct= males_onothwomboards_pct1 )  board_size avg_age  tenure_avg total_assets Cash salesEff  rnd_sales_ratio1 rndmissing advmissing adv_sales_ratio1 CEO_comp_total CEO_comp_curr i.year_annualmeet, ffirst
  }


******************************
*** create lagged restot1 and pretot1 variables 
******************************

local files:dir "/Users/pradeep/Workingdirectory/Data/" files "*4June.dta"

foreach file in `files' {

 sort gvkey year_annualmeet 
 by gvkey: gen restot1_lead1 = res_tot1[_n+1] if year_annualmeet+1  == year_annualmeet[_n+1]
 by gvkey: gen restot1_lead3 = res_tot1[_n+3] if year_annualmeet+1  == year_annualmeet[_n+1]
 by gvkey: gen restot1_lead5 = res_tot1[_n+5] if year_annualmeet+1  == year_annualmeet[_n+1]

 sort gvkey year_annualmeet 
 by gvkey: gen pretot1_lead1 = pre_tot1[_n+1] if year_annualmeet+1  == year_annualmeet[_n+1]
 by gvkey: gen pretot1_lead3 = pre_tot1[_n+3] if year_annualmeet+1  == year_annualmeet[_n+1]
 by gvkey: gen pretot1_lead5 = pre_tot1[_n+5] if year_annualmeet+1  == year_annualmeet[_n+1]

 *### create lagged vars ###

 sort gvkey year_annualmeet 
 by gvkey: gen rdc1_lag2yr = rnd_expense[_n-1] if year_annualmeet  == year_annualmeet[_n-1]+1


* gen lnboardsize = ln(1+board_size)
 gen lnceocomp_tot = ln(1+CEO_comp_total)
 gen lnceocomp_cur = ln(1+ CEO_comp_curr)

*## abandonment and other variables ##
foreach x in failure  abd_4yr abd_8yr abd_12yr abd_aft12yr nabandoned_focusyr {
recode `x' .= 0
}

foreach x in failure  abd_4yr abd_8yr abd_12yr abd_aft12yr nabandoned_focusyr  {
gen ln`x' = ln(1+`x')
}
save "`file'", replace

}

******************************************
*******************regressions ***********************
 
** regressions  bdata all
set more off

local files1 : dir "/Users/pradeep/Workingdirectory/Data/" files "bdataall*1Jun.dta"

foreach file in `files1' {
log using "/Users/pradeep/Workingdirectory/Data/womsummary_1June_v3.smcl", append
display "`file'"
use `file', clear

sum wom_pct males_onothwomboards_pct1 board_size indepdir_frac lnsales sales_entropy 

** replication results 

 xtivreg lntobinsq (wom_pct =  males_onothwomboards_pct1 ) lnboard_size indepdir_frac lnsales sales_entropy i.year_annualmeet , fe i(gvkey) first
 outreg2 using jun1reg2`file'.doc, append 
 
 xtivreg lntobinsq_ab (wom_pct =  males_onothwomboards_pct1 ) lnboard_size indepdir_frac lnsales sales_entropy i.year_annualmeet , fe i(gvkey) first
 outreg2 using jun1reg2`file'.doc, append 

** regress lagged variables

 foreach x in lnbreakthroughs lnpat lnavg_generality lnplaintiff lndefendant lnfailure  lnabd_4yr lnabd_8yr lnabd_12yr lnabd_aft12yr lnnabandoned_focusyr res_tot1 pre_tot1 restot1_lead1 restot1_lead3 restot1_lead5 pretot1_lead1 pretot1_lead3 pretot1_lead5 {
  xi:ivreg2 `x' (wom_pct= males_onothwomboards_pct1 )  lnboard_size avg_age  tenure_avg total_assets Cash salesEff  rnd_sales_ratio1 rndmissing advmissing adv_sales_ratio1  i.year_annualmeet, ffirst
  outreg2 using jun1reg2`file'.doc, append 
  }
 log close
  }
  
** regressions  bdata all *** try all other res and pre variables 
set more off

local files1 : dir "/Users/pradeep/Workingdirectory/Data/" files "bdataall*1Jun.dta"

foreach file in `files1' {
log using "/Users/pradeep/Workingdirectory/Data/womsummary_1June_v3.smcl", append
display "`file'"
use `file', clear

** regress lagged variables

 foreach x in res_bk1 res_sl1 res_cf1 res_ea1 pre_bk1 pre_sl1 pre_cf1 pre_ea1 {
  xi:ivreg2 `x' (wom_pct= males_onothwomboards_pct1 )  lnboard_size avg_age  tenure_avg total_assets Cash salesEff  rnd_sales_ratio1 rndmissing advmissing adv_sales_ratio1  i.year_annualmeet, ffirst
  outreg2 using jun1reg2`file'.doc, append 
  }
 log close
  }

*********************************
*** regressions overlap datasets 
*********************************
set more off
local files2 : dir "/Users/pradeep/Workingdirectory/Data/" files "*4June.dta"

foreach file in `files2' {
log using "/Users/pradeep/Workingdirectory/Data/womsummary_4June_v3.smcl", append
display "`file'"
use `file', clear


sum wom_pct males_onothwomboards_pct1 board_size indepdir_frac lnsales sales_entropy  CEO_comp_total CEO_frac_inc 


**##### replication regression ###

 xtivreg lntobinsq (wom_pct =  males_onothwomboards_pct1 ) lnboard_size indepdir_frac lnsales sales_entropy i.year_annualmeet , fe i(gvkey) first
 outreg2 using jun4`file'.doc, append 
 xtivreg lntobinsq_ab (wom_pct =  males_onothwomboards_pct1 ) lnboard_size indepdir_frac lnsales sales_entropy i.year_annualmeet , fe i(gvkey) first
 outreg2 using jun4`file'.doc, append 


*### regress lagged variables

 foreach x in lnbreakthroughs lnpat lnavg_generality lnplaintiff lndefendant lnfailure  lnabd_4yr lnabd_8yr lnabd_12yr lnabd_aft12yr lnnabandoned_focusyr res_tot1 pre_tot1 res_tot1 pre_tot1 restot1_lead1 restot1_lead3 restot1_lead5 pretot1_lead1 pretot1_lead3 pretot1_lead5 {
  xi:ivreg2 `x' (wom_pct= males_onothwomboards_pct1 ) lnboard_size avg_age  tenure_avg total_assets Cash salesEff  rnd_sales_ratio1 rndmissing advmissing adv_sales_ratio1  i.year_annualmeet, ffirst
  outreg2 using jun4`file'.doc, append 
  }

 foreach x in lnbreakthroughs lnpat lnavg_generality lnplaintiff lndefendant lnfailure  lnabd_4yr lnabd_8yr lnabd_12yr lnabd_aft12yr lnnabandoned_focusyr res_tot1 pre_tot1 res_tot1 pre_tot1 restot1_lead1  restot1_lead3 restot1_lead5 pretot1_lead1 pretot1_lead3 pretot1_lead5 {
  xi:ivreg2 `x' (wom_pct= males_onothwomboards_pct1 ) lnboard_size avg_age  tenure_avg total_assets Cash salesEff  rnd_sales_ratio1 rndmissing advmissing adv_sales_ratio1 lnceocomp_tot lnceocomp_cur i.year_annualmeet, ffirst
  outreg2 using jun4`file'.doc, append 
 }
log close
}


*** try all other res and pre variables 

set more off
local files2 : dir "/Users/pradeep/Workingdirectory/Data/" files "*4June.dta"

foreach file in `files2' {
log using "/Users/pradeep/Workingdirectory/Data/womsummary_4June_v3.smcl", append
display "`file'"
use `file', clear

 foreach x in res_bk1 res_sl1 res_cf1 res_ea1 pre_bk1 pre_sl1 pre_cf1 pre_ea1 {
  xi:ivreg2 `x' (wom_pct= males_onothwomboards_pct1 ) lnboard_size avg_age  tenure_avg total_assets Cash salesEff  rnd_sales_ratio1 rndmissing advmissing adv_sales_ratio1  i.year_annualmeet, ffirst
  outreg2 using jun4`file'.doc, append 
  }

 foreach x in res_bk1 res_sl1 res_cf1 res_ea1 pre_bk1 pre_sl1 pre_cf1 pre_ea1{
  xi:ivreg2 `x' (wom_pct= males_onothwomboards_pct1 ) lnboard_size avg_age  tenure_avg total_assets Cash salesEff  rnd_sales_ratio1 rndmissing advmissing adv_sales_ratio1 lnceocomp_tot lnceocomp_cur i.year_annualmeet, ffirst
  outreg2 using jun4`file'.doc, append 
 }
log close
}







seeout using "jun1reg2bdataall_nogenderize_1Jun.dta.txt"
seeout using "jun1reg2bdataall_genderize_1Jun.dta.txt"
seeout using "jun1reg2bdataexeco_genderize_1June.dta.txt"
seeout using "jun1reg2bdataexeco_nogenderize_1June.dta.txt"

*** create execucomp flag

*** create genderize flag


*******************
** generate percentile in the failure dataset 
use "patent_citations.dta"
egen rank = rank(fw_cites_bs)
egen n = count(fw_cites_bs )
gen percentile= (rank -0.5)/n
gen failure = 1 if fw_cites_bs ==0
replace failure = 1 if percentile <0.05
recode failure . = 0
*******************

******************************
*** create lagged R&D expenses and nb tq
******************************

*** nick bloom tq ***

use "nkbl_tq_rdexp_8903_compustat.dta", clear
gen tq_nickbloom = (mkvalt + dltt)/(ppent +invt )

** r&D expense lags **
 sort gvkey fyear 
 by gvkey: gen xrd_l1 = xrd[_n-1] if fyear  == fyear[_n-1]+1
 by gvkey: gen xrd_l2 = xrd[_n-2] if fyear  == fyear[_n-2]+2
 by gvkey: gen xrd_l3 = xrd[_n-3] if fyear  == fyear[_n-3]+3 
 by gvkey: gen xrd_l4 = xrd[_n-4] if fyear  == fyear[_n-4]+4
 by gvkey: gen xrd_l5 = xrd[_n-5] if fyear  == fyear[_n-5]+5
 by gvkey: gen xrd_l6 = xrd[_n-6] if fyear  == fyear[_n-6]+6
 by gvkey: gen xrd_l7 = xrd[_n-7] if fyear  == fyear[_n-7]+7
 
 
*** cleaning of data ***
drop fyear_y npat_y permno_y datadate_y xrd_y breakthroughs_y avg_generality_y datadate_y gvkey_y


