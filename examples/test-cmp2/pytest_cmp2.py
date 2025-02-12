import pytest

@pytest.mark.parametrize(
    'target', [
        'esp32',
    ], indirect=True
)
@pytest.mark.generic
def test_cmp2(dut):
    dut.expect('func2')
