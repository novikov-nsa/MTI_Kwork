from PyQt5 import QtWidgets, uic, QtCore

from mc_model import MCCards

class MCMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.mainwindow  = QtWidgets.QWidget.__init__(self, parent)
        self.mainwindow = uic.loadUi("qml_forms/main.ui", self)
        self.desktop = QtWidgets.QApplication.desktop()
        self.center()
        self.mainwindow.list_cards.triggered.connect(self.show_modal_window)
        self.mainwindow.new_card.triggered.connect(self.show_modal_newcard_window)
        self.mainwindow.exit.triggered.connect(self.close_app)




    @QtCore.pyqtSlot()
    def close_app(self):
        QtWidgets.qApp.quit()

    def show_modal_window(self):
        global modal_window
        modal_window = QtWidgets.QWidget(self, QtCore.Qt.Window)
        modal_window.setWindowModality(QtCore.Qt.WindowModal)
        modal_window.setWindowTitle('Список оборудования')
        rect = self.mainwindow.geometry()
        x = rect.left()
        y = rect.top()
        w = rect.width()-30
        h = rect.height()-120

        if w <600:
            w = 600
        if h < 400:
            h = 400
        modal_window.setGeometry(x, y, w, h)
        self.create_table()

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        modal_window.setLayout(self.layout)
        modal_window.move(x+5, y+50)
        modal_window.show()

    def create_table(self):
        # Create table
        #self.tableWidget = QtWidgets.QTableWidget()
        default_col_width = [70, 300, 100, 300, 100, 500]
        self.tableWidget = QtWidgets.QTableView()
        cards = MCCards()
        self.cards_model = cards.get_all_cards()
        self.tableWidget.setModel(self.cards_model)
        for i, item in enumerate(default_col_width):
            self.tableWidget.setColumnWidth(i, item)

        self.tableWidget.move(0, 0)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.openMenu)
        self.tableWidget.doubleClicked.connect(self.on_double_click_table)



    #@QtCore.pyqtSlot()
    def openMenu(self, position):
        self.context_menu = QtWidgets.QMenu()
        self.insert_action = self.context_menu.addAction("Создать")
        self.edit_action = self.context_menu.addAction("Редактировать")
        self.delete_action = self.context_menu.addAction("Удалить")

        act = self.context_menu.exec_(self.tableWidget.mapToGlobal(position))
        if act == self.edit_action:
            self.on_double_click_table()
        if act == self.insert_action:
            self.show_modal_edit_window(2)
        if act == self.delete_action:
            self.delete_card()

    @QtCore.pyqtSlot()
    def on_double_click_table(self):
        print("двойной клик")
        self.list_fields_card = []
        index = self.tableWidget.currentIndex()
        data = self.cards_model.data(index, QtCore.Qt.DisplayRole)
        self.current_row = index.row()
        for i in range(0,6):
            self.list_fields_card.append(self.cards_model.item(self.current_row, i).text())
        print(data, index.row(), index.column(), list)
        self.show_modal_edit_window(1)

    @QtCore.pyqtSlot()
    def show_modal_newcard_window(self):

        self.show_modal_edit_window(2)

    def show_modal_edit_window(self, mode):
        #mode - Режим открытия окна. 0- просмотр, 1- редактирование, 2- новая запись
        global edit_window
        self.edit_window = QtWidgets.QWidget(self, QtCore.Qt.Window)
        self.edit_window.setWindowModality(QtCore.Qt.WindowModal)
        equipmentNameLabel = QtWidgets.QLabel('Оборудование')
        equipmentTypelabel = QtWidgets.QLabel('Тип оборудования')
        orgNameLabel = QtWidgets.QLabel('Организация')
        quantityLabel = QtWidgets.QLabel('Количество')
        commentCardLabel = QtWidgets.QLabel('Комментарий')
        self.equipmentNameEdit = QtWidgets.QLineEdit()
        self.equipmentTypeEdit = QtWidgets.QLineEdit()
        self.orgNameEdit = QtWidgets.QLineEdit()
        self.quantityEdit = QtWidgets.QLineEdit()
        self.commentCardEdit = QtWidgets.QTextEdit()

        okButton = QtWidgets.QPushButton('Сохранить')
        cancelButton = QtWidgets.QPushButton('Отмена')

        if mode == 0:
            self.equipmentNameEdit.setDisabled(True)
            self.equipmentTypeEdit.setDisabled(True)
            self.orgNameEdit.setDisabled(True)
            self.quantityEdit.setDisabled(True)
            self.commentCardEdit.setDisabled(True)
            okButton.setDisabled(True)

        if mode == 1:
            if len(self.list_fields_card) > 0:
                self.equipmentNameEdit.setText(self.list_fields_card[1])
                self.equipmentTypeEdit.setText(self.list_fields_card[2])
                self.orgNameEdit.setText(self.list_fields_card[3])
                self.quantityEdit.setText(self.list_fields_card[4])
                self.commentCardEdit.setText(self.list_fields_card[5])


        grid = QtWidgets.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(equipmentNameLabel, 1, 0, 1, 1)
        grid.addWidget(self.equipmentNameEdit, 1, 1, 1, 4)
        grid.addWidget(equipmentTypelabel, 2, 0, 1, 1)
        grid.addWidget(self.equipmentTypeEdit, 2, 1, 1, 4)
        grid.addWidget(orgNameLabel, 3, 0, 1, 1)
        grid.addWidget(self.orgNameEdit, 3, 1, 1, 4)
        grid.addWidget(quantityLabel, 4, 0, 1, 1)
        grid.addWidget(self.quantityEdit, 4, 1, 1, 4)
        grid.addWidget(commentCardLabel, 5, 0, 1, 1)
        grid.addWidget(self.commentCardEdit, 5, 1, 3, 4)

        grid.addWidget(okButton, 11, 3)
        grid.addWidget(cancelButton, 11, 4)
        self.edit_window.setLayout(grid)
        self.edit_window.setGeometry(200, 300, 600, 300)
        self.edit_window.setWindowTitle('Карточка оборудования')
        if mode == 2: #создание новой записи
            okButton.clicked.connect(self.add_new_card)
        elif mode == 1: #сохранение данных в модели и БД
            okButton.clicked.connect(self.save_card)

        cancelButton.clicked.connect(self.close_card)
        self.edit_window.show()

    @QtCore.pyqtSlot()
    def add_new_card(self):
        new_card = MCCards()
        new_card.equipmentName = self.equipmentNameEdit.text()
        new_card.equipmentType = self.equipmentTypeEdit.text()
        new_card.orgName = self.orgNameEdit.text()
        new_card.quantity = int(self.quantityEdit.text())
        new_card.commentCard = self.commentCardEdit.toPlainText()
        
        #new_card.comment = self.commentEdit.
        new_card.add_card()
        print('добавить новую карточку')
        self.edit_window.close()

    @QtCore.pyqtSlot()
    def save_card(self):
        print('сохранить карточку', self.current_row)
        self.list_fields_card[1] = self.equipmentNameEdit.text()
        self.list_fields_card[2] = self.equipmentTypeEdit.text()
        self.list_fields_card[3] = self.orgNameEdit.text()
        self.list_fields_card[4] = self.quantityEdit.text()
        self.list_fields_card[5] = self.commentCardEdit.toPlainText()
        mccard = MCCards()
        mccard.update_card(self.cards_model, self.current_row, self.list_fields_card)
        self.edit_window.close()

    @QtCore.pyqtSlot()
    def close_card(self):
        print('отмена')
        self.edit_window.close()

    def delete_card(self):
        print("удаление карточки")
        index = self.tableWidget.currentIndex()
        current_row = index.row()
        model = MCCards()
        model.del_card(self.cards_model, current_row)

    def center(self):

        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
