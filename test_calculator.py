from calculator import Calc

def test_calc_sum():
    c = Calc("1+2+3")
    result = c.result()
    assert result == 6

def test_calc_sub():
    c = Calc("10-4")
    result = c.result()
    assert result == 6

def test_calc_mult():
    c = Calc("1*2*3")
    result = c.result()
    assert result == 6

def test_calc_div():
    c = Calc("12/2")
    result = c.result()
    assert result == 6