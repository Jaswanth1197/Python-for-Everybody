import re
fname = input('Enter the file name: ')
file = open(fname)
lst = list()

for lines in file:
    lines = lines.rstrip()
    numbers = re.findall('[0-9]+', lines)
    for item in numbers:
        lst.append(float(item))

print(sum(lst))
    


    
