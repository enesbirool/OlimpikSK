from PyQt5.QtWidgets import QWidget
from PAGES.idcard_python import Ui_Form

class IdCardPage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.photo=""
        self.ui.setupUi(self)
        self.ui.kaydetybutton.clicked.connect(self.kaydet)

    def kaydet(self):
        print(self.photo)

