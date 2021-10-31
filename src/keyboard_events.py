import sys
from capture import root

def close(event):
    sys.exit(0)

def init_keyboard_events():
    root.bind('<Escape>', close)
