from pprint import pprint
import DataBase
import time


class Bot_Logic():
	def set_db(self):
		self.db = DataBase.Bot_Database()

	def set_telegram(self, telegram):
		self.answer = telegram

	def check_main(self, text, chat_id):
		if text == "/start":
			check = self.check_user(chat_id)
			if check==False:
				print(1)
				self.put_action(chat_id, "assd", text)
			else:
				print(2)
				self.db.change_action(chat_id, text, "asas")

			self.get_action(chat_id, text)
		else:
			self.get_action(chat_id, text)
	def check_user(self, chat_id):
		self.set_db()
		list1 = self.db.get_data(chat_id)
		if list1!=[]:
			if list1[0][0] == str(chat_id):
				return True
			else:
				return False
		else:
			return False
	def check_answer(self, chat_id, text, last_action):
		if text == "/start":
			self.answer.send_message(chat_id, "Hello from bot! You need to log in and then you can continue to talk with me")
			self.answer.send_message(chat_id, "Write 'log in' if you want to log into your account or 'sign in' to make an account")
		if text == "sign in" or text == "signin" or text == "Sign in" or text == "Signin" or last_action == "signin" or last_action=="signin_name" or last_action=="signin_start":
			self.sign_in(text, chat_id, last_action)
		if text == "log in" or text == "login" or text == "Log in" or text == "Login" or last_action == "login" or last_action == "login_name" or last_action=="login_start" or last_action=="login_choise":
			self.log_in(text, chat_id, last_action)
				
		time.sleep(1)

	def get_action(self, chat_id, text):
		block = self.db.get_data(chat_id)
		print(block)
		self.check_answer(chat_id, text, block[0][1])


	def put_action(self, chat_id, last_action, text):
		self.db.add_data(chat_id, last_action, text)

	def sign_in(self, data, chat_id, last_action):
		name = ""
		password = ""

		print(data, chat_id, last_action)

		if last_action == "signin_start":

			self.db.change_action(chat_id, data, "signin_name")

			self.answer.send_message(chat_id, "Password:")
		elif last_action == "signin_name":
			password = data

			block = self.db.get_data(chat_id)
			self.db.add_user(block[0][2], password, chat_id)
			self.answer.send_message(chat_id, "You are successfully sign in!!")
			self.answer.send_message(chat_id, "Now you need to log in, write 'log in' to log in")
			self.db.change_action(chat_id, data, "asas")

		else:
			self.db.change_action(chat_id, data, "signin_start")

			self.answer.send_message(chat_id, "Name:")
		time.sleep(1)
	def log_in(self, data, chat_id, last_action):
		if last_action =="login_start":
			self.answer.send_message(chat_id, "Password: ")
			self.db.change_action(chat_id, data, "login_name")

		elif last_action == "login_name":
			a = True
			password = data
			b = self.db.get_data(chat_id)
			login = b[0][2]
			block = self.db.get_user()
			for i in range(len(block)):
				if block[i][1] == str(login) and block[i][2] == str(password):		
					self.answer.send_message(chat_id, "You are successfully log in!!\n")
					self.answer.send_message(chat_id, "Hello " + str(login) + "!\n")
					self.answer.send_message(chat_id, "Do you want to log out?(yes or no)")
					self.db.change_action(chat_id, data, "login_choise")

					return

				else:
					a = False

			if a==False:
				self.answer.send_message(chat_id, "Try Again!")
				self.answer.send_message(chat_id, "Name:")
				self.db.change_action(chat_id, data, "login_start")

		elif last_action =="login_choise":
			if data == "yes" or data=="Yes":
				self.answer.send_message(chat_id, "Good")
				self.answer.send_message(chat_id, "Write 'login' if you want to log into your account or 'signin' to make an account")
				self.db.change_action(chat_id, data, "assd")
				self.get_action(chat_id, data)
			elif data =="no" or data=="No":
				self.db.change_action(chat_id, data, "assd")
				self.answer.send_message(chat_id, "Ok:(")
				self.db.change_action(chat_id, data, "assd")
			else:
				self.answer.send_message(chat_id, "I can't understand you :(")
		else:
			self.answer.send_message(chat_id, "Name:")
			self.db.change_action(chat_id, data, "login_start")
				
		time.sleep(1)