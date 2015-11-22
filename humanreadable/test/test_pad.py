import humanreadable
from hypothesis import given
from hypothesis.strategies import integers, text


@given(text=text(alphabet='abcdefghijklmnopqrstuvwxyz \n'),
       width=integers(min_value=8, max_value=140))
def test_width(text, width):
    padded = humanreadable.pad_text(text, width)
    for line in padded.split('\n'):
        assert len(line) >= width


@given(text=text(alphabet='abcdefghijklmnopqrstuvwxyz \n'),
       width=integers(min_value=8, max_value=140))
def test_left_padding(text, width):
    padded = humanreadable.pad_text(text, width)
    print('---1---')
    print(text)
    print('---2---')
    print(padded)
    print('-------')

    spaces = []
    for original, changed in zip(text.split('\n'), padded.split('\n')):
        if not original.strip():
            continue
        # Count the padding that was added to the line
        left_space = len(changed) - len(changed.lstrip(' '))
        left_space -= len(original) - len(original.lstrip(' '))
        spaces.append(left_space)

    # Assert that all items are equal
    if spaces:
        assert spaces.count(spaces[0]) == len(spaces)


def test_basic():
    text = """This
text
should
be
padded"""
    expect = " This   \n text   \n should \n be     \n padded "
    assert humanreadable.pad_text(text, width=8) == expect
