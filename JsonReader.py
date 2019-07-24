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

csvFile="selfharm.csv"
url="https://i.instagram.com/api/v1/users/"
Link="https://www.instagram.com/"
urlEnd="/info/"
printValues={}
# open outfile here.... and you will get file descriptor.
#with open(csv_File,'w+',newLine='') as csvFile:
fd=open(csvFile,'w+')
fd.write("OwnerID, ShortCode,POST_CNT,URL,username,full_name,is_private, " +
         "is_verified,has_anonymous_profile_picture,post_count, " +
         "follower,following,following_tag_count,biography, " +
         "total_igtv_videos,total_ar_effects,usertags_count,is_interest_account, " +
         "latest_reel_media, "+
         "has_highlight_reels,can_be_reported_as_fraud, " +
         "is_potential_business,auto_expand_chaining,highlight_reshare_disabled,\n")
with open('id-shortcode.csv') as myFile:
    reader=csv.DictReader(myFile)
    for row in reader: 
        ownId=row['OWNER_ID']
        shorty=row['SHORTCODE']
        cnt =row['POST_CNT']
        try:
            newUrl=url+ownId+urlEnd
            uClient=uReq(newUrl)
            page_html=uClient.read()
            uClient.close()
            #We need to parse the html
            page_soup=soup(page_html,"html.parser")
            stuff=page_soup.get_text()
            data=json.loads(stuff)
            del data['user']['pk']
            del data["user"]["profile_pic_url"]
            del data['user']['profile_pic_id']
            del data['user']['hd_profile_pic_versions']
            del data['user']['hd_profile_pic_url_info']
            del data['user']['external_url']
            user=data['user']['username']
            Linky=Link+user
            for key,value in data['user'].items():
                printValues[key]=value
            fd.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" %(ownId,shorty,cnt,Linky,printValues['username'],printValues['full_name'],printValues['is_private'],printValues['is_verified'],printValues['has_anonymous_profile_picture'],printValues['media_count'],printValues['follower_count'],printValues['following_count'],printValues['following_tag_count'],printValues['biography'],printValues['total_igtv_videos'],printValues['total_ar_effects'],printValues['usertags_count'],printValues['is_interest_account'],printValues['latest_reel_media'],printValues['has_highlight_reels'],printValues['can_be_reported_as_fraud'],printValues['is_potential_business'],printValues['auto_expand_chaining'],printValues['highlight_reshare_disabled']))
        except IOError:
            fd.write("N/A\n")
        except UnicodeEncodeError:
            fd.write("N/A\n")
        except KeyError:
            fd.write("N/A\n")
