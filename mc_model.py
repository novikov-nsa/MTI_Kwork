from core_db import CoreDB

class MCCards:
    def __init__(self):
        self.name_oper = ''
        self.sum_oper = 0

    def get_all_cards(self):
        self.sql_string = 'SELECT f1, f2, f3, f4 FROM mc_cards'
        self.db = CoreDB()
        self.list_cards = self.db.select_data(self.sql_string)
        return self.list_cards

    def add_card(self, id_card):
        pass

    def del_card(self, id_card):
        pass

    def update_card(self, id_card):
        pass
