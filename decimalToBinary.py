#Kyle Stanfield
#Convert decimal integer to binary string and tests

def decimalToBinary(x):
    "Given an integer x, will return an equivalent binary string"
    binary = ""
    while x >= 1:
        binary += str(x%2)
        x //= 2
    return binary[::-1]
    
def test_dec2Bin_1():
    assert decimalToBinary(1) == "1"
def test_dec2Bin_2():
    assert decimalToBinary(2) == "10"
def test_dec2Bin_3():
    assert decimalToBinary(3) == "11"
def test_dec2Bin_4():
    assert decimalToBinary(4) == "100"
def test_dec2Bin_5():
    assert decimalToBinary(8) == "1000"
def test_dec2Bin_6():
    assert decimalToBinary(4501) == "1000110010101"