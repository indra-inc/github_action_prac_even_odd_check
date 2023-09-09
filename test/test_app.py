from app import calculation_addition,calculation_mul

def test_calculation_even():

    result_add = calculation_addition(3, 5) 
    assert result_add == "Even Number"

    result_mul = calculation_mul(4, 5) 
    assert result_mul == "Even Number"

def test_calculation_odd():
    
    result_add = calculation_addition(4, 5) 
    assert result_add == "Odd Number"

    result_mul = calculation_mul(7, 9) 
    assert result_mul == "Odd Number"