#Kyle Stanfield
#Convert Hex to binary and tests

hexToBinaryDict = {'0':'0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

def hexToBinary(hex):
    "Convert a hex string into a binary string"
    binary = ""
    for nibble in hex:
        binary += hexToBinaryDict[nibble]
    return binary
    
def test_hex2bin_0():
    assert hexToBinary("0") == '0000'
def test_hex2bin_1():
    assert hexToBinary("1") == '0001'
def test_hex2bin_2():
    assert hexToBinary("2") == '0010'
def test_hex2bin_3():
    assert hexToBinary("3") == '0011'
def test_hex2bin_4():
    assert hexToBinary("4") == '0100'
def test_hex2bin_5():
    assert hexToBinary("5") == '0101'
def test_hex2bin_6():
    assert hexToBinary("6") == '0110'
def test_hex2bin_7():
    assert hexToBinary("7") == '0111'
def test_hex2bin_8():
    assert hexToBinary("8") == '1000'
def test_hex2bin_9():
    assert hexToBinary("9") == '1001'
def test_hex2bin_10():
    assert hexToBinary("A") == '1010'
def test_hex2bin_11():
    assert hexToBinary("B") == '1011'
def test_hex2bin_12():
    assert hexToBinary("C") == '1100'
def test_hex2bin_13():
    assert hexToBinary("D") == "1101"
def test_hex2bin_14():
    assert hexToBinary("E") == '1110'
def test_hex2bin_15():
    assert hexToBinary("F") == '1111'
def test_hex2bin_16():
    assert hexToBinary("DEADBEEF") == '11011110101011011011111011101111'