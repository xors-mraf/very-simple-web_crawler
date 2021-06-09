# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from bs4 import BeautifulSoup
import lxml
import requests
import hashlib
count=0

d2={}

def link_finder(link):
 links = []
 try:
  req = requests.get(link)
 except requests.exceptions.RequestException as e:
     pass
 soup= BeautifulSoup(req.text,'lxml')
 for linq in soup.findAll('a'):
   st=linq.get('href')
   if st:
     if (st.startswith('https')):
           links.append(st)
 for lin in links:
     hash=hashlib.md5(lin.encode('utf-8')).hexdigest()
     if hash in d2:
         d2[hash] += 1
     else:
         d2.update({hash: 1})
     print(lin)
     if(d2[hash]<=1):
        link_finder(lin)
     else:
         continue


if __name__=="__main__":
 link=input('hello please enter you link for crawling!:')
 link_finder(link)




