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

from bs4 import BeautifulSoup

BASE_URL = 'http://kindle4rss.com/'
USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')

# build opener
o = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
urllib.request.install_opener(o)

# login
p = urllib.parse.urlencode({
    'email_address': USERNAME,
    'password': PASSWORD
}).encode("utf-8")
doc = BeautifulSoup(o.open(BASE_URL + '/login/',
                           p).read().decode('utf8', 'replace'),
                    features="html.parser")

# get list of articles
doc = BeautifulSoup(o.open(BASE_URL, p).read().decode('utf8', 'replace'),
                    features="html.parser")

#print doc as DEBUG
#print(doc)

# if not get the HTML doc then exit
if not doc:
    sys.exit(3)
else:
    # get only the unread items in our article list
    table = doc.find("table", {"class": "feed-items"})
    if table:
        t = table.findAll("tr")
        print(len(t))
        # see if we have any unread articles to send
        if int(len(t)) > 0:
            # click send the send now button
            BeautifulSoup(o.open(BASE_URL + '/send_now/').read().decode(
                'utf8', 'replace'),
                          features="html.parser")
