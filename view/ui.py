from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from model.playEvent import playEvent
from model.rulesEvent import rulesEvent
from model.backEvent import backEvent

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.event_map = {
            "play": playEvent(),
            "rules": rulesEvent(),
            "back": backEvent(),
        }
        self.easy_button = None
        self.medium_button = None
        self.hard_button = None
        self.main_menu()

    def clear_layout(self):
        layout = self.layout()  # Get the current layout
        if layout:
            # Clear all widgets in the layout
            for i in reversed(range(layout.count())):
                widget = layout.itemAt(i).widget()
                if widget:
                    widget.deleteLater()  # Safely remove the widget

    def main_menu(self):
        # self.clear_layout()  # Clear existing widgets
        self.setWindowTitle("Minesweeper")
        self.setGeometry(100, 100, 400, 500)
        self.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.setStyleSheet("background-color: #98bce4;") 

        layout = QVBoxLayout(self)

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Game Logo
        self.logo_label = QLabel(self)
        pixmap = QPixmap("G:/Hripsime/Education/UNI/4rd_kurs/Minesweeper_pyhton/view/icons/game_logo.png") 
        self.logo_label.setPixmap(pixmap)
        self.logo_label.setScaledContents(True)
        scaled_pixmap = pixmap.scaled(300, 125, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.logo_label.setPixmap(scaled_pixmap)
        self.logo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.logo_label, alignment=Qt.AlignCenter)

        # Spacer between logo and buttons
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.play_button = self.create_button("Play", "#FFFFFF", "#41719c", lambda: self.sendEvent("play"))
        layout.addWidget(self.play_button, alignment=Qt.AlignCenter)

        self.rules_button = self.create_button("Rules", "#FFFFFF", "#41719c", lambda: self.sendEvent("rules"))
        layout.addWidget(self.rules_button, alignment=Qt.AlignCenter)
        
        self.back_button = self.create_button("Back", "#FFFFFF", "#41719c", lambda: self.sendEvent("back"), visible=False)
        layout.addWidget(self.back_button, alignment=Qt.AlignCenter)

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    def difficulty_menu(self):
        # self.clear_layout()
        self.logo_label.hide()
        self.play_button.hide()
        self.rules_button.hide()

        self.difficulty_label = QLabel("Choose Difficulty", self)
        self.difficulty_label.setStyleSheet("font-size: 20px; color: #FFFFFF; font-weight: bold;")
        self.difficulty_label.setAlignment(Qt.AlignCenter)
        self.layout().addWidget(self.difficulty_label, alignment=Qt.AlignCenter)

        # Add new buttons to the same layout
        self.easy_button = self.create_button("Easy", "#FFFFFF", "#41719c", lambda: self.sendEvent("easy"))
        self.layout().addWidget(self.easy_button, alignment=Qt.AlignCenter)

        self.medium_button = self.create_button("Medium", "#FFFFFF", "#41719c", lambda: self.sendEvent("medium"))
        self.layout().addWidget(self.medium_button, alignment=Qt.AlignCenter)

        self.hard_button = self.create_button("Hard", "#FFFFFF", "#41719c", lambda: self.sendEvent("hard"))
        self.layout().addWidget(self.hard_button, alignment=Qt.AlignCenter)

        # self.layout().addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Show back button
        self.back_button.setVisible(True)
        self.layout().addWidget(self.back_button, alignment=Qt.AlignCenter)

    def create_button(self, text, text_color, border_color, callback, visible=True):
        button = QPushButton(text, self)
        button.setFixedSize(200, 50)  # Set button size
        button.setStyleSheet(
            f"""
            QPushButton {{
                background-color: transparent;
                border: 2px solid {border_color};
                color: {text_color};
                font-size: 18px;
                padding: 10px;
                border-radius: 10px;
                background-color: rgba(145,186,228,255);
            }}
            QPushButton:hover {{
                background-color: rgba(91,155,213,255);
            }}
            """
        )
        button.clicked.connect(callback)
        button.setVisible(visible)
        return button

    def sendEvent(self, event_type):
        event = self.event_map.get(event_type)
        if event:
            event.handle(self)
        else:
            print(f"Unknown event type: {event_type}")