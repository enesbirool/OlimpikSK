import os

import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox

from PAGES.derece_paneli_python import Ui_Form
from PAGES.derece_ekle import DereceEkle
import sqlite3 as sql
from assets.comments import close_window_header, dereceler_export_file


class DerecePanel(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.derece_ekle=DereceEkle()
        self.tc=""
        self.doldur()
        self.ui.derece_add_button.clicked.connect(self.open_derece_ekle)
        self.ui.sayfa_yenile_button.clicked.connect(self.doldur)
        self.ui.tableWidget.itemDoubleClicked.connect(self.item)
        self.ui.excel_aktar_button.clicked.connect(self.exportToExcelDerece)

    def item(self):
        try:
            id=self.ui.tableWidget.item(self.ui.tableWidget.currentRow(),0).text()
            reply = QMessageBox.question(self, "İnfo", "Dereceyi silmek İstediğinize emin misiniz?",
                                         QMessageBox.Close | QMessageBox.Ok)
            if reply == QMessageBox.Ok:
                self.conn = sql.connect("./db/mxsoftware.db")
                self.c = self.conn.cursor()
                self.c.execute("DELETE FROM dereceler WHERE Id=?", (id,))
                self.conn.commit()
                self.conn.close()
                QMessageBox.question(self, 'İnfo Page', "Seçili Olan Maç Bilgisi Silindi", QMessageBox.Ok)
                self.doldur()
            else:
                pass
        except:
            pass
    def doldur(self):
        self.ui.tableWidget.setColumnCount(8)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ('Id','TC', 'Ad', 'Soyad', 'Branş', 'T.Adı', 'T.İli', 'Derece'))
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        db = sql.connect('./db/mxsoftware.db')
        cur = db.cursor()
        cur.execute("SELECT Id,tc,isim,soyad ,brans, turnuva_adi,turnuva_yeri,derece FROM dereceler WHERE tc=?",(self.tc,))
        rows = cur.fetchall()
        self.ui.tableWidget.setRowCount(len(rows))
        for satirIndeks, satirVeri in enumerate(rows):
            for sutunIndeks, sutunVeri in enumerate(satirVeri):
                self.ui.tableWidget.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))
        db.close()
    def open_derece_ekle(self):
        self.derece_ekle.show()
        self.derece_ekle.tc=self.tc

    def exportToExcelDerece(self):
        try:
            columnHeaders = []
            for j in range(self.ui.tableWidget.model().columnCount()):
                columnHeaders.append(self.ui.tableWidget.horizontalHeaderItem(j).text())
            df = pd.DataFrame(columns=columnHeaders)
            for row in range(self.ui.tableWidget.rowCount()):
                for col in range(self.ui.tableWidget.columnCount()):
                    df.at[row, columnHeaders[col]] = self.ui.tableWidget.item(row, col).text()
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop/')
            df.to_excel(desktop+self.tc+dereceler_export_file, index=False)
        except Exception as error:
            columnHeaders = []
            for j in range(self.ui.tableWidget.model().columnCount()):
                columnHeaders.append(self.ui.tableWidget.horizontalHeaderItem(j).text())
            df = pd.DataFrame(columns=columnHeaders)
            for row in range(self.ui.tableWidget.rowCount()):
                for col in range(self.ui.tableWidget.columnCount()):
                    df.at[row, columnHeaders[col]] = self.ui.tableWidget.item(row, col).text()
            df.to_excel(dereceler_export_file+self.tc , index=False)
            ProjectFolder = os.getcwd() + "/"+self.tc + dereceler_export_file
            reply = QMessageBox.question(self, close_window_header, "Open a Tıklayarak Excel Çıktısını Görebilirsiniz",
                                         QMessageBox.Close | QMessageBox.Open)
            if reply == QMessageBox.Open:
                os.system(ProjectFolder)
            else:
                pass