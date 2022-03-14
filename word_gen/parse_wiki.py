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
with open('locations.csv', encoding='utf-8') as loc_file:
	spamreader = csv.reader(loc_file, delimiter=',', quotechar='"')
	for row in spamreader:
		if row[1].lower() not in stop_words:
			stop_words.append(row[1].lower())
		if row[4].lower() not in stop_words:
			stop_words.append(row[4].lower())
		if row[7].lower() not in stop_words:
			stop_words.append(row[7].lower())
print('locations done')

valid_guesses = ['abomb', 'abraxas', 'ajax', 'alien', 'amazo', 'angel', 'antman', 'aquababy', 'aqualad', 'aquaman', 'arachne', 'arclight', 'ardina', 'ares', 'ariel', 'armor', 'atlas', 'aurora', 'azazel', 'azrael', 'bane', 'banshee', 'bantam', 'batgirl', 'batman', 'beast', 'beyonder', 'bishop', 'bizarro', 'blackout', 'blade', 'bling!', 'blink', 'blob', 'bloodaxe', 'boomboom', 'brainiac', 'buffy', 'bullseye', 'bushido', 'cable', 'callisto', 'carnage', 'catwoman', 'century', 'chamber', 'cheetah', 'cloak', 'colossus', 'copycat', 'crystal', 'cyborg', 'cyclops', 'dagger', 'darkhawk', 'darkman', 'darkseid', 'darkstar', 'dash', 'data', 'dazzler', 'deadman', 'deadpool', 'deadshot', 'deathlok', 'domino', 'doomsday', 'dormammu', 'electro', 'elektra', 'etrigan', 'evilhawk', 'exodus', 'falcon', 'faora', 'feral', 'firebird', 'firelord', 'firestar', 'flash', 'forge', 'frenzy', 'frozone', 'galactus', 'gambit', 'gamora', 'giganta', 'godzilla', 'goku', 'gravity', 'greedo', 'groot', 'hancock', 'havok', 'hawk', 'hawkeye', 'hawkgirl', 'hela', 'hellboy', 'hellcat', 'hercules', 'hitgirl', 'hulk', 'huntress', 'husk', 'hybrid', 'hydroman', 'hyperion', 'iceman', 'impulse', 'indigo', 'isis', 'jackjack', 'joker', 'jolt', 'jubilee', 'junkpile', 'justice', 'kang', 'kickass', 'kilowog', 'kingpin', 'klaw', 'krypto', 'leader', 'leech', 'legion', 'leonardo', 'lizard', 'lobo', 'loki', 'longshot', 'luna', 'machiv', 'magneto', 'magog', 'magus', 'manbat', 'manthing', 'manwolf', 'mandarin', 'mantis', 'match', 'maverick', 'maxima', 'medusa', 'meltdown', 'mephisto', 'mera', 'metallo', 'metron', 'mimic', 'misfit', 'modok', 'morlun', 'mysterio', 'mystique', 'namor', 'namora', 'namorita', 'nebula', 'nova', 'odin', 'oracle', 'osiris', 'penguin', 'phoenix', 'plantman', 'polaris', 'predator', 'psylocke', 'punisher', 'pyro', 'question', 'quill', 'rambo', 'raphael', 'raven', 'rhino', 'riddler', 'robin', 'rogue', 'ronin', 'sage', 'sandman', 'sauron', 'scorpia', 'scorpion', 'sentry', 'shangchi', 'shehulk', 'shething', 'shocker', 'shriek', 'silk', 'sinestro', 'siren', 'siryn', 'skaar', 'snowbird', 'sobek', 'songbird', 'spawn', 'spectre', 'speedy', 'spock', 'spyke', 'starlord', 'stardust', 'starfire', 'stargirl', 'static', 'steel', 'storm', 'sunspot', 'superboy', 'superman', 'swarm', 'sylar', 'synch', 'syndrome', 'tempest', 'thanos', 'cape', 'comedian', 'thing', 'thor', 'thundra', 'tigra', 'tinkerer', 'toad', 'toxin', 'triton', 'twoface', 'ultron', 'vanisher', 'vegeta', 'venom', 'vibe', 'vision', 'vixen', 'vulture', 'walrus', 'warlock', 'warp', 'warpath', 'wasp', 'watcher', 'wildfire', 'wordgirl', 'xman', 'ymir', 'yoda', 'zatanna', 'zoom']
word_list = ['abomb', 'abraxas', 'ajax', 'alien', 'amazo', 'angel', 'antman', 'aquababy', 'aqualad', 'aquaman', 'arachne', 'arclight', 'ardina', 'ares', 'ariel', 'armor', 'atlas', 'aurora', 'azazel', 'azrael', 'bane', 'banshee', 'bantam', 'batgirl', 'batman', 'beast', 'beyonder', 'bishop', 'bizarro', 'blackout', 'blade', 'bling!', 'blink', 'blob', 'bloodaxe', 'boomboom', 'brainiac', 'buffy', 'bullseye', 'bushido', 'cable', 'callisto', 'carnage', 'catwoman', 'century', 'chamber', 'cheetah', 'cloak', 'colossus', 'copycat', 'crystal', 'cyborg', 'cyclops', 'dagger', 'darkhawk', 'darkman', 'darkseid', 'darkstar', 'dash', 'data', 'dazzler', 'deadman', 'deadpool', 'deadshot', 'deathlok', 'domino', 'doomsday', 'dormammu', 'electro', 'elektra', 'etrigan', 'evilhawk', 'exodus', 'falcon', 'faora', 'feral', 'firebird', 'firelord', 'firestar', 'flash', 'forge', 'frenzy', 'frozone', 'galactus', 'gambit', 'gamora', 'giganta', 'godzilla', 'goku', 'gravity', 'greedo', 'groot', 'hancock', 'havok', 'hawk', 'hawkeye', 'hawkgirl', 'hela', 'hellboy', 'hellcat', 'hercules', 'hitgirl', 'hulk', 'huntress', 'husk', 'hybrid', 'hydroman', 'hyperion', 'iceman', 'impulse', 'indigo', 'isis', 'jackjack', 'joker', 'jolt', 'jubilee', 'junkpile', 'justice', 'kang', 'kickass', 'kilowog', 'kingpin', 'klaw', 'krypto', 'leader', 'leech', 'legion', 'leonardo', 'lizard', 'lobo', 'loki', 'longshot', 'luna', 'machiv', 'magneto', 'magog', 'magus', 'manbat', 'manthing', 'manwolf', 'mandarin', 'mantis', 'match', 'maverick', 'maxima', 'medusa', 'meltdown', 'mephisto', 'mera', 'metallo', 'metron', 'mimic', 'misfit', 'modok', 'morlun', 'mysterio', 'mystique', 'namor', 'namora', 'namorita', 'nebula', 'nova', 'odin', 'oracle', 'osiris', 'penguin', 'phoenix', 'plantman', 'polaris', 'predator', 'psylocke', 'punisher', 'pyro', 'question', 'quill', 'rambo', 'raphael', 'raven', 'rhino', 'riddler', 'robin', 'rogue', 'ronin', 'sage', 'sandman', 'sauron', 'scorpia', 'scorpion', 'sentry', 'shangchi', 'shehulk', 'shething', 'shocker', 'shriek', 'silk', 'sinestro', 'siren', 'siryn', 'skaar', 'snowbird', 'sobek', 'songbird', 'spawn', 'spectre', 'speedy', 'spock', 'spyke', 'starlord', 'stardust', 'starfire', 'stargirl', 'static', 'steel', 'storm', 'sunspot', 'superboy', 'superman', 'swarm', 'sylar', 'synch', 'syndrome', 'tempest', 'thanos', 'cape', 'comedian', 'thing', 'thor', 'thundra', 'tigra', 'tinkerer', 'toad', 'toxin', 'triton', 'twoface', 'ultron', 'vanisher', 'vegeta', 'venom', 'vibe', 'vision', 'vixen', 'vulture', 'walrus', 'warlock', 'warp', 'warpath', 'wasp', 'watcher', 'wildfire', 'wordgirl', 'xman', 'ymir', 'yoda', 'zatanna', 'zoom']
with open('mcu_wiki.txt','r', encoding='utf-8') as file:
	for line in file:
		line = line.lower().replace('the ','').replace('-','').replace('\'','').replace('.','').replace('ø','o').strip()
		if '(' in line:
			line = line[:line.index('(')].strip()
		if len(line)>=4 and len(line)<=8 and pattern.fullmatch(line) is not None and line not in valid_guesses:
			valid_guesses.append(line)
			if line not in stop_words:
				word_list.append(line)

print(valid_guesses)
random.shuffle(word_list)
print(word_list)