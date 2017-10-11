from PyQt5 import QtWidgets, uic, QtCore
from mc_model import MCCards

class MCMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        mainwindow  = QtWidgets.QWidget.__init__(self, parent)
        mainwindow = uic.loadUi("qml_forms/main.ui", self)
        mainwindow.list_cards.triggered.connect(self.show_modal_window)
        mainwindow.new_card.triggered.connect(self.show_modal_newcard_window)
        mainwindow.exit.triggered.connect(self.close_app)


    @QtCore.pyqtSlot()
    def close_app(self):
        QtWidgets.qApp.quit()

    def show_modal_window(self):
        global modal_window
        modal_window = QtWidgets.QWidget(self, QtCore.Qt.Window)
        modal_window.setWindowModality(QtCore.Qt.WindowModal)
        modal_window.setWindowTitle('Список оборудования')
        modal_window.setGeometry(200, 300, 600, 300)

        self.create_table()
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        modal_window.setLayout(self.layout)

        modal_window.show()


    def create_table(self):
        # Create table
        self.tableWidget = QtWidgets.QTableWidget()
        cards = MCCards()
        list_cards = cards.get_all_cards()
        #max_oper = len(list_oper)
        self.tableWidget.setRowCount(len(list_cards))
        self.tableWidget.setColumnCount(4)
        for i, item in enumerate(list_cards):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(list_cards[i][0]))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(list_cards[i][1]))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(list_cards[i][2]))
            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(list_cards[i][3]))

        self.tableWidget.move(0, 0)
        self.tableWidget.doubleClicked.connect(self.on_double_click_table)

    @QtCore.pyqtSlot()
    def on_double_click_table(self):
        current_line_value = []
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

        #current_line_value[0] = self.tableWidget.column(self.tableWidget.selectedItems)
        self.show_modal_edit_window(1)

    @QtCore.pyqtSlot()
    def show_modal_newcard_window(self):
        self.show_modal_edit_window(2)

    def show_modal_edit_window(self, mode):
        #mode - Режим открытия окна. 0- просмотр, 1- редактирование, 2- новая запись

        global edit_window
        self.edit_window = QtWidgets.QWidget(self, QtCore.Qt.Window)
        self.edit_window.setWindowModality(QtCore.Qt.WindowModal)
        title = QtWidgets.QLabel('Title')
        author = QtWidgets.QLabel('Author')
        review = QtWidgets.QLabel('Review')
        titleEdit = QtWidgets.QLineEdit()
        authorEdit = QtWidgets.QLineEdit()
        reviewEdit = QtWidgets.QTextEdit()
        okButton = QtWidgets.QPushButton('Сохранить')
        cancelButton = QtWidgets.QPushButton('Отмена')

        if mode == 0:
            titleEdit.setDisabled(True)
            authorEdit.setDisabled(True)
            reviewEdit.setDisabled(True)
            okButton.setDisabled(True)

        titleEdit.setText('строка 1')

        grid = QtWidgets.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(title, 1, 0, 1, 1)
        grid.addWidget(titleEdit, 1, 1, 1, 4)
        grid.addWidget(author, 2, 0, 1, 1)
        grid.addWidget(authorEdit, 2, 1, 1, 4)
        grid.addWidget(review, 3, 0, 1, 1)
        grid.addWidget(reviewEdit, 3, 1, 5, 4)
        grid.addWidget(okButton, 9, 3)
        grid.addWidget(cancelButton, 9, 4)
        self.edit_window.setLayout(grid)
        self.edit_window.setGeometry(200, 300, 600, 300)
        self.edit_window.setWindowTitle('Карточка оборудования')
        if mode == 2:
            okButton.clicked.connect(self.add_new_card)
        elif mode == 1:
            okButton.clicked.connect(self.save_card)

        cancelButton.clicked.connect(self.close_card)
        self.edit_window.show()

    @QtCore.pyqtSlot()
    def add_new_card(self):
        print('добавить новую карточку')
        self.edit_window.close()

    @QtCore.pyqtSlot()
    def save_card(self):
        print('сохранить карточку')
        self.edit_window.close()

    @QtCore.pyqtSlot()
    def close_card(self):
        print('отмена')
        self.edit_window.close()