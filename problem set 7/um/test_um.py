from um import count

def test_valid():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks, um...") == 2

def test_cap():
    assert count("Um, um, UM") == 3

def test_invalid():
    assert count("yummy") == 0
    assert count("umbrella") == 0
