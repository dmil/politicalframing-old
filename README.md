# DEPRECATED - PLEASE SEE https://github.com/PoliticalFraming/politicalframing


Name: Political Framing
Description: A machine learning approach to studying rhetoric in the US congress.
Author: Dhrumil Mehta
Version: 0.0

Requirements: 
Python 2.7

Dependancies: 
wordnet 2.1
scikit-learn

Motivation:
In "Metaphors We Live By", George Lakoff and Mark Johnson argue that certain metaphorical structures are deeply embedded in our use of language. 
A conceptual metaphor is a domain through which we can understand an idea. For example, when we use phrases like "he shot down my argument", 
we are understanding argumentation through the metaphor of  war or battle. This project is the first in a series that aims to computataionally 
identify and parse such metaphors. I have chosen the domain of politics because large datasets of similar type of speech are avaliable and also
because I hope that the results will be valueable in better understanding political rhetoric as it effects descisionmaking and promotes political
accountability.

Overview: 
In this project, we have mined the past 15 years worth of speeches from US Senate and House of Representatives and are studying its rhetoric by 
creating a model of rhetorical framing. First, the speeches are partitioned by topic and the classifier is trained to classify a novel speech into
its appropriate speech category. Having ascertained that the program can do this with a fair amount of accuracy, we can then feed the classifier 
a frame rather than a speech. A "frame" is modeled as a "bag-of-words" that contains words that are highly associated with a particular term. 
Example frames can be found in "/data/frames". The program will put the log-likelihoods table in the "/results/" directory where they can be extracted
and viewed. We can extrapolate further infromation from these results.

Data: 
*Please note that data is not is included in the source-control, actual dataset is 2GB and growing*
10,000 speeches were mined for each of the following topics: "Afghanistan, defecit, education, foreign+policy, health+care, immigration, Iraq, marriage, social+security, welfare"
Speeches were mined from the "capitol words api" - http://capitolwords.org/api

Methodology: 
- Building a frame: 
	Frames were built using an algorithm that mines wordnet with the help of a user. The algorithm is found in framemaker.py
- Classifying: 
	A multinomial naive bayes classifier was used to train a classifier to classify a novel speech into one of the topics mentioned in the "data" section above.
	The aim in v0.0 was simplicity not optimalization; the goal was to test if the methodology has any merit. Version 2.0 will have implemented this using different 
	algorithms including simple counting as well as support vector machines and decision trees. 
	
	The classifier can classify a novel speech with approximately 65% accuracy on 7 topics (chance would be ~14% so it works pretty well)
	
	Rather than feeding it a novel speech, we then feed it a frame and can analyze the log likelihoods which are output into "/results/"
	
	code is found in "classifier.py"
	
- Validating: 
	20 fold cross-validation was used 
	code is found in "crossvalidator.py"

Results: 
	Initial results are very promising and show intuitively interesting things. They can be found in raw format or in annotated excel documents in the "/results/"
	directory.


Additional Documentation: 
	Additional documentation about this project can be found in the docstrings of each module and each function.
	Also at www.dhrumilmehta.com/nicar 
	A very preliminary version can be found at www.politicalframing.byethost10.com
	
Files for Driver/User:
	classifier.py - classification algorithms are here
	framemaker.py - frame-building utilities are here
	crossvalidator.py - does crossvalidation on a classifier

