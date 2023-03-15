# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 14:01:48 2022

@author: nbald
"""


# requires 
#     pymed 
#     fetch_pdfs
#     habanero 
#     pandas 
#     requests
#     requests3
#     beautifulsoup4
#     lxml


# Pymed can be downloaded from link below and installed manually.
# https://github.com/gijswobben/pymed
# fetch_pdfs can be downloaded via 
# https://github.com/billgreenwald/Pubmed-Batch-Download





# query must be in single then double quotes, 
# so that the parser can deal with the spaces 
# in the string

#query = '"parietal tms"'
#query = '"IPS tms"'
#query = '"IPS tms anxiety"'
#query = '"parietal tms anxiety"'

#query = '"parietal TBS"'
#query = '"IPS tbs"'
#query = '"IPS tbs anxiety"'
#query = '"parietal tbs anxiety"'

#query = '"parietal rtms"'
#query = '"IPS rtms"'
#query = '"IPS rtms anxiety"'


#queries = np.array(['"ips working memory"', '"ips attention"', '"ips arousal"', '"parietal arousal"'], dtype=object)
queries = np.array(['"tbs ptsd"', '"tbs insomnia"'], dtype=object)


for q in queries:
    
    
    query = q
    
    maxr = "500"
    pdfs = "yes"
    scrdir = 'C:/data/code/pubmed_stuff'
    
    
    inargs =  ' -query ' + query + ' -maxr ' + maxr + ' -pdfs ' + pdfs
    
    runfile('C:/data/code/pubmed_stuff/pubmed_search.py', wdir=scrdir, args=inargs)
