from PyQt5 import QtCore

class regex2nfa(QtCore.QObject):

    send_error=QtCore.pyqtSignal("QString")
    
    def __init__(self,regex):
        super(QtCore.QObject,self).__init__()
        self.union_op="+"
        self.concat_op="."
        self.open_bracket="("
        self.close_bracket=")"
        self.regex=regex 

    def convert_to_nfa(self):
        self.send_error.emit("Hello")

