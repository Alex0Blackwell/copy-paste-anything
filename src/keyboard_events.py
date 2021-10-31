import sys


def close(event):
    sys.exit(0)


def init_keyboard_events(root):
    root.bind("<Escape>", close)
