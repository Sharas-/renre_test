def deal_reader_returns_columns_and_all_lines():
    with open(deals.py, 'w') as f:
        f.writelines(
            ["DealId,Company,Peril,Location",
            "1,WestCoast,Earthquake,USA",
            "2,WestCoast,Hailstone,Canada",
            "3,AsianCo,Hurricane,Philippines",
            "4,AsianCo,Earthquake,New Zealand",
            "5,GeorgiaInsurance,Hurricane,USA",
            "6,MidWestInc,Tornado,USA"],

