from src.gui_il import Gui
from PyQt5 import QtWidgets
import sys
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Gui()
    ui.show()
    sys.exit(app.exec_())