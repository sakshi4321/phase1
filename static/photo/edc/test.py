import csv

with open('7_6_2021_19:15.xls', "r") as f:
    reader = csv.DictReader(f)
    headers = reader.fieldnames
    table = []
    for row in reader:
        table.append([row[h] for h in headers])
   

from tabulate import tabulate

            










table = []
for f in files:
    table.append(["<a href='%s'>%s</a>" % (datasets[f], f)])
t = tabulate(table, tablefmt="html")
with open("index.html", "w") as f:
    f.write(t)
