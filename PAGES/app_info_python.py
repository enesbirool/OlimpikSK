from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 318)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/assets/martialarts_g.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Lisans Sözleşmesi"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">MXSoftware SON KULLANICI LİSANS SÖZLEŞMESİ </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1110SKLS01 </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Önemli: Bu lisans sözleşmesinde belirtilen hakları ve yükümlülükleri dikkatle okuyunuz. Kurulum esnasında bu şartları kabul edip etmediğiniz size sorulacaktır. Eğer kabul etmiyorsanız yazılım bilgisayarınıza yüklenmeyecektir. Programı bilgisayarınıza yüklemeniz, sözleşme şartlarını kabul ettiğinizi gösterir.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"> Bu sözleşme MXSoftware Yazılımı için (YAZILIM), MXSoftware ile SON KULLANICI (gerçek veya tüzel) arasında yapılan yasal bir sözleşmedir. YAZILIM\'ı yüklemeniz bu sözleşmenin hükümlerini kabul ettiğiniz anlamına gelir. Sözleşmeyi kabul etmediğiniz taktirde YAZILIM\'ı yükleyemez ve kullanamazsınız. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">I- SON KULLANICI\'NIN HAK VE YÜKÜMLÜLÜKLERİ: </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1. SON KULLANICI, YAZILIM için gerekli olan minimum sistem gereksinimlerini (benioku.txt belgesinde tanımlanmıştır.) karşılamakla yükümlüdür. YAZILIM\'ın çalışması için gerekli olan alt yapı hizmetlerini (Örnek: İnternet, yazarkasa sistemi veya donanım ürünlerinin tamamı yazılımı kullanacak firmaya aittir) kullanmayı kabul, taahhüt ve beyan eder. SON KULLANICI, yukarıda yazılı hükme aykırı davranması sebebi ile sözleşme konusu üründe meydana gelecek hasar ve ziyanlardan dolayı iş bu sözleşmenin bend III- 1.b, 1.c madde hükümlerinden yararlanma hakkının ortadan kalkacağını bildiğini beyan ve kabul eder. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2. SON KULLANICI, YAZILIM\'ı sadece tek bir bilgisayara veya ağ ortamındaki bilgisayarlara yükleyeceğini ve yalnızca bu ortamlarda kullanacağını, herhangi bir araçla ve herhangi bir şekilde sürekli veya geçici olarak başka bir ortama aktarmayacağını kabul, taahhüt ve beyan eder. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">3. SON KULLANICI; YAZILIM, çok kullanıcılı sistemi destekliyor ise ağda birden fazla bilgisayara kurup çalıştırılabileceğini, ağdaki her bir bilgisayar için lisans alması gerektiği hususunu ve bir YAZILIM lisansının paylaşılamayacağını ve YAZILIM\'ın değişik bilgisayarlarda aynı anda kullanılamayacağını bildiğini beyan ve kabul eder. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">4. YAZILIM, çok kullanıcılı kullanılıyor ise; SON KULLANICI, çalıştırılabilecek maksimum programı lisans alırken belirtilen, client sayısı kadar diğer bilgisayarlara kurma hakkına haizdir. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">5. SON KULLANICI, demo sürümünü, MXSoftware\'un belirlediği kayıt adedi ve süresince kullanacağını, her ne sebeple olursa olsun, ticari veya mesleki amaçlarla veya diğer kar getirici sebeplerle kullanmayacağını kabul, taahhüt ve beyan eder.</span></p></body></html>"))
        self.label.setText(_translate("Form", "copyright © MXSoftware 2022 tüm hakları saklıdır"))

