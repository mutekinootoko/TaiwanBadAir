# -*- coding: utf-8 -*-
import requests
import json
import time

places = [u'Xindian', u'Yonghe', u'Zhongshan']
locationStr = requests.get(
    'https://taqm.epa.gov.tw/taqm/aqs.ashx?lang=tw&act=aqi-epa&ts=' + str(time.time()))
locations = json.loads(locationStr.text)
for location in locations['Data']:
    if location['SiteKey'] in places:
        print (u'名稱：{}（{}）, AQI:{} , PM2.5:{}, PM10:{}'.format(
            location[u'SiteName'], location[u'SiteKey'], location[u'AQI'], location[u'PM25'], location[u'PM10']))
