import sys
sys.path.append('../code')
from modules import loss_calculator

def test_loss_calculator_aggregates_losses_by_event_type_and_caps_losses_to_max_amount():
    events = (['EventId','DealId','Loss'],
                [(1,1,2000),
                (2,1,1500),
                (3,5,4000),
                (4,6,1000)])
    deals = (['DealId','Company','Peril','Location'],
            [(1,'WestCoast','Earthquake','USA'),
            (2,'WestCoast','Hailstone','Canada'),
            (3,'AsianCo','Hurricane','Philippines'),
            (4,'AsianCo','Earthquake','New Zealand'),
            (5,'GeorgiaInsurance','Hurricane','USA'),
            (6,'MidWestInc','Tornado','USA')])
    max_amount = 3000
    cols, losses = loss_calculator.get_by_peril(deals, events, max_amount)
    assert sorted(losses) == sorted([['Hurricane', 3000],
                                     ['Earthquake', 3500],
                                     ['Tornado', 1000]])
