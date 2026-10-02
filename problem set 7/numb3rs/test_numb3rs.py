from numb3rs import validate

def test_valid():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True

def test_invalid_range():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False

def test_invalid_format():
    assert validate("192.168.001.1") == False
    assert validate("cat") == False
    assert validate("123.2.3") == False

def test_leading_zero():
    assert validate("001.34.56.78") == False
