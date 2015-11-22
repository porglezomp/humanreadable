import humanreadable


def test_basic():
    text = """Here's
some.

paragraphs
in writing"""
    expect = " Here's some. \n              \n paragraphs   \n in writing   "
    assert humanreadable.readable(text, 12, 14) == expect
