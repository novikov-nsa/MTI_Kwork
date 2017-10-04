import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QDesktopWidget, \
                             QTableWidget, QTableWidgetItem, QMainWindow, QAction, QVBoxLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import pyqtSlot
from mc_model import Operation

class MCView(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Учет техники'
        self.left = 0
        self.top = 0
        self.width = 300
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
        for i in self.list_oper:
            self.tableWidget.setItem(self.list_oper.index(i)-1, 0, QTableWidgetItem(i[self.list_oper.index(i)-1][0]))
            self.tableWidget.setItem(self.list_oper.index(i)-1, 1, QTableWidgetItem(i[self.list_oper.index(i)-1][1]))

        self.tableWidget.move(0, 0)
