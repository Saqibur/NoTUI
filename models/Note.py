from flask_sqlalchemy import SQLAlchemy
from app import db

class Note(db.Model):
    __tablename__ = "note"
    id       = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name     = db.Column(db.String(120))
    content  = db.Column(db.String(300))
    x_coord  = db.Column(db.Integer)
    y_coord  = db.Column(db.Integer)
    category = db.Column(db.Integer)

    board     = db.Column(db.Integer, db.ForeignKey('board.id'))
    board_rel = db.relationship("Board", cascade="delete", backref="board_note", foreign_keys=[board])