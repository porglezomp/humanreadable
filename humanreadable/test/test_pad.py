import humanreadable
from hypothesis import given, example
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
            assert len(changed) == width
            continue
        # Count the padding that was added to the line
        left_space = len(changed) - len(changed.lstrip(' '))
        left_space -= len(original) - len(original.lstrip(' '))
        spaces.append(left_space)

    # Assert that all items are equal
    if spaces:
        assert spaces.count(spaces[0]) == len(spaces)


@given(text=text(alphabet='abcdefghijklmnopqrstuvwxyz \n'),
       width=integers(min_value=8, max_value=140))
def test_right_padding(text, width):
    padded = humanreadable.pad_text(text, width, align='right')
    print('---1---')
    print(text)
    print('---2---')
    print(padded)
    print('-------')

    spaces = []
    for original, changed in zip(text.split('\n'), padded.split('\n')):
        if not original.strip():
            assert len(changed) == width
            continue
        # Count the padding that was added to the right of the line
        right_space = len(changed) - len(changed.rstrip())
        spaces.append(right_space)

    # Assert that all items are equal
    if spaces:
        assert spaces.count(spaces[0]) == len(spaces)


@given(text=text(alphabet='abcdefghijklmnopqrstuvwxyz \n'),
       width=integers(min_value=8, max_value=140))
@example(text='  ', width=8)
def test_center_padding(text, width):
    padded = humanreadable.pad_text(text, width, align='center')
    print('---1---')
    print(text)
    print('---2---')
    print(padded)
    print('-------')

    for original, changed in zip(text.split('\n'), padded.split('\n')):
        if not changed.strip():
            assert len(changed) == width
            continue
        # Count the padding to the left of the line
        left_space = len(changed) - len(changed.lstrip(' '))
        left_space -= len(original) - len(original.lstrip(' '))
        # and the padding to the right_pad of the line
        right_space = len(changed) - len(changed.rstrip(' '))
        assert abs(left_space - right_space) <= 1


def test_basic():
    text = """This
text
should
be
padded"""
    expect = " This   \n text   \n should \n be     \n padded "
    assert humanreadable.pad_text(text, width=8) == expect


def test_wrong_align():
    try:
        humanreadable.pad_text('Hello, World!', align='hello')
    except ValueError:
        pass
    else:
        assert False  # Unreachable!


def test_pad_indented():
    text = "Here's some text\n    and this text is indented"
    expect = " Here's some text               \n     and this text is indented  "
    assert humanreadable.pad_text(text, width=32) == expect














