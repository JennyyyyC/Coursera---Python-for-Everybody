hr = list()
counts = dict()
name = input("Enter file: ")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    if not line.startswith('From '): continue
    line = line.rstrip()
    #print(line)
    words = line.split()
    hr.append(words[5].split(":")[0])
for count in hr:
    counts[count] = counts.get(count, 0) + 1
#print(counts)
hrsort = list()
for k, v in counts.items():
    hrsort.append((k, v))
hrsort = sorted(hrsort)
for v, k in hrsort:
    print(v, k)

#for k, v in counts.items():
    #newtuple = (v, k)
    #print(newtuple)
    #timelist.append(newtuple)
#timelist = sorted(timelist, reverse=True)
#for v, k in timelist:
    #print(k, v)
