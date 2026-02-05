from flask import Flask, render_template, request
from Base import FranchiseRequest, FranchisePhoto, Menu, get_db
from sqlalchemy.orm import Session
from pswd import *

app = Flask(__name__)
app.secret_key = coffee_secret_key
#дописать админку

#Узнать почему при смене '/' на '/home' получаю ошибку 404
@app.route('/', methods = ['GET'])
def home():
    return render_template('home.html')

#не работает форма? проверь html не id а name
@app.route('/franchise', methods = ['GET', 'POST'])
def get_franchise_info():
    coffeeshop_with_kitchen = []
    coffeeshop_without_kitchen = []
    db: Session = get_db()
    coffeeshop_with_kitchen = db.query(FranchisePhoto).filter_by(franchise_type = 'with_kitchen').all()
    coffeeshop_without_kitchen = db.query(FranchisePhoto).filter_by(franchise_type = "without_kitchen").all()
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        try:
            new_request = FranchiseRequest(
                full_name = full_name,
                phone = phone,
                email = email
            )
            db.add(new_request)
            db.commit()
        except Exception as e:
            db.rollback()
            print(f"ошибка сохранения заявки {e}")
    db.close
    return render_template('franchise.html', 
                           coffeeshop_with_kitchen = coffeeshop_with_kitchen, 
                           coffeeshop_without_kitchen = coffeeshop_without_kitchen)

#написать логику для карточек - готово
@app.route('/menu', methods = ['GET'])
def get_menu():
    croissants = []
    sandwichs = []
    salats = []
    coffee = []
    black_tea = []
    green_tea = []
    db: Session = get_db()
    croissants = db.query(Menu).filter_by(category = 'croissant').all()
    sandwichs = db.query(Menu).filter_by(category = 'sandwich').all()
    salats = db.query(Menu).filter_by(category = 'salat').all()
    coffee = db.query(Menu).filter_by(category = 'coffee').all()
    black_tea = db.query(Menu).filter_by(category = 'blacktea').all()
    green_tea = db.query(Menu).filter_by(category = 'greentea').all()
    raf_coffee = db.query(Menu).filter_by(category = 'rafcoffee').all()
    return render_template('menu.html', croissants = croissants, 
                           sandwichs = sandwichs, 
                           salats = salats,
                           coffee = coffee,
                           black_tea = black_tea,
                           green_tea = green_tea,
                           raf_coffee = raf_coffee)

@app.route('/story', methods = ['GET'])
def get_philosophy():
    return render_template('story.html')

if __name__ == '__main__':
    app.run(debug=True)