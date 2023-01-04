from ipaddress import ip_address

from PySide6.QtWidgets import QInputDialog, QLineEdit, QMessageBox


def connect_new_device(self):
    ip, ok = QInputDialog.getText(self,
                                  'Connect new device',
                                  'Type IP address',
                                  QLineEdit.EchoMode.Normal,
                                  'Please follow the format 0.0.0.0')

    if ok:
        try:
            ip_address(ip)
            port, ok = QInputDialog.getText(self,
                                            'Connect new device',
                                            'Type PORT',
                                            QLineEdit.EchoMode.Normal,
                                            'Only numbers')
            if ok:
                if str(port).isdigit():
                    device_ip_address = f'{ip}:{port}'
                    print(device_ip_address)
                else:
                    raise ValueError

        except ValueError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText(f"It's seems you entered a invalid IP or PORT")
            msg.setWindowTitle("SKTQA says")
            msg.exec()
