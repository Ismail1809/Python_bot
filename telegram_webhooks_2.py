from flask import Flask
from flask import request
from flask import jsonify
from pprint import pprint
from add_data import FileClass

import requests
import time

app = Flask(__name__)


def send_message(chat_id, text):
	token = "1355290045:AAFD96LRCoEbYXbwYgowpVCNnssE3M5ptnw"
	url = "https://api.telegram.org/bot" + token + "/sendMessage"

	message = {
		"chat_id": chat_id,
		"text": text,
	}

	response = requests.post(url, json = message)

def check_answer(chat_id, text, last_action):
	if text == "/start":
		send_message(chat_id, "Hello from bot! You need to log in and then you can continue to talk with me")
		send_message(chat_id, "Write 'log in' if you want to log into your account or 'sign in' to make an account")
	if text == "sign in" or text == "signin" or text == "Sign in" or text == "Signin" or last_action == "signin" or last_action=="signin_name" or last_action=="signin_start":
		sign_in(text, chat_id, last_action)
	if text == "log in" or text == "login" or text == "Log in" or text == "Login" or last_action == "login" or last_action == "login_name" or last_action=="login_start" or last_action=="login_choise":
		log_in(text, chat_id, last_action)
			
	time.sleep(1)

def get_action(chat_id, text):
	actions_file = open("action.txt", "r")

	users_data = actions_file.readlines()

	last_action = ""

	for row in users_data:
		split_info = row.split()
		print(split_info[0], chat_id)
		if split_info[0] == str(chat_id):
			last_action = split_info[1]
			print(last_action)
	actions_file.close()

	check_answer(chat_id, text, last_action)

def sign_in(data, chat_id, last_action):
	file2 = FileClass() 

	name = ""
	password = ""

	print(data, chat_id, last_action)

	if last_action == "signin_start":
		change_action(chat_id, "signin_name")
		file2 = FileClass()

		name = data

		users_list = file2.add(chat_id, name)

		send_message(chat_id, "Password:")
	elif last_action == "signin_name":
		password = data

		users_list = file2.add_password(chat_id, password)

		send_message(chat_id, "You are successfully sign in!!")
		send_message(chat_id, "Now you need to log in, write 'log in' to log in")
		change_action(chat_id, "login")

	else:
		change_action(chat_id, "signin_start")

		send_message(chat_id, "Name:")
	time.sleep(1)
def log_in(data, chat_id, last_action):
	file2 = FileClass() 
	
	if last_action =="login_start":
		users_list = file2.read_all(chat_id)

		if 'login' not in list(users_list.keys()):
			send_message(chat_id, "You are not registered yet")

		elif users_list['login'] == str(data):
	 		send_message(chat_id, "Password: ")
	 		change_action(chat_id, "login_name")

		elif users_list['login'] != str(data):
		 	send_message(chat_id, "Try Again!")
		 	send_message(chat_id, "Name:")
		 	change_action(chat_id, "login_start")
	elif last_action == "login_name":
		users_list = file2.read_all(chat_id)

		if users_list['password'] == str(data):
	 		send_message(chat_id, "You are successfully log in!!\n")
	 		send_message(chat_id, "Hello " + str(users_list["login"]) + "!\n")
	 		send_message(chat_id, "Do you want to log out?(yes or no)")
	 		change_action(chat_id, "login_choise")

		elif users_list['password'] != str(data):
		 	send_message(chat_id, "Try Again!")
		 	send_message(chat_id, "Name:")
		 	change_action(chat_id, "login_start")

	elif last_action =="login_choise":
		if data == "yes" or data=="Yes":
			send_message(chat_id, "Good")
			send_message(chat_id, "Write 'login' if you want to log into your account or 'signin' to make an account")
			change_action(chat_id, "assd")
			get_action(chat_id, data)
		elif data =="no" or data=="No":
			change_action(chat_id, "assd")
			send_message(chat_id, "Ok:(")
			change_action(chat_id, "assd")
		else:
			send_message(chat_id, "I can't understand you :(")
	else:
		send_message(chat_id, "Name:")
		change_action(chat_id, "login_start")
			
	time.sleep(1)

def put_action(chat_id, action):
	actions_file = open("action.txt", "a")

	actions_file.write(str(chat_id) + " " + str(action) + "\n")

	actions_file.close()

def change_action(chat_id, action):
	actions_file = open("action.txt", "r")

	users_data = actions_file.readlines()
	for i in range(len(users_data)-1, -1, -1):
			split_info = users_data[i].split()

			print(split_info)

			if split_info[0] == str(chat_id):
				print(1)
				split_info[1] = (str(action)+"\n")

				users_data[i] = ' '.join(split_info) # convert split_info to str

				print(users_data)

				break
	actions_file.close()
	file = open("action.txt", "w")
	print(2)
	print(users_data)
	for row in users_data:
		print(row)
		file.write(row)

	file.close()
# def chech_user(chat_id):
	
@app.route("/", methods = ["POST"])
def proceed_request():
	updates = request.get_json()
	chat_id = updates["message"]["chat"]["id"]
	text = updates["message"]["text"]
	print(text, chat_id)
	if text == "/start":
		put_action(chat_id, "assd")
		get_action(chat_id, text)
	else:
		get_action(chat_id, text)

	pprint(updates)

	return jsonify(updates)

app.run()