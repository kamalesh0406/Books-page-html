from flask import Flask ,request ,render_template ,redirect , url_for , session , flash
import MySQLdb
from datetime import datetime
from datetime import timedelta
import json
date_value=0;


db = MySQLdb.connect("localhost","your username","your password","BOOKS")

curs = db.cursor() 

app = Flask(__name__)
app.secret_key = 'GHESGFHFH'

@app.before_request
def make_session_permanent():
    session.permanent = False

@app.route("/")
def welcome():
	return render_template('homepage.html')

@app.route("/activity",methods=['GET','POST'])
def activity():
	if request.method== 'POST':
		dict = {}
		want = []
		sql="SELECT * FROM WANT WHERE user='%s'"%(session['username'])
		curs.execute(sql)
		data = curs.fetchall()

		for row in data:
			sql2 = "SELECT * FROM books WHERE book_id='%s'"%(row[1])
			curs.execute(sql2)
			new_data = curs.fetchall()
			for values in new_data:
				want.append(values[1:])
		isreading = []
		sql="SELECT * FROM ISREADING WHERE user='%s'"%(session['username'])
		curs.execute(sql)
		data = curs.fetchall()

		for row in data:
			sql2 = "SELECT * FROM books WHERE book_id='%s'"%(row[1])
			curs.execute(sql2)
			new_data = curs.fetchall()
			for values in new_data:
				isreading.append(values[1:])
		read=[]
		sql="SELECT * FROM READING WHERE user='%s'"%(session['username'])
		curs.execute(sql)
		data = curs.fetchall()

		for row in data:
			sql2 = "SELECT * FROM books WHERE book_id='%s'"%(row[1])
			curs.execute(sql2)
			new_data = curs.fetchall()
			for values in new_data:
				read.append(values[1:])
		fav = []
		sql="SELECT * FROM FAVOURITES WHERE user='%s'"%(session['username'])
		curs.execute(sql)
		data = curs.fetchall()

		for row in data:
			sql2 = "SELECT * FROM books WHERE book_id='%s'"%(row[1])
			curs.execute(sql2)
			new_data = curs.fetchall()
			for values in new_data:
				fav.append(values[1:])
		rating= []
		sql="SELECT * FROM RATING WHERE user='%s'"%(session['username'])
		curs.execute(sql)
		data = curs.fetchall()

		for row in data:
			sql2 = "SELECT * FROM books WHERE book_id='%s'"%(row[1])
			curs.execute(sql2)
			new_data = curs.fetchall()
			for values in new_data:
				rating.append(values[1:]+(row[2],))
		return (json.dumps({'want':want,'isreading':isreading,'read':read,'favourite':fav,'rating':rating}))
@app.route("/library",methods=['GET','POST'])
def library():
	if request.method == 'POST':
		sql = "SELECT * FROM LIBRARY WHERE user='%s'"%(session['username'])
		curs.execute(sql)
		data = curs.fetchall()
		books=[]
		for row in data:
			print (row)
			sql2 = "SELECT * FROM BOOKS WHERE book_id='%s'"%(row[1])
			curs.execute(sql2)
			new_data = curs.fetchall()
			books.append(new_data[0])
		return (json.dumps(books))
		
@app.route("/book",methods=['GET','POST'])
def book():
	if request.method == 'GET':
		return (render_template('bookspage.html'))
	if request.method == 'POST':

		if request.form['activity']=='lib':
			sql2 = 'INSERT INTO BOOKS(book_id,name,author) VALUES("%(id)s","%(name)s","%(author)s")'%(request.form)
			sql3 = 'INSERT INTO LIBRARY(user,book_val) VALUES("%s","%s")'%(session['username'],request.form['id'])

			try:
				curs.execute(sql2)
			except MySQLdb.IntegrityError:
				db.rollback()
				pass
			curs.execute(sql3)
			db.commit()
			return(json.dumps({'status':'ok'}))
		elif request.form['activity']=='want':
			sql2 = 'INSERT INTO BOOKS(book_id,name,author) VALUES("%(id)s","%(name)s","%(author)s")'%(request.form)
			sql3 = 'INSERT INTO WANT(user,book_val) VALUES("%s","%s")'%(session['username'],request.form['id'])

			try:
				curs.execute(sql2)
			except MySQLdb.IntegrityError:
				db.rollback()
				pass
			curs.execute(sql3)
			db.commit()
			return(json.dumps({'status':'ok'}))
		elif request.form['activity']=='reading':
			sql2 = 'INSERT INTO BOOKS(book_id,name,author) VALUES("%(id)s","%(name)s","%(author)s")'%(request.form)
			sql3 = 'INSERT INTO ISREADING(user,book_val) VALUES("%s","%s")'%(session['username'],request.form['id'])

			try:
				curs.execute(sql2)
			except MySQLdb.IntegrityError:
				db.rollback()
				pass
			curs.execute(sql3)
			db.commit()
			return(json.dumps({'status':'ok'}))
		elif request.form['activity']=='read':
			sql2 = 'INSERT INTO BOOKS(book_id,name,author) VALUES("%(id)s","%(name)s","%(author)s")'%(request.form)
			sql3 = 'INSERT INTO READING(user,book_val) VALUES("%s","%s")'%(session['username'],request.form['id'])

			try:
				curs.execute(sql2)
			except MySQLdb.IntegrityError:
				db.rollback()
				pass
			curs.execute(sql3)
			db.commit()
			return(json.dumps({'status':'ok'}))
		elif request.form['activity']=='fav':
			sql2 = 'INSERT INTO BOOKS(book_id,name,author) VALUES("%(id)s","%(name)s","%(author)s")'%(request.form)
			sql3 = 'INSERT INTO FAVOURITES(user,book_val) VALUES("%s","%s")'%(session['username'],request.form['id'])

			try:
				curs.execute(sql2)
			except MySQLdb.IntegrityError:
				db.rollback()
				pass
			curs.execute(sql3)
			db.commit()
			return(json.dumps({'status':'ok'}))
		elif request.form['activity']=='rating':
			sql2 = 'INSERT INTO BOOKS(book_id,name,author) VALUES("%(id)s","%(name)s","%(author)s")'%(request.form)
			sql3 = 'INSERT INTO RATING(user,book_val,rating) VALUES("%s","%s",%d)'%(session['username'],request.form['id'],int(request.form['rating']))

			try:
				curs.execute(sql2)
			except MySQLdb.IntegrityError:
				db.rollback()
				pass
			curs.execute(sql3)
			db.commit()
			return(json.dumps({'status':'ok'}))
		else:
			return(json.dumps({'status':'ok'}))		
@app.route("/login",methods=['GET','POST'])
def login():
	error = None	
	if request.method =="GET":
		return render_template('loginpage.html',error = error)
	if request.method == "POST":
		values = request.form
		sql = "SELECT * FROM USER"
		try:
			curs.execute(sql)
			result = curs.fetchall()
			if len(result)!=0:
				for row in result:
					if row[0]== values['username']:
						if row[1] == values['password']:
							session['username'] = values['username'];
							flash("You have succesfully logged in")
							return redirect(url_for('book'))
							
				else:
					error ="Incorrect Login Credentials"
					return render_template('loginpage.html',error = error)
			else:
				error ="Create An Account"
				return render_template('loginpage.html',error = error)
		except ValueError:
			pass

@app.route("/signup",methods=['GET','POST'])
def signup():
	error =None
	if request.method == "GET":
		return render_template('signup.html',error=error)

	if request.method == "POST":
		values = request.form;
		sql ="INSERT INTO USER(user_name,password) VALUES('%s','%s')"%(values['username'],values['password'])
		
		try:
			curs.execute(sql);

			db.commit();
			return redirect(url_for('welcome'))
		except MySQLdb.IntegrityError:
			error="Username Already Taken"
			return render_template('signup.html',error=error)
			db.rollback()
	


if __name__ =="__main__":
	app.run(debug=True)
