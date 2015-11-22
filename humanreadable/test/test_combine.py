import humanreadable


def test_joins():
    lines = ["This is", "multiple", '"lines"', "of text."]
    assert (humanreadable.combine_lines(lines) ==
            'This is multiple "lines" of text.')


def test_join_sentences():
    lines = ["This is one sentence.", "And this is another."]
    assert (humanreadable.combine_lines(lines) ==
            'This is one sentence. And this is another.')


def test_join_whitespace():
    lines = ["      This text has lots of      ", "     junk whitespace.     "]
    assert (humanreadable.combine_lines(lines) ==
            "This text has lots of junk whitespace.")
