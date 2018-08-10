########################################
########################################
########Linkedin data extraction########
########################################
########################################


library(readxl)
linkedin_profile_data1 <- read_excel("~/Google Drive (pradeep_pachigolla@isb.edu)/Crowdfunding/crowdfunding/linkedin_profile_Data/linkedin_profile_data1.xls")
View(linkedin_profile_data1)

library(readxl)
linkedin_profile_data2 <- read_excel("~/Google Drive (pradeep_pachigolla@isb.edu)/Crowdfunding/crowdfunding/linkedin_profile_Data/linkedin_profile_data2.xls")
View(linkedin_profile_data2)

linkedin_cf<-rbind(linkedin_profile_data1,linkedin_profile_data2)

View(linkedin_cf)

save(linkedin_cf, file ="~/Google Drive (pradeep_pachigolla@isb.edu)/Crowdfunding/crowdfunding/linkedin_profile_Data/linkedin_cf.R")
load("~/Google Drive (pradeep_pachigolla@isb.edu)/Crowdfunding/crowdfunding/linkedin_profile_Data/linkedin_cf.R")

write.csv("~/Google Drive (pradeep_pachigolla@isb.edu)/Crowdfunding/crowdfunding/linkedin_profile_Data/linkedin_cf.csv", x=linkedin_cf)

library(stringr)

linkedin_cf$entre_exp <- str_detect(linkedin_cf$`Experience role`,regex("founder|co-founder|founding", ignore_case = TRUE))

linkedin_cf$tech_edu <- str_detect(linkedin_cf$`School Course`, regex("engineering|tech|computer|bachelor of science
                                                                      |master of science", ignore_case = TRUE))
linkedin_cf$mgmt_edu <- str_detect(linkedin_cf$`School Course`, regex("business|MBA|administration|
                                                                      management|m.b.a|economics|finance", ignore_case= TRUE))
linkedin_cf$edulvl_phd <- 
  str_detect(linkedin_cf$`School Course`, regex("doctor|phd|ph\\.d", ignore_case = TRUE))

linkedin_cf$edulvl_masters <-
  str_detect(linkedin_cf$`School Course`, regex("MS|master|M\\.S|graduate|post graduate|pgdm|MD|MBA|m\\.b\\.a|m\\.sc|m..sc", ignore_case = TRUE))

linkedin_cf$edulvl_bachelors <- 
  str_detect(linkedin_cf$`School Course`, regex("bachelor|BS|bsc|b\\.sc|be|btech|
                                                b\\.e|b\\.tech|diploma|BA|B\\.a|JD|b\\.sc|LLB|b..sc",ignore_case= TRUE))
linkedin_cf$edulvl_dropout <- 
  str_detect(linkedin_cf$`School Course`, regex("dropout|dropped", ignore_case = TRUE))

linkedin_cf$education <- ifelse(linkedin_cf$edulvl_phd == "TRUE", "PhD", 
                                ifelse(linkedin_cf$edulvl_masters == "TRUE", "MASTERS",
                                       ifelse(linkedin_cf$edulvl_bachelors == "TRUE", "BACHELORS",
                                              ifelse(linkedin_cf$edulvl_dropout == "TRUE", "DROPOUT","high school"))))



#linkedin_cf$firstname <- str_extract(linkedin_cf$Name, "\\d+(?=\\s)")
#regex("^[a-z]..", ignore_case = TRUE) )

######################
#########gender#######

library(readxl)
linkedin_gender <- read_excel("~/Dropbox (Pradeep ISB)/linkedin_gender.xlsx", 
                              col_types = c("text", "numeric", "text", 
                                            "text"))
View(linkedin_gender)


### get company names against founder and gender###
founder_gender <- merge(vxpert_companies,linkedin_gender,by.x = "ID" , by.y = "Invnum",all.y = TRUE )
View(founder_gender)

### get firstnames from linkedin founder names###

linkedin_cf$firstname <- sapply(strsplit(linkedin_cf$Name, " "), `[`, 1)

### join linkedin founder file with gender file based on company name and firstname to get gender for each founder###
linkedin_cf_temp1 <- merge(linkedin_cf,founder_gender,by.x = c("StartUp","firstname"), by.y = c("company_name","Firstname"),all.x = TRUE )
View(linkedin_cf_temp1)

dups.x<- linkedin_cf_temp1[duplicated(linkedin_cf_temp1,incomparables = FALSE),]

### get unique accounts###
linkedin_cf_2<- linkedin_cf_temp1[!duplicated(linkedin_cf_temp1,incomparables = FALSE),]

View(linkedin_cf_2)

##### dataset to get data where gender is missing######
linkedin_g_na <- linkedin_cf_nodupes[is.na(linkedin_cf_nodupes$Gender),]
View(linkedin_g_na)
write.csv(file = "gender_missing.csv", x= linkedin_g_na)

####### schooling #######

linkedin_cf$gradyr <- as.numeric(str_extract(linkedin_cf$`School Years`, "....$"))
linkedin_cf$yrs_since_grad <- 2017- linkedin_cf$gradyr
linkedin_cf$age <- linkedin_cf$yrs_since_grad + 22

#####note: high school - bachelors not mentioned. age also a bit 
##### need to handle exceptions like years not mentioned#####

linkedin_cf_export_5dec<- linkedin_cf_2[,c(1:29,36,37)]
View(linkedin_cf_export_5dec)

save(linkedin_cf_export_5dec , file = "linkedin_cf.R")

write.csv(file = "linkedin_export_5dec.csv", x=linkedin_cf_export_5dec)


##### experience ######

linkedin_cf$yrs_workex <- str_extract(linkedin_cf$`Experience date`, "^years"+)

linkedin_cf$firstname <- sapply(strsplit(linkedin_cf$Name, " "), `[`, 1)


#### replicate prof. Anand's results ###
##### read firmdata final ###

library(haven)
firmdata_angelovx8mar <- read_dta("~/Google Drive (pradeep_pachigolla@isb.edu)/Crowdfunding/Data for paper/firmdata_angelovx8mar.dta")
View(firmdata_angelovx8mar)


##### read old data ###

library(haven)
Startup_round_Stata3_v13 <- read_dta("~/Google Drive (pradeep_pachigolla@isb.edu)/Crowdfunding/Data for paper/Startup_round_Stata3_v13.dta")
View(Startup_round_Stata3_v13)


### angelovx data##
library(haven)
angelovx <- read_dta("~/Google Drive (pradeep_pachigolla@isb.edu)/Crowdfunding/Data for paper/angelovx.dta")
View(angelovx)


sr13<- merge(Startup_round_Stata3_v13, firmdata_angelovx8mar, by.x = c("CompanyName","RoundNumber"), by.y = c("company_name","RoundNumber"), all.x = TRUE)

write_dta(sr13,"./startupround_v14.dta")

