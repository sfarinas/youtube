# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frame_youtube.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from mhyt import yt_download
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(629, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_download = QtWidgets.QPushButton(self.centralwidget)
        self.bt_download.setGeometry(QtCore.QRect(160, 230, 91, 31))
        self.bt_download.setObjectName("bt_download")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 160, 22, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(79, 189, 30, 16))
        self.label_2.setObjectName("label_2")
        self.txt_link = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_link.setGeometry(QtCore.QRect(120, 160, 371, 20))
        self.txt_link.setObjectName("txt_link")
        self.txt_titulo = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_titulo.setGeometry(QtCore.QRect(120, 186, 133, 20))
        self.txt_titulo.setObjectName("txt_titulo")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 30, 131, 101))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 60, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 290, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(79, 219, 45, 42))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rb_mp3 = QtWidgets.QRadioButton(self.widget)
        self.rb_mp3.setObjectName("rb_mp3")
        self.verticalLayout.addWidget(self.rb_mp3)
        self.rb_mp4 = QtWidgets.QRadioButton(self.widget)
        self.rb_mp4.setChecked(True)
        self.rb_mp4.setObjectName("rb_mp4")
        self.verticalLayout.addWidget(self.rb_mp4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 629, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ## BOTAO ##
        self.bt_download.clicked.connect(self.download)

    def download(self):
        if self.rb_mp4.isChecked() == True:
            url = self.txt_link.text()
            titulo = self.txt_titulo.text()
            titulo_mp4 = titulo + '.mp4'

            yt_download(url,titulo_mp4)

        elif self.rb_mp3.isChecked() == True:
            try:
                url = self.txt_link.text()
                titulo = self.txt_titulo.text()
                titulo_mp3 = titulo + '.mp3'

                yt_download(url,titulo_mp3, ismusic = True, codec = 'mp3')
            except:
                pass    


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_download.setText(_translate("MainWindow", "Download"))
        self.label.setText(_translate("MainWindow", "Link:"))
        self.label_2.setText(_translate("MainWindow", "Titulo:"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/youtube/youtube.png\"/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Download.      "))
        self.label_5.setText(_translate("MainWindow", "dev. sfarinass"))
        self.rb_mp3.setText(_translate("MainWindow", "mp3"))
        self.rb_mp4.setText(_translate("MainWindow", "mp4"))

## IMAGEM ##
import youtube


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
