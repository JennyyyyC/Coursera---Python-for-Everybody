count = 0
fname = input("Enter file name: ")
fh = open(fname, 'r')
for line in fh:
    if line.startswith("From"):
        if line.startswith("From:"): continue
        line = line.rstrip()
        line = line.split()
        #print(line)
        print(line[1])
        count = count + 1
print("There were", count, "lines in the file with From as the first word")
