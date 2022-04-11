import sqlite3
import time

class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS Nomes (id INTEGER PRIMARY KEY, nome text, hora text) ")
        self.conn.commit()
        
    def fetch(self):
        self.cur.execute("SELECT * FROM Nomes")
        rows = self.cur.fetchall()
        return rows

    def insert(self,nome,hora):
        self.cur.execute("INSERT INTO Nomes VALUES (NULL, ?, ?)", (nome, hora))
        self.conn.commit()
        
    def remove(self, id):
        self.cur.execute("DELETE FROM Nomes WHERE id=?",(id,))
        self.conn.commit()
        
    def __del__(self):
        self.conn.close()
        
db = Database('Monitoria.db')  