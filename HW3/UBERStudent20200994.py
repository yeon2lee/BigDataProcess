#/user/bin/python3

import sys
import datetime

inputfile = sys.argv[1]
outputfile = sys.argv[2]

uber_list = dict()
days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
with open(inputfile, "rt") as fp:
	for line in fp:
		uber = line.strip().split(",")
		day = uber[1].split("/")
		day = days[datetime.date(int(day[2]), int(day[0]), int(day[1])).weekday()]
		if uber[0] not in uber_list:
			uber_list[uber[0]] = {}

		if day not in uber[0]:
			uber_list[uber[0]][day] = [uber[2], uber[3]]
		else:		
			uber_list[uber[0]][day][0] += uber[2]
			uber_list[uber[0]][dat][1] += uber[3] 
	
with open(outputfile, "wt") as fp:
	for uber in uber_list:
		for day in uber_list[uber]:
			fp.write("{},{}\t{},{}\n".format(uber, day, uber_list[uber][day][0], uber_list[uber][day][1]))
		
