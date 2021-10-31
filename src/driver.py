import keyboard_events
from tkinter import PhotoImage
from capture import root


def main():
    icon = PhotoImage(file="./imgs/icon.ppm")
    root.tk.call("wm", "iconphoto", root._w, icon)
    keyboard_events.init_keyboard_events()
    root.mainloop()


if __name__ == "__main__":
    main()
