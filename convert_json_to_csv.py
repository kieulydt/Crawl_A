import json
import csv

f = open('output.json')
data = json.load(f)
f.close()

def write_csv(data, file_name):
    with open(file_name, 'w+', encoding="utf-8") as outf:
        writer = csv.DictWriter(outf, data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)

write_csv(data, 'title.csv')