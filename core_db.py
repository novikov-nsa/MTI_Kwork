'''Основные операции работы с БД'''
import sqlite3

class CoreDB:
    list_fields = {'mc_cards': 'CREATE TABLE mc_cards (f1 text, f2 text, f3 text, f4 text)'}
    def connect_db(self):
        self.conn = sqlite3.connect("manage_comp.db")
        self.cur = self.conn.cursor()
        return self.conn, self.cur

    def check_tables(self):

        self.list_tables = self.list_fields.keys()
        self._cur = self.connect_db()[1]

        for i in self.list_tables:
            self.s = self._cur.execute("SELECT 1 from SQLITE_MASTER where tbl_name = ?", [i])
            self.s_result = self.s.fetchall()
            if len(self.s_result) == 0:
                self._cur.execute(self.list_fields[i])
        return

    def insert_data(self, table_name, fields_list, fields_value_list):
        '''имя таблицы - строка, передается имя таблицы, в которую будет вставлена запись
        список полей- строка, передается строка со списков полей в виде "поле1, поле2, поле3"
        список значение- строка передается список значений в виде 'значение 1', 'значение 2', 'значение 3' '''
        self.conn = self.connect_db()[0]
        self.cur = self.connect_db()[1]
        self.result_comand = """INSERT INTO """+table_name+""" ("""+fields_list+""") VALUES ("""+fields_value_list+""")"""
        self.cur.execute(self.result_comand)
        self.conn.commit()
        self.conn.close()
        return

    def delete_item(self, table_name, id_value):
        # удаление строки по условиям
        return

    def update_item(self, table_name, fields_list, values_list, id_value):
        #обновление записи по ID
        return

    def select_data(self, sql_string):
        self.conn = self.connect_db()[0]
        self.cur = self.connect_db()[1]
        self.select_result = self.cur.execute(sql_string).fetchall()
        self.conn.close()
        return self.select_result