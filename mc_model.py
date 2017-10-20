from core_db import CoreDB
from PyQt5 import QtGui

class MCCards:
    def __init__(self):
        self.equipmentName = ''     #Наименование оборудования
        self.equipmentType = ''     #Тип оборудования
        self.orgName = ''           #Наименование организации
        self.quantity = 0           #Количество
        self. commentCard= ''       #Комментарий
        self.flist = ['equipmentName', 'equipmentType', 'orgName', 'quantity', 'commentCard']
        self.fields = "equipmentName, equipmentType, orgName, quantity, commentCard"

    def get_all_cards(self):
        self.sql_string = 'SELECT rowid, equipmentName, equipmentType, orgName, quantity, commentCard FROM mc_cards'
        self.db = CoreDB()
        self.list_cards = self.db.select_data(self.sql_string)
        self.cards_model = QtGui.QStandardItemModel()
        self.cards_model.setHorizontalHeaderLabels(['Номер', 'Оборудование', 'Тип оборудования', 'Организация',\
                                                    'Количество', 'Комментарий'])
        for x, line in enumerate(self.list_cards):
            for y, column in enumerate(line):
                self.cards_model.setItem(x, y, QtGui.QStandardItem(str(column)))

        return self.cards_model

    def add_card(self):

        data = '"'+self.equipmentName+'", "'+ self.equipmentType+'", "'+ self.orgName+'", "'+ str(self.quantity)+'", "'+self.commentCard+'"'
        db = CoreDB()
        db.insert_data("mc_cards", self.fields, data)


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
        db.update_item('mc_cards', self.flist, record, int(record[0]))

