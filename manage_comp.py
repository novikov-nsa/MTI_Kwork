'''Основной модуль'''
from core_db import CoreDB

db = CoreDB()
db.check_tables()
db.insert_data('mc_operation', 'f1, f2', '"oper 4", 45786')
db.cur.close()
db.conn.close()