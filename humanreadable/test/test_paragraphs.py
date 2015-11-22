import humanreadable


def test_basic():
    test = """Let's include some text in here!

We'll have two paragraphs!
    """
    paragraphs = humanreadable.find_paragraphs(test)
    assert [["Let's include some text in here!"],
            ["We'll have two paragraphs!"]] == paragraphs


def test_no_trailing_newline():
    test = """Let's include some text in here!

We'll have two paragraphs!"""
    paragraphs = humanreadable.find_paragraphs(test)
    assert [["Let's include some text in here!"],
            ["We'll have two paragraphs!"]] == paragraphs


def test_large_spacing():
    test = """Paragraph 1





Paragraph 2"""
    paragraphs = humanreadable.find_paragraphs(test)
    assert [["Paragraph 1"], ["Paragraph 2"]] == paragraphs
