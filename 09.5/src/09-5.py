fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fhand = open(fname)
counts = 0
allemails = dict()
for line in fhand.readlines():
    emails = line.split()
    if line.startswith("From ") :   
        allemails[emails[1]] = allemails.get(emails[1], 0) + 1
for key in allemails :
    if allemails[key] > counts :
        counts = allemails[key]
        email = key
print(email, counts)
