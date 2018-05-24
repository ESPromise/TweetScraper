import json

with open("ip.json") as f:
    d = json.load(f)
    for ip in d:
        if (ip['is_available'] == True and ip['is_stable'] == True):
            print (ip['type'] + "://" + ip['ip'] + ":" + str(ip['port']))

