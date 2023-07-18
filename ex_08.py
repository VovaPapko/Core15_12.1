import csv

with open("data.csv", "w", newline="") as f:
    fields = ["name", "age", "phones"]
    writer = csv.writer(f)
    writer.writerow(fields)
    writer.writerow(["Garry", "33", "34562728;628494"])
    writer.writerow(["Marry", "23", "67837229;648959"])


with open("data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)