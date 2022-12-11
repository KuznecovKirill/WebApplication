from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Магазин.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True) #id товара
    name = db.Column(db.String(50), nullable=False) # название
    price = db.Column(db.Integer, nullable=False) #цена
    #picture = db.Column(db.Text, unique=True, nullable=False) #картинка (возможно)
    def __repr__(self):
        return self.name

with app.app_context():
    db.create_all()

@app.route('/')
def mainMenu(): #функция главной страницы
    products = Product.query.all()
    return render_template("mainMenu.html", data=products)

@app.route('/about')
def about(): 
    return render_template("about.html")

@app.route('/addProduct', methods=['POST','GET'])
def addProduct():
    if request.method == "POST":
        nameProduct = request.form['name']
        price = request.form['price']
        product = Product(name=nameProduct, price = price)
        try:
            db.session.add(product)
            db.session.commit()
            return redirect('/') # возращает пользователя на главную страницу
        except:
            return "Error в вводе"
    else:
        return render_template("addProduct.html")    

if __name__ == "__main__":
    app.run(debug=True)