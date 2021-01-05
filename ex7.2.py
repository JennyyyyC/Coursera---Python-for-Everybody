count = 0
tot = 0
fname = input("Enter file name: ")
fh = open(fname, 'r')
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        line = line.rstrip()
        #print(line)
        count = count + 1
        pos = line.find(":")
        tot = float(line[pos+2:]) + tot
#print("count is:", count)
#print("sum is:", tot)
print("Average spam confidence:", tot/count)
