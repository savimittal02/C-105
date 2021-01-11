import math
import csv

with open ("class1.csv",newline = "") as f :
    reader = csv.reader(f)
    fileData = list(reader)

data = fileData[1]
def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total+=int(x)
    mean = total/n
    print(mean)
    return mean

squarelist = []
for number in data :
    a =int(number)-mean(data)
    a = a**2
    squarelist.append(a)   

sum = 0
for i in squarelist:
    sum = sum+i

result = sum/(len(data)-1)
stdev = math.sqrt(result)

print(stdev)