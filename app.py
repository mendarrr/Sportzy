import click
from db.connection import get_connection
from models.games import Game
from models.equipment import Equipment
from models.players import Player
from models.coach import Coach

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
        click.echo(f"These are the details for {game_name}")
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
            + "\n".join(f"  {choice}" for choice in ['Create', 'Find By Id', 'Get all', 'Delete']),
            type=click.Choice(['Create', 'Find By Id', 'Get all', 'Update', 'Delete']),
            show_choices=False,
        )

        # Map admin roles to their corresponding create functions
        admin_role_create_functions = {
            "games manager": Game.create_game,
            "player manager": Player.create_player,
            "equipment manager": Equipment.create_equipment,
            "coach manager": Coach.create_coach,
        }
        if admin_action is not None:
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

            if admin_action.lower() == "find by id":
                if admin_role == "games manager":
                    game_id = input("Enter the ID of the game to get details of: ")
                    game_details = Game.get_game_by_id(game_id)
                    if game_details:
                        click.echo(f"These are the details for game with id {game_id}")
                        print(f"ID: {game_details[0]}")
                        print(f"Name: {game_details[1]}")
                        print(f"Number of Players per team: {game_details[2]}")
                        print(f"Game Coach: {game_details[3]}")
                    pass
                elif admin_role == "player manager":
                    player_id = input("Enter the ID of the player to get details of: ")
                    player_details = Player.get_player_by_id(player_id)
                    if player_details:
                        click.echo(f"These are the details for player with id {player_id}")
                        print(f"ID: {player_details[0]}")
                        print(f"Name: {player_details[1]}")
                        print(f"Age: {player_details[5]}")
                        print(f"Gender: {player_details[3]}")
                    pass
                elif admin_role == "equipment manager":
                    equipment_id = input("Enter the ID of the equipment to get details of: ")
                    equipment_details = Equipment.get_equipment_by_id(equipment_id)
                    if equipment_details:
                        click.echo(f"These are the details for equipment with id {equipment_id}")
                        print(f"ID: {equipment_details[0]}")
                        print(f"Name: {equipment_details[1]}")
                        print(f"Game Name: {equipment_details[2]}")
                    pass
                elif admin_role == "coach manager":
                    coach_id = input("Enter the ID of the coach to get details of: ")
                    coach_details = Coach.get_coach_by_id(coach_id)
                    if coach_details:
                        click.echo(f"These are the details for coach with id {coach_id}")
                        print(f"ID: {coach_details[0]}")
                        print(f"Name: {coach_details[1]}")
                        print(f"Year of Birth: {coach_details[2]}")
                        print(f"Gender: {coach_details[3]}")
                        print(f"Game Name: {coach_details[4]}")
                    pass

            if admin_action.lower() == "get all":
                if admin_role == "games manager":
                    click.echo("These are details for all games in Sportzy")
                    all_games = Game.get_all_games()
                    for game in all_games:
                        print("ID:", game["id"])
                        print("Game Name:", game["game_name"])
                        print("Number of Players per team:", game["number_of_players"])
                        print("Game Coach:", game["coach_name"])
                        print("")
                    pass

                if admin_role == "player manager":
                    click.echo("These are details for all players in Sportzy")
                    all_players = Player.get_all_players()
                    for player in all_players:
                        print("ID:", player["id"])
                        print("Player Name:", player["player_name"])
                        print("Year of Birth:", player["year_of_birth"])
                        print("Gender:", player["gender"])
                        print("Game Name:", player["game_name"])
                        print("Age:", player["age"])
                        print("")
                        pass

                elif admin_role == "equipment manager":
                    click.echo("These are details for all equipment in Sportzy")
                    all_equipment = Equipment.get_all_equipment()
                    for equipment in all_equipment:
                        print("ID:", equipment["id"])
                        print("Equipment Name:", equipment["equipment_name"])
                        print("Game Name:", equipment["game_name"])
                        print("")
                    pass

                elif admin_role == "coach manager":
                    click.echo("These are details for all coaches in Sportzy")
                    all_coaches = Coach.get_all_coaches()
                    for coach in all_coaches:
                        print("ID:", coach["id"])
                        print("Coach Name:", coach["coach_name"])
                        print("Year of Birth:", coach["year_of_birth"])
                        print("Gender:", coach["gender"])
                        print("Game Name:", coach["game_name"])
                        print("Age:", coach["age"])
                        print("")
                    pass

            else:
                click.echo("Please enter a Valid admin role for Sportzy")


if __name__ == "__main__":
    main()