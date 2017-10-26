import urllib2
url = "http://noobsandnerds.com/portal/*REPOSITORY%20PORTAL/"
response = urllib2.urlopen(url)
scraped = response.read()
split1 = scraped.split("href=")
file_list=[]
for x in range(0,len(split1)):
    if split1[x].find(".zip") != -1:
        file_list.append(split1[x][1:(split1[x].find(".zip")+4)])

#print file_list[0]
from os.path import expanduser
home = expanduser("~")
print home

for x in range(0,len(file_list)):
    url = "http://noobsandnerds.com/portal/*REPOSITORY%20PORTAL/" + file_list[x]
    response = urllib2.urlopen(url)
    zipcontent = response.read()
    print "writing " +  home + "/kodi_ubuntu/repo/" + file_list[x] + " ..."
    with open(home + "/kodi_ubuntu/repo/" + file_list[x], 'w') as f:
	       f.write(zipcontent)
