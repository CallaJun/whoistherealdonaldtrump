import json
data = json.load(open('nov1to5.json'))
outputFile = open('output.txt', 'w')

for item in data:
    outputFile.write(item["text"].encode('utf-8') + " ")

outputFile.close()