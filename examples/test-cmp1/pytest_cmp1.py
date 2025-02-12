import pytest

@pytest.mark.parametrize(
    'target', [
        'esp32',
    ], indirect=True
)
@pytest.mark.generic
def test_cmp1(dut):
    dut.expect('func1')
    dut.expect('func2')
