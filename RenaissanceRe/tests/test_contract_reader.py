import sys
sys.path.append('../code')
from modules import contract_reader

def test_contract_reader_returns_max_ammount_and_covered_events_table():
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
    (cols, rows), max_amount = contract_reader.read(fname)
    assert max_amount == 3000
    assert sorted(rows) == sorted([('Tsunami', 'USA'),
                                ('Tsunami', 'Canada'),
                                ('Hailstone', 'USA'),
                                ('Hailstone', 'Canada'),
                                ('Earthquake', 'USA'),
                                ('Earthquake', 'Canada'),
                                ('Hurricane', 'USA'),
                                ('Hurricane', 'Canada')])
