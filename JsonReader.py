#import packages
import json
import csv
import os
import string
import webbrowser
import string
import re
import urllib
import urllib.error
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from pprint import pprint

csvFile="selfharm.csv"
new=2
url="http://www.instagram.com/p/"
url2="http://www.instagram.com/"
#See where the json file is and we use the system call because it is more efficient
CWD=os.getcwd()
#Creating a blank dictionary 
CONFIG_PROPERTIES={}
listValues={}

#reading the csv first

# open outfile here.... and you will get file descriptor.
#with open(csv_File,'w+',newLine='') as csvFile:
fd=open(csvFile,'w+')
fd.write("OwnerID, ShortCode,POST_CNT,ID,Followers,Following,Posts,URL\n")
with open('id-shortcode.csv') as myFile:
    reader=csv.DictReader(myFile)
    for row in reader: 
        ownId=row['OWNER_ID']
        shorty=(row['SHORTCODE'])
        cnt = (row['POST_CNT'])
        try:
            newUrl=url+shorty
            #webbrowser.open(newUrl,new=new)
            #Open Connection and grabbing the page and then we store it
            uClient=uReq(newUrl)
            
            page_html=uClient.read()
            uClient.close()
            #We need to parse thee html
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
            else:
                newUser=userProfile
                profileLink=url2+userProfile
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
            contentUser=(metaDescript.get('content'))
            listValues=re.findall('\d+', contentUser)
            if(len(listValues)>3):
                del listValues[3:len(listValues)]
            #This has the followers, following, post count
            listValues.insert(0,ownId)
            listValues.insert(1,shorty)
            listValues.insert(2,cnt)
            listValues.insert(3,newUser)
            listValues.append(profileLink)
            fd.write("%s,%s,%s,%s,%s,%s,%s,%s\n" %(listValues[0], listValues[1],listValues[2],listValues[3],listValues[4],listValues[5],listValues[6],listValues[7]))
        except IOError:
            fd.write("N/A,N/A,N/A,N/A,N/A,N/A,N/A,N/A\n")
            #print("Got past the error")
    
