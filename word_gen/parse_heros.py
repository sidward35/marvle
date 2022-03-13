import json
import random

f = open('all.json')
data = json.load(f)
f.close()

names = []
for item in data:
	name = item['name'].replace('-','').lower().replace('the ','')
	if ' ' not in name and len(name)<=8 and len(name)>=4 and not any(chr.isdigit() for chr in name) and name not in names:
		names.append(name)
random.shuffle(names)
print(names, len(names))

len_count = {}
for name in names:
	try:
		len_count[len(name)]+=1
	except:
		len_count[len(name)] = 1
marklist = sorted(len_count.items(), key=lambda x:x[1], reverse=True)
sortdict = dict(marklist)
print(sortdict)