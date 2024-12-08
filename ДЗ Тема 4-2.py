import json

purchases = {}

with open(file='/Users/maxxxxxxu/Downloads/purchase_log.txt', mode='r', encoding='utf-8') as purchase_log:
    for line in purchase_log:
        temp = json.loads(line)
        purchases[temp['user_id']] = temp['category']

with open(file='/Users/maxxxxxxu/Downloads/funnel.csv', mode='w', encoding='utf-8') as funnel:
    funnel.write("user_id,source,category\n")
    with open(file='/Users/maxxxxxxu/Downloads/visit_log.csv', mode='r', encoding='utf-8') as visit_log:
        visit_log.readline()
        for line2 in visit_log:
            data = line2.strip().split(',')
            
            if purchases.get(data[0]) != None:
                funnel.write(f"{data[0]},{data[1]},{purchases[data[0]]}\n")