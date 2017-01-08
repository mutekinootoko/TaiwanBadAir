# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import json
import pycurl
from urllib import urlencode

locations = [u'Xindian', u'Yonghe', u'Zhongshan']

soup = BeautifulSoup(urllib2.urlopen('http://taqm.epa.gov.tw/taqm/tw/AqiMap.aspx'), 'html.parser')

areas = soup.find_all('area')
#print len(areas)
warning = ''
for eachArea in areas :
	if eachArea.has_attr('jtitle'):
		jtitle = json.loads(eachArea['jtitle'])
		#<area shape='rect' class='jTip' title='永和' alt='永和' jTitle='{"SiteName":"永和", "SiteKey":"Yonghe", "AreaKey":"North", "AQI":"", "AQIStyle":"AQI0", "MainPollutant":"","MainPollutantKey":"","PM10":"","PM25":"","O3":"","SO2":"","CO":"", "NO2":"","X":112,"Y":183,"O3_8":"","PM10_AVG":"","PM25_AVG":"","MonobjName":"交通"}' coords='112,183,120,191' href=javascript:showInfo('Yonghe'); id='Yonghe' />
		# bad air condition 
		if jtitle[u'SiteKey'] in locations and int(jtitle[u'AQI']) > 48:
			warning += '{} , AQI:{} , PM2.5:{}, PM10:{}. '.format(jtitle[u'SiteKey'], jtitle[u'AQI'], jtitle[u'PM25'], jtitle[u'PM10'])
print warning
c = pycurl.Curl()
c.setopt(pycurl.URL, 'https://maker.ifttt.com/______YOUR IFTTT MAKER URL KEY HERE__________')
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, json.dumps({'value1': warning}))
c.setopt(pycurl.HTTPHEADER, ['Content-Type:application/json'])
c.perform()
#print c.getinfo(pycurl.HTTP_CODE)
c.close()
