fname = input("Enter file name: ")
fh = open(fname)
all = list()
for line in fh:
    line = line.rstrip()
    linesplit = line.split()
    #print(linesplit)
    for w in linesplit:
        if w not in all:
            all.append(w)
print(sorted(all))
