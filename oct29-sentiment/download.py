import json
import requests
from pprint import pprint

def getData(symbol, max_msgid = 0, depth = 0, max_depth = 10):

	if max_msgid == 0:
		req = requests.get("https://api.stocktwits.com/api/2/streams/symbol/%s.json" % (symbol))
	else:
		req = requests.get("https://api.stocktwits.com/api/2/streams/symbol/%s.json?max=%d" % (symbol, max_msgid))
	
	if req.status_code != 200 or depth > max_depth:
		print "Quitting with status code %d and depth %d (of %d)" % (req.status_code, depth, max_depth)
		return True

	d = json.loads(req.text)

	f = open("stocktwits-%s_%d-%d.json" % (symbol, int(d['cursor']['since']), int(d['cursor']['max'])), 'w')
	f.write(req.text.encode('utf-8','ignore'))
	f.close()

	pprint(d['cursor'])

	# recursive call to download more data
	return getData(symbol, max_msgid=int(d['cursor']['since']), depth=(depth+1), max_depth=max_depth)

getData('AAPL', max_depth=500)