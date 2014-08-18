#mine data with metadata using python
import requests
#import pprint 
#import json
import os 
import math

def output_files(data, phrase, page_no):
    folder_path1 = os.path.dirname(__file__)+ "\\data\\IEMS\\" + phrase + "_category1"
    folder_path2 = os.path.dirname(__file__)+ "\\data\\IEMS\\" + phrase + "_category2"

    #make paths if they don't exist
    if not os.path.exists(folder_path1):
        os.makedirs(folder_path1)
    if not os.path.exists(folder_path2):
        os.makedirs(folder_path2)
    
    
    count = (page_no * 1000) - 999 #start count at appropriate place
    
    for result in data[u'results']:
        if result[u'date'] < u'2001-09-11':  
            outputfile = open(folder_path1 + "\\\\" + str(count) + '.json', 'w')
        else:
            outputfile = open(folder_path2 + "\\\\" + str(count) + '.json', 'w')
            
        outputfile.write(str(result))
        outputfile.close()
        count = count + 1


phrase = 'terrorist' #phrase to search for
results_per_page = 500 #number of results per page
page_number = 1
query_parameters = {'apikey': '8e87cf0e8a92499e9d14b67165f7018f',
                                   'phrase': phrase,
                                   'per_page' : results_per_page,
                                   'page': page_number, }
endpoint = 'http://capitolwords.org/api/text.json'
response = requests.get(endpoint, params = query_parameters)
data = response.json
num_speeches_found = data[u'num_found']
print num_speeches_found
output_files(data,phrase, page_number) #write these files

for page_no in range(int(math.ceil(float(num_speeches_found)/results_per_page))):    
    page_number = page_number + 1
    print page_number
    query_parameters = {'apikey': '8e87cf0e8a92499e9d14b67165f7018f',
                                   'phrase': phrase,
                                   'per_page' : results_per_page,
                                   'page': page_number, }
    endpoint = 'http://capitolwords.org/api/text.json'
    response = requests.get(endpoint, params = query_parameters)
    data = response.json
    num_speeches_found = data[u'num_found']
    results = data[u'results']
    output_files(data,phrase,page_number) #write these files
    
