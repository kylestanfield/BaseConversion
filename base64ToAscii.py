#Kyle Stanfield
#Decode base64 into ASCII

from binaryToAscii import binaryToAscii
base64Dict = {'A': '000000', 'B': '000001', 'C': '000010', 'D': '000011', 'E': '000100', 'F': '000101',
 'G': '000110', 'H': '000111', 'I': '001000', 'J': '001001', 'K': '001010', 'L': '001011',
 'M': '001100', 'N': '001101', 'O': '001110', 'P': '001111', 'Q': '010000', 'R': '010001',
 'S': '010010', 'T': '010011', 'U': '010100', 'V': '010101', 'W': '010110', 'X': '010111',
 'Y': '011000', 'Z': '011001', 'a': '011010', 'b': '011011', 'c': '011100', 'd': '011101',
 'e': '011110', 'f': '011111', 'g': '100000', 'h': '100001', 'i': '100010', 'j': '100011',
 'k': '100100', 'l': '100101', 'm': '100110', 'n': '100111', 'o': '101000', 'p': '101001',
 'q': '101010', 'r': '101011', 's': '101100', 't': '101101', 'u': '101110', 'v': '101111',
 'w': '110000', 'x': '110001', 'y': '110010', 'z': '110011', '0': '110100', '1': '110101',
 '2': '110110', '3': '110111', '4': '111000', '5': '111001', '6': '111010', '7': '111011',
 '8': '111100', '9': '111101', '+': '111110', '/': '111111'}

def base64ToAscii(base64):
    binary = ""
    base64 = base64.replace('=','')
    for char in base64:
        binary += base64Dict[char]
    return binaryToAscii(binary)

def test_base64ToAscii_1():
    assert base64ToAscii('SGVsbG8sIFdvcmxkIQ==') == 'Hello, World!'
def test_base64ToAscii_2():
    assert base64ToAscii('SXQgd2FzIHRoZSBiZXN0IG9mIHRpbWVzLCBpdCB3YXMgdGhlIHdvcnN0IG9mIHRpbWVzLg==') == 'It was the best of times, it was the worst of times.'
def test_base64ToAscii_3():
    assert base64ToAscii('SSBhbSBhIHNvdWwtbGVzcyBkZXZpbCBiZWFzdA==') == 'I am a soul-less devil beast'
def test_base64ToAscii_4():
    assert base64ToAscii('V3JpdGluZyB0ZXN0cyBpcyBhIGdvb2Qgd2F5IHRvIG1ha2Ugc3VyZSB5b3Uga25vdyB0aGF0IHlvdXIgZnVuY3Rpb25zIHdvcmsgYXMgaW50ZW5kZWQuIEJ1dCBpdCBjYW4gYmUgaGFyZCB0byBjb21lIHVwIHdpdGggYXBwcm9wcmlhdGUgY29ybmVyIGNhc2VzIGFuZCBzdWNoIHRvIHRlc3QgdGhlIGxpbWl0cyBvZiB5b3VyIGNvZGUu') == 'Writing tests is a good way to make sure you know that your functions work as intended. But it can be hard to come up with appropriate corner cases and such to test the limits of your code.'
