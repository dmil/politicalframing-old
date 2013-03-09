"""This module allows for cross-validation"""

import random
import naivebayes
import csv

def run_cross_val(d,r,n,path):
        """runs crss validation scripts"""
	dem_part,rep_part = partition_data(d,r,n)
	dem_error,rep_error = cross_val(dem_part,rep_part,path,n,d+r)
	out = csv.writer(open("cross_val_error.csv","w"),delimiter=',',quoting=csv.QUOTE_NONE)
	out.writerows([dem_error,rep_error])


def partition_data(d,r,n):
        """partitions data into democrat and republican parts"""
	dem_part = [] #democrat partition
	rep_part = [] #republican partition
	dem_perm = range(d) 
	random.shuffle(dem_perm) #democrat permutation
	rep_perm = range(r) 
	random.shuffle(rep_perm) #republican permutation
	dem_size = d/n #size per partition
	rep_size = r/n #size per partition

	i = 0
	j = 0
	count = 0
	for x in range(0,n):
		if count < d%n:
			dem_part.append(dem_perm[i:i+dem_size+1])
			i = i+dem_size+1
		elif x == n-1:
			dem_part.append(dem_perm[i:d])
		else:
			dem_part.append(dem_perm[i:i+dem_size])
			i = i+dem_size
		if count < r%n:
			rep_part.append(rep_perm[i:i+rep_size+1])
			j = j+rep_size+1
		elif x == n-1:
			rep_part.append(rep_perm[j:r])
		else:
			rep_part.append(rep_perm[j:j+rep_size])
			j = j+rep_size
		count = count + 1

	return dem_part,rep_part


# n = number of folds
# dem_part = democrat partition
# rep_part = republican partition
# topic path, self explanatory
# N = total number of documents
def cross_val(dem_part,rep_part,topic_path,n,N):
	"""conduct crossval on individual parts"""
	dem_error = []
	rep_error = []

	dem_count = 0

	for x in range(0,n):
		#for each fold
		dem_dict = {}
		rep_dict = {}
		ndict={}
		dem_dict_count = 0
		rep_dict_count = 0

		#build dictionary!
		for b in range(0,n):
			if b != x:
				for y in dem_part[b]:
					dem_dict,ndict = addfile2dict(open(topic_path+'/D/'+str(y)+'.txt'),dem_dict,ndict)
				for z in rep_part[b]:
					rep_dict,ndict = addfile2dict(open(topic_path+'/R/'+str(z)+'.txt'),rep_dict,ndict)

		dem_dict = tfidf(dem_dict,ndict,N)
		rep_dict = tfidf(rep_dict,ndict,N)
		d_err_ct = 0;
		r_err_ct = 0;
		#classify that shizz!
		for w in dem_part[x]:
			if classify_crossval(open(topic_path+'/D/'+str(w)+'.txt'),dem_dict,rep_dict) != 1:
				d_err_ct = d_err_ct + 1
		for e in rep_part[x]:
			if classify_crossval(open(topic_path+'/R/'+str(e)+'.txt').read().split()) != 0:
				r_err_ct = r_err_ct + 1

		dem_error.append(d_err_ct/len(dem_part[x]))
		rep_error.append(r_err_ct/len(rep_part[x]))

	return dem_error,rep_error

def test_file_shizz(topic_path):
        """Cross validate and test a file."""
	L = [[1,2,3],[4,5,6]]
	print(open(topic_path+'/D/'+str(L[1][0])+'.txt'))

#test_file_shizz('/Users/Natalie/Desktop/eecs349/Final Project/Data/abortion')



