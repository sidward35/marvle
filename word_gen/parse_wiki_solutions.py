import random
import csv
import re
pattern = re.compile("[a-z]+")

stop_words = []
with open('last_names.txt', encoding='utf-8') as ln_file:
	for line in ln_file:
		stop_words.append(line.lower()[line.index(' ')+1:line.index(' – ')])
print('last names done')
with open('first_names.csv', encoding='utf-8') as fn_file:
	spamreader = csv.reader(fn_file, delimiter=',', quotechar='"')
	for row in spamreader:
		if row[1].lower() not in stop_words:
			stop_words.append(row[1].lower())
print('first names done')

word_list = []
with open('mcu_wiki_small.txt','r', encoding='utf-8') as file:
	for line in file:
		line = line.lower().replace('the ','').replace('-','').replace('\'','').replace('.','').replace('ø','o').replace(' ','').strip()
		if '(' in line:
			line = line[:line.index('(')].strip()
		if len(line)>=4 and len(line)<=8 and pattern.fullmatch(line) is not None and line not in word_list and line not in stop_words:
			word_list.append(line)

random.shuffle(word_list)
print(word_list)