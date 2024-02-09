from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(342, 435)
        self.software_name_label = QLabel(Dialog)
        self.software_name_label.setObjectName(u"software_name_label")
        self.software_name_label.setGeometry(QRect(30, 10, 271, 91))
        self.software_name_label.setScaledContents(True)
        self.software_name_label.setAlignment(Qt.AlignCenter)
        self.qr_contents_field = QLineEdit(Dialog)
        self.qr_contents_field.setObjectName(u"qr_contents_field")
        self.qr_contents_field.setGeometry(QRect(50, 120, 231, 20))
        self.generate_qr_btn = QPushButton(Dialog)
        self.generate_qr_btn.setObjectName(u"generate_qr_btn")
        self.generate_qr_btn.setGeometry(QRect(280, 120, 31, 21))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.generate_qr_btn.setFont(font)
        self.generate_qr_btn.setText(u"GO")
        self.download_qr_btn = QPushButton(Dialog)
        self.download_qr_btn.setObjectName(u"download_qr_btn")
        self.download_qr_btn.setGeometry(QRect(80, 360, 191, 23))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.download_qr_btn.sizePolicy().hasHeightForWidth())
        self.download_qr_btn.setSizePolicy(sizePolicy)
        self.qr_code_field = QLabel(Dialog)
        self.qr_code_field.setObjectName(u"qr_code_field")
        self.qr_code_field.setGeometry(QRect(70, 150, 200, 200))
        self.qr_code_field.setPixmap(QPixmap(u"ExampleQR.png"))
        self.qr_code_field.setScaledContents(True)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"QR CODE GENERATOR", None))
        self.software_name_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; font-style:italic;\">QR CODE<br/>GENERATOR</span></p></body></html>", None))
        self.qr_contents_field.setText("")
        self.qr_contents_field.setPlaceholderText(QCoreApplication.translate("Dialog", u"QR Code Contents", None))
        self.download_qr_btn.setText(QCoreApplication.translate("Dialog", u"DOWNLOAD QR CODE", None))
        self.qr_code_field.setText("")
    # retranslateUi