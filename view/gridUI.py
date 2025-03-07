import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

class gridUI(QWidget):
    def __init__(self, rows=10, cols=10, mines=15):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]
        self.marked = set()
        self.initUI()
        self.placeMines()
    
    def initUI(self):
        layout = QGridLayout()
        
        for row in range(self.rows):
            for col in range(self.cols):
                btn = QPushButton(' ')
                btn.setFixedSize(40, 40)
                btn.clicked.connect(lambda _, r=row, c=col: self.revealCell(r, c))
                btn.setContextMenuPolicy(3)  # Enable right-click menu
                btn.customContextMenuRequested.connect(lambda _, r=row, c=col: self.markCell(r, c))
                self.buttons[row][col] = btn
                layout.addWidget(btn, row, col)
        
        self.setLayout(layout)
        self.setWindowTitle('Minesweeper')
        self.show()
    
    def placeMines(self):
        count = 0
        while count < self.mines:
            r, c = random.randint(0, self.rows - 1), random.randint(0, self.cols - 1)
            if self.grid[r][c] != -1:
                self.grid[r][c] = -1  # -1 represents a mine
                count += 1
                self.updateNumbers(r, c)
    
    def updateNumbers(self, row, col):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] != -1:
                self.grid[nr][nc] += 1
    
    def revealCell(self, row, col):
        if (row, col) in self.marked:
            return
        
        if self.grid[row][col] == -1:
            self.buttons[row][col].setText('*')
            self.buttons[row][col].setStyleSheet('background-color: red')
        else:
            self.buttons[row][col].setText(str(self.grid[row][col]))
            self.buttons[row][col].setStyleSheet('background-color: lightgray')
    
    def markCell(self, row, col):
        if self.buttons[row][col].text() == 'F':
            self.buttons[row][col].setText(' ')
            self.marked.discard((row, col))
        else:
            self.buttons[row][col].setText('F')
            self.marked.add((row, col))
            
