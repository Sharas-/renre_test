import sys
sys.path.append('../code')
from modules import contract_reader

def test_contract_reader_returns_product_of_all_covered_locations_and_events():
    fname = 'tmpcontract.json'
    with open(fname, 'w') as f:
        f.write("""{
                  "Coverage": [
                    {
                      "Attribute": "Location",
                      "Include": [
                        "USA", "Canada"
                      ]
                    },
                    {
                      "Attribute": "Peril",
                      "Exclude": [
                        "Tornado"
                      ]
                    }
                  ],
                  "MaxAmount": 3000
                }""")
    cols, rows = contract_reader.get_covered_events(fname)
    assert sorted(rows) == sorted([('Tsunami', 'USA'),
                                ('Tsunami', 'Canada'),
                                ('Hailstone', 'USA'),
                                ('Hailstone', 'Canada'),
                                ('Earthquake', 'USA'),
                                ('Earthquake', 'Canada'),
                                ('Hurricane', 'USA'),
                                ('Hurricane', 'Canada')])
