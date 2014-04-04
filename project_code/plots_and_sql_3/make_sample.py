import random
import csv

with open('data_ejam.csv', 'r') as in_file:
    with open('data_ejam.sample.csv', 'w') as out_file:
        r = csv.reader(in_file)
        in_lines = list(r)

        sample_lines = random.sample(in_lines, 10000)

        w = csv.writer(out_file)
        w.writerows(sample_lines)
