#Kyle Stanfield
#Convert binary string into hex string and tests
def binaryToHex(binary):
    "Given a string of binary, return an equivalent string in hex"
    hex = ""
    binaryToHexDict = {"0000":"0", "0001":"1", "0010":"2", "0011":"3", "0100":"4", "0101":"5", "0110":"6", "0111":"7",
    "1000":"8","1001":"9", "1010":"A","1011":"B", "1100":"C", "1101":"D", "1110":"E", "1111":"F"}
    binary = ((4-(len(binary)%4))%4) * "0" + binary #Pads the binary string so it has a length divisble by 4
    for i in range(len(binary)//4):
        hex += binaryToHexDict[binary[4*i:4*i+4]]
    return hex
    
def test_bin2Hex_1():
    assert binaryToHex("1") == '1'
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