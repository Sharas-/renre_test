from modules import *

def create_coverage_report(deals_file, contract_file, output_file):
    """Creates a report on insurance deals covered by a reinsurance contract"""
    all_deals = csv_reader.read(deals_file)
    adverse_events = contract_reader.get_covered_events(contract_file)
    covered_deals = deal_filter.find_affected_deals(all_deals, adverse_events, out_format=deal_filter.format_str)
    coverage_report.create(covered_deals, output_file) 

