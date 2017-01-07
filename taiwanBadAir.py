# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import json

locations = [u'Xindian', u'Yonghe', u'Zhongshan']

soup = BeautifulSoup(urllib2.urlopen('http://taqm.epa.gov.tw/taqm/tw/AqiMap.aspx'), 'html.parser')

areas = soup.find_all('area')
#print len(areas)
for eachArea in areas :
	if eachArea.has_attr('jtitle'):
		jtitle = json.loads(eachArea['jtitle'])
		#<area shape='rect' class='jTip' title='永和' alt='永和' jTitle='{"SiteName":"永和", "SiteKey":"Yonghe", "AreaKey":"North", "AQI":"", "AQIStyle":"AQI0", "MainPollutant":"","MainPollutantKey":"","PM10":"","PM25":"","O3":"","SO2":"","CO":"", "NO2":"","X":112,"Y":183,"O3_8":"","PM10_AVG":"","PM25_AVG":"","MonobjName":"交通"}' coords='112,183,120,191' href=javascript:showInfo('Yonghe'); id='Yonghe' />
		if jtitle[u'SiteKey'] in locations:
			print '{} , AQI:{} , PM2.5:{}, PM10:{}'.format(jtitle[u'SiteKey'], jtitle[u'AQI'], jtitle[u'PM25'], jtitle[u'PM10'])
