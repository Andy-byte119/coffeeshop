from flask import Flask, render_template, request, flash, redirect, url_for
from Base import FranchiseRequest, get_db
from sqlalchemy.orm import Session

app = Flask(__name__)
app.secret_key = 'Secret_Key_119'
#дописать админку

#Узнать почему при смене '/' на '/home' получаю ошибку 404
@app.route('/', methods = ['GET'])
def home():
    return render_template('home.html')

#не работает форма? проверь html не id а name
@app.route('/franchise', methods = ['GET', 'POST'])
def get_franchise_info():
    if request.method == 'POST':
        db: Session = get_db()
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
        finally:
            db.close
    return render_template('franchise.html')

@app.route('/menu', methods = ['GET'])
def get_menu():
    return render_template('menu.html')

@app.route('/story', methods = ['GET'])
def get_philosophy():
    return render_template('story.html')

if __name__ == '__main__':
    app.run(debug=True)