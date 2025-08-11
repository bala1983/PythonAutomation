import csv

with open('random.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    rows1 = list(reader)

with open('random-michaels.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    rows2 = list(reader)

all_rows = rows1 + rows2

unique_rows = list(set(tuple(row) for row in all_rows))

with open('result.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(unique_rows)