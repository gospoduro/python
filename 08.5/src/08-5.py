fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fhand = open(fname)
count = 0
for line in fhand.readlines():
    line = line.strip()
    if not line.startswith("From ") :
        continue 
    count = count + 1
    pieces = line.split()
    email = pieces[1]
    print(email)
print("There were", count, "lines in the file with From as the first word")
