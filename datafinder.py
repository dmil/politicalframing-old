### Use This file to find a folder of speeches
### for speeches with particular parameters

import os
print os.path.dirname(__file__) + "/data/"

global filepath 
filepath1 = "C:\\Users\\Dhrumil\\Documents\\GitHub\\PoliticalFraming\\data\\IEMS\\terrorist_category1"
filepath2 = "C:\\Users\\Dhrumil\\Documents\\GitHub\\PoliticalFraming\\data\\IEMS\\terrorist_category2"

import glob
import json, ast

#for speech_file in glob.glob(filepath+"/*"):
#    f = open(speech_file,'r')
#    datastring = f.read()
#    data = ast.literal_eval(datastring)
#    if data[u'bioguide_id'] == "L000304":
#        print speech_file
#    f.close()
joe_lieberman = "L000304"
dick_durbin = "D000563"
russ_feingold = "F000061"
rand_paul = "P000603"
marco_rubio = "R000595"
john_mccain = "M000303"
charles_grassley = "G000386"
chuck_hagel = "H001028"
ted_cruz = "C001098"
linsey_graham = "G000359"
arlen_specter = "S000709" 
robert_kerry = "K000146"


#The following functions return a list of speech numbers that match the query
def speeches_by_congressperson(bioguide):
    print "Pre 9/11"
    for speech_file in glob.glob(filepath1+"/*"):
        f = open(speech_file,'r')
        datastring = f.read()
        data = ast.literal_eval(datastring)
        if data[u'bioguide_id'] == bioguide:
            print os.path.basename(speech_file)
        f.close()
        
    print "\nPost 9/11"
    for speech_file in glob.glob(filepath2+"/*"):
        f = open(speech_file,'r')
        datastring = f.read()
        data = ast.literal_eval(datastring)
        if data[u'bioguide_id'] == bioguide:
            print os.path.basename(speech_file)
        f.close()

def speeches_by_congressperson_pre(bioguide):
    print "Pre 9/11"
    list_of_speeches = []
    for speech_file in glob.glob(filepath1+"/*"):
        f = open(speech_file,'r')
        datastring = f.read()
        data = ast.literal_eval(datastring)
        if data[u'bioguide_id'] == bioguide:
            list_of_speeches.append(os.path.basename(speech_file))
        f.close()
    return list_of_speeches

def speeches_by_congressperson_post(bioguide):
    print "Post 9/11"
    list_of_speeches = []
    for speech_file in glob.glob(filepath2+"/*"):
        f = open(speech_file,'r')
        datastring = f.read()
        data = ast.literal_eval(datastring)
        if data[u'bioguide_id'] == bioguide:
            list_of_speeches.append(os.path.basename(speech_file))
        f.close()
    return list_of_speeches
        
def speeches_by_party_pre(party_letter):
    print "Pre 9/11"
    list_of_speeches = []
    for speech_file in glob.glob(filepath1+"/*"):
        f = open(speech_file,'r')
        datastring = f.read()
        data = ast.literal_eval(datastring)
        if data[u'speaker_party'] == party_letter:
            list_of_speeches.append(os.path.basename(speech_file))
        f.close()
    return list_of_speeches
    
def speeches_by_party_post(party_letter):
    print "Post 9/11"
    list_of_speeches = []
    for speech_file in glob.glob(filepath2+"/*"):
        f = open(speech_file,'r')
        datastring = f.read()
        data = ast.literal_eval(datastring)
        if data[u'speaker_party'] == party_letter:
            list_of_speeches.append(os.path.basename(speech_file))
        f.close()
    return list_of_speeches
    
def speeches_by_party_and_year(party_letter, start_date, end_date):
    print "Speeches_by_party_and_year"
    list_of_speeches1 = []
    list_of_speeches2 = []

    for speech_file in glob.glob(filepath1+"/*"):
        f = open(speech_file,'r')
        datastring = f.read()
        data = ast.literal_eval(datastring)
        if (data[u'speaker_party'] == party_letter) and (data[u'date'] > start_date) and (data[u'date'] < end_date):
            list_of_speeches1.append(os.path.basename(speech_file))
        f.close()
    for speech_file in glob.glob(filepath2+"/*"):
        f = open(speech_file,'r')
        datastring = f.read()
        data = ast.literal_eval(datastring)
        if (data[u'speaker_party'] == party_letter) and (data[u'date'] > start_date) and (data[u'date'] < end_date):
            list_of_speeches2.append(os.path.basename(speech_file))
        f.close()
    return list_of_speeches1+list_of_speeches2

execfile(os.path.dirname(__file__)+"/junkremover.py") 

#print "\n BY YEAR \n"
#filepath = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\terrorism\\republicans\\r_12_13.txt"
#speeches = speeches_by_party_and_year("R", "2012-01-01", "2013-01-01")
#print speeches
#
#filepath = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\terrorism\\republicans\\r_11_12.txt"
#speeches = speeches_by_party_and_year("R", "2011-01-01", "2012-01-01")
#print speeches
#
#remove_junk(filepath, speeches)
#filepath = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\terrorism\\republicans\\r_10_11.txt"
#speeches = speeches_by_party_and_year("R", "2010-01-01", "2011-01-01")
#print speeches
#remove_junk(filepath, speeches)
#
#filepath = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\terrorism\\republicans\\r_09_10.txt"
#speeches = speeches_by_party_and_year("R", "2009-01-01", "2010-01-01")
#print speeches
#remove_junk(filepath, speeches)
#
#filepath = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\terrorism\\republicans\\r_08_09.txt"
#speeches = speeches_by_party_and_year("R", "2008-01-01", "2009-01-01")
#print speeches
#remove_junk(filepath, speeches)
#
#filepath = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\terrorism\\republicans\\r_07_08.txt"
#speeches = speeches_by_party_and_year("R", "2007-01-01", "2008-01-01")
#print speeches
#remove_junk(filepath, speeches)
#
#filepath = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\terrorism\\republicans\\r_06_07.txt"
#speeches = speeches_by_party_and_year("R", "2006-01-01", "2007-01-01")
#print speeches
#remove_junk(filepath, speeches)
#
#filepath = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\terrorism\\republicans\\r_05_06.txt"
#speeches = speeches_by_party_and_year("R", "2005-01-01", "2006-01-01")
#print speeches
#remove_junk(filepath, speeches)
#
#filepath = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\terrorism\\republicans\\r_04_05.txt"
#speeches = speeches_by_party_and_year("R", "2004-01-01", "2005-01-01")
#print speeches
#remove_junk(filepath, speeches)
#
#filepath = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\terrorism\\republicans\\r_03_04.txt"
#speeches = speeches_by_party_and_year("R", "2003-01-01", "2004-01-01")
#print speeches
#remove_junk(filepath, speeches)
#
#filepath = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\terrorism\\republicans\\r_02_03.txt"
#speeches = speeches_by_party_and_year("R", "2002-01-01", "2003-01-01")
#print speeches
#remove_junk(filepath, speeches)
#
#filepath = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\terrorism\\democrats\\d_01_02.txt"
#speeches = speeches_by_party_and_year("D", "2001-01-01", "2002-01-01")
#print speeches
#remove_junk(filepath, speeches)

filepath = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\terrorism\\democrats\\d_00_01.txt"
speeches = speeches_by_party_and_year("D", "2000-01-01", "2001-01-01")
print speeches
remove_junk(filepath, speeches)

filepath = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\terrorism\\republicans\\r_01_02.txt"
speeches = speeches_by_party_and_year("R", "2001-01-01", "2002-01-01")
print speeches
remove_junk(filepath, speeches)

filepath = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\terrorism\\republicans\\r_00_01.txt"
speeches = speeches_by_party_and_year("R", "2000-01-01", "2001-01-01")
print speeches
remove_junk(filepath, speeches)

#filepath = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\terrorism\\democrats\\d_99_00.txt"
#speeches = speeches_by_party_and_year("D", "1999-01-01", "2000-01-01")
#print speeches
#remove_junk(filepath, speeches)
#
#filepath = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\terrorism\\democrats\\d_98_99.txt"
#speeches = speeches_by_party_and_year("D", "1998-01-01", "1999-01-01")
#print speeches
#remove_junk(filepath, speeches)
#
#filepath = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\terrorism\\democrats\\d_97_98.txt"
#speeches = speeches_by_party_and_year("D", "1997-01-01", "1998-01-01")
#print speeches
#remove_junk(filepath, speeches)
#
#filepath = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\terrorism\\democrats\\d_96_97.txt"
#speeches = speeches_by_party_and_year("R", "1996-01-01", "1997-01-01")
#print speeches
#remove_junk(filepath, speeches)
#


#print "\n BY PARTY \n"
#democrats = "D"
#republicans = "R"
#print "\n DEMOCRAT PARTY PRE \n"
#filepath_pre = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\terrorism\\combined_speeches\\democrats_pre.txt"
#speeches_pre = speeches_by_party_pre(democrats)
#print speeches_pre
#remove_junk(filepath_pre, speeches_pre)
#
#print "\n DEMOCRAT PARTY POST \n"
#filepath_pre = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\terrorism\\combined_speeches\\democrats_post.txt"
#speeches_post = speeches_by_party_post(democrats)
#print speeches_post
#remove_junk(filepath_pre, speeches_post)





#print "\nJOE LIEBERMAN\n"
#filepath_pre = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\combined_speeches\\lieberman_pre.txt"
#speeches_pre = speeches_by_congressperson_pre(joe_lieberman)
#print speeches_pre
#remove_junk(filepath_pre, speeches_pre)
#
#filepath_post = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\combined_speeches\\lieberman_post.txt"
#speeches_post = speeches_by_congressperson_post(joe_lieberman)
#print speeches_post
#remove_junk(filepath_post, speeches_post)
#
#print "\nDICK DURBIN\n"
#filepath_post = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\combined_speeches\\durbin_post.txt"
#dick_durbin_post = speeches_by_congressperson_post(dick_durbin)
#remove_junk(filepath_post, dick_durbin_post)
#
#print "\nCHUCK HAGEL\n"
#filepath_pre = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\combined_speeches\\hagel_pre.txt"
#speeches_pre = speeches_by_congressperson_pre(chuck_hagel)
#print speeches_pre
#remove_junk(filepath_pre, speeches_pre)
#
#filepath_post = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\combined_speeches\\hagel_post.txt"
#speeches_post = speeches_by_congressperson_post(dick_durbin)
#print speeches_post
#remove_junk(filepath_post, speeches_post)
#
#print "\nRUSS FEINGOLD\n"
#filepath_pre = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\combined_speeches\\feingold_pre.txt"
#speeches_pre = speeches_by_congressperson_pre(russ_feingold)
#print speeches_pre
#remove_junk(filepath_pre, speeches_pre)
#
#filepath_post = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\combined_speeches\\feingold_post.txt"
#speeches_post = speeches_by_congressperson_post(russ_feingold)
#print speeches_post
#remove_junk(filepath_post, speeches_post)
#
#print "\nRAND PAUL\n"
#filepath_pre = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\combined_speeches\\rand_paul_pre.txt"
#speeches_pre = speeches_by_congressperson_pre(rand_paul)
#print speeches_pre
#remove_junk(filepath_pre, speeches_pre)
#
#filepath_post = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\combined_speeches\\rand_paul_post.txt"
#speeches_post = speeches_by_congressperson_post(rand_paul)
#print speeches_post
#remove_junk(filepath_post, speeches_post)
#
#print "\nMARCO RUBIO\n"
#filepath_pre = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\combined_speeches\\marco_rubio_pre.txt"
#speeches_pre = speeches_by_congressperson_pre(marco_rubio)
#print speeches_pre
#remove_junk(filepath_pre, speeches_pre)
#
#filepath_post = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\combined_speeches\\marco_rubio_post.txt"
#speeches_post = speeches_by_congressperson_post(marco_rubio)
#print speeches_post
#remove_junk(filepath_post, speeches_post)
#
#print "\nJOHN MCCAIN\n"
#filepath_pre_Reg = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\terrorism\\combined_speeches\\john_mccain_pre.txt"
#filepath_pre = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\terrorism\\combined_speeches\\john_mccain_pre.txt"
#speeches_pre = speeches_by_congressperson_pre(john_mccain)
#print speeches_pre
#remove_junk(filepath_pre, speeches_pre)
#
#filepath_post_reg = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\terrorism\\combined_speeches\\john_mccain_post.txt"
#filepath_post = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\terrorism\\combined_speeches\\john_mccain_post.txt"
#speeches_post = speeches_by_congressperson_post(john_mccain)
#print speeches_post
#remove_junk(filepath_post, speeches_post)
#
#print "\nCHARLES GRASSLEY\n"
#filepath_pre = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\combined_speeches\\charles_grassley_pre.txt"
#speeches_pre = speeches_by_congressperson_pre(charles_grassley)
#print speeches_pre
#remove_junk(filepath_pre, speeches_pre)
#
#filepath_post = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\combined_speeches\\charles_grassley_post.txt"
#speeches_post = speeches_by_congressperson_post(charles_grassley)
#print speeches_post
#remove_junk(filepath_post, speeches_post)
#
#print "\nTED CRUZ\n"
#filepath_post = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\combined_speeches\\ted_cruz_post.txt"
#speeches_post = speeches_by_congressperson_post(ted_cruz)
#print speeches_post
#remove_junk(filepath_post, speeches_post)
#
#print "\n LINSEY GRAHAM \n"
#filepath_pre = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\combined_speeches\\linsey_graham_pre.txt"
#speeches_pre = speeches_by_congressperson_pre(linsey_graham)
#print speeches_pre
#remove_junk(filepath_pre, speeches_pre)
#
#filepath_post = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\combined_speeches\\linsey_graham_post.txt"
#speeches_post = speeches_by_congressperson_post(linsey_graham)
#print speeches_post
#remove_junk(filepath_post, speeches_post)
#
#print "\n ARLEN SPECTER \n"
#filepath_pre = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\combined_speeches\\arlen_specter_pre.txt"
#speeches_pre = speeches_by_congressperson_pre(arlen_specter)
#print speeches_pre
#remove_junk(filepath_pre, speeches_pre)
#
#filepath_post = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\combined_speeches\\arlen_specter_post.txt"
#speeches_post = speeches_by_congressperson_post(arlen_specter)
#print speeches_post
#remove_junk(filepath_post, speeches_post)
#
#
#print "\n ROBERT KERRY \n"
#filepath_pre = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\combined_speeches\\robert_kerry_pre.txt"
#speeches_pre = speeches_by_congressperson_pre(robert_kerry)
#print speeches_pre
#remove_junk(filepath_pre, speeches_pre)
#
#filepath_post = "C:\\Users\\Dhrumil\\Dropbox\\IEMS\\combined_speeches\\robert_kerry_post.txt"
#speeches_post = speeches_by_congressperson_post(robert_kerry)
#print speeches_post
#remove_junk(filepath_post, speeches_post)

