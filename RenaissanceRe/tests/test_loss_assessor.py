import sys
import os
sys.path.append('../code')
import loss_assessor

def test_loss_assessor_creates_non_empty_report():
    outfile = 'tmpreport.txt'
    try:
        os.remove(outfile)
    except OSError:
        pass
    loss_assessor.report_losses('files/deals.csv', 'files/contract.json', 'files/losses.csv', outfile)
    assert os.path.isfile(outfile)
    assert os.path.getsize(outfile) > 0
