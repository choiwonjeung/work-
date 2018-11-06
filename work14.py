from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.vox.com/2018/9/25/17901082/trump-un-2018-speech-full-text")
res = BeautifulSoup(html, features="xml")
#res = BeautifulSoup(html.read(),"html5lib")
 
tags = res.findAll("",{"class":"c-entry-content"})

a=[]
for tag in tags:
    a=(tag.getText().split())

counts=dict()
for w in a:
    if w in counts:
        counts[w]+= 1        
    else:
        counts[w] =1
   
for k in sorted(counts, key=counts.get, reverse=True):
    if counts[k]==20: break
    print('%s: %s'%(k, counts[k]))
