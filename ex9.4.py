emails = list()
counts = dict()
name = input("Enter file name: ")
handle = open(name)
for line in handle:
    if line.startswith("From"):
        if line.startswith("From:"): continue
        line = line.rstrip()
        line = line.split()
        emails.append(line[1])
#print(emails)
for email in emails:
    counts[email] = counts.get(email, 0) + 1
#print(counts)
bigcount = None
bigword = None
for person,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = person
        bigcount = count
print(bigword, bigcount)
