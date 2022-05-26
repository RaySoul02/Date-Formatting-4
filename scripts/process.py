import csv
from datetime import datetime

r = csv.reader(open("source.csv","r"), delimiter =",")
header = next(r)
header1 = ['date', 'region', 'value']
with open('result.csv', 'w') as result:
    writer = csv.writer(result, lineterminator='\n')
    writer.writerow(header1)
    for row in r:
        row[0] = datetime.strptime(row[0] + '-' + row[1],'%Y-%b').strftime("%Y-%m-%d")
        writer.writerow([row[0],row[2],row[3]])