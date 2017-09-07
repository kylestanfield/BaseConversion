#Kyle Stanfield
#Converts ascii string into binary string

from decimalToBinary import decimalToBinary

def asciiToBinary(text):
    binary = ""
    for char in text:
        byte = decimalToBinary(ord(char))
        byte = ((8-(len(byte)%8))%8) * '0' + byte #pad each byte to 8 bits
        binary += byte
    return binary
    
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