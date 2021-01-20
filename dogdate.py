import os
import sys
import click
from flask_migrate import Migrate, upgrade
from app import create_app, db
from app.models import User, Follow, Role, Permission, Post, Comment

basedir = os.path.abspath(os.path.dirname(__file__))

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Follow=Follow, Role=Role, Permission=Permission, Post=Post, Comment=Comment)


@app.cli.command()
def deploy():
    upgrade()

    Role.insert_roles()

    User.add_self_follows()
