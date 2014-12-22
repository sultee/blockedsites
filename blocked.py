# -*- coding: utf-8 -*-

import urllib2
import json

adr = 'http://api.antizapret.info/group.php?data=domain'
bazar = urllib2.urlopen(adr).read()
baza = bazar.splitlines()

check_list = []

for i in baza:
	if 'meduza' in i or 'facebook' in i or 'vk.com' in i or 'twitter' in i or '.io' in i:
		infolink = 'http://api.antizapret.info/get.php?item=' + str(i) + '&type=json'
		info = json.load(urllib2.urlopen(infolink))
		check_list.append(i+ '  Included  ' + info['register'][0]['includeTime'] + '  by  ' + info['register'][0]['org'] + '  url:  ' + info['register'][0]['url'])





for i in check_list:
	print i
print len(baza)
