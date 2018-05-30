
################################################################################
#Step 0: Set required dataset as df. Change dataset_name to the name of your dataset in below code
################################################################################
df <- dataset_name

################################################################################
#Step 1: cap outliers 
################################################################################

# function for outlier capping #################

outlierfn <- function(x){
  qnt <- quantile(x, probs = c(0.01,0.99), na.rm = T)
  caps <- quantile(x, probs = c(0.01,0.99), na.rm = T )
  x[x< qnt[1]] <- caps[1]
  x[x> qnt[2]] <- caps[2]
  return(x)
}

# How to:
# Step 1.1: put vars_capping as all the numeric variables that need to be capped  ###
# Modify below code - put variable names in place of var1, var2, var3

vars_capping <- c('var1','var2','var3')

# Step 1.2: run the below loop

for(i in vars_capping){
  df[[i]] <- outlierfn(df[[i]])
}

#################################################################################
# Step 2: missing value treatment 
#################################################################################

# Step 2.1: Replace missings with Zeros for variables that you are sure of as being zero
#summary(df$state)

#### Do it in python. Thats a lot easier!!! One line of code and you can do groupwise means etc.

## python code - to be modified / adapted

# put xzero as all variables you want to replace missings with zero: xzero= ['var1','var2']
# df[xzero] = df[xzero].fillna(0)

# put group_summary as all variables you want to replace missings with means/median and the groupby unit, in this case 'district'.
# group_summary = ['var1','var2','var3','district']
# df[group_summary] = df[group_summary].fillna(df[group_summary].groupby('district').transform('median'))


######### R code just to replace missings with zeros. Not concrete, might throw errors ###
#a<- df[xzero]
#df[xzero][is.na(df[xzero])]<-0 
#df['avg_emp_pay'][is.na(df['avg_emp_pay'])] <-0


#################################################################################
# Step 3: plot the variables and create visualizations
#################################################################################

##############################
# barplot fn with facet wrap #
##############################


#change output path below before running code
barplotx <- function(xset, prefix){
  for(i in seq_along(xset)){
    g<- ggplot(data = df) + geom_bar(mapping = aes_string(x = xset[i], fill = xset[i])) + facet_wrap(~state) + 
      scale_x_discrete(labels = abbreviate) + 
      theme(legend.position = 'right', axis.text.x = element_text(angle = 45, hjust = 1)) +
      theme(legend.text = element_text(size = 5), legend.title = element_blank()) + 
      theme(axis.text.x = element_text(angle = 45, hjust =1, size = 8)) 
    print(g)
    ggsave(g, filename = paste(prefix, xset[i],'.png',sep = ''),path = 'D://Pradeep/Data/plots/')
  }
}

###############################
# barplots without facet wrap #
###############################


#change output path below before running code
barplotx2<- function(xset, prefix){
  for(i in seq_along(xset)){
    g<- ggplot(data = df) + geom_bar(mapping = aes_string(x = 'state', fill = xset[i])) +  
      scale_x_discrete() + 
      theme(legend.position = 'right', axis.text.x = element_text(angle = 45, hjust = 1)) +
      theme(legend.text = element_text(size = 5), legend.title = element_blank()) + 
      theme(axis.text.x = element_text(angle = 45, hjust =1, size = 8)) 
    print(g)
    ggsave(g, filename = paste(prefix, xset[i],'.png',sep = ''),path = 'D://Pradeep/Data/plots/')
  }
}

######################
# horizontal barplot #
######################

#change output path below before running code
barplotx2_hor<- function(xset, prefix){
  for(i in seq_along(xset)){
    g<- ggplot(data = df) + geom_bar(mapping = aes_string(x = 'state', fill = xset[i])) +  
      scale_x_discrete() + 
      theme(legend.position = 'right', axis.text.x = element_text(angle = 45, hjust = 1)) +
      theme(legend.text = element_text(size = 5), legend.title = element_blank()) + 
      theme(axis.text.x = element_text(angle = 45, hjust =1, size = 8)) + coord_flip()
    print(g)
    ggsave(g, filename = paste(prefix, xset[i],'.png',sep = ''),path = 'D://Pradeep/Data/plots/')
  }
}

######################
# fully stacked bars #
######################

#change output path below before running code
barplotx3_full<- function(xset, prefix){
  for(i in seq_along(xset)){
    g<- ggplot(data = df) + geom_bar(mapping = aes_string(x = 'state', fill = xset[i]), position = 'fill') +  
      scale_x_discrete() + 
      theme(legend.position = 'right', axis.text.x = element_text(angle = 45, hjust = 1)) +
      theme(legend.text = element_text(size = 8), legend.title = element_blank(), legend.position = 'bottom') + 
      theme(axis.text.x = element_text(angle = 45, hjust =1, size = 8),
            axis.title.x = element_blank(), axis.title.y = element_blank()) 
    print(g)
    ggsave(g, filename = paste(prefix, xset[i],'.png',sep = ''),path = 'D://Pradeep/Data/plots/')
  }
}



##############
# histograms #
##############

histx <- function(xset, prefix){
  for(i in seq_along(xset)){
    g<- ggplot(data = df) + geom_histogram(mapping = aes_string(x = xset[i])) + facet_wrap(~state)  
    #      scale_x_discrete(labels = abbreviate) + 
    #      theme(legend.position = 'right', axis.text.x = element_text(angle = 45, hjust = 1)) +
    #      theme(legend.text = element_text(size = 5)) + 
    #      theme(axis.text.x = element_text(angle = 45, hjust =1, size = 8)) 
    print(g)
    ggsave(g, filename = paste(prefix, xset[i],'.png',sep = ''),path = 'D://Pradeep/Data/plots/')
  }
}

###########
# boxplot #
###########

boxplotx <- function(xset, prefix){
  for(i in seq_along(xset)){
    g<- ggplot(data = df, aes( fill = state)) + geom_boxplot(mapping = aes_string(x = 'state', y = xset[i]))
    print(g)
    ggsave(g, filename = paste(prefix, xset[i], '.png', sep = ''), path = 'D://Pradeep/Data/plots/')
  }
}


##############################################################################
##################### misc plots : Template ##################################
##############################################################################


# pie chart - template
ggplot(data = df, aes(x = "", y = gender, fill = gender))+ geom_bar(stat = 'identity', width = 1) +  coord_polar('y', start = 0) +
  theme(axis.title.x  = element_blank(), axis.title.y= element_blank(), legend.position = 'bottom')


# errorbar - template
ggplot(df_eqpmt, aes(x = variable, y = value)) + 
  stat_boxplot(aes(x = variable, y = value, colour = variable), geom = 'errorbar', linetype = 1, width = 0.5)+
  stat_summary(fun.y = mean, geom = 'point', size = 2, colour = 'brown') +
  theme( legend.position = 'bottom')+
  theme(axis.text.x = element_text(angle = 80, size = 8, hjust = 1)) +
  facet_grid(~state) 

# histogram with dotted lines at quantiles - template
q1 <- quantile(df$earnings_cscservices, na.rm = T, probs = c(0.1, 0.25,0.5,0.75,0.95))
ggplot(data = df, aes(x = earnings_cscservices, fill = state))+geom_histogram() + facet_wrap(~state) +geom_vline(xintercept = q1, colour = 'red', alpha = 0.5, linetype = 2, show.legend = TRUE)


# special chart1 : multiple column boxplots 'statewise' facet wrap - template
df_eqpmt <- melt(df[c(equip_count, 'state')],id.vars  = 'state')

ggplot(df_eqpmt) + geom_boxplot(aes(x = variable, y = value, colour = variable)) +
  theme( legend.position = 'bottom')+
  theme(axis.text.x = element_text(angle = 80, size = 8, hjust = 1)) +
  facet_wrap(~state) 


# special chart2 : multiple column boxplots 'statewise' grid - template
df_distances <- melt( df[c(distances, 'state')], id.vars = 'state')

ggplot(df_distances, aes(x = variable, y = value)) +
  geom_boxplot(aes(x = variable, y = value, colour = variable)) +
  theme(legend.position = 'bottom', legend.text = element_text(size = 8)) +
  theme(axis.text.x = element_text(angle = 45, size =8, hjust = 1), 
        axis.title.x = element_blank(), axis.title.y = element_blank())+
  facet_grid(~state)


# special chart3 :  barplot with multiple bars for different variables - displayed as a grid for each group (eg for group: state) - template
df_per <- melt(df[permissions], variable.name = 'perms', value.name = 'number', id.vars = 'state')

ggplot(data = df_per) + geom_bar(aes(x = perms, fill = number))+ 
  theme(legend.position = 'bottom', legend.text = element_text(size = 8), legend.title = element_blank())+
  theme(axis.text.x = element_text(angle = 54, hjust = 1, size = 8), axis.title.x = element_blank())+
  facet_grid(~state)


# special chart4 : horizontal barplot with yes/no split for a category with multiple fields - template

# Eg:  ID  Influencer
#       1   a,c
#       2   b,c
# Chart : a = 1 out of 2, b = 1 out of 2, c = 2 out of 2

influencer <- c("influencer_Family member / Relative",               
                "influencer_Friend / Colleague",                                
                "influencer_Govt Official",                                
                "influencer_NGO / Other Institution",                            
                #           "influencer_Other",                           
                "influencer_Self")

influencer_df <- df[c(influencer,'state')]

influencer_melt <- melt(influencer_df, idvars = 'state')

influencer_melt$value[influencer_melt$value == 1] <- 'Yes'
influencer_melt$value[influencer_melt$value == 0] <- 'No'

ggplot(data = influencer_melt) + geom_bar(aes(x = variable, fill = value), position = 'fill') +
  facet_grid(~state) +
  theme(legend.position = 'bottom', legend.text = element_text(size = 8), legend.title = element_blank())+
  theme(axis.text.x = element_text(angle = 54, hjust = 1, size = 8), axis.title.x = element_blank())+
  scale_x_discrete(limits = c("influencer_NGO / Other Institution" , 
                              "influencer_Govt Official",
                              "influencer_Friend / Colleague",
                              "influencer_Family member / Relative",
                              "influencer_Self"),
                   labels = c("influencer_Self"  ='Self',
                              "influencer_Family member / Relative"= 'Family Member/Relative',
                              "influencer_Friend / Colleague" = 'Friend/Colleague', 
                              "influencer_Govt Official" = 'Govt. Official', 
                              "influencer_NGO / Other Institution" = 'NGO/Other Institution'))+
  facet_wrap(~state) +coord_flip()




##############################################################################
### factor analysis: chronbach alpha for checking constructs - template ######
##############################################################################

############### chronbach alpha ####################
############### factor analysis ####################

vle_factor <- c( 'char_like_workinghard',
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
                 'char_problem_manysolns')

df_char <- df[vle_char]

df_factor <- df[vle_factor]

df_factor2<- na.omit(df_factor)

factanal(df_factor2, factors = 5, rotation = 'varimax')

summary(df_factor)

library(psych)

###Achievement Motivation

achvmnt_mot <- c('char_like_workinghard',
                 'char_personaldemand',
                 'char_othppl_perception_dontworkhard')

locus_ctrl <- c('char_numfriends_fate',
                'char_workaccomplishment_lovejob',
                'char_getwhatiwant_workhard',
                'char_planahead_unwise_fortune',
                'char_leaders_reason_rightplacetime')

meta_cog <- c('char_unsucessfulbizstrategy_experiment',
              'char_monitor_areasneedmorepractice',
              'char_goalsetting_direction_success',
              'char_thingsdontunderstand_adj_strat')

self_efficacy <- c('char_sticktoaims_accomplishgoals_easy',
                   'char_unexpectedevents_conf',
                   'char_calm_difficulties_copingabilities',
                   'char_problem_manysolns')


psych::alpha(df[achvmnt_mot], check.keys = TRUE)

achvmt_mot2 <- c('char_like_workinghard',
                 'char_personaldemand')

psych::alpha(df[achvmt_mot2], check.keys = TRUE)

psych::alpha(df[locus_ctrl], check.keys = TRUE)

psych::alpha(df[meta_cog])

psych::alpha(df[self_efficacy])

alpha(df_factor2, check.keys = TRUE)

##############################################################################






