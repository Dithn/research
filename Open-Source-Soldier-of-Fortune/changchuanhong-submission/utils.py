"""
Submission by: @changchuanhong
These are utlity Functions that will be used in my notebook.
"""

import bs4 as bs
import requests
import pandas as pd
import random

def getSPXTickers(count):
    """
    This function retrieves a list all of SPX tickers from wikipedia and randomly selects the required number of tickers to be returned.

    :param count: Number of tickers required.
    """
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})

    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        #fourth element is the sector
        industry = row.findAll('td')[4].text
        
        tickers.append(ticker)

    tickers = list(map(lambda s: s.strip(), tickers))

    return random.sample(tickers, k=count)