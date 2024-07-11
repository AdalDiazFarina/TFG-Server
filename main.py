# main.py
## General Imports
import click
import time
from flask import Flask
from flask_restx import Swagger
from flask_cors import CORS
from flask_socketio import emit
from app_context import create_app, api
from app.commands.db import commmand_db_create, command_db_delete
from app.commands.migrations import command_create_migration, command_update_migration, command_delete_migration
from app.controllers.auth_controller import RegisterController, LoginController, RefreshController
from app.controllers.user_controller import UserController
from app.controllers.investment_profile_controller import InvestmentProfileController, InvestmentProfileWithoutIdController
from app.controllers.strategy_controller import StrategyController
from app.controllers.operation_controller import OperationController
from app.services.kafka_service import KafkaService

# Initialization of the app
app, socketio = create_app()
CORS(app)
api.init_app(app)
swagger = Swagger(api)

@socketio.on('run_task')
def handle_run_task(data):
    kafkaService = KafkaService()
    kafkaService.send('tasks', data)
    message = kafkaService.receive('completed_tasks')
    print('message: ', message)
    emit('task_completed', message)

@click.group()
def cli():
    pass

@cli.command()
def run():
    """Run the application"""
    if __name__ == '__main__':
        socketio.run(app, allow_unsafe_werkzeug=True)

@cli.command()
def init():
    """Build the application"""
    command_db_delete()
    commmand_db_create()
    ## Waiting for database connection
    time.sleep(3)
    command_update_migration()

@cli.command()
@click.argument('description')
def create_migration(description):
    """Create a new migration with the given description"""
    command_create_migration(description)

@cli.command()
def update_migration():
    """Update the database"""
    command_update_migration()

@cli.command()
@click.argument('flag')
def delete_migration(flag):
    """Removes a migration with the given flag"""
    command_delete_migration(flag) 

if __name__ == '__main__':
    cli()