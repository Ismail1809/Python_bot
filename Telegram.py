from flask import Flask
from flask import request
from flask import jsonify
import Logic
import DataBase

import requests


class Telegram():
	def __init__(self):
		self.app = Flask(__name__)

	def set_logic(self, logic_class):
		self.logic = logic_class

	def send_message(self, chat_id, text):
		token = "1355290045:AAFD96LRCoEbYXbwYgowpVCNnssE3M5ptnw"
		url = "https://api.telegram.org/bot" + token + "/sendMessage"

		message = {
			"chat_id": chat_id,
			"text": text,
		}

		response = requests.post(url, json = message)

	def start(self):
		@self.app.route("/", methods = ["POST"])
		def proceed_request():
			updates = request.get_json()
			chat_id = updates["message"]["chat"]["id"]
			text = updates["message"]["text"]
			print(text, chat_id)
			self.logic.check_main(text, chat_id)
			return jsonify(updates)
		self.app.run()


if __name__ == "__main__":
	logic = Logic.Bot_Logic()

	telegram = Telegram()
	telegram.set_logic(logic)

	logic.set_telegram(telegram)

	database = DataBase.Bot_Database()

	logic.set_database(database)


	telegram.start()