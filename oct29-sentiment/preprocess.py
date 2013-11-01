import os
import json
from pprint import pprint 

# wrapper for loading a .json file into an array
def jsonLoadFile(file):
	try:
		return json.loads(open(file).read())
	except:
		return False;

# parse in all json objects and path name (as tuple) from data directory
data = [(jsonLoadFile("data/%s" % f), "data/%s" % f) for f in os.listdir("data") if ".json" in f]

# if there was a failed load, print it
for i in data:
	if i[0] == False:
		print "Failed to load file %s. " % i[1]

# go through data and put it into a csv file

td = []
for f in range(0, len(data)):
	if data[f][0] != False:
		for i in data[f][0]["messages"]:
			datastr = "%s\t%s" % (i['created_at'], i['body'])
			td.append(datastr)
			print datastr

f = open('data.td', 'w')
f.write("\n".join(td).encode('utf-8','ignore'))
f.close()

print "%d entries written to ./data.td" % len(td)