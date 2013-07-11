#Temporal Analysis

import json
import os 
from bintrees import BinaryTree

#Variables 
speech_tree = BinaryTree() #binary tree whose values are ID/Date tuples and is aranged by date

#linux
folder_path = os.path.dirname(__file__) + "/data/immigration/" 

if not os.path.exists(folder_path):
    print "ERROR: Folder Path not Found"


def getid(file_name):
    '''gets the speech id from the file name'''
    basename = os.path.basename(file_name)
    return basename[basename.rfind("\\") + 1 : basename.rfind(".")]
    

        
## build a binary tree of file numbers arranged by (date,file_number) tuple
for root, subFolders, files in os.walk(folder_path):
    for f in files: 
        file_name = root+'/'+f
        s = open(file_name,'r')
        speech = json.loads(s.read()) #speech is a key-value Dictionary
        #add ID to speech
        speech['id'] = getid(file_name) 
        speech_id = speech['id']
        speech_date = speech['date']
        speech_tuple = speech_date, speech_id
        speech_tree.insert(speech_tuple,speech_id)  
        s.close()
    

## find the earliest and latest date in the folder
min_speech_date = speech_tree.min_item()
max_speech_date = speech_tree.max_item()

## conduct a moving average of framing


## output results