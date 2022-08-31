import os
import shutil
import sqlite3 as sql
import datetime
from datetime import date
import pandas as pd
from PIL import Image, ImageFont, ImageDraw
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QTableWidgetItem, QMainWindow, QMessageBox, QFileDialog
from PAGES.mail_page import MailPage
from PAGES.aidat_add import AidatAdd
from PAGES.app_info import AppInfoPage
from PAGES.connections import main as sqlconnection
from PAGES.create_table import main as createTable
from PAGES.main_python import Ui_MainWindow
from PAGES.profile_page import ProfilePage
from assets.comments import *


class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        sqlconnection()
        createTable()
        self.btnListeleClick()
        self.btnListele2Click()
        self.info_page = AppInfoPage()
        self.aidat_add_page = AidatAdd()
        self.profile_page = ProfilePage()
        self.mail_page=MailPage()
        self.ui.actionlicence_sozlesme.triggered.connect(self.open_app_info_page)       
        self.ui.ogr_export_button.hide()
        self.ui.aidat_export_button.hide()
        self.ui.actionExport_Data.toggled[bool].connect(self.btnstate)    
        self.ui.actionBilgi_Boloncuklar_2.toggled[bool].connect(self.BoloncukState)
        self.ui.ogrenciler_tableWidget.itemSelectionChanged.connect(self.ListOnClick)
        self.ui.ogr_export_button.clicked.connect(self.exportToExcelOgr)
        self.ui.aidat_export_button.clicked.connect(self.exportToExcelAidat)  
        self.ui.register_button.clicked.connect(self.student_add)
        self.ui.more_detail_button.clicked.connect(self.open_detail)
        self.ui.serach_all_pushButton.clicked.connect(self.btnListeleClick)
        self.ui.serach_all_pushButton.clicked.connect(self.btnListele2Click)
        self.ui.search_button.clicked.connect(self.btnAra)
        self.ui.update_button.clicked.connect(self.btnUpdate)
        self.ui.aidat_add_button.clicked.connect(self.open_aidat_page)
        self.ui.delete_button.clicked.connect(self.btnSilClick)
        self.ui.actionSave_Database.triggered.connect(self.export_data)
        self.ui.actionLoad_Database_2.triggered.connect(self.load_database)
        self.ui.actionToplu_Mail_G_nder.triggered.connect(self.open_mail_page)
        self.ui.aidatlar_tableWidget.doubleClicked.connect(self.aidat_sil)
        

    ##################### SUPPORTS #############################################
    def open_mail_page(self):
        self.mail_page.show()
    def bilgi_boloncuklari(self):

        self.ui.more_detail_button.setToolTip("Öğrenciler Hakkında Ayrıntılı Bilgi Penceresi Açar...")
        self.ui.serach_all_pushButton.setToolTip("Liste yenileme veya bütün bilgileri getirir...")
        self.ui.search_button.setToolTip("Öğrenci Aramanızı sağlar...")
        self.ui.update_button.setToolTip("Öğrenci Güncellemenizi sağlar...")
        self.ui.aidat_add_button.setToolTip("Öğrenci Aidat Eklemenizi sağlar...")
        self.ui.delete_button.setToolTip("Öğrenci Silmenizi sağlar...")
        self.ui.register_button.setToolTip("Öğrenci Eklemenizi sağlar...")

    def btnstate(self, state):
        if (state == True):
            self.ui.ogr_export_button.show()
            self.ui.aidat_export_button.show()
            self.ui.statusBar.showMessage(export_buttons_showed, 5000)
        else:
            self.ui.ogr_export_button.hide()
            self.ui.aidat_export_button.hide()
            self.ui.statusBar.showMessage(export_buttons_hide, 5000)
    def BoloncukState(self,state):
        if (state == True):
            self.bilgi_boloncuklari()
            self.ui.statusBar.showMessage("Bilgi Boloncukları Açıldı", 5000)
        else:
            self.ui.statusBar.showMessage("Bilgi Boloncukları Kapatıldı", 5000)
            self.ui.more_detail_button.setToolTip("")
            self.ui.serach_all_pushButton.setToolTip("")
            self.ui.search_button.setToolTip("")
            self.ui.update_button.setToolTip("")
            self.ui.aidat_add_button.setToolTip("")
            self.ui.delete_button.setToolTip("")
            self.ui.register_button.setToolTip("")
    def btnTemizle(self):
        self.ui.ogr_tc_edit.clear()
        self.ui.ogr_name_edit.clear()
        self.ui.ogr_surname_lineEdit.clear()
        self.ui.ogr_number_edit.clear()
        self.ui.register_dateEdit.setDate(datetime.date.today())
        self.ui.register_finish_dateEdit.setDate(datetime.date.today())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, close_window_header, close_window_event_commment,
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            self.ui.statusBar.showMessage(close_window_cancel, 5000)

    def open_app_info_page(self):
        self.info_page.show()
    def detail_ui_clear(self):
        self.profile_page.ui.tc_edit.clear()
        self.profile_page.ui.isim_edit.clear()
        self.profile_page.ui.soyad_edit.clear()
        self.profile_page.ui.phone_edit.clear()
        self.profile_page.ui.register_edit.clear()
        self.profile_page.ui.register_finish_edit.clear()
        self.profile_page.ui.veli_name_edit.clear()
        self.profile_page.ui.veli_phone_edit.clear()
        self.profile_page.ui.lisans_no_edit.clear()
        self.profile_page.ui.photo_label.clear()
        self.profile_page.ui.date_of_birth_edit.clear()
        self.profile_page.ui.hes_code_edit.clear()
        self.profile_page.ui.kusak_edit.clear()
        self.profile_page.ui.mail_edit.clear()
        self.profile_page.ui.veli_name_edit.clear()
    def get_details(self):

        try:
            pixmap = QtGui.QPixmap()

            tc=self.ui.ogr_tc_edit.text()
            self.conn = sql.connect("./db/mxsoftware.db")
            self.c = self.conn.cursor()
            self.c.execute("SELECT * FROM details WHERE tc=? OR (tc=? AND tc=?) OR tc=? ",
                           (tc, tc, tc, tc))
            self.conn.commit()
            for i in self.c:
                self.profile_page.ui.veli_name_edit.setText(i[3])
                self.profile_page.ui.date_of_birth_edit.setText(i[1])
                self.profile_page.ui.kusak_edit.setText(i[2])
                self.profile_page.ui.veli_phone_edit.setText(i[4])
                self.profile_page.ui.lisans_no_edit.setText(i[5])
                self.profile_page.ui.hes_code_edit.setText(i[7])
                self.profile_page.ui.mail_edit.setText(i[8])
                pixmap.loadFromData(i[6], 'png')
                self.profile_page.ui.photo_label.clear()
                self.profile_page.ui.photo_label.setPixmap(pixmap)
                pixmap.save(self.profile_page.ui.tc_edit.text()+".png")

        except Exception as e:
            print("Hata")
    def open_detail(self):
        self.profile_page.detail_ui_clear()
        tc = self.ui.ogr_tc_edit.text()
        isim = self.ui.ogr_name_edit.text().upper()
        soyad = self.ui.ogr_surname_lineEdit.text().upper()
        numara = self.ui.ogr_number_edit.text()
        brans = self.ui.brans_combox.currentText()
        kayit = self.ui.register_dateEdit.text()
        bitis = self.ui.register_finish_dateEdit.text()
        if len(tc) != 0:
            self.profile_page.show()
            self.profile_page.ui.tc_edit.clear()
            self.profile_page.ui.isim_edit.clear()
            self.profile_page.ui.soyad_edit.clear()
            self.profile_page.ui.phone_edit.clear()
            self.profile_page.ui.register_edit.clear()
            self.profile_page.ui.register_finish_edit.clear()
            self.profile_page.ui.veli_name_edit.clear()
            self.profile_page.ui.veli_phone_edit.clear()
            self.profile_page.ui.lisans_no_edit.clear()
            self.profile_page.ui.photo_label.clear()
            self.profile_page.ui.date_of_birth_edit.clear()
            self.profile_page.ui.hes_code_edit.clear()
            self.profile_page.ui.kusak_edit.clear()
            self.profile_page.ui.mail_edit.clear()
            self.profile_page.ui.veli_name_edit.clear()
            self.profile_page.ui.tc_edit.setText(tc)
            self.profile_page.ui.isim_edit.setText(isim)
            self.profile_page.ui.soyad_edit.setText(soyad)
            self.profile_page.ui.phone_edit.setText(numara)
            self.profile_page.ui.brans_comboBox.setCurrentText(brans)
            self.profile_page.ui.register_edit.setText(kayit)
            self.profile_page.ui.register_finish_edit.setText(bitis)
            self.profile_page.name=isim
            self.profile_page.surname=soyad
            self.profile_page.numara=numara
            self.profile_page.id=tc
            self.profile_page.kayit=kayit
            self.get_details()

        else:
            self.ui.statusBar.showMessage(select_student_for_detail, 5000)


    def open_aidat_page(self):
        self.aidat_add_page.show()
        self.aidat_add_page.combo_ekle()


    ################################# CRUD OPERATIONS #############################

    def btnListeleClick(self):
        self.btnTemizle()
        self.ui.register_dateEdit.setDate(QDate(2020, 6, 10))
        self.ui.register_finish_dateEdit.setDate(QDate(2020, 6, 10))
        self.ui.ogrenciler_tableWidget.clear()
        self.ui.ogrenciler_tableWidget.setColumnCount(7)
        self.ui.register_dateEdit.setDate(datetime.date.today())
        self.ui.register_finish_dateEdit.setDate(datetime.date.today())
        self.ui.ogrenciler_tableWidget.setHorizontalHeaderLabels(
            ('TC', 'Ad', 'Soyad', 'Numara', 'Brans', 'Kayit', 'Bitis'))
        self.ui.ogrenciler_tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        db = sql.connect('./db/mxsoftware.db')
        cur = db.cursor()
        selectquery = "SELECT tc,isim,soyad,telefon,brans,kayit_tarihi,bitis_tarihi FROM ogrenciler"
        cur.execute(selectquery)
        rows = cur.fetchall()
        self.ui.ogrenciler_tableWidget.setRowCount(len(rows))

        for satirIndeks, satirVeri in enumerate(rows):
            for sutunIndeks, sutunVeri in enumerate(satirVeri):
                self.ui.ogrenciler_tableWidget.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))
        db.close()
    def aidat_sil(self):
        try:
            self.id=self.ui.aidatlar_tableWidget.item(self.ui.aidatlar_tableWidget.currentRow(),0).text()
            self.tc = self.ui.aidatlar_tableWidget.item(self.ui.aidatlar_tableWidget.currentRow(), 1).text()
            self.tarih=self.ui.aidatlar_tableWidget.item(self.ui.aidatlar_tableWidget.currentRow(),4).text()
            self.ucret = self.ui.aidatlar_tableWidget.item(self.ui.aidatlar_tableWidget.currentRow(), 6).text()
            self.ay = self.ui.aidatlar_tableWidget.item(self.ui.aidatlar_tableWidget.currentRow(), 4).text()
            self.yil = self.ui.aidatlar_tableWidget.item(self.ui.aidatlar_tableWidget.currentRow(), 5).text()
            self.name = self.ui.aidatlar_tableWidget.item(self.ui.aidatlar_tableWidget.currentRow(), 2).text()
            self.surname = self.ui.aidatlar_tableWidget.item(self.ui.aidatlar_tableWidget.currentRow(), 3).text()
            reply = QMessageBox.question(self, "İnfo", "Dereceyi silmek İstediğinize emin misiniz?\n\n "
                                                       "Save Butonuna Tıklayarak Fatura oluşturabilirsiniz...",
                                         QMessageBox.Save | QMessageBox.Ok|QMessageBox.Cancel)
            if reply == QMessageBox.Ok:
                self.conn = sql.connect("./db/mxsoftware.db")
                self.c = self.conn.cursor()
                self.c.execute("DELETE FROM aidatlar WHERE Id=?", (self.id,))
                self.conn.commit()
                self.conn.close()
                self.btnListele2Click()
            elif reply == QMessageBox.Save:
                self.generate_card().show()

                try:
                    self.generate_card().save(os.path.join(os.path.join(os.environ['USERPROFILE']),
                                                           'Desktop/') +self.tc+self.tarih+".png")
                    print(self.id)
                    QMessageBox.question(self, 'İnfo Page', "Fatura Otomatik olarak masaüstüne kayıt edildi...",
                                         QMessageBox.Ok)
                except:
                    pass
            else:
                pass
        except:
            pass
    def generate_card(self):
        template = Image.open("fatra.png")
        fontsize = 27
        font = ImageFont.truetype("FontsFree-Net-arial-bold.ttf", fontsize)
        fontsize2 = 23
        font2 = ImageFont.truetype("FontsFree-Net-arial-bold.ttf", fontsize2)
        id = ImageDraw.Draw(template)
        id.text((350, 615),self.id , fill="black", font=font)

        aidat_ucret = ImageDraw.Draw(template)
        aidat_ucret.text((1190, 855), self.ucret+" TL", fill="black", font=font)

        total = ImageDraw.Draw(template)
        total.text((1190, 1555), self.ucret + " TL", fill="black", font=font)

        tarih = ImageDraw.Draw(template)
        tarih.text((150, 855), self.ay+" "+self.yil, fill="black", font=font)

        aciklama = ImageDraw.Draw(template)
        aciklama.text((550, 855), self.name+" "+self.surname+" İsimli Sporcunun Aidat Ücreti", fill="black", font=font2)
        today = date.today()
        fatra_date=today.strftime("%d %B, %Y")

        fatra_Date = ImageDraw.Draw(template)
        fatra_Date.text((1130, 620), fatra_date, fill="black", font=font2)

        return template
    def btnListele2Click(self):
        self.btnTemizle()
        self.ui.aidatlar_tableWidget.clear()
        self.ui.aidatlar_tableWidget.setColumnCount(7)
        self.ui.aidatlar_tableWidget.setHorizontalHeaderLabels(('Id','TC', 'Ad', 'Soyad', 'Ay', 'Yıl', 'Ücret'))
        self.ui.aidatlar_tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        db = sql.connect('./db/mxsoftware.db')
        cur = db.cursor()
        selectquery = """SELECT *
FROM aidatlar
ORDER BY
  yıl DESC,
  (CASE ay
    WHEN 'OCAK' THEN 1
    WHEN 'ŞUBAT' THEN 2
    WHEN 'MART' THEN 3
    WHEN 'NİSAN' THEN 4
    WHEN 'MAYIS' THEN 5
    WHEN 'HAZİRAN' THEN 6
    WHEN 'TEMMUZ' THEN 7
    WHEN 'AĞUSTOS' THEN 8
    WHEN 'EYLÜL' THEN 9
    WHEN 'EKİM' THEN 10
    WHEN 'KASIM' THEN 11
    WHEN 'ARALIK' THEN 12
  END) DESC,
  ay DESC ;"""
        cur.execute(selectquery)
        rows = cur.fetchall()
        self.ui.aidatlar_tableWidget.setRowCount(len(rows))
        for satirIndeks, satirVeri in enumerate(rows):
            for sutunIndeks, sutunVeri in enumerate(satirVeri):
                self.ui.aidatlar_tableWidget.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))
        db.close()

    def ListOnClick(self):
        try:
            self.ui.ogr_tc_edit.setText(
                self.ui.ogrenciler_tableWidget.item(self.ui.ogrenciler_tableWidget.currentRow(), 0).text())
            self.ui.ogr_name_edit.setText(
                self.ui.ogrenciler_tableWidget.item(self.ui.ogrenciler_tableWidget.currentRow(), 1).text())
            self.ui.ogr_surname_lineEdit.setText(
                self.ui.ogrenciler_tableWidget.item(self.ui.ogrenciler_tableWidget.currentRow(), 2).text())
            self.ui.ogr_number_edit.setText(
                self.ui.ogrenciler_tableWidget.item(self.ui.ogrenciler_tableWidget.currentRow(), 3).text())
            self.ui.brans_combox.setCurrentText(
                self.ui.ogrenciler_tableWidget.item(self.ui.ogrenciler_tableWidget.currentRow(), 4).text())
            register_date=self.ui.ogrenciler_tableWidget.item(self.ui.ogrenciler_tableWidget.currentRow(), 5).text()
            register_date.split(".")
            gun=register_date[0]+register_date[1]
            ay=register_date[3]+register_date[4]
            yil=register_date[6]+register_date[7]+register_date[8]+register_date[9]
            d = QDate(int(yil), int(ay), int(gun))
            self.ui.register_dateEdit.setDate(d)

            register_finish=self.ui.ogrenciler_tableWidget.item(self.ui.ogrenciler_tableWidget.currentRow(), 6).text()
            register_finish.split(".")
            gun_1 = register_finish[0] + register_finish[1]
            ay_1 = register_finish[3] + register_finish[4]
            yil_1 = register_finish[6] + register_finish[7] + register_finish[8] + register_finish[9]
            f = QDate(int(yil_1), int(ay_1), int(gun_1))
            self.ui.register_finish_dateEdit.setDate(f)
        except Exception as error:
            self.ui.statusBar.showMessage("Aradığınız Kişi Bulunamadı....", 6000)



    def btnUpdate(self):
        tc = self.ui.ogr_tc_edit.text()
        isim = self.ui.ogr_name_edit.text().upper()
        soyad = self.ui.ogr_surname_lineEdit.text().upper()
        numara = self.ui.ogr_number_edit.text()
        brans = self.ui.brans_combox.currentText()
        kayit = self.ui.register_dateEdit.text()
        bitis = self.ui.register_finish_dateEdit.text()
        if (len(tc) != 0):
            reply = QMessageBox.question(self, student_update_window_header, update_info_window + isim,
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                try:
                    self.conn = sql.connect("./db/mxsoftware.db")
                    self.c = self.conn.cursor()
                    self.c.execute("UPDATE ogrenciler SET  isim = ?,soyad = ?, telefon = ?, \
                brans = ?, kayit_tarihi = ?, bitis_tarihi = ? WHERE tc = ?",
                                   (isim, soyad, numara, brans, kayit, bitis, tc))
                    self.conn.commit()
                    self.c.close()
                    self.conn.close()
                    self.ui.statusBar.showMessage(isim + update_accept_student, 6000)
                except Exception:
                    print('Error', could_not_update_student)
                self.btnListeleClick()
                self.btnTemizle()
            else:
                self.ui.statusBar.showMessage(cancel_update_student, 5000)
        else:
            self.ui.statusBar.showMessage(select_student_for_update, 5000)
    def btnSilClick(self):
        id = self.ui.ogr_tc_edit.text()
        isim = self.ui.ogr_name_edit.text()
        if len(id) != 0:
            reply = QMessageBox.question(self, student_delete_window_header, delete_info_window + isim,
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                try:
                    self.conn = sql.connect("./db/mxsoftware.db")
                    self.c = self.conn.cursor()
                    self.c.execute('DELETE FROM ogrenciler WHERE tc = ?  ', (id,))
                    self.c.execute('DELETE FROM aidatlar WHERE tc = ?  ', (id,))
                    self.c.execute('DELETE FROM details WHERE tc = ?  ', (id,))
                    self.conn.commit()
                    self.c.close()
                    self.conn.close()
                    self.ui.statusBar.showMessage(isim + delete_accept_student, 6000)
                except Exception:
                    print('Error', could_not_delete_student)
                self.btnListeleClick()
                self.btnListele2Click()
                self.btnTemizle()
            else:
                self.ui.statusBar.showMessage(cancel_delete_student, 5000)
        else:
            self.ui.statusBar.showMessage(select_student_for_delete, 5000)

    def btnAra(self):
        aranan1 = self.ui.ogr_tc_edit.text()
        aranan2 = self.ui.ogr_name_edit.text().upper()
        aranan3 = self.ui.ogr_surname_lineEdit.text().upper()
        self.conn = sql.connect("./db/mxsoftware.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM ogrenciler WHERE tc=? OR (isim=? AND soyad=?) OR soyad=? ",
                       (aranan1, aranan2, aranan3, aranan3))
        self.conn.commit()
        self.ui.ogrenciler_tableWidget.clear()
        self.ui.ogrenciler_tableWidget.setHorizontalHeaderLabels(
            ('TC', 'Ad', 'Soyad', 'Numara', 'Brans', 'Kayit', 'Bitis'))
        for satirIndeks, satirVeri in enumerate(self.c):
            for sutunIndeks, sutunVeri in enumerate(satirVeri):
                self.ui.ogrenciler_tableWidget.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))
        aranan1 = self.ui.ogr_tc_edit.text()
        aranan2 = self.ui.ogr_name_edit.text().upper()
        aranan3 = self.ui.ogr_surname_lineEdit.text().upper()
        self.conn = sql.connect("./db/mxsoftware.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM aidatlar WHERE tc=? OR (isim=? AND soyad=?) OR soyad=? ",
                       (aranan1, aranan2, aranan3, aranan3))
        self.conn.commit()
        self.ui.aidatlar_tableWidget.clear()
        self.ui.aidatlar_tableWidget.setHorizontalHeaderLabels(('Id','TC', 'Ad', 'Soyad', 'Ay', 'Yıl', 'Ücret'))
        for satirIndeks, satirVeri in enumerate(self.c):
            for sutunIndeks, sutunVeri in enumerate(satirVeri):
                self.ui.aidatlar_tableWidget.setItem(satirIndeks, sutunIndeks, QTableWidgetItem(str(sutunVeri)))
        self.conn.close()

    def student_add(self):
        tc = self.ui.ogr_tc_edit.text()
        isim = self.ui.ogr_name_edit.text().upper()
        soyad = self.ui.ogr_surname_lineEdit.text().upper()
        numara = self.ui.ogr_number_edit.text()
        brans = self.ui.brans_combox.currentText()
        kayit = self.ui.register_dateEdit.text()
        bitis = self.ui.register_finish_dateEdit.text()
        if (len(tc) >10 and len(isim) != 0 and len(numara) != 0 and len(bitis) != 0):
            try:
                self.conn = sql.connect("./db/mxsoftware.db")
                self.c = self.conn.cursor()
                self.c.execute("INSERT INTO ogrenciler VALUES (?,?,?,?,?,?,?)",
                               (tc, isim, soyad, numara, brans, kayit, bitis))
                self.conn.commit()
                self.c.close()
                self.conn.close()
                self.conn = sql.connect("./db/mxsoftware.db")
                self.c = self.conn.cursor()
                self.c.execute("INSERT INTO details VALUES (?,?,?,?,?,?,?,?,?)",
                               (tc," "," "," "," "," "," "," "," "))
                self.conn.commit()
                self.c.close()
                self.ui.statusBar.showMessage(register_accept, 5000)
                self.btnTemizle()
                self.btnListeleClick()
            except Exception as error:
                self.ui.statusBar.showMessage(register_error + str(error), 5000)
        else:
            self.ui.statusBar.showMessage(ogr_can_not_be_null_error, 5000)

    ########################### EXPORT DATA ####################################
    def load_database(self):        
        try:
            self.fname=QFileDialog.getOpenFileName(self, 'Open file', 'D:/',"Select Database File (*.db)")
            source_file=self.fname[0]
            destination_folder=os.getcwd()+"/db"
            shutil.copy(source_file,destination_folder)
            QMessageBox.question(self, 'İnfo Page', "Database Yedeğiniz Programa Yüklendi Programı Kapatıp Açınız veya tüm sonuçlara tıklayarak bilgileri getirebilirsiniz... mxsoftware.db",
			QMessageBox.Ok)
            os.remove(self.fname[0])
        except Exception as error:
            print(error)
    def export_data(self):        
        try:
            source_file=os.getcwd()+"/db/mxsoftware.db"
            destination_folder=QFileDialog.getExistingDirectory(None,"Select Folder : ","C://",QFileDialog.ShowDirsOnly)
            shutil.copy(source_file,destination_folder)
            QMessageBox.question(self, 'İnfo Page', "Database Yedeğiniz Kopyalandı... mxsoftware.db",
			QMessageBox.Ok)
        except Exception as error:
            print(error)
    def exportToExcelOgr(self):
        try:
            columnHeaders = []
            for j in range(self.ui.ogrenciler_tableWidget.model().columnCount()):
                columnHeaders.append(self.ui.ogrenciler_tableWidget.horizontalHeaderItem(j).text())
            df = pd.DataFrame(columns=columnHeaders)
            for row in range(self.ui.ogrenciler_tableWidget.rowCount()):
                for col in range(self.ui.ogrenciler_tableWidget.columnCount()):
                    df.at[row, columnHeaders[col]] = self.ui.ogrenciler_tableWidget.item(row, col).text()
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop/')
            df.to_excel(desktop + ogrenciler_export_file, index=False)
            self.ui.statusBar.showMessage(ogrenciler_export_accept_status, 9000)
        except Exception as error:
            columnHeaders = []
            for j in range(self.ui.ogrenciler_tableWidget.model().columnCount()):
                columnHeaders.append(self.ui.ogrenciler_tableWidget.horizontalHeaderItem(j).text())
            df = pd.DataFrame(columns=columnHeaders)
            for row in range(self.ui.ogrenciler_tableWidget.rowCount()):
                for col in range(self.ui.ogrenciler_tableWidget.columnCount()):
                    df.at[row, columnHeaders[col]] = self.ui.ogrenciler_tableWidget.item(row, col).text()
            df.to_excel(ogrenciler_export_file, index=False)
            ProjectFolder = os.getcwd() + "/" + ogrenciler_export_file
            reply = QMessageBox.question(self, close_window_header, "Open a Tıklayarak Excel Çıktısını Görebilirsiniz",
                                         QMessageBox.Close | QMessageBox.Open)
            if reply == QMessageBox.Open:
                os.system(ProjectFolder)
            else:
                self.ui.statusBar.showMessage("İptal Edildi", 5000)
    def exportToExcelAidat(self):
        try:
            columnHeaders = []
            for j in range(self.ui.aidatlar_tableWidget.model().columnCount()):
                columnHeaders.append(self.ui.aidatlar_tableWidget.horizontalHeaderItem(j).text())
            df = pd.DataFrame(columns=columnHeaders)
            for row in range(self.ui.aidatlar_tableWidget.rowCount()):
                for col in range(self.ui.aidatlar_tableWidget.columnCount()):
                    df.at[row, columnHeaders[col]] = self.ui.aidatlar_tableWidget.item(row, col).text()
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop/')
            df.to_excel(desktop + aidatlar_export_file, index=False)
            self.ui.statusBar.showMessage(aidatlar_export_accept_status, 9000)
        except Exception as error:
            columnHeaders = []
            for j in range(self.ui.aidatlar_tableWidget.model().columnCount()):
                columnHeaders.append(self.ui.aidatlar_tableWidget.horizontalHeaderItem(j).text())
            df = pd.DataFrame(columns=columnHeaders)
            for row in range(self.ui.aidatlar_tableWidget.rowCount()):
                for col in range(self.ui.aidatlar_tableWidget.columnCount()):
                    df.at[row, columnHeaders[col]] = self.ui.aidatlar_tableWidget.item(row, col).text()

            df.to_excel(aidatlar_export_file, index=False)

            ProjectFolder=os.getcwd()+"/"+aidatlar_export_file
            reply = QMessageBox.question(self, close_window_header, "Open a Tıklayarak Excel Çıktısını Görebilirsiniz",
                                         QMessageBox.Close | QMessageBox.Open)
            if reply == QMessageBox.Open:
                os.system(ProjectFolder)
            else:
                self.ui.statusBar.showMessage("İptal Edildi", 5000)