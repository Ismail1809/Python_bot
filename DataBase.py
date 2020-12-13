import sqlite3

class Bot_Database():
	def __init__(self):
		self.conn = sqlite3.connect("users_list.db")

		self.cursor = self.conn.cursor()
		self.cursor.execute("CREATE TABLE IF NOT EXISTS users (chat_id text, login text, password text)")
		self.conn.commit()
		self.cursor.execute("CREATE TABLE IF NOT EXISTS act (chat_id text, last_act text, last_login text)")
		self.conn.commit()


	def add_user(self, login, password, chat_id):
		block = [(chat_id, login, password)]

		self.cursor.executemany("INSERT INTO users VALUES(?, ?, ?);", block)
		self.conn.commit()
	def get_user(self):
		self.cursor.execute("SELECT * FROM users")
		data = self.cursor.fetchall()

		return data
	def delete(self):
		# block = [("1114074475", "asas", "cd")]

		# self.cursor.executemany("INSERT INTO act VALUES(?, ?, ?);", block)
		# self.conn.commit()

		self.cursor.execute("DELETE FROM users")
		self.conn.commit()
	def add_data(self, chat_id, last_action, data):
		block = [(chat_id, last_action, data)]

		self.cursor.executemany("INSERT INTO act VALUES(?, ?, ?);", block)
		self.conn.commit()
	def get_data(self, chat_id):
		t = (chat_id, )
		self.cursor.execute("SELECT * FROM act WHERE chat_id=?", t)
		data = self.cursor.fetchall()

		return data
	def change_action(self, chat_id, text, action):
		block = [(text, chat_id)]
		self.cursor.execute("UPDATE act SET last_login = ? WHERE chat_id = ?;", (text, chat_id))
		block = [(action, chat_id)]
		self.cursor.execute("UPDATE act SET last_act = ? WHERE chat_id = ?;", (action, chat_id))
		self.conn.commit()