#import packages
import json
import os
import webbrowser
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

new=2;
url="http://www.instagram.com/p/"

#See where the json file is and we use the system call because it is more efficient
CWD=os.getcwd()
JSON_CONFIG_FILE_PATH='%s/%s' % (CWD,'2013-04-10_23-53-22_UTC.json')

#Creating a blank dictionary 
CONFIG_PROPERTIES={}

#Open the json file, parse file, and store them in dictionary
#With is a good method because it will always close
#We use load because we are reading from a json file
try:
    with open(JSON_CONFIG_FILE_PATH,"r") as data_file:
        CONFIG_PROPERTIES=json.load(data_file)
        shortcode=(CONFIG_PROPERTIES['node']['shortcode'])
        newUrl=url+shortcode
        webbrowser.open(newUrl,new=new)
        #Open Connection and grabbing the page and then we store it
        uClient=uReq(newUrl)
        page_html=uClient.read()
        uClient.close()
        #We need to parse the html
        page_soup=soup(page_html,"html.parser")
        profile=page_soup.find("script",type="application/ld+json")
        stringProfile=profile.string
        #Converts the html tag to a type of dictionary 
        dictProfile=json.loads(stringProfile)
        #This will grap the profileurl
        profileName=dictProfile['author']['mainEntityofPage']
        profileLink=profileName['@id']
        webbrowser.open(profileLink,new=new)
        
        
except IOError as e:
    print (e)
    print ("IOError:Unable to open JSON file")
    exit(1)
