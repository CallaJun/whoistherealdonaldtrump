import json
data = json.load(open('nov1to5.json'))
for item in data:
    print item["text"]