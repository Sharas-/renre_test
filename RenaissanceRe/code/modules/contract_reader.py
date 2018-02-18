import json
import itertools

columns = ['Peril', 'Location']

def _read_json(jfile):
    with open(jfile) as f:
        return json.load(f)

def read(contract_file):
    """Returns a table of all adverse events and locations covered by a contract"""
    perils = {'Hailstone', 'Earthquake', 'Tornado', 'Tsunami', 'Hurricane'}
    locations = set()

    contract = _read_json(contract_file)
    for node in contract['Coverage']:
        target_list = locations if node['Attribute'] == "Location" else perils
        includes = node.get("Include")
        if includes is not None:
            target_list.update(includes)
        else:
            target_list = target_list.difference_update(node['Exclude'])
    rows = list(itertools.product(perils, locations))
    return ((columns, rows), contract['MaxAmount']) 

