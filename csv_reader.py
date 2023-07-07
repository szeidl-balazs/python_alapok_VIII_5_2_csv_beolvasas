import csv
import sys

def read_csv(name):
    csv_list = []

    try:
        target_file = open(name)

        try:
                content = csv.reader(target_file)

                for row in content:
                    csv_list.append(row)

        finally:
            target_file.close()

    except OSError:
        sys.exit('Hibás file név!')
    
    else:
        return csv_list

print(read_csv('meetup.csv'))