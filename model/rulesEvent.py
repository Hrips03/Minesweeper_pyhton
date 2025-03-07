from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from model.IEvent import IEvent

class rulesEvent(IEvent):
    def handle(self, ui_instance):
        ui_instance.logo_label.hide()
        ui_instance.play_button.hide()
        ui_instance.rules_button.hide()

        ui_instance.rules_label = QLabel(
            "Minesweeper Rules:\n"
            "1. Uncover squares to reveal numbers or mines.\n"
            "2. Numbers indicate how many mines are adjacent.\n"
            "3. Right-click to place a flag on a suspected mine.\n"
            "4. Clear the board without detonating a mine to win.\n"
            "5. If you click on a mine, you lose the game.",
            ui_instance
        )
        ui_instance.rules_label.setWordWrap(True)
        ui_instance.rules_label.setStyleSheet("color: white; font-size: 17px;")
        ui_instance.rules_label.setAlignment(Qt.AlignCenter)

        ui_instance.layout().insertWidget(1, ui_instance.rules_label)

        ui_instance.rules_label.show()
        ui_instance.back_button.show()
