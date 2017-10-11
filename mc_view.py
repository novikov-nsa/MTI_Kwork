import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QDesktopWidget, \
                             QTableWidget, QTableWidgetItem, QMainWindow, QAction, QVBoxLayout, \
                             QLabel, QLineEdit, QTextEdit, QGridLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import pyqtSlot
from PyQt5 import Qt as qt
from PyQt5 import QtGui
from mc_model import Operation
from mc_view_edit import MCViewEdit

class MCMainView(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Учет техники'
        self.left = 500
        self.top = 300
        self.width = 600
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


        self.createTable()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Сообщение',
                                     "Вы уверены, что желаете выйти из программы?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def createTable(self):
        # Create table
        self.tableWidget = QTableWidget()
        self.oper = Operation()
        self.list_oper = self.oper.get_all_operation()
        self.max_oper = len(self.list_oper)
        self.tableWidget.setRowCount(len(self.list_oper))
        self.tableWidget.setColumnCount(2)
        for i, item in enumerate(self.list_oper):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(self.list_oper[i][0]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(self.list_oper[i][1])))

        self.tableWidget.move(0, 0)
        self.tableWidget.doubleClicked.connect(self.on_double_click)

    @pyqtSlot()
    def on_double_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
        modal_window = MCViewEdit()
        modal_window.show()



