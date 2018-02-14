import numpy
import pandas as pd

def _normalize_columns(cols):
    return [c.upper() for c in cols]

def find_affected_policies(policies, pcolumns, adverse_events, ecolumns):
    """returns policies affected by adverse events"""
    index_columns = ['PERIL', 'LOCATION']
    df_policies = pd.DataFrame(data = policies, columns = _normalize_columns(pcolumns)).set_index(index_columns)
    df_events = pd.DataFrame(data = adverse_events, columns = _normalize_columns(ecolumns)).set_index(index_columns)

    affected = df_policies[df_policies.index.isin(df_events.index)].reset_index()
    return (affected.columns.values.tolist(), affected.values.tolist())
