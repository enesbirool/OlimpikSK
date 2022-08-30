from PyQt5.QtWidgets import QWidget
from PAGES.app_info_python import Ui_Form

class AppInfoPage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)