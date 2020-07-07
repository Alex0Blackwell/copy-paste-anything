'''
Alex Blackwell
July 6, 2020
'''

import os, capture


def main():
    capture.root.mainloop()

    os.remove(".capture.png")


if __name__ == '__main__':
    main()
