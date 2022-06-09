from pymed import PubMed
from habanero import counts
import pandas as pd
import argparse


# In[20]:


parser=argparse.ArgumentParser()
parser._optionals.title = "Flag Arguments"
parser.add_argument('-query',help="input your pubmed query in single quotes", default='')
parser.add_argument('-maxr',help="input the maximum results to return", default=500)
parser.add_argument('-pdfs',help="yes=fetch_pdfs, no=do_not_fetch", default='no')
inargs = vars(parser.parse_args())

# Create a PubMed object that GraphQL can use to query
# Note that the parameters are not required but kindly requested by PubMed Central
# https://www.ncbi.nlm.nih.gov/pmc/tools/developers/

pubmed = PubMed(tool="MyTool", email="nicholas.balderston@pennmedicine.upenn.edu")

# Create a GraphQL query in plain text
try:
    query = inargs['query']
except:
    query = "parietal tms anxiety"

try:
    maxr = int(inargs['max'])

except:
    maxr = 500

try:
    pdfs = inargs['pdfs']
except:
    pdfs = "no"




queryfn = query + ".txt"
queryfn = queryfn.replace("[", "-")
queryfn = queryfn.replace("]", "")
queryfn = queryfn.replace(" ", "_")


# Execute the query against the API
results = pubmed.query(query, max_results=maxr)
df = pd.DataFrame(columns = ["query", "date", "doi", "pubmed_id", "citations", "journal", "firstauthor", "lastauthor", "title"])
# Loop over the retrieved articles
for article in results:
    
    try:
        doi = article.doi.split("\n")
        doilink = "http://doi.org/" + doi[0]
        c = counts.citation_count(doi = doi[0])
    except:
        doi = ["null"]
        c = ["null"]
        
    try:
        pubmed_id = article.pubmed_id.split("\n")
    except:
        pubmed_id = ["null"]
    
    try:
        lastauthor = article.authors[len(article.authors)-1]
        lastvalue = lastauthor['lastname']
    except:
        lastvalue = "null"
    
    try:
        firstauthor = article.authors[0]
        firstvalue = firstauthor['lastname']
    except:
        firstvalue = "null"
    
    try:
        journal = article.journal
    except:
        journal = "null"

    try:
        date = article.publication_date
    except:
        date = "null"

    try:
        title = article.title
    except:
        title = "null"
    


    current = []    
    current += [query, date, doilink, pubmed_id[0], c, journal, firstvalue, lastvalue, title]

    df_length = len(df)
    df.loc[df_length] = current

    if(pdfs == 'yes'):
        fetch_args = ' -pmids ' + pubmed_id[0] + ' -out ' + query.replace(" ", "_")
        runfile('C:/data/code/pubmed_stuff/fetch_pdfs.py', wdir='C:/data/code/pubmed_stuff', args=fetch_args)
    else:
        print('not fetching pdf')
            
    
df.to_csv(queryfn, sep='\t')


