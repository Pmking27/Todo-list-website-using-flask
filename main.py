from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap
from database import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'duyasvfxjhcryt52sx3xqscytxx1ex'

Bootstrap(app)

db.init_app(app)
app.app_context().push()
db.create_all()


@app.route('/', methods=["GET", "POST"])
def home():
    todolist = TodoList.query.all()
    return render_template('index.html', Alltodo=todolist)


@app.route('/delete/<int:sno>', methods=["GET", "POST"])
def delete(sno):
    todo = TodoList.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')


@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = TodoList.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")

    todo = TodoList.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)


@app.route('/create', methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        todo = TodoList(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
