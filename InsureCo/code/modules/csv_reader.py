import csv

def read(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        cols = next(reader, None)
        if cols is None:
            return ([], [])
        return (cols, list(reader))
