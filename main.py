from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from cred import username, passwd, address, port, db_name
import datetime

app = Flask(__name__)
#app.config ['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://'+username+':'+passwd+'@'+address+':'+port+'/'+db_name

engine = create_engine('postgresql+psycopg2://'+username+':'+passwd+'@'+address+':'+port+'/'+db_name)
base = declarative_base()
#db = SQLAlchemy(app)

class users(base):
    __tablename__ = 'users'
    user_id = Column('id',Integer, primary_key = True)
    name = Column(String)
    middle_name = Column(String)
    bornDate = Column(Date)
    gender = Column(String)

class users_info(base):
    __tablename__ = 'users_info'
    user_id = Column('id', Integer, primary_key = True)
    education = Column(String)
    comment = Column(String)
    citizenship = Column(String)
#class users(db.Model):
#    user_id = db.Column('id', db.Integer, primary_key = True)
#    name = db.Column(db.String())
#    middle_name = db.Column(db.String())
#    bornDate = db.Column(db.Date)
#    gender = db.Column(db.String())
#
#class users_info(db.Model):
#    user_id = db.Column('id', db.Integer, primary_key = True)
#    education = db.Column(db.String())
#    comment = db.Column(db.String())
#    citizenship = db.Column(db.String())

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

        dateBorn = datetime.datetime.strptime(dateBorn, '%Y-%m-%d').date()

        new_user = users(name=username, middle_name=surname, gender=gender, bornDate=dateBorn)
        new_user_info = users_info(education=education, comment=comment, citizenship=citizen)

        Session = sessionmaker(engine)  
        session = Session()

        base.metadata.create_all(engine)
        session.add(new_user)
        session.add(new_user_info)
        session.commit()
        #db.session.add(new_user)
        #db.session.add(new_user_info)
        #db.session.commit()


    return render_template("picture.html")


if __name__ == '__main__':
#    db.create_all()
    app.run()
