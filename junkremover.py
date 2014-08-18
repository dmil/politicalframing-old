import os
print os.path.dirname(__file__) + "/data/"

global filepath 
filepath1 = "C:\\Users\\Dhrumil\\Documents\\GitHub\\PoliticalFraming\\data\\IEMS\\terrorist_category1"
filepath2 = "C:\\Users\\Dhrumil\\Documents\\GitHub\\PoliticalFraming\\data\\IEMS\\terrorist_category2"

import glob
import json, ast

durbin_pre = [1042, 11015, 15249, 15390, 15434,18151,18159,18228,20025,20233,24006,24442,24489,26020,27248,28276,28323,28344,4141,463,5300,6488,7180,9343]
filepath_durbin = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\durbin_pre.txt"

#output_file2 = os.path.dirname(__file__) + "/data/IEMS/russfeingoldpost.txt"
#if not os.path.exists(output_file):
#    os.makedirs(output_file)


def remove_junk(output_file, list_of_speeches):
    f = open(output_file,'w')
    print list_of_speeches
    for speech_number in list_of_speeches:
        for speech_file in glob.glob(filepath1+"/*"):
            if os.path.basename(speech_file) == str(speech_number):
                speech_f = open(speech_file,'r')
                datastring = speech_f.read()
                speech = ast.literal_eval(datastring)
                speaking_part = speech[u'speaking']
                
                speaking_string = ""
                for sentance in speaking_part:
                    speaking_string += sentance
                    speaking_string += " "
                
                f.write(speaking_string)
                speech_f.close()
                
        for speech_file in glob.glob(filepath2+"/*"):
            if os.path.basename(speech_file) == str(speech_number):
                speech_f = open(speech_file,'r')
                datastring = speech_f.read()
                speech = ast.literal_eval(datastring)
                speaking_part = speech[u'speaking']
                
                speaking_string = ""
                for sentance in speaking_part:
                    speaking_string += sentance
                    speaking_string += " "
                
                f.write(speaking_string)
                speech_f.close()           
    f.close()
        