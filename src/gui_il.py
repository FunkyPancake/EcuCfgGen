from src.Parser import Parser
from src.DataContainer import A2LContainer
from src.ui import main_ui
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import QSettings


class Gui(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = main_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        # connect buttons
        self.ui.baseToolButton.clicked.connect(self.baseToolButtonClicked)
        self.ui.cfgToolButton.clicked.connect(self.cfgToolButtonClicked)
        self.ui.mapToolButton.clicked.connect(self.mapToolButtonClicked)
        self.ui.genButton.clicked.connect(self.genButtonClicked)
        self.ui.updateButton.clicked.connect(self.updateButtonClicked)
        # read settings
        settings = QSettings("settings.ini", QSettings.IniFormat)
        self.ui.baseLineEdit.setText(settings.value('BASE_PATH', [], str))
        self.ui.mapLineEdit.setText(settings.value('MAP_PATH', [], str))
        self.ui.cfgLineEdit.setText(settings.value('CFG_PATH', [], str))

    def baseToolButtonClicked(self):
        dname = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if dname:
            self.ui.baseLineEdit.setText(dname)

    def cfgToolButtonClicked(self):
        [fname, extension] = (QFileDialog.getOpenFileName(self, 'Open file', '', "A2L files (*.a2l)"))
        if fname:
            self.ui.cfgLineEdit.setText(fname)

    def mapToolButtonClicked(self):
        [fname, extension] = QFileDialog.getOpenFileName(self, 'Open file', '', "MAP files (*.map)")
        if fname:
            self.ui.mapLineEdit.setText(fname)

    def updateButtonClicked(self):
        out_data = A2LContainer()
        Parser.parse_a2l_file(self.ui.cfgLineEdit.text(), out_data)
        print(out_data.prefix)

    def genButtonClicked(self):
        pass

    def closeEvent(self, event):
        # save settings
        settings = QSettings("settings.ini", QSettings.IniFormat)
        settings.setValue('BASE_PATH', self.ui.baseLineEdit.text())
        settings.setValue('MAP_PATH', self.ui.mapLineEdit.text())
        settings.setValue('CFG_PATH', self.ui.cfgLineEdit.text())
        super().closeEvent(event)
