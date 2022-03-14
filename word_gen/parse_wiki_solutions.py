import random
import csv
import re
pattern = re.compile("[a-z]+")

word_list = []
with open('mcu_wiki_small.txt','r', encoding='utf-8') as file:
	for line in file:
		line = line.lower().replace('the ','').replace('-','').replace('\'','').replace('.','').replace('ø','o').replace(' ','').strip()
		if '(' in line:
			line = line[:line.index('(')].strip()
		if len(line)>=4 and len(line)<=8 and pattern.fullmatch(line) is not None and line not in word_list:
			word_list.append(line)

random.shuffle(word_list)
print(word_list)