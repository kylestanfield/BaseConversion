#Kyle Stanfield
#Convert ascii into base64

def asciiToBase64(text):
    base64 = ""
    binary = asciiToBinary(text)
    base64Dict = {'000000':'A', '000001':'B', '000010':'C', '000011':'D', '000100':'E', '000101':'F', '000110':'G',
    
    '000111':'H', '001000':'I', '001001':'J', '001010':'K', '001011':'L', '001100':'M', '001101':'N', '001110':'O',
    
    '001111':'P', '010000':'Q', '010001':'R', '010010':'S', '010011':'T', '010100':'U', '010101':'V', '010110':'W',
    
    '010111':'X', '011000':'Y', '011001':'Z', '011010':'a', '011011':'b', '011100':'c', '011101':'d', '011110':'e',
    
    '011111':'f', '100000':'g', '100001':'h', '100010':'i', '100011':'j', '100100':'k', '100101':'l', '100110':'m',
    
    '100111':'n', '101000':'o', '101001':'p', '101010':'q', '101011':'r', '101100':'s', '101101':'t', '101110':'u',
    
    '101111':'v', '110000':'w', '110001':'x', '110010':'y', '110011':'z', '110100':'0', '110101':'1', '110110':'2',
    
    '110111':'3', '111000':'4', '111001':'5', '111010':'6', '111011':'7', '111100':'8', '111101':'9', '111110':'+', '111111':'/'}
    padding = 0
    
    if len(binary) % 24 != 0: #establish how many equal signs of padding are needed
        padding = (24-(len(binary)%24))//8
    #Make the binary string have even sets of six bits
    if len(binary) % 6 != 0:
        binary = binary + ((6-(len(binary)%6))*'0')
    
    for i in range(len(binary)//6):
        base64 += base64Dict[binary[6*i:6*i+6]]
    
    return base64 + padding*'='
                        

def test_ascii2base64_1():
    assert asciiToBase64('abcdefghijklmnopqrstuvwxyz') == 'YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXo='
def test_ascii2base64_2():
    assert asciiToBase64('ABCDEFGHIJKLMNOPQRSTUVWXYZ[]{}\\|=-+_1234567890!@#$%^&*(),./<>?;\':"') == 'QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVpbXXt9XHw9LStfMTIzNDU2Nzg5MCFAIyQlXiYqKCksLi88Pj87Jzoi'
def test_ascii2base64_3():
    assert asciiToBase64('Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasure.') == 'TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlzIHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1c3Qgb2YgdGhlIG1pbmQsIHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0aGUgY29udGludWVkIGFuZCBpbmRlZmF0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdlLCBleGNlZWRzIHRoZSBzaG9ydCB2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3VyZS4='
    