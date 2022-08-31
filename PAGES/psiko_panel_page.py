import os

import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PAGES.psiko_panel_python import Ui_Form
from PAGES.psiko_ekle import PsikoEkle
import sqlite3 as sql

from assets.comments import close_window_header, psiko_export_file


class PsikoPanelPage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.PsikoEkle=PsikoEkle()
        self.tc=""
        self.ui.psiko_add_button.clicked.connect(self.psikoEklePage)
        self.doldur()
        self.ui.sayfa_yenile_button.clicked.connect(self.doldur)
        self.ui.tableWidget.doubleClicked.connect(self.item)
        self.ui.excel_aktar_button.clicked.connect(self.exportToExcelPsiko)

    def item(self):
        try:
            id=self.ui.tableWidget.item(self.ui.tableWidget.currentRow(),0).text()
            reply = QMessageBox.question(self, "İnfo", "Psiko silmek İstediğinize emin misiniz?",
                                         QMessageBox.Close | QMessageBox.Ok|QMessageBox.Open)
            if reply == QMessageBox.Ok:
                self.conn = sql.connect("./db/mxsoftware.db")
                self.c = self.conn.cursor()
                self.c.execute("DELETE FROM psiko WHERE Id=?", (id,))
                self.conn.commit()
                self.conn.close()
                QMessageBox.question(self, 'İnfo Page', "Seçili Olan Psiko Bilgisi Silindi", QMessageBox.Ok)
                self.doldur()
            if reply == QMessageBox.Open:
                self.PsikoEkle.show()
                self.PsikoEkle.ui.ekle_button.hide()
                tarih = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 4).text()
                boy = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 5).text()
                kilo = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 6).text()
                denge = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 7).text()
                uzunat = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 8).text()
                dikeysic = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 9).text()
                esneklik = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 10).text()
                kisametre = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(),11).text()
                uzunmetre = self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 12).text()
                self.PsikoEkle.setWindowTitle("Piskomotor Bilgileri")
                self.PsikoEkle.ui.tarih_edit.setText(tarih)
                self.PsikoEkle.ui.boy_edit.setText(boy)
                self.PsikoEkle.ui.kilo_edit.setText(kilo)
                self.PsikoEkle.ui.denge_edit.setText(denge)
                self.PsikoEkle.ui.uzun_at_edit.setText(uzunat)
                self.PsikoEkle.ui.dikey_sic_edit.setText(dikeysic)
                self.PsikoEkle.ui.esneklik_edit.setText(esneklik)
                self.PsikoEkle.ui.kisametre_edit.setText(kisametre)
                self.PsikoEkle.ui.uzun_metre_edit.setText(uzunmetre)
                self.readonly(True)

            else:
                pass
        except:
            pass
    def readonly(self,bool):
        self.PsikoEkle.ui.tarih_edit.setReadOnly(bool)
        self.PsikoEkle.ui.boy_edit.setReadOnly(bool)
        self.PsikoEkle.ui.kilo_edit.setReadOnly(bool)
        self.PsikoEkle.ui.denge_edit.setReadOnly(bool)
        self.PsikoEkle.ui.uzun_at_edit.setReadOnly(bool)
        self.PsikoEkle.ui.dikey_sic_edit.setReadOnly(bool)
        self.PsikoEkle.ui.esneklik_edit.setReadOnly(bool)
        self.PsikoEkle.ui.kisametre_edit.setReadOnly(bool)
        self.PsikoEkle.ui.uzun_metre_edit.setReadOnly(bool)
    def psikoEklePage(self):
        self.PsikoEkle.show()
        self.readonly(False)
        self.PsikoEkle.tc = self.tc
        self.PsikoEkle.ui.ekle_button.show()
        self.PsikoEkle.setWindowTitle("Piskomotor Ekle")
        self.PsikoEkle.temizle()

    def doldur(self):
        self.ui.tableWidget.setColumnCount(13)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ('Id','TC', 'Ad', 'Soyad', 'Tarih', 'Boy', 'Kilo', 'Denge', 'Uzun Atlama', 'Dikey Sıçrama', 'Esneklik', '30 Metre', '100 Metre'))
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        db = sql.connect('./db/mxsoftware.db')
        cur = db.cursor()
        cur.execute("SELECT Id,tc,isim,soyad,tarih,boy,kilo,denge,uzun_atlama,dikey_sicrama,esneklik,kisa_metre,uzun_metre FROM psiko WHERE tc=?",(self.tc,))
        rows = cur.fetchall()
        self.ui.tableWidget.setRowCount(len(rows))

        for satirIndeks, satirVeri in enumerate(rows):
            for sutunIndeks, sutunVeri in enumerate(satirVeri):
                self.ui.tableWidget.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))
        db.close()
    def exportToExcelPsiko(self):
        try:
            columnHeaders = []
            for j in range(self.ui.tableWidget.model().columnCount()):
                columnHeaders.append(self.ui.tableWidget.horizontalHeaderItem(j).text())
            df = pd.DataFrame(columns=columnHeaders)
            for row in range(self.ui.tableWidget.rowCount()):
                for col in range(self.ui.tableWidget.columnCount()):
                    df.at[row, columnHeaders[col]] = self.ui.tableWidget.item(row, col).text()
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop/')
            df.to_excel(desktop+self.tc+psiko_export_file, index=False)
        except Exception as error:
            columnHeaders = []
            for j in range(self.ui.tableWidget.model().columnCount()):
                columnHeaders.append(self.ui.tableWidget.horizontalHeaderItem(j).text())
            df = pd.DataFrame(columns=columnHeaders)
            for row in range(self.ui.tableWidget.rowCount()):
                for col in range(self.ui.tableWidget.columnCount()):
                    df.at[row, columnHeaders[col]] = self.ui.tableWidget.item(row, col).text()
            df.to_excel(psiko_export_file+self.tc , index=False)
            ProjectFolder = os.getcwd() + "/"+self.tc + psiko_export_file
            reply = QMessageBox.question(self, close_window_header, "Open a Tıklayarak Excel Çıktısını Görebilirsiniz",
                                         QMessageBox.Close | QMessageBox.Open)
            if reply == QMessageBox.Open:
                os.system(ProjectFolder)
            else:
                pass