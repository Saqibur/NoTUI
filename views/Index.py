from flask import render_template
from flask import render_template, redirect, url_for, request, session
from app import db
from models import Board, Note, Category

## TODO: Board updates and other changes. Not required right now for the functional demo.

def index():
    return render_template('index.html')

def all_boards():
    boards = Board.Board.query.all()

    return render_template(
            'all_boards.html',
            boards=boards,
        )

def all_notes():
    notes = Note.Note.query.all()

    return render_template(
            'all_notes.html',
            notes=notes,
        )
    
def update_board():
    notes = Note.Note.query.all()

    return redirect(url_for('all_notes'))

def create_board_page():
    return render_template('create_board.html')

def create_board():
    board_name        = str(request.form["board_name"])
    board_description = str(request.form["board_description"])

    new_board             = Board.Board()
    new_board.name        = board_name
    new_board.description = board_description

    db.session.add(new_board)
    db.session.commit()

    ## TODO: Change this to a valid homepage later.
    return redirect(url_for('index'))

def create_test_note_page():
    return render_template('create_test_note.html')

def create_test_note():
    note_content = str(request.form["note_content"])

    note          = Note.Note()
    note.board    = 1
    note.category = Category.Category.Doing.value
    note.content  = note_content
    note.x_coord  = 150
    note.y_coord  = 150

    db.session.add(note)
    db.session.commit()

    ## TODO: Change this to a valid homepage later.
    return redirect(url_for('index'))