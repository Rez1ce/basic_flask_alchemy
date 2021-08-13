from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'

db = SQLAlchemy(app)
class users(db.Model):
    user_id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    middle_name = db.Column(db.String(100))
    bornDate = db.Column(db.String(100))
    gender = db.Column(db.String(100))

class users_info(db.Model):
    user_id = db.Column('id', db.Integer, primary_key = True)
    education = db.Column(db.String(100))
    comment = db.Column(db.String(100))
    citizenship = db.Column(db.String(100))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('userName')
        surname = request.form.get('userSurname')
        gender = request.form.get('gender')
        citizen = request.form.get('citizen')
        dateBorn = request.form.get('dateBorn')
        education = request.form.get('education')
        comment = request.form.get('comment')

        new_user = users(name=username, middle_name=surname, gender=gender, bornDate=dateBorn)
        new_user_info = users_info(education=education, comment=comment, citizenship=citizen)
        db.session.add(new_user)
        db.session.add(new_user_info)
        db.session.commit()


    return render_template("picture.html")


if __name__ == '__main__':
    db.create_all()
    app.run()
