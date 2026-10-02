from plates import is_valid

def test_length():
    assert is_valid("E") == False
    assert is_valid("IFSIDJFBN") == False
    assert is_valid("GDFG") == True

def test_start():
    assert is_valid("CS50") == True
    assert is_valid("C45") == False
    assert is_valid("345") == False

def test_numbers():
    assert is_valid("56SF") == False
    assert is_valid("SS3R") == False
    assert is_valid("DC05") == False
    assert is_valid("CS50") == True

def test_others():
    assert is_valid("NUM,") == False
    assert is_valid("HE LLO") == False
