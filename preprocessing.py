import argparse
import csv
import os
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='name of csv file for cleaning', 
    required=True)
parser.add_argument('-y', '--year', help='year or comma separated years to \
    include in output. Will include all years in output  if left blank')
args = parser.parse_args()

def get_years(years_string):
    """
    Takes a string of a single year, comma separated years or hyphen 
    separated ranges, and returns them as a list of strings.
    """
    split_string = years_string.split(',')
    result = [x for x in split_string if '-' not in x]
    years_range = [x for x in split_string if '-' in x]
    if years_range:
        for x in years_range:
            years = [int(y) for y in x.split('-')]
            expanded_years = list(range(years[0], years[1] + 1))
            for y in expanded_years:
                if y not in result:
                    result.append(str(y))
    return result

def yield_rows(csv_file):
    with open(csv_file, 'r') as f:
        data = csv.reader(f)
        for row in data:
            yield row

fn = os.path.splitext(args.file)[0]
if args.year:
    clean_fn = fn + '_clean_' + args.year + '.csv'
    dirty_fn = fn + '_dirty_' + args.year + '.csv'
else:
    clean_fn = fn + '_clean.csv'
    dirty_fn = fn + '_dirty.csv'

with open(clean_fn, 'w') as clean_output:
    with open(dirty_fn, 'w') as dirty_output:
        clean_writer = csv.writer(clean_output)
        dirty_writer = csv.writer(dirty_output)

        if args.year:
            year_filter = get_years(args.year)

        for index, row in enumerate(yield_rows(args.file)):
            if index == 0:
                row.append('Count')

                clean_writer.writerow(row)
                dirty_writer.writerow(row)
            else:
                if year_filter:
                    if row[5] not in year_filter:
                        continue

                # Date formatting
                row_date = ' '.join([row[3],row[4],row[5]])
                row[2] = datetime.strptime(row_date, '%d %B %Y').strftime('%d.%m.%Y')

                # Hour rounding
                if int(row[9]) > 30:
                    row[8] = str(int(row[8]) + 1)

                # appending data for count dimension
                row.append('1')

                if '-9' not in row:
                    clean_writer.writerow(row)
                else:
                   dirty_writer.writerow(row)
