import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QTableWidget, QMenu, qApp, QTableView

app = QApplication([])
tableWidget = QTableView()
tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)

def openMenu(position):

    menu = QMenu()
    quitAction = menu.addAction("Quit")
    action = menu.exec_(tableWidget.mapToGlobal(position))
    if action == quitAction:
        qApp.quit()

tableWidget.customContextMenuRequested.connect(openMenu)
tableWidget.show()
sys.exit(app.exec_())
