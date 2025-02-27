from model.IEvent import IEvent  
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class backEvent(IEvent):
    def handle(self, ui_instance):
        # ui_instance.main_menu()

        ui_instance.rules_label.hide()
        ui_instance.back_button.hide()

        if ui_instance.easy_button is not None:
            ui_instance.difficulty_label.hide()
            ui_instance.easy_button.hide()
            ui_instance.medium_button.hide()
            ui_instance.hard_button.hide()


        ui_instance.logo_label.show()
        ui_instance.play_button.show()
        ui_instance.rules_button.show()