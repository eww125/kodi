from bs4 import BeautifulSoup
import urllib2

resp = urllib2.urlopen(""http://noobsandnerds.com/portal/*REPOSITORY%20PORTAL"")
soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))

for link in soup.find_all('a', href=True):
    print link['href']
