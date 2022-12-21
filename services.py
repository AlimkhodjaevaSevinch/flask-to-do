from flask import request
from models import Todo
from init import db


class TodoServices:
    @staticmethod
    def show_all():
        todo_list = Todo.query.all()
        return todo_list

    @staticmethod
    def second_id():
        todo = Todo.query.order_by(Todo.id.desc()).first()
        if todo:
            return todo.id + 1
        return 1

    @staticmethod
    def create():
        title = request.form.get("title")
        priorities = request.form.get("priorities")
        second_id = TodoServices.second_id()
        new_todo = Todo(title=title, status=False,
                        priorities=priorities, second_id=second_id)
        db.session.add(new_todo)
        db.session.commit()
        return new_todo

    @staticmethod
    def delete(todo_id):
        del_todo = Todo.query.filter_by(id=todo_id).first()
        db.session.delete(del_todo)
        db.session.commit()
        return del_todo

    @staticmethod
    def update():
        newtodo = request.form.get("newtodo")
        oldtodo = request.form.get("oldtodo")
        todo = Todo.query.filter_by(title=oldtodo).first()
        todo.title = newtodo
        db.session.commit()

    @staticmethod
    def status(todo_id):
        todo = Todo.query.filter_by(id=todo_id).first()
        todo.status = not todo.status
        db.session.commit()

    @staticmethod
    def up_todo(todo_id):
        todo = Todo.query.filter_by(id=todo_id)\
            .first()
        up_todo = Todo.query.filter(Todo.second_id < todo.second_id) \
            .order_by(Todo.second_id.desc()).first()
        if up_todo is None:
            return 'None'
        else:
            up_todo.second_id, todo.second_id, up_todo.title, todo.title, \
                up_todo.priorities, todo.priorities, \
                up_todo.status, todo.status = \
                todo.second_id, up_todo.second_id, \
                todo.title, up_todo.title, \
                todo.priorities, up_todo.priorities, \
                todo.status, up_todo.status
            db.session.commit()
        return up_todo.second_id, todo.second_id

    @staticmethod
    def down_todo(todo_id):
        todo = Todo.query.filter_by(id=todo_id).first()
        down_todo = Todo.query.filter(Todo.second_id > todo.second_id) \
            .order_by(Todo.second_id.asc()).first()
        if down_todo is None:
            return 'None'
        else:
            down_todo.second_id, todo.second_id, down_todo.title, todo.title, \
                down_todo.priorities, todo.priorities, \
                down_todo.status, todo.status = \
                todo.second_id, down_todo.second_id, \
                todo.title, down_todo.title, \
                todo.priorities, down_todo.priorities, \
                todo.status, down_todo.status
            db.session.commit()
        return down_todo.second_id, todo.second_id