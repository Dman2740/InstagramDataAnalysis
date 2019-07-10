#import packages
import json
import csv
import os
import string
import webbrowser
import string
import re
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from pprint import pprint

csv_File="selfharm.csv"
new=2
url="http://www.instagram.com/p/"
url2="http://www.instagram.com/"
#See where the json file is and we use the system call because it is more efficient
CWD=os.getcwd()
#Creating a blank dictionary 
CONFIG_PROPERTIES={}

#Open the json file, parse file, and store them in dictionary
#With is a good method because it will always close
#We use load because we are reading from a json file
with open(csv_File,'w+',newline='') as csvFile:
    csvFile.write("ID,Followers,Following,Posts,URL\n")
    for file in os.listdir(os.getcwd()):
    
        # w=csv.writer(csvFile)
        # w.writerow(["ID","Followers","Following","Posts","URL"])
        
        if file.endswith(".json"):
            try:
                with open(file,"r") as data_file:
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
                    listValues.insert(0,newUser)
                    listValues.append(profileLink)
                    # pprint (listValues)
                    # dictList={i:listValues[i] for i in range(0,len(listValues))}
                    # valuesPrint=dictList.values()
                    #pprint(listValues)
                    csvFile.write("%s,%s,%s,%s,%s\n" %(listValues[0], listValues[1],listValues[2],listValues[3],listValues[4]))
            except IOError:
                print ("IOError:Unable to open JSON file")
                exit(1)
            # except UnicodeEncodeError:
            #     print((metaTitle.get('content').encode('UTF-8')))
            #     print((metaDescript.get('content').encode('UTF-8')))
            #     print((metaUrl.get('content').encode('UTF-8')))
    
