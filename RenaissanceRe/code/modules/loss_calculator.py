import pandas as pd

col_loss = 'Loss'
col_dealid = 'DealId'
col_peril = 'Peril'

format_str = 'out_str'
format_table = 'out_table'

def get_by_peril(deals_table, events_table, max_amount, out_format=format_table):
    """Calculates losses on reinsurance deals given adverse events that affect them. Losses are aggregated by event type."""
    dcols, drows = deals_table
    ecols, erows = events_table
    df_deals = pd.DataFrame(columns = dcols, data = drows)
    df_events = pd.DataFrame(columns = ecols, data = erows)
    df_events[col_loss][df_events[col_loss] > max_amount] = max_amount
    df_affected = df_deals.merge(df_events, on=col_dealid)
    df_losses = df_affected.groupby(col_peril, as_index=False)[col_loss].sum()
    if(out_format == format_str):
        return str(df_losses)
    return (df_losses.columns.values.tolist(), df_losses.values.tolist())
