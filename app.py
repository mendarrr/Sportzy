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

        # Check Authentication

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
        game_name = input("Enter game name: ")
        number_of_players = int(input("Enter number of players: "))
        coach_name = input("Enter coach name: ")
        cursor.execute("INSERT INTO games (game_name, number_of_players, coach_name) VALUES (?,?,?)",
                        (game_name, number_of_players, coach_name))
        conn.commit()
        game_id = cursor.lastrowid
        print(f"Game created successfully! Game ID: {game_id}")

    elif admin_role == "Player Manager":
        # Add a new Player
        conn = get_connection()
        cursor = conn.cursor()
        player_name = input("Enter player name: ")
        year_of_birth = int(input("Enter your year of Birth: "))
        gender = input("Enter your gender(F or M): ")
        game_name = input("Enter game played: ")
        cursor.execute("INSERT INTO players (player_name, year_of_birth, gender, game_name) VALUES (?,?,?,?)",
                       (player_name, year_of_birth, gender, game_name))
        conn.commit()
        player_id = cursor.lastrowid
        print(f"{user_role} {user_name}, the player, {player_name} has been added to the database successfully! Player ID is: {player_id}.")
        pass
    elif admin_role == "Equipment Manager":
        # Add a new Equipment
        conn = get_connection()
        cursor = conn.cursor()
        equipment_name = input("Enter equipment name: ")
        game_name = input(f"Enter the game that will use a {equipment_name}: ")
        cursor.execute("INSERT INTO equipment (equipment_name, game_name) VALUES (?,?)", 
                       (equipment_name, game_name))
        conn.commit()
        equipment_id = cursor.lastrowid
        print(f"{user_role} {user_name}, the equipment, {equipment_name} has been added to the database successfully! Equipment ID is: {equipment_id}.")
        pass
    elif admin_role == "Coach Manager":
        # Hire a new Coach
        conn = get_connection()
        cursor = conn.cursor()
        coach_name = input("Enter coach name: ")
        year_of_birth = int(input("Enter your year of Birth: "))
        gender = input("Enter your gender(F or M): ")
        game_name = input(f"Which game will Coach {coach_name} be coaching: ")
        cursor.execute("INSERT INTO coach (coach_name, year_of_birth, gender, game_name) VALUES (?,?,?,?)",
                       (coach_name, year_of_birth, gender, game_name))
        conn.commit()
        coach_id = cursor.lastrowid
        print(f"{user_role} {user_name}, the coach, {coach_name} has been added to the database successfully! Coach ID is: {coach_id}.")
        pass

if __name__ == "__main__":
    main()