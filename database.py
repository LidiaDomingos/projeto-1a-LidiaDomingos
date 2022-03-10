import sqlite3
import string

from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

comando_criacao = "CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title TEXT UNIQUE, content TEXT NOT NULL UNIQUE);"



class Database():
    def __init__(self, string):
        self.conn = sqlite3.connect(string + ".db")
        self.note = self.conn.execute(comando_criacao)

    def add(self, Note):
        self.conn.execute("INSERT INTO note (id, title, content) VALUES (?, ?, ?)",(Note.id, Note.title,Note.content))
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("SELECT id, title, content FROM note",())
        notes = []
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            notes.append(Note(id=id, title=title, content=content))
        return notes

    def update(self, entry):
        self.conn.execute("UPDATE note SET title = ?, content = ? WHERE id = ?",(entry.title, entry.content, entry.id))
        self.conn.commit()
        
    def delete(self, note_id):
        self.conn.execute("DELETE FROM note WHERE id = ?",(note_id,))
        self.conn.commit()

