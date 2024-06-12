import click
from db.connection import get_connection
from models.games import Game
from models.equipment import Equipment
from models.players import Player
from models.coach import Coach
from models.admin import Admin

#Prompt the user to input his/her role in Sportzy
def prompt_for_user_role():
    user_role = click.prompt("What is your role in Sportzy?", type=click.Choice(['Player', 'Coach', 'Admin'], case_sensitive=False))
    return user_role.lower()

#Prompt an admin for their specific managerial role
def prompt_for_admin_role():
    admin_role = click.prompt(f"What type of Manager are you?\n"
        + "\n".join(f"  {choice}" for choice in ['Player Manager', 'Games Manager', 'Equipment Manager', 'Coach Manager']),
        type=click.Choice(['Player Manager', 'Games Manager', 'Equipment Manager', 'Coach Manager']),
        show_choices=False,
    )
    return admin_role.lower()

def main():
    # Entry of my CLI App
    user_name = click.prompt("Please enter your name", type=str)
    click.echo(f"Welcome to Sportzy {user_name}!")

    user_role = prompt_for_user_role()
    click.echo(f"Hey {user_role} {user_name}")

    if user_role == "admin":
        admin_role = prompt_for_admin_role()
        conn = get_connection()
        cursor = conn.cursor()
    
        # Map admin roles to their corresponding create functions
        admin_role_functions = {
            "games manager": Game.create_game,
            "player manager": Player.create_player,
            "equipment manager": Equipment.create_equipment,
            "coach manager": Coach.create_coach,
        }
        
        if admin_role in admin_role_functions:
            admin_role_functions[admin_role]()
        else:
            click.echo("Please enter a Valid admin role for Sportzy")

if __name__ == "__main__":
    main()