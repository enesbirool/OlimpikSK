from PyQt5.QtWidgets import QMessageBox, QWidget
from PAGES.aidat_add_python import Ui_Form
import sqlite3 as sql
from assets.comments import *

class AidatAdd(QWidget):
    def __init__(self):

        super().__init__()
        self.isimler=[]

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_info)
        self.ui.add_aidat_button.clicked.connect(self.add_aidat)
        self.ui.exit_button.clicked.connect(lambda x:self.close())
        
    def open_info(self):
        QMessageBox.question(self, 'İnfo Page', info_page_comment,
			QMessageBox.Ok| QMessageBox.Retry)
        if QMessageBox.Retry:
            self.combo_ekle()
            QMessageBox.question(self, 'İnfo Page', "Güncellendi...",
			QMessageBox.Ok)
    def eklendi_info(self):
        QMessageBox.question(self, 'İnfo Page', "Aidat Eklendi",
			QMessageBox.Ok)
    def combo_ekle(self):     
        db = sql.connect('./db/mxsoftware.db')
        cur = db.cursor()
        selectquery = "SELECT * FROM ogrenciler"
        cur.execute(selectquery)
        rows=cur.fetchall()
        self.ui.aidat_comboBox.clear()
        self.isimler.clear()
        for isim in rows:
            self.isimler.append(str(isim[1]+" "+isim[2]))
        self.ui.aidat_comboBox.addItems(self.isimler)
    
    def add_aidat(self):
        try:
            secili_kisi=self.ui.aidat_comboBox.currentText()
            ayrilmis=secili_kisi.split(" ")
            isim=ayrilmis[0]
            soyad=ayrilmis[1]
            tc=""
            ay=self.ui.ay_cmb_aidat.currentText()
            yil=self.ui.yil_cmb_aidat.currentText()
            ucret=self.ui.money_lineEdit.text()

            self.conn = sql.connect("./db/mxsoftware.db")
            self.c = self.conn.cursor() 
            self.c.execute("SELECT * FROM ogrenciler WHERE isim = ? AND soyad = ?",(isim,soyad))
            self.conn.commit()
            veri = self.c.fetchall()
            for i in veri:
                tc=i[0]
            self.c.execute("INSERT INTO aidatlar (tc,isim,soyad,ay,yıl,ucret) VALUES (?,?,?,?,?,?)",(tc,isim,soyad,ay,yil,ucret))
            self.conn.commit()
            self.conn.close()
            self.eklendi_info()
            self.close()
        except Exception:
            QMessageBox.question(self, 'İnfo Page', "Aidat Eklenmedi... Lütfen Öğrenci seçin...",
			QMessageBox.Ok)


        
        
        
        



        