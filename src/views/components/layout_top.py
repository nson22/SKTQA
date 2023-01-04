from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QFrame, QSpacerItem, QPushButton, QSizePolicy, QHBoxLayout


class LayoutTop(QFrame):
    def __init__(self):
        super().__init__()
        # Top Menu
        self.setMaximumHeight(50)
        self.setMinimumHeight(50)

        self.top_space = QSpacerItem(1, 1, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.btn_connect = QPushButton()
        self.btn_connect.setFixedSize(45, 45)
        self.btn_connect.setIcon(QIcon('src/assets/icons/connect.svg'))

        self.btn_disconnect = QPushButton()
        self.btn_disconnect.setFixedSize(45, 45)
        self.btn_disconnect.setIcon(QIcon('src/assets/icons/disconnect.svg'))

        self.content_top_layout = QHBoxLayout(self)
        self.content_top_layout.setContentsMargins(10, 0, 10, 0)
        self.content_top_layout.addWidget(self.btn_connect)
        self.content_top_layout.addWidget(self.btn_disconnect)
        self.content_top_layout.addItem(self.top_space)
