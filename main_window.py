import sys
import logging
from PyQt5 import QtWidgets,QtCore,QtGui

from ui_main_window import Ui_MainWindow
from regex2nfa import regex2nfa
from nfa2dfa import nfa2dfa
from dfa2mindfa import dfa2mindfa
from automata import automata


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
        nfa=self.regex2nfa_obj.nfa
        automata.display_nx_automata(nfa, "nfa", "NFA")

        nfa2dfa_obj = nfa2dfa('nfa2dfa')
        nfa2dfa_obj.set_nfa(nfa)
        nfa2dfa_obj.set_charset(nfa.char_set)
        nfa2dfa_obj.build_dfa()
        aut_dfa = nfa2dfa_obj.dfa
        nfa2dfa_obj.display_automata()
        automata.display_nx_automata(aut_dfa, "dfa", "DFA")


        dfa2mindfa_obj = dfa2mindfa(aut_dfa)
        dfa2mindfa_obj.minimiseIt()

        self.min_dfa = automata("min_dfa")
        self.min_dfa = dfa2mindfa_obj.create_new_dfa()
        self.min_dfa.display_automata()
        automata.display_nx_automata(self.min_dfa, "min_dfa", "MINIMAL DFA")

        self.show_graph()

    
    def test_btn_clicked(self):
        result=self.min_dfa.accepting_string(self.ui.test_line_edit.text())
        if result:
            self.ui.test_result_line_edit.setText("Accepted")
        else:
            self.ui.test_result_line_edit.setText("Rejected")


    def show_error(self,error):
        QtWidgets.QMessageBox.critical(self,"Error",error)

    def show_graph(self):
        self.nfa_scene=QtWidgets.QGraphicsScene(self)
        self.dfa_scene=QtWidgets.QGraphicsScene(self)
        self.min_dfa_scene=QtWidgets.QGraphicsScene(self)
        
        nfa_pic = QtGui.QPixmap.fromImage(QtGui.QImage("pics/nfa.png"))
        self.nfa_scene.addPixmap(nfa_pic)
        self.ui.nfa_graphic_view.setScene(self.nfa_scene)

        dfa_pic = QtGui.QPixmap.fromImage(QtGui.QImage("pics/dfa.png"))
        self.dfa_scene.addPixmap(dfa_pic)
        self.ui.dfa_graphic_view.setScene(self.dfa_scene)

        min_dfa_pic = QtGui.QPixmap.fromImage(QtGui.QImage("pics/min_dfa.png"))
        self.min_dfa_scene.addPixmap(min_dfa_pic)
        self.ui.min_dfa_graphic_view.setScene(self.min_dfa_scene)




