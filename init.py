import MySQLdb
db = MySQLdb.connect("localhost","your username","your password","CALENDAR")

curs = db.cursor()

curs.execute("CREATE TABLE USER(user_name varchar(12) NOT NULL ,password varchar(10), PRIMARY KEY(user_name))")
curs.execute(" CREATE TABLE books(book_id varchar(20) NOT NULL,name varchar(60) NOT NULL , author varchar(60) NOT NULL,PRIMARY KEY(book_id))")
curs.execute(" CREATE TABLE LIBRARY(user varchar(12) NOT NULL , book_val varchar(20) NOT NULL ,FOREIGN KEY(user) REFERENCES USER(user_name), FOREIGN KEY(book_val) REFERENCES books(book_id))")
curs.execute(" CREATE TABLE WANT(user varchar(12) NOT NULL , book_val varchar(20) NOT NULL ,FOREIGN KEY(user) REFERENCES USER(user_name), FOREIGN KEY(book_val) REFERENCES books(book_id))")
curs.execute("CREATE TABLE ISREADING(user varchar(12) NOT NULL , book_val varchar(20) NOT NULL ,FOREIGN KEY(user) REFERENCES USER(user_name), FOREIGN KEY(book_val) REFERENCES books(book_id));")
curs.execute("CREATE TABLE READING(user varchar(12) NOT NULL , book_val varchar(20) NOT NULL ,FOREIGN KEY(user) REFERENCES USER(user_name), FOREIGN KEY(book_val) REFERENCES books(book_id))")
curs.execute("CREATE TABLE RATING(user varchar(12) NOT NULL , book_val varchar(20) NOT NULL ,rating int NOT NULL,FOREIGN KEY(user) REFERENCES USER(user_name), FOREIGN KEY(book_val) REFERENCES books(book_id));")
curs.execute("CREATE TABLE FAVOURITES(user varchar(12) NOT NULL , book_val varchar(20) NOT NULL ,rating int NOT NULL,FOREIGN KEY(user) REFERENCES USER(user_name), FOREIGN KEY(book_val) REFERENCES books(book_id))")
db.commit()
db.close()