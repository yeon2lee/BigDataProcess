import sys
import calendar

inputfile = sys.argv[1]
outputfile = sys.argv[2]

uber_dict = dict()
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
with open(inputfile, "rt") as fp:
    for line in fp:
        uber = line.split(",")
        day_list = uber[1].split("/")
        tmp = calendar.weekday(int(day_list[2]), int(day_list[0]), int(day_list[1]))
        day = days[tmp]		
        key = (uber[0], day)
        if key not in uber_dict:
            uber_dict[key] = [int(uber[2]), int(uber[3])]
        else:
            uber_dict[key][0] += int(uber[2])
            uber_dict[key][1] += int(uber[3])

keys = uber_dict.keys()
result = ""
for key in keys:
    value = uber_dict[key]
    result += key[0] + "," + key[1] + " " + str(value[0]) + "," + str(value[1]) + "\n"

with open(outputfile, "wt") as fp:
    fp.write(result)
