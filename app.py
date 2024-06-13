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

    # Functionality for Player user role
    if user_role == "player":
        click.echo(f"This is a list of games played in sportzy")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT game_name FROM games")
        games = cursor.fetchall()
        for game in games:
            click.echo(f"{game[0]}")
        game_name = click.prompt("Which game would you like to join?", type=str)
        cursor.execute("SELECT * FROM games WHERE game_name = ?", (game_name,))
        game_details = cursor.fetchone()
        if game_details:
            click.echo(f"Game Name: {game_details[1]}")
            click.echo(f"Number of Players per team: {game_details[2]}")  
            click.echo(f"Game Coach: {game_details[3]}")
        else:
            click.echo("Game not found")

    # Functionality for Coach user role
    elif user_role == "coach":
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT game_name FROM games")
        games = cursor.fetchall()
        for game in games:
            click.echo(f"{game[0]}")
        game_name = click.prompt("Which game do you coach?", type=str)
        cursor.execute("SELECT player_name FROM players WHERE game_name = ?", (game_name,))
        players = cursor.fetchall()
        if players:
            click.echo(f"The list of players you are coaching in {game_name} are:")
            for player in players:
                click.echo(f"{player[0]}")
        else:
            click.echo(f"No players found for {game_name}")
        
        player_name = click.prompt("Which player's details would you like to view?", type=str)
        cursor.execute("SELECT * FROM players WHERE player_name = ?", (player_name,))
        player_details = cursor.fetchone()
        if player_details:
            click.echo(f"Player Name: {player_details[1]}")
            click.echo(f"Age: {player_details[5]}")
            click.echo(f"Gender: {player_details[3]}")
        else:
            click.echo(f"The player chosen does not play {game_name}")


    elif user_role == "admin":
        admin_role = prompt_for_admin_role()
        admin_action = click.prompt(f"What do you want to do?\n"
        + "\n".join(f"  {choice}" for choice in ['Create', 'Get', 'Delete']),
        type=click.Choice(['Create', 'Get', 'Update', 'Delete']),
        show_choices=False,
        )

    # Map admin roles to their corresponding create functions
    admin_role_create_functions = {
        "games manager": Game.create_game,
        "player manager": Player.create_player,
        "equipment manager": Equipment.create_equipment,
        "coach manager": Coach.create_coach,
    }

    if admin_action.lower() == 'create':
        if admin_role in admin_role_create_functions:
            admin_role_create_functions[admin_role]()  
        else:
            click.echo("Please enter a Valid admin role for Sportzy")

    if admin_action.lower() == "delete":
        if admin_role == "games manager":
            game_id = input("Enter the ID of the game to be removed from Sportzy: ")
            Game.delete_game(game_id)
            pass
        elif admin_role == "player manager":
            player_id = input("Enter the ID of the player to be removed from Sportzy: ")
            Player.delete_player(player_id)
            pass
        elif admin_role == "equipment manager":
            equipment_id = input("Enter the ID of the equipment to be removed from Sportzy: ")
            Equipment.delete_equipment(equipment_id)
            pass
        elif admin_role == "coach manager":
            coach_id = input("Enter the ID of the coach to be removed from Sportzy: ")
            Coach.delete_coach(coach_id)
            pass

    else:
        click.echo("Please enter a Valid admin role for Sportzy")


if __name__ == "__main__":
    main()