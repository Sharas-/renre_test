import sys
sys.path.append('..')

import policy_filter as pf

def test_affected_policies_found_by_adverse_event_type_and_location():
    pcolumns=('DealId','Company','Peril','Location')
    policies = [
        (1,'WestCoast','Earthquake','USA'),
        (2,'WestCoast','Hailstone','Canada'),
        (3,'AsianCo','Hurricane','Philippines'),
        (4,'AsianCo','Earthquake','New Zealand'),
        (5,'GeorgiaInsurance','Hurricane','USA'),
        (6,'MidWestInc','Tornado','USA')]
    ecolumns = ('Peril', 'Location')
    adverse_events = [
        ('Hailstone', 'Canada'),
        ('Hailstone', 'USA'),
        ('Earthquake', 'Canada'),
        ('Earthquake', 'USA'),
        ('Hurricane', 'Canada'),
        ('Hurricane', 'USA')]
    (cols, affected) = pf.find_affected_policies(policies, pcolumns, adverse_events, ecolumns)
    expected = [{1,'WestCoast','Earthquake','USA'},
                {2,'WestCoast','Hailstone','Canada'},
                {5,'GeorgiaInsurance','Hurricane','USA'}]
    assert sorted(expected) == sorted([set(row) for row in affected])
