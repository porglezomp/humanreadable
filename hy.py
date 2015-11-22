import humanreadable

if __name__ == '__main__':
    import sys
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--width', type=int, default=80,
                        help='the width to display the text')
    parser.add_argument('-p', '--pad-width', type=int,
                        help='the total width of the padding')
    parser.add_argument('filename', nargs='?', type=file, default=sys.stdin)
    args = parser.parse_args(sys.argv[1:])
    width = args.width
    pad_width = args.pad_width

    if pad_width is None:
        import fcntl
        import termios
        import struct
        zeros = struct.pack('HHHH', 0, 0, 0, 0)
        winsize = fcntl.ioctl(0, termios.TIOCGWINSZ, zeros)
        term_h, term_w, _, _ = struct.unpack('HHHH', winsize)
        pad_width = term_w

    text = args.filename.read()
    print(humanreadable.readable(text, width, pad_width))
