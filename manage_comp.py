'''Основной модуль'''
import sys
from core_db import CoreDB
from mc_view import MCView
from PyQt5.QtWidgets import QApplication

db = CoreDB()
db.check_tables()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MCView()
    sys.exit(app.exec_())



#db.insert_data('mc_operation', 'f1, f2', '"oper 4", 45786')
#db.cur.close()
#db.conn.close()