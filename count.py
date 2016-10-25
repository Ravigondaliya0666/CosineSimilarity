#!/usr/bin/python
import collections
import math
import sys

#Find the dot product between two vectors
def dot_pro(word1, word2) :
	dot_product = 0

	for name1, count1 in word1.iteritems():
		for name2, count2 in word2.iteritems():
			if name1 == name2:
				dot_product += count1*count2
				break

	return  dot_product

#Find the vector length 
def vector_length(word) :
	sum_of_square = 0

	for name, count in word.iteritems():
		sum_of_square += count*count

	return  math.sqrt( sum_of_square )

#main function
def main():
	wordcount1 = collections.Counter()
	wordcount2 = collections.Counter()

#Open and read document 1
	with open("doc1.txt") as f1:
	    for line1 in f1:
	        wordcount1.update(line1.split())

#Open and read document 2
	with open("doc2.txt") as f2:
	    for line2 in f2:
	        wordcount2.update(line2.split())

	for name1,count1 in wordcount1.iteritems():
	    print name1,count1
	print "***********************"

	for name2,count2 in wordcount2.iteritems():
	    print name2,count2
	print "***********************"

	dot_product = dot_pro(wordcount1, wordcount2)
	cosine_similarity = (dot_product)/(vector_length(wordcount1)*vector_length(wordcount2))
	print cosine_similarity

#Calling the main function
if __name__ == "__main__":
    main()
