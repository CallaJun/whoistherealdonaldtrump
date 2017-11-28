import json
import re 

data = json.load(open('tweets.json'))
outputFile = open('output.txt', 'w')

for item in data:
    outputFile.write(re.sub(r"http\S+", '', item["text"].encode('utf-8') + " ", flags=re.MULTILINE))

outputFile.close()