# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 22:58:11 2019

@author: bogdan



"""



from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.error import HTTPError
import re
import ssl
from datetime import datetime


now = datetime.now()
date = str(now).split(' ')[0]






ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE




text = 0
pages = set()
h1 = set()
promo = set()

def get_page(urlcomp):
    global pages
    global text
    global h1
    global promo
    
    #try to get html
    try:
        html = urlopen(urlcomp, context=ctx)
        
    
        
    except HTTPError:
        return print('no html')
    try:
        bsobj = bs(html, 'html.parser')
    except:
        print("no bsobj")
    
    #try to get page title
    try:
        head = bsobj.h1.get_text()
        h1.add(head)
        print(head)
    except AttributeError:
        print('No header')
        
    # try to get page description
    try:
        if bsobj.find('div', {'class', 'bxr-section-desc'}):
            text += 1
            promo.add(bsobj.find('div', {'class', 'bxr-section-desc'}).text)
            print('All pages-{}, find text-{}'.format(len(pages), text))
        else:
            print('All pages-{} No text'.format(len(pages)))
    except AttributeError:
        print('No text in this page')
    
    # try to get URL
    for i in bsobj.find_all('a', href=re.compile("(/catalog/)") ):
        if 'href' in i.attrs:
            if i.attrs['href'] not in pages:
                
                
                
                if len(i.attrs['href'].split('/')) < 7:
                    print(len(i.attrs['href'].split('/')))
                    
                    
                    if '?' not in i.attrs['href']:
                                        
                        
                        newpage = i.attrs['href']
                        print(newpage)
                        pages.add(newpage)
                        get_page(newpage)

get_page("https://elomsk.ru")

pages = [i + '\n' for i in pages]

# write URL in file

with open('elomskcatn.txt', 'w') as f:
    f.writelines(pages)