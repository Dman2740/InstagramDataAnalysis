#import packages
import json
import os

#See where the json file is and we use the system call because it is more efficient
CWD=os.getcwd()
JSON_CONFIG_FILE_PATH='%s/%s' % (CWD,'2013-04-10_23-53-22_UTC.json')

#Creating a blank dictionary 
CONFIG_PROPERTIES={}


#Open the json file, parse file, and store them in dictionary
#With is a good method because it will always close 
try:
    with open(JSON_CONFIG_FILE_PATH) as data_file:
        CONFIG_PROPERTIES=json.load(data_file)
        
except IOError as e:
    print (e)
    print ('IOError:Unable to open JSON file')
    exit(1)
print (CONFIG_PROPERTIES)