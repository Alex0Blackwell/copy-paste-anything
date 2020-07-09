import pyautogui
import pyperclip
import convert
from tkinter import *


class Application():
    """
    This is a class for the GUI for screen snipping text.

    Attributes:
        master (Tk()): Required to start the tkinter GUI.
    """
    def __init__(self, master):
        """The constructor for Application class"""
        self.master = master
        self.x = self.y = 0
        self.rect   = None
        self.startX = None
        self.startY = None
        self.curX   = None
        self.curY   = None

        root.attributes("-alpha", 1)
        root.geometry('250x50+100+100')  # set window dimensions
        root.title('Copy')
        self.menu_frame = Frame(master, bg="#4a4a4a")
        self.menu_frame.pack(fill=BOTH, expand=YES)

        self.buttonBar = Frame(self.menu_frame, bg="#1f1f1f")
        self.buttonBar.pack(fill=BOTH,expand=YES)


        self.snipButton = Button(self.buttonBar, text='Clip', width=5, command=self.createScreenCanvas, background="#5a6778")
        self.snipButton.pack(expand=YES)

        self.master_screen = Toplevel(root)
        self.master_screen.withdraw()
        self.master_screen.attributes("-alpha", .8)
        self.picture_frame = Frame(self.master_screen, background = "#8698b0")
        self.picture_frame.pack(fill=BOTH, expand=YES)


    def snip(self, left, top, width, height):
        """
        The method to take a screenshot given an area.

        Parameters:
            left (int): The left position.
            top (int): The top position.
            width (int): The width.
            height (int): The height.
        """
        im = pyautogui.screenshot(region=(left, top, width, height))
        im.save(".capture.png")


    def createScreenCanvas(self):
        """ The method to create the focused screen overlay and handle events. """

        self.master_screen.deiconify()
        root.withdraw()

        self.screenCanvas = Canvas(self.picture_frame, cursor="cross", bg="#696969")
        self.screenCanvas.pack(fill=BOTH, expand=YES)

        self.screenCanvas.bind("<ButtonPress-1>", self.on_button_press)      # left click
        self.screenCanvas.bind("<B1-Motion>", self.on_move_press)            # mouse drag
        self.screenCanvas.bind("<ButtonRelease-1>", self.on_button_release)  # left release

        self.master_screen.attributes('-fullscreen', True)
        self.master_screen.attributes('-alpha', .2)
        self.master_screen.lift()
        self.master_screen.attributes("-topmost", True)


    def on_button_press(self, event):
        """
        The method for when the left mouse button is pressed and a selection
        should be started.

        Parameters:
            event: Bound to <ButonPress-1>.
        """

        # save mouse drag start position
        self.startX = self.screenCanvas.canvasx(event.x)
        self.startY = self.screenCanvas.canvasy(event.y)

        self.rect = self.screenCanvas.create_rectangle(self.x, self.y, 1, 1, outline='#dbf3ff', width=2)


    def on_move_press(self, event):
        """
        The method for when the left mouse button is held down and dragged.

        Parameters:
            event: Bound to <B1-Motion>.
        """

        self.curX, self.curY = (event.x, event.y)
        # update rectangle as you drag the mouse
        self.screenCanvas.coords(self.rect, self.startX, self.startY, self.curX, self.curY)


    def on_button_release(self, event):
        """
        The method after an area is selected and a screenshot must be taken.

        Parameters:
            event: Bound to <ButtonRelease-1>.
        """

        self.exitScreenshotMode()

        left   = min(self.startX, self.curX)
        top    = min(self.startY, self.curY)
        width  = abs(self.startX - self.curX)
        height = abs(self.startY - self.curY)

        self.snip(left, top, width, height)

        self.text = convert.getText()

        print("Text is:\n" + '-'*10)
        print(self.text)
        print('-'*10)
        try:
            pyperclip.copy(self.text);
            print("This has been copied to your clipboard")
        except Exception as e:
            print("Sorry, the above text could not be copied to your clipboard")
            raise

        # let's end the program as soon as the text is copied to the clipboard
        self.exit_application()


    def exitScreenshotMode(self):
        """ Method to exit the selecting mode. """
        self.screenCanvas.destroy()
        self.master_screen.withdraw()
        root.deiconify()


    def exit_application(self):
        """ Method to end the application. """
        root.quit()


root = Tk()
app = Application(root)
