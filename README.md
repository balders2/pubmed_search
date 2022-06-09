# pubmed_search
quick script to download metadata and pdfs from a pubmed search




# requires 
pymed 
fetch_pdfs
habanero 
pandas 
requests
requests3
beautifulsoup4
lxml


Pymed can be downloaded from link below and installed manually.

https://github.com/gijswobben/pymed

fetch_pdfs can be downloaded via 

https://github.com/billgreenwald/Pubmed-Batch-Download





# example

query = '"dlpfc parietal"'

maxr = "50"

pdfs = "yes"

scrdir = 'C:/data/code/pubmed_stuff'

inargs =  ' -query ' + query + ' -maxr ' + maxr + ' -pdfs ' + pdfs


runfile('C:/data/code/pubmed_stuff/pubmed_search.py', wdir=scrdir, args=inargs)
