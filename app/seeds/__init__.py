from flask.cli import AppGroup

from app.seeds.artifacts import seed_artifacts, undo_artifacts
from app.seeds.user_artifacts import seed_user_artifacts, undo_user_artifacts
from .users import seed_users, undo_users

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_artifacts()
    seed_user_artifacts()


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_artifacts()
    undo_user_artifacts()
