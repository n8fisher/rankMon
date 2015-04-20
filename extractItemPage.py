#!/usr/bin/python

import time
import urllib2
from BeautifulSoup import BeautifulSoup
from lxml import etree
import json

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-q','--query',help='Query')

args = parser.parse_args()
search=args.query

doc={}
results=[]

def main():
    page = urllib2.urlopen('http://www.walmart.com/search/?query=%s' % (search))
#soup = BeautifulSoup(page)
#print soup
#x = soup.body.find('div', attrs={'class' : 'container'}).text
    xpathselector1='//*[@id="tile-container"]/div[1]/div/div/h4/a/@href'
    xpathselector2='//*[@id="tile-container"]/div[2]/div/div/h4/a/@href'
    xpathselector3='//*[@id="tile-container"]/div[3]/div/div/h4/a/@href'
    htmlparser = etree.HTMLParser()
    tree = etree.parse(page, htmlparser)    
    subtree1 = tree.xpath(xpathselector1)
    subtree2 = tree.xpath(xpathselector2)
    subtree3 = tree.xpath(xpathselector3)
    results.append(subtree1[0])
    results.append(subtree2[0])
    results.append(subtree3[0])

    doc['query']=search
    doc['date']=time.strftime("%d/%m/%Y-%H:%M:%S")
    doc['results']=results
    
    print json.dumps(doc)

main()
