#/user/bin/python3

import sys

inputfile = sys.argv[1] 
outputfile = sys.argv[2]

count_genre = dict()
with open(inputfile, "rt") as fp:
	for line in fp:
		movie = line.split("::")
		genre_list = movie[2].strip().split("|")
		for genre in genre_list:
			if genre not in count_genre:
				count_genre[genre] = 1
			else:
				count_genre[genre] += 1

with open(outputfile, "wt") as fp:
	for genre in count_genre:
		fp.write("{} {}\n".format(genre, count_genre[genre]))
