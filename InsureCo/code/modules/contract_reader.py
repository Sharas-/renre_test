import json
import itertools

columns = ['Peril', 'Location']

def get_covered_events(contract_file):
    """Returns a table of all adverse events and locations covered by a contract"""
    perils = {'Hailstone', 'Earthquake', 'Tornado', 'Tsunami', 'Hurricane'}
    locations = set()

    with open(contract_file) as f:
        contract = json.load(f)

    for node in contract['Coverage']:
        target_list = locations if node['Attribute'] == "Location" else perils
        includes = node.get("Include")
        if includes is not None:
            target_list.update(includes)
        else:
            target_list = target_list.difference_update(node['Exclude'])
    return (columns, list(itertools.product(perils, locations)))

