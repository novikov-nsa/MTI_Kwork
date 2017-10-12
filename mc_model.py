from core_db import CoreDB

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
        return self.list_cards

    def add_card(self):
        print('карточка добавлена', self.field1, self.field2, self.field3, self.field4)
        fields = "f1, f2, f3, f4"
        data = '"'+self.field1+'", "'+ self.field2+'", "'+ self.field3+'", "'+ self.field4+'"'
        db = CoreDB()
        db.insert_data("mc_cards", fields, data)


    def del_card(self, id_card):
        pass

    def update_card(self, id_card):
        pass
