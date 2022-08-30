from PyQt5.QtWidgets import QApplication
from PAGES.main_page import MainPage
from qt_material import apply_stylesheet

app=QApplication([])
window=MainPage()
window.show()
extra = {'density_scale': '-2',}
apply_stylesheet(app, 'default', invert_secondary=False, extra=extra)
app.exec_()
