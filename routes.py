from flask import redirect, url_for, render_template
from services import TodoServices
from init import app


@app.route("/")
def home():
    todo_list = TodoServices.show_all()
    return render_template("homee.html", todo_list=todo_list)


@app.route("/add", methods=["POST", "GET"])
def add():
    TodoServices.create()
    return redirect(url_for('home'))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    TodoServices.delete(todo_id)
    return redirect(url_for("home"))


@app.route("/update", methods=["POST", "GET"])
def update():
    TodoServices.update()
    return redirect(url_for("home"))


@app.route("/update/<int:todo_id>")
def update_status(todo_id):
    TodoServices.status(todo_id)
    return redirect(url_for("home"))


@app.route("/up/<int:todo_id>", methods=["POST", "GET"])
def up_todo(todo_id):
    TodoServices.up_todo(todo_id)
    return redirect(url_for("home"))


@app.route("/down/<int:todo_id>", methods=["POST", "GET"])
def down_todo(todo_id):
    TodoServices.down_todo(todo_id)
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
