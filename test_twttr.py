from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"

def test_mixed():
    assert shorten("TWittER") == "TWttR"

def test_numbers():
    assert shorten("cs50") == "cs50"

def test_punctuation():
    assert shorten("twitter!") == "twttr!"

def test_empty():
    assert shorten("") == ""
