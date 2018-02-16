import sys
import os
sys.path.append('../code')
import contract_evaluator

def test_contract_evaluator_creates_non_empty_report():
    outfile = 'tmpreport.txt'
    try:
        os.remove(outfile)
    except OSError:
        pass
    contract_evaluator.create_coverage_report('files/deals.csv', 'files/contract.json', outfile)
    assert os.path.isfile(outfile)
    assert os.path.getsize(outfile) > 0
