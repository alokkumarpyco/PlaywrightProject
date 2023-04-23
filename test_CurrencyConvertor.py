from currencyConvertor import CurrencyConverter

def test_CurrencyConverter():
    # Test case 1
    converter = CurrencyConverter(10, 100)
    print(converter)
    assert converter.YenToDollar() == 100.76

    # Test case 2
    converter = CurrencyConverter(10, 100)
    print(converter)
    assert converter.DollarToYen() == 13190.0

