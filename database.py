from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class TodoList(db.Model):
    __tablename__ = "todolist"
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=False)
    desc = db.Column(db.String(500), nullable=False, unique=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno}  - {self.title}"
