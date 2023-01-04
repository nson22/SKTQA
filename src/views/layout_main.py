from PySide6.QtWidgets import QMainWindow, QFrame, QVBoxLayout

from src.views.components.layout_top import LayoutTop


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_frame = QFrame()

        self.main_layout = QVBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.content_top = LayoutTop()

        # Main content
        self.content_main = QFrame()
        self.content_main.setStyleSheet('background-color: #fff')

        self.main_layout.addWidget(self.content_top)
        self.main_layout.addWidget(self.content_main)

        self.setCentralWidget(self.central_frame)
