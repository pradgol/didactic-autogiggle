# didactic-autogiggle
Useful codes for working with structured data

'dataprep_plots_code_pp' has code for the the following purposes for now:

1. Outlier treatment (cap at 1 percentile and 99 percentile)
2. Missing value treatment (substitute with 0 or substitute with median/mean)
3. Create visualizations (13 different types) all customized in terms of fonts etc so that it can be directly inserted into word doc reports.
4. Factor analysis template to check whether the responses to survey questions used to measure different constructs are coming out consistently or not using chronback alpha


LDAR code has code for applying LDA for text classification using R. Once you have the docs it does the following operations:

1. Makes text lowercase, removes stopwords, numbers and whitespaces and creates DTM
2. Creates vocabulary from DTMs
3. Create ngrams
4. Apply LDA
5. identify top terms for each topic
6. Score the documents on topics

LDApy code has code for applying LDA for text classification using python. Still WIP:
1. remove stop words, tokenize, lemmatize, create dtm, apply LDA

SIC_assignment assigns Standard Industrial Codes to Angel.co companies based on textual description of the company:
1. Tokenize words, create vocab and create DTM from each text document
2. calculate tfidf for each dtm
3. calculate cosine similarity of each document with SIC code with document with SIC code
4. assign SIC code to document without SIC code based on the closest company calculated using cosine similarity
