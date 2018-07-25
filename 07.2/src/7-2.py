# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fhand = open(fname)
count = 0
fnums = 0.0
average = 0.0
for line in fhand.readlines():
    line = line.strip()
    if not line.startswith("X-DSPAM-Confidence:") :
        continue 
    count = count + 1
    numpos = line.find('0')
    num = line[numpos:].rstrip()
    fnum = float(num)
    fnums = fnums + fnum
average = fnums / count
print("Average spam confidence:", average)
