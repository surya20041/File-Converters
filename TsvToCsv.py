import csv
import re

with open("C:/Users/surya/Downloads/corpus_documents.tsv", 'r') as inp, open("C:/Users/surya/Downloads/Output .csv", 'w', newline='') as out:
    tsv_reader = csv.reader(inp, delimiter='\t')
    csv_writer = csv.writer(out, delimiter=',')
    for row in tsv_reader:
        csv_writer.writerow([re.sub("\t", ",", x) for x in row])