# main.py
## General Imports
import click
import time
from flask import Flask, Blueprint
from app_context import create_app
from app.commands.db import commmand_db_create, command_db_delete
from app.commands.migrations import command_create_migration, command_update_migration, command_delete_migration

#Controllers imports
from app.controllers.user_controller import user_controller
# Initialization of the app
app = create_app()

## Here the controllers are registered
app.register_blueprint(user_controller, url_prefix='/api')

@click.group()
def cli():
    pass

@cli.command()
@click.option('--run', '-r', help='Start the application')
def run(run):
    if __name__ == '__main__':
        app.run(debug=True)


@cli.command()
@click.option('--init', '-i', help='Create everything you need and run the application for the first time')
def init(init):
    command_db_delete()
    commmand_db_create()
    ## Waiting for database connection
    time.sleep(2)
    command_update_migration()
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
@click.option('--delete-migration', '-dm', help='Delete a migration')
def delete_migration(flag):
    command_delete_migration(flag) 

if __name__ == '__main__':
    cli()