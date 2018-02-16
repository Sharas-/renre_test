from modules import *

def create_coverage_report(deals_file, contract_file, report_file):
    """Creates a report on insurance deals covered by a reinsurance contract"""
    deals = deal_reader.read(deals_file)
    adverse_events = contract_reader.get_covered_events(contract_file)
    covered_deals = deal_filter.find_affected_deals_str(deals, adverse_events)
    report_formater.create_report(covered_deals, report_file) 

