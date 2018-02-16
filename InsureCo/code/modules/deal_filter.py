import pandas as pd

def _normalize_columns(cols):
    return [c.upper() for c in cols]

def _filter_deals(deals_table, events_table):
    dcolumns, deals = deals_table
    ecolumns, events = events_table
    index_columns = ['PERIL', 'LOCATION']
    df_deals = pd.DataFrame(data = deals, columns = _normalize_columns(dcolumns)).set_index(index_columns)
    df_events = pd.DataFrame(data = events, columns = _normalize_columns(ecolumns)).set_index(index_columns)
    return df_deals[df_deals.index.isin(df_events.index)]

def find_affected_deals(deals_table, events_table):
    """returns insurance deals affected by adverse events as a data table"""
    affected = _filter_deals(deals_table, events_table).reset_index()
    return (affected.columns.values.tolist(), affected.values.tolist())

def find_affected_deals_str(deals_table, events_table):
    """returns insurance deals affected by adverse events as a string"""
    return str(_filter_deals(deals_table, events_table))


