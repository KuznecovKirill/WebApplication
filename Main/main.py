from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')

def mainMenu(): #функция главной страницы
    return render_template("mainMenu.html")


if __name__ == "__main__":
    app.run(debug=True)