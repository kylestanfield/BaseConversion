#Kyle Stanfield
#Binary to decimal conversion and tests with pytest

def binaryToDecimal(binary):
    "Given a binary string, will return equivalent decimal representation"
    decimal = 0
    binary = binary[::-1]
    for i in range(len(binary)):
        decimal += int(binary[i]) * 2**i
    return decimal

def test_bin2Dec_1():
    assert binaryToDecimal("1") == 1
def test_bin2Dec_2():
    assert binaryToDecimal("10") == 2
def test_bin2Dec_3():
    assert binaryToDecimal("11") == 3
def test_bin2Dec_4():
    assert binaryToDecimal("100") == 4
def test_bin2Dec_5():
    assert binaryToDecimal("1000") == 8
def test_bin2Dec_6():
    assert binaryToDecimal("1000110010101") == 4501
    