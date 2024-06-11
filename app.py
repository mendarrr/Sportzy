import click
from db.setup import create_tables
from db.connection import get_connection
from models.games import Game
from models.equipment import Equipment
from models.players import Player
from models.coach import Coach

def main():
    # Initialise the create tables function
    create_tables()

    # Prompt the user to enter name for welcoming
    user_name = click.prompt("Please enter your name", type=str)
    click.echo(f"Welcome to Sportzy {user_name}!")

    # Create a dictionary that will map user_roles to their respective roles
    roles = {
        "coach": [
            'Analysing Game Stats',
            'Developing Game plans',
            'Organising Game Events',
            'Making in-game decisions',
            'Motivating players'
        ],

        "player": [
            'Scoring goals for a team',
            'Preventing opposing team from scoring',
            'Tackling the opposing team',
            'Defending against the opposing team',
            'Being a midfielder'
        ]
    }

    # Prompt the user to select their role
    user_role = click.prompt("What is your role in Sportzy?", type=click.Choice(['Player', 'Coach'], case_sensitive=False))
    # Convert user_role to lowercase to match the keys for easy mapping
    role_to_lowercase = user_role.lower()
    click.echo(f"Your are a: {user_role}")

    # Display the list of roles based on the user's input
    if role_to_lowercase == "player":
        click.echo(f"{user_name}, your responsibilities are:")
        for role in roles["player"]:
            click.echo(f" - {role}")

    if role_to_lowercase == "coach":
        click.echo(f"{user_name}, your responsibilities are:")
        for role in roles["coach"]:
            click.echo(f" - {role}")

    games = {}
    

if __name__ == "__main__":
    main()