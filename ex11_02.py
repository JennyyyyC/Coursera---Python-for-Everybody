import re
numlist = list()
file = open('regex_sum_1122998.txt', 'r')
for line in file:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    if len(stuff) < 1: continue
    #print(stuff)
    for num in range(0, len(stuff)):
        stuff[num] = int(stuff[num])
    for i in range(0, len(stuff)):
        numlist.append(stuff[i])
#print(numlist)
print(sum(numlist))
