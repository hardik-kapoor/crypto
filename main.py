from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import rsa_image,rsa_text,sha_hashcal,sha_otpcal


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 686)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rsaTextButton = QtWidgets.QPushButton(self.centralwidget)
        self.rsaTextButton.setGeometry(QtCore.QRect(90, 90, 291, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rsaTextButton.setFont(font)
        self.rsaTextButton.setObjectName("rsaTextButton")
        self.shabutton = QtWidgets.QPushButton(self.centralwidget)
        self.shabutton.setGeometry(QtCore.QRect(90, 290, 291, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.shabutton.setFont(font)
        self.shabutton.setObjectName("shabutton")
        self.mainText = QtWidgets.QLabel(self.centralwidget)
        self.mainText.setGeometry(QtCore.QRect(90, 470, 651, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.mainText.setFont(font)
        self.mainText.setAlignment(QtCore.Qt.AlignCenter)
        self.mainText.setObjectName("mainText")
        self.rsaImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.rsaImageButton.setGeometry(QtCore.QRect(450, 90, 291, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rsaImageButton.setFont(font)
        self.rsaImageButton.setObjectName("rsaImageButton")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 290, 281, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.rsaImageButton.clicked.connect(self.clickRI)
        self.rsaTextButton.clicked.connect(self.clickRT)
        self.shabutton.clicked.connect(self.clickSH)
        self.pushButton.clicked.connect(self.clickSO)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rsaTextButton.setText(_translate("MainWindow", "RSA Text Encryption/ Decryption"))
        self.shabutton.setText(_translate("MainWindow", "SHA-256 Hash Calculator"))
        self.mainText.setText(_translate("MainWindow", "Choose any one of the button to run "))
        self.rsaImageButton.setText(_translate("MainWindow", "RSA Image encryption/ Decryption"))
        self.pushButton.setText(_translate("MainWindow", "SHA-256 OTP Generation"))

    def clickRI(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=rsa_image.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def clickRT(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=rsa_text.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def clickSO(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=sha_otpcal.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def clickSH(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=sha_hashcal.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
