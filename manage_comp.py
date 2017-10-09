'''Основной модуль'''
import sys
from core_db import CoreDB
from mc_view import MCMainView
from PyQt5.QtWidgets import QApplication

db = CoreDB()
db.check_tables()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MCMainView()
    sys.exit(app.exec_())



#db.insert_data('mc_operation', 'f1, f2', '"oper 4", 45786')
#db.cur.close()
#db.conn.close()