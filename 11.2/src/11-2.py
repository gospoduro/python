# Sample data: regex_sum_42.txt (There are 90 values with a sum=445833)
# Actual data: regex_sum_115636.txt (There are 102 values and the sum ends with 411)

import re

fname = input("Enter file name: ")
fhand = open(fname)
sumnums = 0
for line in fhand.readlines():
    nums = re.findall('[0-9]+',line)
    if not nums :
        continue
    else:
        for num in nums:
            sumnums += int(num)
print(sumnums)
