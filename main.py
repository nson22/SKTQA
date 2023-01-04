import sys

from PySide6.QtWidgets import QApplication

from src.model.adb.adb_get_devices import get_device_ids
from src.views.layout_main import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_windows = MainWindow()
    main_windows.setMinimumSize(1280, 720)
    main_windows.setWindowTitle('SKTQA')
    main_windows.show()
    sys.exit(app.exec())
