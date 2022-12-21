from init import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    status = db.Column(db.Boolean)
    priorities = db.Column(db.String(15))
    second_id = db.Column(db.Integer)

    def __init__(self, title, status, priorities, second_id):
        self.title = title
        self.status = status
        self.priorities = priorities
        self.second_id = second_id