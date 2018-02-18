import pandas as pd

format_str = 'out_str'
format_table = 'out_table'

def find_affected_deals(deals_table, events_table, out_format=format_table):
    dcolumns, deals = deals_table
    ecolumns, events = events_table
    index_columns = ['Peril', 'Location']
    df_deals = pd.DataFrame(data = deals, columns = dcolumns).set_index(index_columns)
    df_events = pd.DataFrame(data = events, columns = ecolumns).set_index(index_columns)
    df_affected = df_deals[df_deals.index.isin(df_events.index)]
    if out_format == format_str:
        return str(df_affected)
    df_affected = df_affected.reset_index()
    return (df_affected.columns.values.tolist(), df_affected.values.tolist())


