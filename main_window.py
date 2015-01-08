import sys
from PyQt5 import QtWidgets

from ui_main_window import Ui_MainWindow


class main_window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.compile_btn.clicked.connect(self.compile_btn_clicked)
        self.ui.test_btn.clicked.connect(self.test_btn_clicked)

    def compile_btn_clicked(self):
        QtWidgets.QMessageBox.information(self,"Info","compile")
    
    def test_btn_clicked(self):
        QtWidgets.QMessageBox.information(self,"Info","test")
