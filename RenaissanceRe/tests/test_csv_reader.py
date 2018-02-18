import sys
import csv
sys.path.append('../code')
from modules import csv_reader as dr

def test_csv_reader_returns_columns_and_all_lines():
    fname = 'tmpdeals.csv'
    with open(fname, 'w') as f:
        writer = csv.writer(f)
        writer.writerows([["DealId","Company","Peril","Location"],
                        ["1","WestCoast","Earthquake","USA"],      
                        ["2","WestCoast","Hailstone","Canada"],
                        ["3","AsianCo","Hurricane","Philippines"],
                        ["4","AsianCo","Earthquake","New Zealand"],
                        ["5","GeorgiaInsurance","Hurricane","USA"],
                        ["6","MidWestInc","Tornado","USA"]])        
    cols, rows = dr.read(fname)
    assert cols == ["DealId","Company","Peril","Location"]
    assert rows == [[1,"WestCoast","Earthquake","USA"],
                    [2,"WestCoast","Hailstone","Canada"],
                    [3,"AsianCo","Hurricane","Philippines"],
                    [4,"AsianCo","Earthquake","New Zealand"],
                    [5,"GeorgiaInsurance","Hurricane","USA"],
                    [6,"MidWestInc","Tornado","USA"]]
