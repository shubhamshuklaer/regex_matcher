import sys

from PyQt5 import QtWidgets
from main_window import main_window 

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = main_window()
    myapp.show()
    sys.exit(app.exec_())
