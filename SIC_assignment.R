
########### code to assign SIC codes to companies scraped from Angel.co based on text descriptions####

##### I use two files to do this ###
## 1. List of companies from Angel.co (or any other) with text describing what the company does
## 2. List of Companies collected from Venturexpert which have preassigned SICs. I use this as reference


library(readr)
library(readxl)
library(data.table)
library(text2vec)
library(data.table)
library(tcR)

angel_companies <- read_excel("Angel_companies_descriptions.xlsx", 
                              sheet = "Sheet2")
View(angel_companies)
vxpert_companies <- read_excel("Vxpert_companies_descriptions.xlsx", 
                               sheet = "Sheet1")
View(vxpert_companies)
vx<-vxpert_companies[complete.cases(vxpert_companies$comp_biz_desc_long),]
vx<-vx[complete.cases(vx$SIC_numeric),]

vxpert_sm<- data.frame(sic=vx$SIC_numeric, 
                       biz_desc_s= vx$comp_biz_desc_short,
                       biz_desc_l=vx$comp_biz_desc_long,stringsAsFactors = FALSE)
vxpert_sm$biz_desc <- paste(vxpert_sm$biz_desc_s,vxpert_sm$biz_desc_l,sep = ", ")

vxpw <- data.frame(sic=vxpert_sm$sic,biz_desc=vxpert_sm$biz_desc,stringsAsFactors = FALSE)
vxpw<-vxpw[order(vxpw$sic),]

setDT(vxpw)
vxpdescvec<-vxpw[,.(biz_desc=paste(biz_desc,collapse = '; ')), by = sic]


##### list of VX companies over SIC#####
vx1<-data.frame(sic=vx$SIC_numeric,comp_name=vx$company_name, stringsAsFactors = FALSE)

vx1<-data.frame(sic=vx$SIC_numeric, comp_name=vx$company_name,
                biz_desc_s= vx$comp_biz_desc_short,
                biz_desc_l=vx$comp_biz_desc_long,stringsAsFactors = FALSE)

vx1<-vx1[complete.cases(vx1$sic),]
vx1$biz_desc <- paste(vxpert_sm$biz_desc_s,vxpert_sm$biz_desc_l,sep = "; ")

setDT(vx1)
vxcompanies<- vx1[,.(comp_name=paste(comp_name, collapse=";"), 
                     biz_desc_s=paste(biz_desc_s,collapse = ";")), by=sic]

write.csv(file = "/Users/pradeep/Workingdirectory/crowdfunding/vxcompanies.csv",x=vxcompanies)

#############end########

######cosine similarity#########

angel_companies$desc<-paste(angel_companies$tag_line,angel_companies$Overview,sep = '. ')
angelcos<-data.frame("startupname"=angel_companies$`Startup name`,"desc"=angel_companies$desc, stringsAsFactors = FALSE)

########creating text vector###########

library(text2vec)
library(data.table)

#############cosine sim vec Method 2###########

setDT(vxpw)
setkey(vxpw,sic)
train=vxpw ### venturexpert data as train set
test=angelcos ### angel data as test set

## creating vocabulary for the Document Term Matrix
prep_fun=tolower
tok_fun=word_tokenizer

it_train= itoken(train$biz_desc,
                 preprocessor = prep_fun,
                 tokenizer= tok_fun,
                 ids = train$sic)

vocab=create_vocabulary(it_train) ## create vocabulary corpus for vectorization
vectorizer=vocab_vectorizer(vocab) ## initializing vectorizer with vocab
dtm_train=create_dtm(it_train,vectorizer) ## create document term matrix
tfidf=TfIdf$new() ## initialize Term Frequency Inverse Document Frequency function

dtm_train_tfidf=fit_transform(dtm_train,tfidf) ## create TFIdf for the VXpert data

## creating DTM and TFIDF for the angel.co data 
it_test= itoken(test$desc,
                preprocessor=prep_fun,
                tokenizer=tok_fun,
                ids=test$startupname)

dtm_test=create_dtm(it_test,vectorizer)
dtm_test_tfidf=create_dtm(it_test,vectorizer) %>% transform(tfidf)

######## calculating cosine similarity between the two datasets#########;
library(tcR)
cosineoutvec2<-matrix(nrow=781,ncol=8396)

colnames(cosineoutvec2)<- rownames(dtm_train_tfidf)
rownames(cosineoutvec2)<- rownames(dtm_test_tfidf)


######cosinesim calculation###

t1<-Sys.time()
options(warn = 0)
for(i in 1:781) {
  for(j in 1:8396) {
    cosineoutvec2[i,j]<-crossprod(dtm_test_tfidf[i,],dtm_train_tfidf[j,])/
      sqrt(crossprod(dtm_test_tfidf[i,])*crossprod(dtm_train_tfidf[j,])) 
  }
}
print(difftime(Sys.time(), t1, units = 'min'))

cosine.similarity(dtm_test_tfidf[297,],dtm_train_tfidf[3,],.do.norm = TRUE)

crossprod(dtm_test_tfidf[297,],dtm_train_tfidf[3,])/
  sqrt(crossprod(dtm_test_tfidf[297,])*crossprod(dtm_train_tfidf[3,]))
rownames(dtm_test_tfidf)

############end cosinesim calculation####

View(cosineoutvec2)
colnames(dtm_train_tfidf)
colnames(vxpert_sm )

i<-data.frame(apply(cosineoutvec2,1,max),apply(cosineoutvec2,2,max),apply(cosineoutvec2,3,max))

i<-apply(cosineoutvec2,1,max)
j<-apply(cosineoutvec2,2,max)
k<-c(i,j)
View(k)
View(i)
View(j)
class(i)

startupsic2<-matrix(data=c(row.names(cosineoutvec2),
                           colnames(cosineoutvec2)[max.col(cosineoutvec2)],
                           #max.col(cosineoutvec2),
                           apply(cosineoutvec2,1,max),
                           angelcos$startupname,
                           angelcos$desc,
                           vx_o_adddetails$ID,
                           vx_o_adddetails$company_name,
                           vx_o_adddetails$comp_biz_desc_short,
                           vx_o_adddetails$comp_biz_desc_long,
                           vx_o_adddetails$SIC_numeric),
                    nrow=781)
View(startupsic2)

######take top 5 cosine SIC codes for each company######

# a function that returns the position of n-th largest
maxn <- function(n) function(x) order(x, decreasing = TRUE)[n]

startupsic.t5<-data.frame(row.names(cosineoutvec2),
                          colnames(cosineoutvec2)[max.col(cosineoutvec2)],
                          #max.col(cosineoutvec2),
                          apply(cosineoutvec2,1,max),
                          angelcos$startupname,
                          angelcos$desc,
                          vx_o_adddetails$ID,
                          vx_o_adddetails$company_name,
                          vx_o_adddetails$comp_biz_desc_short,
                          vx_o_adddetails$comp_biz_desc_long,
                          vx_o_adddetails$SIC_numeric,
                          colnames(cosineoutvec2)[apply(cosineoutvec2,1,maxn(2))],
                          apply(cosineoutvec2,1,function(x)x[maxn(2)(x)]),
                          colnames(cosineoutvec2)[apply(cosineoutvec2,1,maxn(3))],
                          apply(cosineoutvec2,1,function(x)x[maxn(3)(x)]),
                          colnames(cosineoutvec2)[apply(cosineoutvec2,1,maxn(4))],
                          apply(cosineoutvec2,1,function(x)x[maxn(4)(x)]),
                          colnames(cosineoutvec2)[apply(cosineoutvec2,1,maxn(5))],
                          apply(cosineoutvec2,1,function(x)x[maxn(5)(x)]),
                          stringsAsFactors = FALSE)
View(startupsic.t5)
write.csv("startupsic_top5.csv",x=startupsic.t5)

library(readxl)
startupsic_top5_23nov <- read_excel("~/Google Drive (pradeep_pachigolla@isb.edu)/Crowdfunding/crowdfunding/startupsic_top5_23nov.xlsx")
View(startupsic_top5_23nov)

save(startupsic_top5_23nov,file="startupsic_top5_23nov.R")


d<-data.frame(cosineoutvec2[11,])
c<-data.frame(colnames(cosineoutvec2),d)
View(c)
View(data.frame(cosineoutvec2[1,]))
row.names(d) <-colnames(cosineoutvec2)

######writing into csv#####

write.csv("angelcos.csv",x=angelcos)
save(angelcos,file="angelcos.R")
load("angelcos.R")

write.csv("D:/startupsic2.csv", x=startupsic2)
save(startupsic2,file="startupsic2.R")
load("startupsic2.R")

save(cosineoutvec2,file="cosineoutvec2.R")
load("cosineoutvec2.R")
write.csv(file = "D:/cosineoutvec2.csv", x=cosineoutvec2)




