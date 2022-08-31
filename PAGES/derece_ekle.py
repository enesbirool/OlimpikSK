from PyQt5.QtWidgets import QWidget, QMessageBox
from PAGES.derece_ekle_page_python import Ui_Form
import sqlite3 as sql
class DereceEkle(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.tc=""
        self.ui.ekle_button.clicked.connect(self.eklendi)

    def eklendi(self):
        self.isim=""
        self.soyad=""
        self.brans=self.ui.brans_combobox.currentText()
        try:
            self.conn = sql.connect("./db/mxsoftware.db")
            self.c = self.conn.cursor()
            self.c.execute("SELECT * FROM ogrenciler WHERE tc = ?", (self.tc,))
            self.conn.commit()
            veri = self.c.fetchall()
            for i in veri:
                self.isim=i[1]
                self.soyad=i[2]
            self.c.execute("INSERT INTO dereceler \
                                 (tc,isim,soyad,brans,turnuva_adi,turnuva_yeri,derece) \
                                  VALUES (?,?,?,?,?,?,?)",(self.tc, self.isim, self.soyad,self.brans , self.ui.turnuva_adi_edit.text(), self.ui.turnuvail_edit.text(),self.ui.derece_edit.text()))
            self.conn.commit()
            self.conn.close()
            self.eklendi_info()
            self.temizle()
        except:
            pass

    def eklendi_info(self):
        QMessageBox.question(self, 'İnfo Page', "Derece Eklendi",QMessageBox.Ok)

    def temizle(self):
        self.ui.turnuva_adi_edit.clear()
        self.ui.turnuvail_edit.clear()
        self.ui.derece_edit.clear()