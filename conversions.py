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

def asciiToBinary(text):
    binary = ""
    for char in text:
        byte = decimalToBinary(ord(char))
        byte = ((8-(len(byte)%8))%8) * '0' + byte #pad each byte to 8 bits
        binary += byte
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

def test_acsii2bin_1():
    assert asciiToBinary(' ') == '00100000'
def test_ascii2bin_2():
    assert asciiToBinary('abcdefghijklmnopqrstuvwxyz') == '0110000101100010011000110110010001100101011001100110011101101000011010010110101001101011011011000110110101101110011011110111000001110001011100100111001101110100011101010111011001110111011110000111100101111010'
def test_ascii2bin_3():
    assert asciiToBinary('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == '0100000101000010010000110100010001000101010001100100011101001000010010010100101001001011010011000100110101001110010011110101000001010001010100100101001101010100010101010101011001010111010110000101100101011010'
def test_ascii2bin_4():
    assert asciiToBinary('The quick brown fox jumps over the lazy dog.') == '0101010001101000011001010010000001110001011101010110100101100011011010110010000001100010011100100110111101110111011011100010000001100110011011110111100000100000011010100111010101101101011100000111001100100000011011110111011001100101011100100010000001110100011010000110010100100000011011000110000101111010011110010010000001100100011011110110011100101110'
def test_ascii2bin_5():
    assert asciiToBinary('!@#$%^&*()_+1234567890-=~!`[]{}\\|;:\'",<.>/?') == '00100001010000000010001100100100001001010101111000100110001010100010100000101001010111110010101100110001001100100011001100110100001101010011011000110111001110000011100100110000001011010011110101111110001000010110000001011011010111010111101101111101010111000111110000111011001110100010011100100010001011000011110000101110001111100010111100111111'
