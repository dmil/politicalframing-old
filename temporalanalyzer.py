#Temporal Analysis

import json
import os 
from bintrees import BinaryTree


#linux
folder_path = os.path.dirname(__file__) + "/data/immigration/" 

if not os.path.exists(folder_path):
    print "ERROR: Folder Path not Found"


def getid(file_name):
    '''gets the speech id from the file name'''
    basename = os.path.basename(file_name)
    return basename[basename.rfind("\\") + 1 : basename.rfind(".")]
    
def build_btree():
    speech_tree = BinaryTree() #binary tree whose values are ID/Date tuples and is aranged by date
    ## build a binary tree of file numbers arranged by (date,file_number) tuple
    oswalkgen = os.walk(folder_path)
    next(oswalkgen)
    for root, subFolders, files in oswalkgen:#os.walk(folder_path):
        for f in files: 
            file_name = root+'/'+f
            s = open(file_name,'r')
            speech = json.loads(s.read()) #speech is a key-value Dictionary
            #add ID to speech
            speech['id'] = getid(file_name) 
            speech_id = speech['id']
            speech_date = speech['date']
            speech_tuple = speech_date, speech_id
            speech_tree.insert(speech_tuple,file_name)  
            s.close()   
    return speech_tree
    ## find the earliest and latest date in the folder
    #min_speech_date = speech_tree.min_item()
    #max_speech_date = speech_tree.max_item()

        


## conduct a moving average of framing

from sklearn.datasets import load_files

def sanitize_training_set(training_set):
    
    def list_to_string(lst):
        string_text = ""
        for sentence in lst:
            string_text += sentence  
        return string_text
    
    spoken_texts = []
    count = 0
    for item in training_set['data']:
        j_speech = json.loads(item)
        speech_text = list_to_string(j_speech['speaking'])
        training_set['data'][count] = speech_text
        count = count + 1
        

    
#build a training set from a set of files
#next version should take in file_list, a function that can take in file_paths and turn 
#them into categories 0,1,2,3,...as well as list of what 0,1,2,3 mean
#Right now hard-coded as a democrat vs republican classifier 
def build_training_set(file_list):
    '''This function is an alternative form of the loads in sklearn but allows 
    me to load from a list of files output by another file rather than the folder
    structure prescribed by giving loads a folder-path'''
    from sklearn.datasets.base import Bunch
    
    b = Bunch()
    b['filenames'] = file_list #filenames
    
    def target_function(filepath):
        #/home/dhrumil/Desktop/PoliticalFraming/data/immigration/D/123.json
        if filepath[filepath.rfind("/")-1] == 'D':
            return 0
        elif filepath[filepath.rfind("/")-1] == 'R':
            return 1
        else:
            print "file must be categorized as D or R : " + str(filepath)
                

    b['target'] = [] #target
    for filepath in file_list:
        b['target'].append(target_function(filepath))
        
    b['target_names'] = ['D','R'] #target_names
    
    b['data'] = [] #data
    for filepath in file_list:
        f = open(filepath,'r')
        jdata = json.loads(f.read())
        f.close()
        
        speech_string = ""
        for sentence in jdata['speaking']:
            speech_string += sentence
            
        b['data'].append(speech_string)
            
    b['DESCR'] = "" #DESCR
    
    return b


### MAIN PART  - DRIVER ### 

b = build_btree()

count = 0
while not b.is_empty():
    file_list = []
    for item in b.nsmallest(500,pop=True):
        file_list.append(item[1])
    
    training_set = build_training_set(file_list)
    
    from findFrames import *
    #from findFrames import return_framing_data
    log_likelihoods = return_framing_data(training_set, folder_path + "analysis" + str(count) + ".txt")    
    print log_likelihoods[5]
    
    count = count + 1














#training_set = load_files(folder_path,shuffle=True)
#sanitize_training_set(training_set)


## output results
#from findFrames import write_framing_data
#write_framing_data(training_set, folder_path + "analysis.txt")    
#pre911gen = (item for item in speech_tree if item[0]<'2001-09-11')
#post911gen = (item for item in speech_tree if item[0]>'2001-09-11')
