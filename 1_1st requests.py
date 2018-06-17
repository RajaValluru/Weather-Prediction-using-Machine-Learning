from datetime import datetime, timedelta  
import time  
from collections import namedtuple  
import pandas as pd  
import requests  
import matplotlib.pyplot as plt  
API_KEY = '5a2f87d4575cc182'  #2 keys---9d4a47d3a3cae4ac---5a2f87d4575cc182---
BASE_URL = "http://api.wunderground.com/api/{}/history_{}/q/NE/Lincoln.json" 
target_date = datetime(2017, 3,2)  
features = ["date", "meantempm", "meandewptm", "meanpressurem", "maxhumidity", "minhumidity", "maxtempm","mintempm", "maxdewptm", "mindewptm", "maxpressurem", "minpressurem", "precipm"]
DailySummary = namedtuple("DailySummary", features)
#records = []
def extract_weather_data(url, api_key, target_date, days):  
    record = []
    request = BASE_URL.format(API_KEY, target_date.strftime('%Y%m%d'))
    response = requests.get(request)
    if response.status_code == 200:
        data = response.json()['history']['dailysummary'][0]
        record.append(DailySummary(
            date=target_date,
            meantempm=data['meantempm'],
            meandewptm=data['meandewptm'],
            meanpressurem=data['meanpressurem'],
            maxhumidity=data['maxhumidity'],
            minhumidity=data['minhumidity'],
            maxtempm=data['maxtempm'],
            mintempm=data['mintempm'],
            maxdewptm=data['maxdewptm'],
            mindewptm=data['mindewptm'],
            maxpressurem=data['maxpressurem'],
            minpressurem=data['minpressurem'],
            precipm=data['precipm']))
    #time.sleep(6)
    
    return record

while(target_date!=datetime(2017,9,28)):
    records += extract_weather_data(BASE_URL, API_KEY, target_date, 500) 
    target_date += timedelta(days=1)
    print(target_date)
    
    
    #raise Exception('exit')
