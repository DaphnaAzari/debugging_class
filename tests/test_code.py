import pytest
from lib.code import *

def test_limit_smaller_than_22():
    result = wrap_text("people",21)
    assert result == "limit needs to be at least 22 for this exercise"

def test_single_word_len_bigger_than_22():
    string_too_long = ""
    for x in range(23):
        string_too_long += "a"
    print(f"loop orint out: {len(string_too_long)}")
    result = wrap_text(string_too_long,22)
    assert result == "can't wrap as at least one word is longer than the limit"
    