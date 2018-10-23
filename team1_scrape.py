# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 09:15:53 2018

@author: jbean
"""

import pandas as pd
from bs4 import BeautifulSoup
import requests


def team_data_scrape(team_abbreviation, year):
    
    site = requests.get('https://www.baseball-reference.com/teams/%s/%i-schedule-scores.shtml' %(team_abbreviation, year))

    soup = BeautifulSoup(site.text, 'html.parser')

    runs_for = soup.find_all('td', {'class':'right', 'data-stat':'R'})
    runs_for = [i.text for i in runs_for]

    runs_against = soup.find_all('td', {'class':'right', 'data-stat':'RA'})
    runs_against = [i.text for i in runs_against]

    opponent = soup.find_all('td', {'class':'left', 'data-stat':'opp_ID'})
    opponent = [i.text for i in opponent]

    team_data = pd.DataFrame({'runs_for':runs_for, 'runs_against':runs_against, 'opponent':opponent})

    team_data['runs_for'] = pd.to_numeric(team_data['runs_for'])
    team_data['runs_against'] = pd.to_numeric(team_data['runs_against'])

    team_data['win'] = [1 if a > b else 0 for a, b in zip(team_data['runs_for'], team_data['runs_against'])]

    return team_data

#nyy_data = team_data_scrape('NYY', 2018)
#bos_data = team_data_scrape('BOS', 2018)
#
#nyy_data.to_csv(r'C:\Users\jbean\Dropbox\Other\Python\WS_simulation\nyy_data.csv', index=False)
#bos_data.to_csv(r'C:\Users\jbean\Dropbox\Other\Python\WS_simulation\bos_data.csv', index=False)
#    
#lad_data = team_data_scrape('LAD', 2018)
#atl_data = team_data_scrape('ATL', 2018)
#
#lad_data.to_csv(r'C:\Users\jbean\Dropbox\Other\Python\WS_simulation\lad_data.csv', index=False)
#atl_data.to_csv(r'C:\Users\jbean\Dropbox\Other\Python\WS_simulation\atl_data.csv', index=False)
#    
#col_data = team_data_scrape('COL', 2018)
#mil_data = team_data_scrape('MIL', 2018)
#
#col_data.to_csv(r'C:\Users\jbean\Dropbox\Other\Python\WS_simulation\col_data.csv', index=False)
#mil_data.to_csv(r'C:\Users\jbean\Dropbox\Other\Python\WS_simulation\mil_data.csv', index=False)
#
#cle_data = team_data_scrape('CLE', 2018)
#hou_data = team_data_scrape('HOU', 2018)
#
#cle_data.to_csv(r'C:\Users\jbean\Dropbox\Other\Python\WS_simulation\cle_data.csv', index=False)
#hou_data.to_csv(r'C:\Users\jbean\Dropbox\Other\Python\WS_simulation\hou_data.csv', index=False)
    
oak_data = team_data_scrape('OAK', 2018)

oak_data.to_csv(r'C:\Users\jbean\Dropbox\Other\Python\WS_simulation\oak_data.csv', index=False)

chc_data = team_data_scrape('CHC', 2018)

chc_data.to_csv(r'C:\Users\jbean\Dropbox\Other\Python\WS_simulation\chc_data.csv', index=False)