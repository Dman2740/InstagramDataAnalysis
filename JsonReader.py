#import packages
import json
import os
import webbrowser

new=2;

#This is in order to get the user profile from the shortcode in the json
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
        
        
except IOError as e:
    print (e)
    print ("IOError:Unable to open JSON file")
    exit(1)
