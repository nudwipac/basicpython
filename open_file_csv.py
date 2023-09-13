import csv

with open("filedata/sample.csv", "r") as file:
    # Read with header
    # csv_reader = csv.reader(file)
    # Read without header
    csv_reader = csv.DictReader(file, delimiter=",")
    for row in csv_reader:
        # print(row)
        print(row['year'], row['amount'])
