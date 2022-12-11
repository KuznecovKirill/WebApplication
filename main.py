from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///Магазин.db'
db = SQLAlchemy
@app.route('/')
def mainMenu(): #функция главной страницы
    return render_template("mainMenu.html")

@app.route('/about')
def about(): 
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)