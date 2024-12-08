import json

purchases = {}

with open('/Users/maxxxxxxu/Downloads/purchase_log.txt') as content:
    for line in content:
        temp = json.loads(line)    
        purchases[temp['user_id']] = temp['category']

print(purchases)