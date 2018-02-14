def read(deals_file):
    with open(deals_file) as f:
        lines = f.read().splitlines()
    if len(lines) == 0:
        return lines
    return (lines[0].split(','), [l.split(',') for l in lines[1:]]

