#mine data with metadata using python
import requests
#import pprint 
import json
import os 
import math

def output_files(data, phrase, page_no):
    #windows):
    #folder_path = os.path.dirname(__file__) + "\\data\\" + phrase

    #linux
    folder_path = os.path.dirname(__file__) + "/data/" + phrase
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
    count = (page_no * 1000) - 999
    for result in data[u'results']:
        #windows
        #outputfile = open(folder_path + "\\\\" + str(count) + '.json', 'w')
        #linux
        outputfile = open(folder_path + "/" + str(count) + '.json', 'wb')
        json.dump(result,outputfile)
        outputfile.close()
        count = count + 1


phrase = 'gun' #phrase to search for
#print phrase outputfile#debug
results_per_page = 1000 #number of results per page
page_number = 1
query_parameters = {'apikey': '8e87cf0e8a92499e9d14b67165f7018f',
                                   'phrase': phrase,
                                   'per_page' : results_per_page,
                                   'page': page_number, }
endpoint = 'http://capitolwords.org/api/text.json'
response = requests.get(endpoint, params = query_parameters)
data = response.json
num_speeches_found = data[u'num_found']
print str(num_speeches_found) + " speeches found"
output_files(data,phrase, page_number) #write these files

for page_no in range(int(math.ceil(float(num_speeches_found)/results_per_page))):
    page_number = page_number + 1
    query_parameters = {'apikey': '8e87cf0e8a92499e9d14b67165f7018f',
                                   'phrase': phrase,
                                   'per_page' : results_per_page,
                                   'page': page_number, }
    endpoint = 'http://capitolwords.org/api/text.json'
    response = requests.get(endpoint, params = query_parameters)
    data = response.json       
    num_speeches_found = data[u'num_found']
    output_files(data,phrase,page_number) #write these files
    
