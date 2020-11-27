from flask import Flask, render_template, send_file, request, redirect, url_for, session
# from flask_sqlalchemy import SQLAlchemy
# import os
# import random


###### BOOTSTRAP APP AND DB ########
app = Flask(__name__)
# print("Welcome to : %s" % __name__)
app.secret_key = b'notuisecretkey'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notui.db'

db = SQLAlchemy(app)

# from models import Liability
# from models import Transaction
# from models import Account

####################################

from views import Index
# from views import Index, Login, User, Account, Liability
## Routes ##
app.add_url_rule('/', view_func=Index.index)
app.add_url_rule('/all_boards', view_func=Index.all_boards)


# app.add_url_rule('/account_history/<account_id>', view_func=Account.account_history)
# app.add_url_rule('/liability_transaction/<liability_id>', view_func=Liability.liability_transaction_page)



app.add_url_rule('/create_board', view_func=Index.create_board, methods=["POST"])
# app.add_url_rule('/create_account', view_func=Account.create_account, methods=["POST"])
# app.add_url_rule('/create_transaction', view_func=User.create_transaction, methods=["POST"])
# app.add_url_rule('/create_liability', view_func=Liability.create_liability, methods=["POST"])
# app.add_url_rule('/clear_liability', view_func=Liability.clear_liability, methods=["POST"])
# app.add_url_rule('/validate_user', view_func=Login.validate_user, methods=["POST"])