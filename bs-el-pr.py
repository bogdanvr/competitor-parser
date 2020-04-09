# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 22:58:11 2019

Find all product in page

"""

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.error import HTTPError
import ssl
from datetime import datetime

now = datetime.now()
date = str(now).split(' ')[0]






ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



stock = set()
text = 0
pages = set()
h1 = set()
promo = set()

def get_page(urlcomp):
    global cat
    global pages
    global text
    global h1
    global promo
    global stock
    
    # try to get html
    
    try:
        html = urlopen(urlcomp, context=ctx)
        
    
        
    except HTTPError:
        return print('no html')
    bsobj = bs(html, 'html.parser')
    num_sp = []
    
    # try to get pagination
    try:
        pagination = bsobj.find('ul', {'class', 'pagination justify-content-center'})
        for i in pagination:
            a = i.find('a').attrs['href']
            
            
            num_a = a.split('/')[-1]
            if len(num_a) < 5:
                num_sp.append(num_a)
       
    except:
        print('error pagination')
    # try to get the maximum number of pages in the category
    try:
        num_sp = [int(i) for i in num_sp]
        num_sp.sort()
    
        tail_url = num_sp[-1:]
        print(tail_url)
        
        #we get all pages in category and add them to the list "cat"
        if tail_url:
        
            for i in range(32, tail_url[0] + 1):
                if i % 32 == 0:
                    newurl = urlcomp.rstrip() + '/' + str(i)
                    if newurl not in cat:
                        cat.append(newurl)
    except:
        print('error num_sp')
            
    # try to get page title and description        
    try:
        head = bsobj.h1.get_text()
        h1.add(head)
        print(head)
    except AttributeError:
        print('No header')
    try:
        if bsobj.find('div', {'class', 'bxr-section-desc'}):
            text += 1
            promo.add(bsobj.find('div', {'class', 'bxr-section-desc'}).text)
            print('All pages-{}, find text-{}'.format(len(pages), text))
        else:
            print('All pages-{} No text'.format(len(pages)))
    except AttributeError:
        print('No text in this page')
        
    # get title and quantity of goods
    for i in bsobj.find_all('div', {'class', 'wrp_title'}):
        a = i.find('a')
        title = a.attrs['title']
        qty = i.find('span', {'class', 'product__info_small_qty_value'})
        qty = qty.text.split(':')[1]
        stock.add('{}#{}'.format(title, qty))
    print(len(stock))
        
    

    
    
    
# write title and quantity                        
with open('elomskcatn.txt') as f:
    cat = f.readlines()

cat = [i.rstrip() for i in cat]

print(cat[8])
                   
for i in cat:
    get_page(i)



with open('bs-el-res.txt', 'w', encoding='utf-8') as f:
    f.writelines(stock)

