from PyQt5.QtWidgets import QWidget, QMessageBox
from PAGES.psiko_ekle_python import Ui_Form
import sqlite3 as sql
class PsikoEkle(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.tc=""
        self.ui.ekle_button.clicked.connect(self.eklendi)
    def eklendi(self):
        self.tarih=self.ui.tarih_edit.text()
        self.boy=self.ui.boy_edit.text()
        self.kilo=self.ui.kilo_edit.text()
        self.denge=self.ui.denge_edit.text()
        self.uzun_atlama=self.ui.uzun_at_edit.text()
        self.dikey_sicrama=self.ui.dikey_sic_edit.text()
        self.esneklik=self.ui.esneklik_edit.text()
        self.kisa_metre=self.ui.kisametre_edit.text()
        self.uzun_metre=self.ui.uzun_metre_edit.text()

        try:
            self.conn = sql.connect("./db/mxsoftware.db")
            self.c = self.conn.cursor()
            self.c.execute("SELECT * FROM ogrenciler WHERE tc = ?", (self.tc,))
            self.conn.commit()
            veri = self.c.fetchall()
            for i in veri:
                self.isim=i[1]
                self.soyad=i[2]
            self.c.execute("INSERT INTO psiko \
                                 (tc,isim,soyad,tarih,boy,kilo,denge,uzun_atlama,dikey_sicrama,esneklik,kisa_metre,uzun_metre) \
                                  VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(self.tc, self.isim, self.soyad,self.tarih ,self.boy,self.kilo,self.denge,self.uzun_atlama,self.dikey_sicrama,self.esneklik,self.kisa_metre,self.uzun_metre))
            self.conn.commit()
            self.conn.close()
            self.eklendi_info()
            self.temizle()
        except:
            pass

    def eklendi_info(self):
        QMessageBox.question(self, 'İnfo Page', "Psiko Eklendi",QMessageBox.Ok)

    def temizle(self):
        self.ui.tarih_edit.clear()
        self.ui.boy_edit.clear()
        self.ui.kilo_edit.clear()
        self.ui.denge_edit.clear()
        self.ui.uzun_at_edit.clear()
        self.ui.dikey_sic_edit.clear()
        self.ui.esneklik_edit.clear()
        self.ui.kisametre_edit.clear()
        self.ui.uzun_metre_edit.clear()