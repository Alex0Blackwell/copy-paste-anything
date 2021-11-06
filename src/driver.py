import argparse
import keyboard_events
from tkinter import *
from capture import Application


def main():
    parser = argparse.ArgumentParser(description="Copy Paste Anything")
    parser.add_argument(
        "-n",
        "--no-copy",
        action="store_true",
        help="Disable automatically copying to the clipboard",
    )
    parser.add_argument(
        "-s",
        "--simple",
        action="store_true",
        help="Start selecting an area of the screen right away",
    )
    args = parser.parse_args()

    root = Tk()
    Application(root, args)

    icon = PhotoImage(file="./imgs/icon.ppm")
    root.tk.call("wm", "iconphoto", root._w, icon)
    keyboard_events.init_keyboard_events(root)
    root.mainloop()


if __name__ == "__main__":
    main()
