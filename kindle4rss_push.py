#!/usr/bin/python3
##################################################################################################################
# name: kindlerss.py
# author: Alex Garcia
# handle: @lexzap
# description: A push to kindle BS4 script for kindle4rss.com website, since I dont want to manually do it once a day
# requirements: pip3 installs of urllib and bs4 , and 2 environment variables for login: KINDLE4RSS_USER and
#               KINDLE4RSS_PASSWORD
# support vendor notice: For >25 articles and free automation please consider signing up for rss4kindle service pro
# original Python2 ported code: www.github.com/dcrystalj/kindle4rss
###################################################################################################################
import os
import sys
import urllib.request, urllib.parse, urllib.error, urllib.request, urllib.error, urllib.parse
import mechanize
import http.cookiejar

#cookielib = http.cookiejarttp.cookiejar

from bs4 import BeautifulSoup

BASE_URL = 'http://kindle4rss.com/'
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

#Debug
#print(USERNAME)
#print(PASSWORD)

# build opener using cookie jar and mechanize
o = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
urllib.request.install_opener(o)

cj = http.cookiejar.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.open(BASE_URL + '/login/')

br.select_form(nr=0)
br.form['email_address'] = USERNAME
br.form['password'] = PASSWORD
br.submit()

#pass the mechanize content back to BeautiFulSoup
doc = BeautifulSoup(br.response().read(), features="html5lib")

#print doc as DEBUG
#print(doc)

# if not get the HTML doc then exit
if not doc:
    sys.exit(3)
else:
    # get only the unread items in our article list
    table = doc.find("table", {"class": "feed-items"})
    #debugprint
    #print(table)
    #create items list holder
    t = []
    if table:
        t = table.findAll("tr")
        print("Number of Articles collected")
        print(len(t))
    # see if we have any unread articles to send
    if int(len(t)) > 0:
        print("sending the articles to kindle")
        # click send the send now button
        br.open(BASE_URL + '/send_now/')
        br.select_form(nr=0)
        br.submit()
    else:
        print("no articles to pull")
