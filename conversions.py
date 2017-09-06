#Kyle Stanfield
#TODO: Convert to and from base64. dec2base64 convert to bin and treat as 6 bit
#groups and use a dictionary to turn them into respective base64 value & concat.

def binaryToDecimal(binary):
    "Given a binary string, will return equivalent decimal representation"
    decimal = 0
    binary = binary[::-1]
    for i in range(len(binary)):
            decimal += int(binary[i]) * 2**i
    return decimal

def decimalToBinary(x):
    "Given an integer x, will return an equivalent binary string"
    binary = ""
    while x >= 1:
            binary += str(x%2)
            x //= 2
    return binary[::-1]
        
def binaryToHex(binary):
    "Given a string of binary, return an equivalent string in hex"
    hex = ""
    binaryToHexDict = {"0000":"0", "0001":"1", "0010":"2", "0011":"3", "0100":"4", "0101":"5", "0110":"6", "0111":"7",
    "1000":"8","1001":"9", "1010":"A","1011":"B", "1100":"C", "1101":"D", "1110":"E", "1111":"F"}
    binary = ((4-(len(binary)%4))%4) * "0" + binary #Pads the binary string so it has a length divisble by 4
    for i in range(len(binary)//4):
        hex += binaryToHexDict[binary[4*i:4*i+4]]
    return hex
        
def hexToBinary(hex):
    "Convert a hex string into a binary string"
    binary = ""
    hexToBinaryDict = {'0':'0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    for nibble in hex:
        binary += hexToBinaryDict[nibble]
    return binary
                        
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
    
def test_bin2Hex_1():
    assert binaryToHex("0001") == '1'
def test_bin2Hex_2():
    assert binaryToHex("10") == '2'
def test_bin2Hex_3():
    assert binaryToHex("100") == '4'
def test_bin2Hex_4():
    assert binaryToHex("1010") == 'A'
def test_bin2Hex_5():
    assert binaryToHex("1011") == 'B'
def test_bin2Hex_6():
    assert binaryToHex("1100") == 'C'
def test_bin2Hex_7():
    assert binaryToHex("1101") == 'D'
def test_bin2Hex_8():
    assert binaryToHex("1110") == 'E'
def test_bin2Hex_9():
    assert binaryToHex("1111") == 'F'
def test_bin2Hex_10():
    assert binaryToHex("11011110101011011011111011101111") == 'DEADBEEF'