from modules import *

def report_losses(deals_file, contract_file, events_file, output_file):
    """Creates loss report given a list of adverse events and exposure to reinsured deals"""
    all_deals = csv_reader.read(deals_file)
    covered_events, max_amount = contract_reader.read(contract_file)
    covered_deals = deal_filter.find_affected_deals(all_deals, covered_events)
    adverse_events = csv_reader.read(events_file)
    losses = loss_calculator.get_by_peril(covered_deals, adverse_events, max_amount, out_format=loss_calculator.format_str) 
    loss_report.create(losses, output_file) 
