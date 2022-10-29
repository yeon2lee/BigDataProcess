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
		info = (uber[0], day)
		if info not in uber_list:
			uber_list[info] = [int(uber[2]), int(uber[3])]
		else:
			uber_list[info][0] += int(uber[2])
			uber_list[info][1] += int(uber[3])

with open(outputfile, "wt") as fp:
	for uber in uber_list:
		fp.write("{},{} {},{}\n".format(uber[0], uber[1], uber_list[uber][0], uber_list[uber][1]))		
