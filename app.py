from flask import Flask,render_template,request,redirect,url_for,flash
import sqlite3 as sql
app=Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    con=sql.connect("db_web.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from students")
    data=cur.fetchall()
    return render_template("index.html",datas=data)

@app.route("/add_user",methods=['POST','GET'])
def add_user():
    if request.method=='POST':
        name=request.form['name']
        surname=request.form['surname']
        date_of_birth=request.form['date_of_birth']
        class_s=request.form['class']
        address=request.form['address']
        gender=request.form['gender']
        con=sql.connect("db_web.db")
        cur=con.cursor()
        cur.execute("insert into students(NAME,SURNAME,DATE_OF_BIRTH,CLASS,ADDRESS,GENDER) values (?,?,?,?,?,?)",(name,surname,date_of_birth,class_s,address,gender))
        con.commit()
        flash('Student Added','success')
        return redirect(url_for("index"))
    return render_template("add_user.html")

@app.route("/edit_user/<string:uid>",methods=['POST','GET'])
def edit_user(uid):
    if request.method=='POST':
        name=request.form['name']
        surname=request.form['surname']
        date_of_birth=request.form['date_of_birth']
        class_s=request.form['class']
        address=request.form['address']
        gender=request.form['gender']
        con=sql.connect("db_web.db")
        cur=con.cursor()
        cur.execute("update students set NAME=?,SURNAME=?,DATE_OF_BIRTH=?,CLASS=?,ADDRESS=?,GENDER=? where UID=?",(name,surname,date_of_birth,class_s,address,gender,uid))
        con.commit()
        flash('Student Updated','success')
        return redirect(url_for("index"))
    con=sql.connect("db_web.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from students where UID=?",(uid,))
    data=cur.fetchone()
    return render_template("edit_user.html",datas=data)
    
@app.route("/delete_user/<string:uid>",methods=['GET'])
def delete_user(uid):
    con=sql.connect("db_web.db")
    cur=con.cursor()
    cur.execute("delete from students where UID=?",(uid,))
    con.commit()
    flash('User Deleted','warning')
    return redirect(url_for("index"))

@app.route("/active_user/<string:uid>/<string:checked>")
def active_user(uid,checked):
    print (checked)
    if checked == "True":
        update_val = "yes"
    else:
        update_val = "no"
    con=sql.connect("db_web.db")
    cur=con.cursor()
    cur.execute("update students set ACTIVE=? where UID=?",(update_val,uid,))
    con.commit()
    return redirect('/index')
    
if __name__=='__main__':
    app.secret_key='admin123'
    app.run(debug=True)