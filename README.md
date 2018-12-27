# didactic-autogiggle
Useful codes for working with structured data


# 'dataprep_plots_code_pp' - basic data prep for structured data before regressions:
Tasks performed by the code:
1. Outlier treatment (cap at 1 percentile and 99 percentile)
2. Missing value treatment (substitute with 0 or substitute with median/mean)
3. Create visualizations (13 different types) all customized in terms of fonts etc so that it can be directly inserted into word doc reports.
4. Factor analysis template to check whether the responses to survey questions used to measure different constructs are coming out consistently or not using chronback alpha


# Code for applying LDA for text classification. 

'LDAR_pradeep_28June.ipynb' code has code in R. Once data is ready in terms of 'documents', it does the following operations:
1. Makes text lowercase, removes stopwords, numbers and whitespaces and creates DTM
2. Creates vocabulary from DTMs
3. Create ngrams
4. Apply LDA
5. identify top terms for each topic
6. Score the documents on topics

'LDApy_pradeep_28June.ipynb' code has code for applying LDA for text classification using python. Still WIP:
1. remove stop words, tokenize, lemmatize, create dtm
2. create vocab from DTM
3. apply LDA


# Code from 'crowdfunding as an alternative to VC funding' project.

'SIC_assignment.R' assigns Standard Industrial Codes to Angel.co companies based on textual description of the company:
1. Tokenize words, create vocab and create DTM from each text document
2. calculate tfidf for each dtm
3. calculate cosine similarity of each document with SIC code with document with SIC code
4. assign SIC code to document without SIC code based on the closest company calculated using cosine similarity

Other data prep codes for the project.
- 'crowdfunding.py' 
- 'CF_dataprep_code_5June.R'
- 'Crowdfunding_2_5_master.egp'


# Code from 'Women on company boards and the impact of diversity on innovation outcomes and risk taking ability of firms'
- 'womboards_4Jun.py' dataprep
- 'womboards_28May.do' regressions


# Success of micro-entrepreneurs in rural settings
- 'CSC.py' dataprep
- 'cscreport_regs.do' analysis and regressions


# dataprep for networks
- 'networks.py'

# dataprep for 'entrepreneurial clusters' project
- 'cluster.py'

# Extract data (tweets) from Elasticsearch and store in CSV format

- 'Elasticsearch_to_csv.ipynb'






