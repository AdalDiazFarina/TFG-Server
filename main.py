# main.py
## General Imports
import click
import time
from flask import Flask
from flask_restx import Swagger
from flask_cors import CORS
from app_context import create_app, api
from app.commands.db import commmand_db_create, command_db_delete
from app.commands.migrations import command_create_migration, command_update_migration, command_delete_migration
from app.controllers.auth_controller import RegisterController, LoginController, RefreshController
from app.controllers.user_controller import UserController
from app.controllers.investment_profile_controller import InvestmentProfileController, InvestmentProfileWithoutIdController

# Initialization of the app
app = create_app()
CORS(app)
api.init_app(app)
swagger = Swagger(api)


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
    time.sleep(3)
    command_update_migration()

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