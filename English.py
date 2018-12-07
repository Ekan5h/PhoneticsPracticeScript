from bs4 import BeautifulSoup
import urllib.request
import random
import time
word='='
while(1):   
    resp = urllib.request.urlopen("http://www.phonemicchart.com/transcribe/biglist.html")
    soup = BeautifulSoup(resp, 'html.parser')
    link = soup.find_all('a', href=True)
    print('\n'+word.split('=')[1]+'\n')
    word=link[random.randint(0,len(link)-1)]['href']
    resp = urllib.request.urlopen("http://www.phonemicchart.com/"+word)
    soup = BeautifulSoup(resp, 'html.parser')
    link = soup.find('center')
    print(link.get_text())
    time.sleep(2)


