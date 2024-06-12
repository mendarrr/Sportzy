import click
from db.connection import get_connection
from models.games import Game
from models.equipment import Equipment
from models.players import Player
from models.coach import Coach
from models.admin import Admin

def main():
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
    user_role = click.prompt("What is your role in Sportzy?", type=click.Choice(['Player', 'Coach', 'Admin'], case_sensitive=False))
    # Convert user_role to lowercase to match the keys for easy mapping
    role_to_lowercase = user_role.lower()
    click.echo(f"Hey {user_role} {user_name}")

    # Display the list of roles based on the user's input
    if role_to_lowercase == "player":
        click.echo(f"{user_name}, your responsibilities are:")
        for role in roles["player"]:
            click.echo(f" - {role}")

    if role_to_lowercase == "coach":
        click.echo(f"{user_name}, your responsibilities are:")
        for role in roles["coach"]:
            click.echo(f" - {role}")

    if role_to_lowercase == "admin":
        admin_role = click.prompt(f"What kind of Manager are you {user_name}?\n"
            + "\n".join(f"  {choice}" for choice in ['Player Manager', 'Games Manager', 'Equipment Manager', 'Coach Manager']),
            type=click.Choice(['Player Manager', 'Games Manager', 'Equipment Manager', 'Coach Manager']),
            show_choices=False,
        )

        #Initialise create_tables function
        from db.setup import create_tables
        create_tables()

    if admin_role == "Games Manager":
        conn = get_connection()
        cursor = conn.cursor()
        # cursor.execute("""
        #     CREATE TABLE IF NOT EXISTS games
        #     (id INTEGER, game_name TEXT PRIMARY KEY, number_of_players INTEGER, coach_name TEXT, FOREIGN KEY(coach_name) REFERENCES coach(coach_name));
        # """)
        
        # Add a new new game
        game_name = input("Enter game name: ")
        number_of_players = int(input("Enter number of players: "))
        coach_name = input("Enter coach name: ")
        cursor.execute("INSERT INTO games (game_name, number_of_players, coach_name) VALUES (?,?,?)",
                        (game_name, number_of_players, coach_name))
        conn.commit()
        game_id = cursor.lastrowid
        print(f"Game created successfully! Game ID: {game_id}")
    elif admin_role == "Player Manager":
        # Add a new Game
        pass
    elif admin_role == "Equipment Manager":
        # Add a new Equipment
        pass
    elif admin_role == "Coach Manager":
        # Hire a new Coach
        pass

if __name__ == "__main__":
    main()