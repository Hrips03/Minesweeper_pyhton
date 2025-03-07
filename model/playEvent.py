from model.IEvent import IEvent  
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from view.gridUI import gridUI

class playEvent(IEvent):
    def __init__(self, difficulty=None):
        self.difficulty = difficulty
        
    def handle(self, ui_instance):
        if self.difficulty==None:
            ui_instance.difficulty_menu()
        elif self.difficulty == "easy":
            gridUI(9,9,10)
        elif self.difficulty == "medium":
            gridUI(16,16,40)
        elif self.difficulty == "hard":
            gridUI(16,30,99)
