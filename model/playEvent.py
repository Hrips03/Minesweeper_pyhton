from model.IEvent import IEvent  
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class playEvent(IEvent):
    def handle(self, ui_instance):
        ui_instance.difficulty_menu()
