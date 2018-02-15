import csv

def read(deals_file):
    with open(deals_file, 'r') as f:
        reader = csv.reader(f)
        cols = next(reader, None)
        if cols is None:
            return ([], [])
        return (cols, list(reader))
