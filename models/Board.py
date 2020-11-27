from flask_sqlalchemy import SQLAlchemy
from app import db

class Board(db.Model):
    __tablename__ = "board"
    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name        = db.Column(db.String(120))
    description = db.Column(db.String(300))