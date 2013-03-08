"""This module contians tools to classify data and frames.

Functions:
classifyFrames(frame_titles, frames)

"""

from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

def classifyFrames(frame_titles, frames):
    """Train a classifier on the 20 Newsgroups training data, feed the frames to the classifier,
    and print results to text file in the results directory.

    Arguments:
        frame_titles -- a list contaitning a string title for each frame in the "frames" arguement
        frames -- a list containing each frame (space deliniated string of words)

    Side-Effects:
        prints a file "20newsgroupsclassifier.txt" to the /results directory
        
    """
    #training_set = load_files('newsgroups',shuffle=True)
    from sklearn.datasets import fetch_20newsgroups
    training_set = fetch_20newsgroups(subset='train')

    #Learn the vocabulary of the dictionary and return a count vector
    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(training_set.data)

    #use tf/idf to give low weight to very common words in training data
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

    #train multinomial naive bayes classifier on 20newsgroups data
    clf = MultinomialNB(alpha=1.0,fit_prior=False).fit(X_train_tfidf,training_set.target)

    #vectorize and weight words in the frames
    X_new_counts = count_vect.transform(frames)
    X_new_tfidf = tfidf_transformer.transform(X_new_counts)
    predicted_logs = clf.predict_log_proba(X_new_tfidf)

    #write output
    f = open('20newsgroupsclassifier.txt','w')
    f.write('Frame Names and Order:\n'+str(frame_order)+'\n\n')
    f.write('Frames:\n'+str(frames)+'\n\n')
    f.write('Training Set:\n'+str(training_set.target_names)+'\n\n')
    f.write('Log-Likelihoods:\n'+str(predicted_logs)+'\n\n')
    f.close()



#for testing
#frames = ['indefensible attack attacked weak demolish demolished shoot strategy wipe shot defend defended losing lose lost won win obliterate destroy ally allied beseige overpower','give budget worth borrow borrowed use loss lost save saved wasting waste wasted','emotion affair love warmheartedness yearn dearest lovingness deepest beloved idol loving fond agape like attached tenderness adore lover feeling sexual romance passion warmhearted fondness enamored idolize affection caring tend loving lovingness care','alluring arousing exquisiteness features stunner young charisma attractive beauteous pleasing pleases sweetheart beaut pleasingness radiant appearance allure glamor graceful enticing stimulates sexappeal delicate handsomeness prettiness looker pleasure''malicious reprehensible conquest unfair reprehensibility wickedness annoyance black murderousness deliberately wicked cruel murder disrespectful immorality weakness nefariousness malefic cruelty deviltry profanation viciousness evil harmful corruption spiteful blasphemous villainous','crazy softheaded madness lunatic dementedness screwball loony demented weirdo mad nutcase half-baked craze unhinged looney craziness brainsick disturbed gaga dotty sick wild unbalanced insane madness insanity mad harebrained insaneness','emotion force joyousness joyous lively happiness proudly rejoice ecstatic cheerful please cheer euphoria elation overjoy exuberance gladden joyful happyrejoicing joy lighten enthusiasm extremely glad extreme delight great joyfulness excitement exhilaration victory pleasure','discontent forsaken fear self-pity unhappy mournfulness loss despondency gloomy uncheerfulness gloom dysphoria selfindulgent heavy demoralization weepiness regret weight  disheartened melancholy sorrow despair hopeless misery sorrowful unhappiness perished weeping  grief abandoned inadequacy deep sad helplessness']
#frame_order = ['war','time','love','beauty','evil','crazy','joy','sadness']


