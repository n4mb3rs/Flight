import json
import os

# Загрузка данных пользователей
def load_user_data():
    if os.path.exists("pass.json"):
        with open("pass.json", "r") as file:
            return json.load(file)
    else:
        return {}

# Сохранение данных пользователей
def save_user_data(user_data):
    with open("pass.json", "w") as file:
        json.dump(user_data, file)