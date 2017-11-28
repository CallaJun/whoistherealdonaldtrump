import json
import re 

data = json.load(open('tweets.json'))
outputFile = open('output.txt', 'w')

for item in data:
	if item["is_retweet"]:
		continue
	outputFile.write(re.sub(r"http\S+", '', item["text"].encode('utf-8') + "\n", flags=re.MULTILINE))

outputFile.close()