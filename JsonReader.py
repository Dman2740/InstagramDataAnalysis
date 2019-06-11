#import packages
import json
import os
import string
import webbrowser
import string
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

new=2
url="http://www.instagram.com/p/"
url2="http://www.instagram.com/"
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
        #webbrowser.open(newUrl,new=new)
        #Open Connection and grabbing the page and then we store it
        uClient=uReq(newUrl)
        page_html=uClient.read()
        uClient.close()
        #We need to parse the html
        page_soup=soup(page_html,"html.parser")
        post=page_soup.find('meta',attrs={'property':'og:description'})
        text=post.get('content')
        index=text.find('@')
        str1=text[(index+1):len(text)]
        stringy=str1.split(' ')
        userProfile=stringy[0]
        if((userProfile[-1]==")")):
            newUser=userProfile[0:(len(userProfile)-1)]
            profileLink=url2+newUser
            webbrowser.open(profileLink,new=new)
        else:
            profileLink=url2+userProfile
            webbrowser.open(profileLink,new=new)
        #Now i need to grab the html from the user profile 
        newRead=uReq(profileLink)
        profilePageHtml=newRead.read()
        newRead.close()
        #Print out the html of the user profile
        profilePage_soup=soup(profilePageHtml,"html.parser")
        #I am grabbing the meta data from the user profile
        metaTitle=profilePage_soup.find('meta',property='og:title')
        metaDescript=profilePage_soup.find('meta',property='og:description')
        metaUrl=profilePage_soup.find('meta',property='og:url')
        print(metaTitle.get('content'))
        print(metaDescript.get('content'))
        print(metaUrl.get('content'))
        
except IOError:
    print ("IOError:Unable to open JSON file")
    exit(1)

