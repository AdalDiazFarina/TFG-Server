# main.py
## Imports
import click
from app.services.user_service import UserService
from flask import Flask
from app.models.user import User, bcrypt
from app_context import create_app
from app.commands.db import commmand_db_create 
from app.commands.migrations import command_create_migration, command_update_migration, command_delete_migration

# Initialization of the app
app = create_app()

## Here the controllers are registered


@click.group()
def cli():
    pass

@cli.command()
@click.option('--run', '-r', help='Start the application')
def run(run):
    user = User(name='John Doe', nickname='johnny', email='john@example.com')
    user.set_password('1234')
    print(UserService.createUser(user))
    print(UserService.get(1))
    print(UserService.updateUser(User(name='John Doe', nickname='johnny', email='john22@example.com')))


@cli.command()
@click.option('--init', '-i', help='Create everything you need and run the application for the first time')
def init(init):
    commmand_db_create()
    app.run()

@cli.command()
@click.argument('description')
def create_migration(description):
    command_create_migration(description)

@cli.command()
@click.option('--update-migration', '-um', help='Update the database with the new migrations')
def update_migration(update_migration):
    command_update_migration()

@cli.command()
@click.argument('flag')
# @click.option('--delete-migration', '-dm', help='Delete a migration')
def delete_migration(flag):
    command_delete_migration(flag) 

if __name__ == '__main__':
    cli()