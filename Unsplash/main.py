#-*-coding:utf-8-*-
# script to download photos from unsplash

from bs4 import BeautifulSoup
from splinter import Browser
import urllib.request
import os

tag = input("Enter tag : ")
link = "https://unsplash.com/search/photos/"+tag

with Browser(driver_name='chrome', executable_path='D:/chromedriver/chromedriver.exe') as browser:
	browser.visit(link)
	html = browser.html
	soup = BeautifulSoup(html, "html.parser")
	allImages = [x.get("src") for x in soup.findAll("img")]
	images = [x.split("?")[0] for x in allImages if "images.unsplash.com" in x]
	# wget the files
	i = 0
	for x in images:
		if("photo" in x):
			print(x)
			f = open('./'+ str(i)+".jpg", 'wb')
			f.write((urllib.request.urlopen(x)).read())
			f.close()
			i = i + 1
		
	