from flask import Flask

app = Flask(__name__)
@app.route('/')

def index(): #функция главной страницы
    return "Hello World"