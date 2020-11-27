from flask import render_template
from flask import render_template, redirect, url_for, request, session
from app import db
from models import Board

## TODO: Board updates and other changes. Not required right now for the functional demo.

def index():
    return render_template('index.html')

def account_history(account_id):

        history = []
        for transaction in debit_transcations:
            history.append({
                "date": transaction.datetime_of_transaction.strftime("%c"),
                "description": transaction.description,
                "debit": '{:,.2f}'.format(transaction.amount),
                "credit": "-",
                "account": Account.Account.query.filter_by(id=transaction.credit_account).first().name if transaction.credit_account else "-",
            })
        for transaction in credit_transactions:
            history.append({
                "date": transaction.datetime_of_transaction.strftime("%c"),
                "description": transaction.description,
                "debit": "-",
                "credit": '{:,.2f}'.format(transaction.amount),
                "account": Account.Account.query.filter_by(id=transaction.debit_account).first().name if transaction.debit_account else "-",
            })
        print(history)
        return render_template(
            'account_history.html',
            history=history,
            account=account,
        )
    else:
        return redirect(url_for('login_page'))

def all_boards():
    boards = Board.Board.query.all()

    return render_template(
            'all_boards.html',
            boards=boards,
        )

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