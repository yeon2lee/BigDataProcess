#/user/bin/python3

import sys
import datetime

inputfile = sys.argv[1]
outputfile = sys.argv[2]

uber_list = []
days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
with open(inputfile, "rt") as fp:
	for line in fp:
		uber = line.strip().split(",")
		day = uber[1].split("/")
		day = days[datetime.date(int(day[2]), int(day[0]), int(day[1])).weekday()]
		uber_list.append([uber[0], day, uber[2], uber[3]])
	
with open(outputfile, "wt") as fp:
	for uber in uber_list:
		fp.write("{},{}\t{},{}\n".format(uber[0], uber[1], uber[2], uber[3]))
		
