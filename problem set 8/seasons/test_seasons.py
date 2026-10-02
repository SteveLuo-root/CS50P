from seasons import convert
import pytest
from datetime import date, timedelta

def test_invalid():
    with pytest.raises(SystemExit):
        convert("January 2, 2003")

def test_today():
    today = date.today().isoformat()
    assert convert(today) == "zero"

def test_one_day():
    yesterday = date.today() - timedelta(days=1)
    assert convert(yesterday.isoformat()) == "one thousand, four hundred forty"
