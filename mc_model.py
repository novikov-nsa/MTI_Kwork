from core_db import CoreDB
from PyQt5 import QtGui

class MCCards:
    def __init__(self):
        self.field1 = ''
        self.field2 = ''
        self.field3 = ''
        self.field4 = ''

    def get_all_cards(self):
        self.sql_string = 'SELECT rowid, f1, f2, f3, f4 FROM mc_cards'
        self.db = CoreDB()
        self.list_cards = self.db.select_data(self.sql_string)
        self.cards_model = QtGui.QStandardItemModel()
        for x, line in enumerate(self.list_cards):
            for y, column in enumerate(line):
                self.cards_model.setItem(x, y, QtGui.QStandardItem(str(column)))

        return self.cards_model

    def add_card(self):
        print('карточка добавлена', self.field1, self.field2, self.field3, self.field4)
        fields = "f1, f2, f3, f4"
        data = '"'+self.field1+'", "'+ self.field2+'", "'+ self.field3+'", "'+ self.field4+'"'
        db = CoreDB()
        db.insert_data("mc_cards", fields, data)


    def del_card(self, cards_model, index_card):
        print("Удалаем ", index_card)

        if index_card < 0:
            return
        record = []
        record.append(cards_model.item(index_card, 0).text())

        cards_model.takeRow(index_card)
        db = CoreDB()
        db.delete_item('mc_cards', record[0])

    def update_card(self,cards_model, index_card, record):
        for y, column in enumerate(record):
            cards_model.setItem(index_card, y, QtGui.QStandardItem(str(column)))
        db = CoreDB()
        flist = ['f1', 'f2', 'f3', 'f4']

        db.update_item('mc_cards', flist, record, int(record[0]))

