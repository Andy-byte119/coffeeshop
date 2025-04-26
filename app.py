from flask import Flask, render_template, request
from Base import FranchiseRequest, session
from flask_admin import Admin

app = Flask(__name__)

#дописать админку

@app.route('/', methods = ['GET'])
def home():
    return render_template('home.html')

@app.route('/franchise', methods = ['GET', 'POST'])
def get_franhcise_info():
    if request.method == 'POST':
        full_name = request.form('name')
        phone = request.form('phone')
        email = request.form('email')
        new_request = FranchiseRequest(full_name = full_name, phone = phone, email = email)
        session.add(new_request)
        session.commit()
        return render_template('franchise.html', success = True)
    return render_template('franchise.html')

@app.route('/menu', methods = ['GET'])
def get_menu():
    return render_template('menu.html')

if __name__ == '__main__':
    app.run(debug=True)