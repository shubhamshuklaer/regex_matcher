import sys
import logging
from PyQt5 import QtWidgets,QtCore

from ui_main_window import Ui_MainWindow
from regex2nfa import regex2nfa
#from nfa2dfa import nfa2dfa
#from dfa2mindfa import dfa2mindfa


class main_window(QtWidgets.QMainWindow):

    @QtCore.pyqtSlot("QString")
    def receive_error(self,error):
        self.show_error(error)

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.compile_btn.clicked.connect(self.compile_btn_clicked)
        self.ui.test_btn.clicked.connect(self.test_btn_clicked)

    def compile_btn_clicked(self):
        self.regex2nfa_obj=regex2nfa(self.ui.regex_line_edit.text())
        self.regex2nfa_obj.send_error.connect(self.receive_error)
        self.regex2nfa_obj.convert_to_nfa()

    
    def test_btn_clicked(self):
        self.show_error("Test")

    def show_error(self,error):
        QtWidgets.QMessageBox.critical(self,"Error",error)


