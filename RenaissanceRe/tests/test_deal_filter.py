import sys
sys.path.append('../code')
from modules import deal_filter as df

def test_affected_deals_found_by_adverse_event_type_and_location():
    deals = (['DealId','Company','Peril','Location'],
            [(1,'WestCoast','Earthquake','USA'),
            (2,'WestCoast','Hailstone','Canada'),
            (3,'AsianCo','Hurricane','Philippines'),
            (4,'AsianCo','Earthquake','New Zealand'),
            (5,'GeorgiaInsurance','Hurricane','USA'),
            (6,'MidWestInc','Tornado','USA')])
    adverse_events = (['Peril', 'Location'],
                    [('Hailstone', 'Canada'),
                    ('Hailstone', 'USA'),
                    ('Earthquake', 'Canada'),
                    ('Earthquake', 'USA'),
                    ('Hurricane', 'Canada'),
                    ('Hurricane', 'USA')])
    (cols, affected) = df.find_affected_deals(deals, adverse_events)
    expected = [{1,'WestCoast','Earthquake','USA'},
                {2,'WestCoast','Hailstone','Canada'},
                {5,'GeorgiaInsurance','Hurricane','USA'}]
    assert sorted(expected) == sorted([set(row) for row in affected])
