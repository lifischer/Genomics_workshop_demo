from  rna import RNA
import pytest
def test_bad_sequence_raises_error():

    with pytest.raises(ValueError):
        RNA('ATB')
def test_bad_sequence_raises_works():

     assert DNA('GUC').complimentary_sequence == DNA('CAG')
     assert DNA('AUC').complimentary_sequence == DNA('UAG')


print('it worked')