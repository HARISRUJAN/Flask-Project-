from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
 #source env/Scripts/activate
 
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:admin@localhost/Students'
 
db=SQLAlchemy(app)
 
class Student(db.Model):
  __tablename__='students'
  id=db.Column(db.Integer,primary_key=True)
  fname=db.Column(db.String(40))
  lname=db.Column(db.String(40))
  email=db.Column(db.String(40))
 
  def __init__(self,fname,lname,email):
    self.fname=fname
    self.lname=lname
    self.email=email
    
    
class FeedbackForm(db.Model):
  __tablename__='feedback'
  id=db.Column(db.Integer,primary_key=True)
  name=db.Column(db.String(40))
  email=db.Column(db.String(40))
  contact=db.Column(db.String(40))
  
  def __init__(self,name,contact,email):
    self.name=name
    self.contact=contact
    self.email=email
 
@app.route('/')
def index():
  return render_template('index.html')
 
@app.route('/submit', methods=['POST'])
def submit():
  fname= request.form['fname']
  lname=request.form['lname']
  email=request.form['email']
  student=Student(fname,lname,email)
  db.session.add(student)
  db.session.commit()
  
  return render_template('success.html', data=fname)
  
@app.route('/feedback', methods=['POST'])
def feedback():
  name= request.form['name']
  contact=request.form['contact']
  email=request.form['email']
  feedback=FeedbackForm(name,contact,email)
  db.session.add(feedback)
  db.session.commit()

  return render_template('feedback.html', data=email)
 
if __name__ == "__main__":
    app.run(debug=True)