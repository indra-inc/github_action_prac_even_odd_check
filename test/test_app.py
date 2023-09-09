from app import calculation

def test_calculation_even():

    result = calculation(3, 5) 
    assert result == "Even Number"

def test_calculation_odd():
    
    result = calculation(4, 5)
    assert result == "Odd Number"