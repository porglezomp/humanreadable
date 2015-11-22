#!/usr/bin/python
from __future__ import print_function


def find_paragraphs(text):
    r"""
    Locate all the paragraphs in a given piece of text and return a list of
    paragraphs, where each paragraph is a list of lines.
    Paragraphs are blocks of text that are seperated by any number of blank
    lines.

    >>> find_paragraphs("Here's some text!\n\nIt's in multiple paragraphs!")
    [["Here's some text!"], ["It's in multiple paragraphs!"]]
    """
    paragraphs = []
    paragraph = []

    for line in text.split('\n'):
        if line.strip() == '':
            paragraphs.append(paragraph)
            paragraph = []
            continue
        paragraph.append(line)
    paragraphs.append(paragraph)
    return [p for p in paragraphs if p]


def combine_lines(lines):
    """
    Combine a list of lines into a single line, properly seperated by spaces.

    >>> combine_lines(["Here's a line.", "Here's another."])
    "Here's a line. Here's another."
    """
    return ' '.join(line.strip() for line in lines)


def justify_text(text, width=80):
    r"""
    Take a block of text and add line breaks in order to keep lines shorter
    than the specified `width`.
    Line breaks will be added at the closest word break before the `width`,
    or hyphenation will be naively added at the end of the line if the last
    space was too far (more than 8 characters) away from the end of the line.

    >>> justify_text("This is just example text.", width=10)
    'This is\njust\nexample\ntext.'
    """
    if width < 8:
        raise ValueError("Invalid width {}, minimum accepted width is 8")
    lines = []
    while text:
        if len(text) <= width:
            lines.append(text)
            break
        last_break = 0
        for i, letter in enumerate(text):
            if i > width:
                break
            if letter.isspace():
                last_break = i
        if last_break and width - last_break < 8:
            lines.append(text[:last_break])
            text = text[last_break:].lstrip(' ')
        else:
            lines.append(text[:width-1]+'-')
            text = text[width-1:]
    return '\n'.join(lines)


def pad_text(text, width=80, align='left'):
    r"""
    Pad text with spaces to a given width.

    The `align` parameter lets you specify an alignment, either 'left',
    'right', or 'center', which determines where the spaces are added.

    Lines longer than the specified width will not be modified.

    >>> pad_text('Hello!', width=8)
    ' Hello! '
    >>> pad_text('Hello\nto the world!', width=16)
    ' Hello          \n to the world!  '
    >>> pad_text('Hello\nto the world!', width=16, align='right')
    '          Hello \n  to the world! '
    >>> pad_text('Hello\nto the world!', width=16, align='center')
    '     Hello      \n to the world!  '
    >>> pad_text('Hello, World!', width=8)
    'Hello, World!'
    """
    text = [line.rstrip() for line in text.split('\n')]
    max_width = min(width, max(len(line) for line in text))
    needed_pad = width - max_width
    output = []
    if align == 'left':
        left_pad = needed_pad // 2
        for line in text:
            pad = width - len(line)
            right_pad = max(0, pad - left_pad)
            output.append(' '*left_pad + line + ' '*right_pad)
    elif align == 'center':
        for line in text:
            pad = max(0, width - len(line))
            left_pad = pad // 2
            right_pad = pad - left_pad
            output.append(' '*left_pad + line + ' '*right_pad)
    elif align == 'right':
        right_pad = needed_pad // 2
        for line in text:
            pad = width - len(line)
            left_pad = max(0, pad - right_pad)
            output.append(' '*left_pad + line + ' '*right_pad)
    else:
        raise ValueError("align must be one of 'left', 'right', or 'center'")
    return '\n'.join(output)


def readable(text, width, pad_width):
    """
    Run the full conversion pipeline on a piece of text.

    This function finds the paragraphs, merges the sentences, breaks the lines
    at `width`, and finally pads out the text to the desired `pad_width`.
    """
    paragraphs = find_paragraphs(text)
    paragraphs = [combine_lines(paragraph) for paragraph in paragraphs]
    paragraphs = [justify_text(paragraph, width) for paragraph in paragraphs]
    text = '\n\n'.join(paragraphs)
    return pad_text(text, pad_width, align='left')
