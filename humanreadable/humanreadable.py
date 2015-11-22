from __future__ import print_function


def find_paragraphs(text):
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
    return ' '.join(line.strip() for line in lines)


def justify_text(text, width=80):
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
    text = [line.rstrip() for line in text.split('\n')]
    max_width = max(len(line) for line in text)
    needed_pad = width - max_width
    output = []
    if align == 'left':
        left_pad = needed_pad // 2
        for line in text:
            pad = width - len(line)
            right_pad = max(0, pad - left_pad)
            line = ' '*left_pad + line + ' '*right_pad
            output.append(line)
    else:
        raise NotImplementedError("Only left align is implemented.")
    return '\n'.join(output)
