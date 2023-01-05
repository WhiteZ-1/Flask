from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
db.init_app(app)

with app.app_context():
    db = SQLAlchemy(app)
    
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route("/" ,methods= ["GET","POST"])
def home():
    if request.method == "POST":
        title = request.form["title"]
        desc = request.form["desc"]
        todo = Todo(title =title , desc=desc)
        db.session.add(todo)
        db.session.commit()

    allTodo= Todo.query.all()
    return render_template("index.html", allTodo=allTodo)

@app.route("/update")
def Update():
    allTodo= Todo.query.all()
    print(allTodo)
    return "this is page"

@app.route("/delete/<int:sno>")
def Delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=8000)




