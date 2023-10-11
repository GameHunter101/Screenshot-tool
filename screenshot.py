from PIL import ImageGrab;
from tkinter import *;
from tkinter import ttk;
from screeninfo import get_monitors;

from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
import sys

class WindowManager:
    root = Tk()
    def __init__(self) -> None:
        self.root.withdraw()
        for i, monitor in enumerate([get_monitors()[0]]):
            print(monitor)
            win = Toplevel(self.root)
            win.geometry(f"{100}x{100}-{-1* int(monitor.width/3)}+100")
            # win.overrideredirect(True)
            win.attributes("-fullscreen",True)

        self.root.bind_all("<Escape>", lambda e: self.escape_close(e))
        self.root.bind_all("<Alt-F4>", lambda e: self.escape_close(e))
    
    def escape_close(self,e):
        self.root.quit()
    
    def main_loop(self) -> None:
        self.root.mainloop()

class Window(QMainWindow): 
  
  
    def __init__(self, pos_x: int, pos_y: int): 
        super().__init__() 
  
  
        # set the title 
        self.setWindowTitle("Python") 
  
        # setting  the geometry of window 
        self.setGeometry(0, 0, 600, 400) 

        screen_number = 1
        screen_geometry = QApplication.desktop().screenGeometry(screen_number)

        # self.move(screen_geometry.x(),screen_geometry.y())
        self.move(pos_x, pos_y)
  
        # setting opacity level 
        self.setStyleSheet("background-color: #0e0e0e;")
        self.setWindowOpacity(0.7) 
  
        # show all the widgets 
        # self.showFullScreen()
        self.show()
    
    def keyPressEvent(self,event):
        if event.key() == Qt.Key_Escape:
            self.close()

def create_window():
    # wm = WindowManager()
    # wm.main_loop()

    App = QApplication(sys.argv)

        

    window = Window()
    window_2 = Window()
    def close_both_windows(e):
        window.close()
        window_2.close()
    window.keyPressEvent = close_both_windows
    window_2.keyPressEvent = close_both_windows
    sys.exit(App.exec())


def print_image(file: str):
    im = ImageGrab.grab(bbox=(0, 0, 100, 100), all_screens=True, include_layered_windows=True)
    im.save(file)

