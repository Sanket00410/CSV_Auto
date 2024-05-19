from twttr import shorten

def test_shorten_no_vowels():
    result = shorten("hmm")
    assert result == "hmm"

def test_shorten_with_vowels():
    result = shorten("Hello World")
    assert result == "Hll Wrld"

def test_shorten_empty_string():
    result = shorten("")
    assert result == ""

def test_shorten_all_vowels():
    result = shorten("AEIOUaeiou")
    assert result == ""

def test_shorten_mixed_case():
    result = shorten("AbCdEfGhIjKlMnOpQrStUvWxYz")
    assert result == "BbCdFghJklMnPQrStVWxYz"