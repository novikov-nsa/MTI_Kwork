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
        db = self.connect_db()
        conn = db[0]
        cur = db[1]
        sql_string = 'DELETE from '+table_name+' WHERE ROWID = '+id_value
        print(sql_string)
        cur.execute(sql_string)
        conn.commit()
        conn.close()

    def update_item(self, table_name, fields_list, values_list, id_value):
        #обновление записи по ID
        max_items = len(fields_list)
        sql_flist_string = 'set '
        for i, sitem in enumerate(fields_list):
            sql_flist_string = sql_flist_string +sitem+' = "'+values_list[i+1]+'" '
            if i != max_items-1:
                sql_flist_string = sql_flist_string + ', '
        sql_update_string = ' UPDATE '+table_name+' '+sql_flist_string+' where ROWID = '+str(id_value)
        print(sql_update_string)
        db = self.connect_db()
        conn = db[0]
        cur = db[1]
        cur.execute(sql_update_string)
        conn.commit()
        conn.close()



    def select_data(self, sql_string):
        conn = self.connect_db()[0]
        cur = self.connect_db()[1]
        self.select_result = cur.execute(sql_string).fetchall()
        conn.close()
        return self.select_result