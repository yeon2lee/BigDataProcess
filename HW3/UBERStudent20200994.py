#/user/bin/python3

import sys
import calendar

inputfile = sys.argv[1]
outputfile = sys.argv[2]

uber_dict = dict()
days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
with open(inputfile, "rt") as fp:
	for line in fp:
		uber = line.strip().split(",")
		day = uber[1].split("/")
		day = days[calendar.weekday(int(day[2]), int(day[0]), int(day[1]))]

		info = (uber[0], day)
		if info not in uber_dict:
			uber_dict[info] = [int(uber[2]), int(uber[3])]
		else:
			uber_dict[info][0] += int(uber[2])
			uber_dict[info][1] += int(uber[3])

with open(outputfile, "wt") as fp:
	for uber in uber_dict:
		fp.write("{},{} {},{}\n".format(uber[0], uber[1], uber_dict[uber][0], uber_dict[uber][1]))		
