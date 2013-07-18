import os
import json
from shutil import move as filemove
from temporalanalyzer import getid

#linux
folder_path = os.path.dirname(__file__) + "/data/gun/" 

# build a binary tree of file numbers arranged by (date,file_number) tuple
for root, subFolders, files in (os.walk(folder_path)):
    for f in files: 
        file_name = folder_path + f
        s = open(file_name,'r')
        speech = json.loads(s.read()) #speech is a key-value Dictionary
        #add ID to speech
        speech['id'] = getid(file_name) 
        s.close()
    
    if speech['speaker_party'] == 'D':
        filemove(file_name, root + "/D/" + f)        
    elif speech['speaker_party'] == 'R':
        filemove(file_name, root + "/R/" + f)
    else: 
        os.remove(file_name)