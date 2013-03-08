from nltk.corpus import wordnet
from sets import Set

import wordnettools
import testinggod
import pickle

frameword = ''

def pickleframe(word):
    fname = word + '.txt'
    f = open(fname, 'w')
    pickle.dump(makeframe(word),f)
    f.close()

def picklemultiframe(framewords,word):
    fname = '1' + word + '.txt'
    f = open(fname, 'w')
    pickle.dump(multimakeframe(framewords,word),f)
    f.close()

def addset2pickledframe(frame, myset):
    fname = frame + '.txt'
    newset = pickle.load(frame).union(myset)
    f = open(fname, 'w')
    pickle.dump(newset,f)
    f.close()
    return newset

def load(word):
    fname = word + '.txt'
    f = open(fname, 'r')
    p = pickle.load(f)
    f.close()
    return p

def makeframe(frameword):
    framesynsets = wordnet.synsets(frameword)
    #### which definitions would you like to include in your frame?
    includedwords = []
    extension = []
    parsedsynsets = Set()
    for synset in framesynsets:
        if not (synset in parsedsynsets):
            parsedsynsets.add(synset)
            print '\does this fit the frame?: ' + str(frameword)
            print str(synset) + '   ' + synset.definition
            print synset.examples

            for rsynset in wordnettools.getrelatedforms(synset):
                if not(rsynset in parsedsynsets):
                    print '\t' + str(rsynset) + '   ' + rsynset.definition
                    print '\t' + str(rsynset.examples)            

            want = True
            correctinput = False
            while correctinput == False:
                userin = raw_input('y or n: ')
                if userin == 'y':
                    want = True
                    correctinput = True
                    # Related term check
                    print '\nrelated forms\n'
                    for rsynset in wordnettools.getrelatedforms(synset):
                        if not(rsynset in parsedsynsets):
                            parsedsynsets.add(rsynset)
                            #print '\t' + str(rsynset) + '   ' + rsynset.definition
                            #print '\t' + str(rsynset.examples)

                            want2 = True
                            correctinput2 = False
                            while correctinput2 == False:
                                userin = 'y'
                                if userin == 'y':
                                    want2 = True
                                    correctinput2 = True
                                elif userin == 'n':
                                    want2 = False
                                    correctinput2 = True
                                else:
                                    print '\tError - only y or n are allowed'
                                    
                            if want2:
                                includedwords = includedwords + wordnettools.getallthingspretty(rsynset)
                                extension = extension + testinggod.frameextension(rsynset)
                        
                elif userin == 'n':
                    want = False
                    correctinput = True
                else:
                    print 'Error - only y or n are allowed'
        
            if want:
                includedwords = includedwords + wordnettools.getallthingspretty(synset)
                extension = extension + testinggod.frameextension(synset)

    return set(includedwords)


