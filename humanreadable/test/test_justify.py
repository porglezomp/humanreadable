import humanreadable
from hypothesis import given
from hypothesis.strategies import text, integers


@given(text=text(), width=integers(min_value=8, max_value=140))
def test_justify_widths(text, width):
    for line in humanreadable.justify_text(text, width).split('\n'):
        assert len(line) <= width


def test_bad_width():
    try:
        humanreadable.justify_text("Hello, World!", width=1)
    except ValueError:
        pass
    else:
        assert False  # Unreachable


def test_justify_specific():
    text = "Here's a specific piece of text that should be justified."
    assert (humanreadable.justify_text(text, 20) ==
            "Here's a specific\npiece of text that\nshould be justified.")

    text = "This is another justification test."
    assert (humanreadable.justify_text(text, 10) ==
            "This is\nanother\njustifica-\ntion test.")

    text = "This text doesn't need to be justified."
    assert (humanreadable.justify_text(text) == text)
