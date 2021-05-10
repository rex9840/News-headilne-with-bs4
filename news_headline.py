from bs4 import BeautifulSoup 
import requests
import os 



request_data=requests.get('https://kathmandupost.com',timeout =10).text
soup=BeautifulSoup(markup=request_data,features='lxml')
title=set()

try:
    for tag in soup.find('div',class_='col-xs-12 col-sm-6 col-md-4 grid-first divider-right order-2--sm'):
        print("Title:\t",tag.h3.text.strip(),end="\n")
        title.add(tag.h3.text.strip())
        print("Author:\t",tag.span.text.strip(),end="\n")
        print("Description:\n",tag.p.text.strip(),end="\n")
        print()
        

    for tag in soup.find_all('article',class_='article-image'):
        if tag.h3.text.strip() not in title:
            print("Title:\t",tag.h3.text.strip(),end="\n")
            print("Author:\t",tag.span.text.strip(),end="\n")
            print("Description:\n",tag.p.text.strip(),end="\n")
            print()
            
        
            
    
except Exception:pass 





