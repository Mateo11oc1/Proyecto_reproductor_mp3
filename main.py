
from view.main_window import Ui_MainWindow
from PyQt6 import QtWidgets
from controller.Main_control import *
import sys

if __name__ == '__main__':
    
    #------------------------------VIEW------------------------------
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    #-----------------------------CONTROLLER----------------------
    ctrl = Main_control(ui)
    
    sys.exit(app.exec())
    
    