from core_db import CoreDB

class Operation:
    def __init__(self):
        self.name_oper = ''
        self.sum_oper = 0

    def get_all_operation(self):
        self.sql_string = 'SELECT f1, f2 FROM mc_operation'
        self.db = CoreDB()
        self.list_operation = self.db.select_data(self.sql_string)
        return self.list_operation
