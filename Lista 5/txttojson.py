import json

file = open("N5000step10.txt").readlines()


values = []
ns = []
for line in file:
    line = line.replace("\n", "")
    data_pair = line.split(" ")
    values.append(float(data_pair[0]) / 10)
    ns.append(int(data_pair[1]))

json.dump((values,ns),open("n5000step10.json", 'w'))