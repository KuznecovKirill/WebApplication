from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Магазин.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True) #id товара
    name = db.Column(db.String(50), nullable=False) # название
    price = db.Column(db.Integer, nullable=False) #цена
    #picture = db.Column(db.Text, unique=True, nullable=False) #картинка (возможно)


@app.route('/')
def mainMenu(): #функция главной страницы
    return render_template("mainMenu.html")

@app.route('/about')
def about(): 
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)