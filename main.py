#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
import sys
import urllib2
import time
from bs4 import BeautifulSoup
from selenium import webdriver
#reload(sys)
#sys.setdefaultencoding('utf8') 

#read list
old_list = [line.rstrip('\n') for line in open('list.txt')]

flag = False

##parse page
url = 'https://v.douyu.com/author/RGJwkGQ6wZjO'
#driver = webdriver.Chrome('/usr/local/Cellar/chromedriver/2.20/bin/chromedriver') #driver for chrome
driver = webdriver.Firefox()
driver.get(url) # open webpage
time.sleep(3)
counter = 0
link_list = []

driver.find_element_by_xpath("//li[@class='long-video-tab']").click()
time.sleep(3)
last_height = driver.execute_script("return document.body.scrollHeight")
while True: 
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(3)

	soup = BeautifulSoup(driver.page_source, "html.parser")
	#print(soup.prettify())
	current_links = soup.find('ul', class_ = 'longvideo-waterfall video-waterfall')
	#print(current_links.prettify())
	for current_link_list in current_links.find_all('a', href=True):
		if current_link_list not in link_list:
			link_list.append(current_link_list['href'])
			counter += 1

	new_height = driver.execute_script("return document.body.scrollHeight")
    	if new_height == last_height:
        	break
    	last_height = new_height


	#links = current_link_list.select('div.waterfall-item > a@href')
#for l in links:
	#print l.text
driver.quit()
print 'Total videos found: '+str(counter)
print ''

change = []
for link in link_list:
	if link not in old_list:
		flag = True
		change.append(link)

cnt = len(change)
if flag:
	print str(cnt) + ' new video(s) detected, list updated. Start downloading'	
	print ''
	file = open('list.txt','w') 
	for link in link_list:
		file.write(link)
		file.write('\n')
	file.close()
	for link in change:
		os.system("python /data/le/DouyuTest/download.py "+link)
else:
	print 'No new videos have found, quit.'


