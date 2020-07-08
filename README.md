# Copy-Paste Anything

## Table of contents
* [Overview](#overview)
* [Examples](#examples)
* [Technologies](#technologies)
* [Setup](#setup)
* [Limitations](#limitations)


## Overview
### Synopsis
Screen snip an area of your screen to have it converted to text and copied to your clipboard! This program allows you to copy text from anywhere on your screen. This means that text from videos, photos, or any filetype can be copied.

### Extended
Often, tutorials contain text that must be copied out line by line. This program, however, allows just a screen snip of an area to be taken, and the text in the area will automatically be converted to text and copied to your clipboard. In addition to its uses while watching videos, there exists literature that is stored in such a file type where it does not support the copy-pasting text. However, with this program, a screen snip of the area you wish to copy can be taken and the text will be copied to your clipboard. Any place you see text on your screen, this program can copy it so you can paste it!


## Examples

> Copy and paste from a code tutorial!

![Screen Recording](./.images/copy.gif "Copy from videos!")

## Technologies
- **Python 3.8**
- **OpenCV 4.2.0**
  - Computer vision library required for converting an image to text
- **pytesseract 0.3**
  - Optical character recognition (OCR) tool
  - Reads the text embedded in images
- **PyAutoGUI 0.9**
  - Cross-platform GUI
- **tkinter 8.6**
  - Windowing toolkit for use with tlc
- **Pyperclip 1.8**
  - Cross-platform module for copy and paste clipboard functions


## Setup
To run this project, install the dependencies and the requirements.  
### Dependencies

#### tesseract
If you are on a *windows* computer, you need to install the command line program [tesseract](https://github.com/tesseract-ocr/tesseract).  
There are builds available [here](https://github.com/UB-Mannheim/tesseract/wiki).
- Make sure this is installed to the default installation directory *(C:\Program Files\Tesseract-OCR)*.

#### pyperclip
- Windows
  - No additional modules needed.
- Mac
  - Needs `pbcopy` and `pbpaste` which should come with the OS.
- Linux
  - Needs `xclip` or `xsel` which should come with the OS.
  - Needs the `gtk` or `PyQt4` modules installed.

### Requirements
Install the requirements:  

    pip3 install -r requirements.txt

### Usage
Run the program:  

    python3 driver.py

I would recommend making a keyboard shortcut for this program. For example, I made a keyboard shortcut for `ctrl-shift-prtSc` which runs `python3 ~/path/to/copy-and-paste-anything/driver.py`  


## Limitations
- The project runs the most up to date machine learning algorithms for parsing the embedded text in images, however, the algorithms will sometimes confuse characters.
- The more content that is in the screen snip, the more likely the machine learning algorithm is to make a mistake.
- [ ] Currently no keyboard shortcut to cancel a screenshot.


## License
Licensed under the [GNU General Public License v3.0](LICENSE).
