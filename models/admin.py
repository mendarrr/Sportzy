import click
from models.games import Game
from models.equipment import Equipment
from models.players import Player
from models.coach import Coach
class Admin:
    def __init__(self, admin_role):
        self.admin_role = admin_role 

    # Prompt an admin for action to be performed
    def prompt_admin_for_action(self):
        print("")
        admin_action = click.prompt(f"What do you want to do?\n"
            + "\n".join(f"  {choice}" for choice in ['Create', 'Find By Id', 'Get all', 'Delete']),
            type=click.Choice(['Create', 'Find By Id', 'Get all', 'Delete']),
            show_choices=False,
        )
        return admin_action
    
    def manage_admin_action(self, admin_action):
        if admin_action.lower() == 'create':
            self.manage_create()
        elif admin_action.lower() == "delete":
            self.manage_delete()
        elif admin_action.lower() == "find by id":
            self.manage_find_by_id()
        elif admin_action.lower() == "get all":
            self.manage_get_all()

    # Adding new records to tables
    def manage_create(self):
        print("")
        click.echo("Fill all the inputs to create a new record in the database")
        # Map admin roles to their corresponding create functions
        admin_role_create_functions = {
            "games manager": Game.create_game,
            "player manager": Player.create_player,
            "equipment manager": Equipment.create_equipment,
            "coach manager": Coach.create_coach,
        }
        if self.admin_role in admin_role_create_functions:
            admin_role_create_functions[self.admin_role]()
        else:
            click.echo("Please enter a Valid admin role for Sportzy")

    # Deleting table records
    def manage_delete(self):
        if self.admin_role == "games manager":
            print("")
            game_id = input("Enter the ID of the game to be removed from Sportzy: ")
            Game.delete_game(game_id)
            pass
        elif self.admin_role == "player manager":
            print("")
            player_id = input("Enter the ID of the player to be removed from Sportzy: ")
            Player.delete_player(player_id)
            pass
        elif self.admin_role == "equipment manager":
             print("")
             equipment_id = input("Enter the ID of the equipment to be removed from Sportzy: ")
             Equipment.delete_equipment(equipment_id)
             pass
        elif self.admin_role == "coach manager":
             print("")
             coach_id = input("Enter the ID of the coach to be removed from Sportzy: ")
             Coach.delete_coach(coach_id)
             pass
        
    # Retrieving records from tables by id
    def manage_find_by_id(self):
        if self.admin_role == "games manager":
            print("")
            game_id = input("Enter the ID of the game you want to get details of: ")
            game_details = Game.get_game_by_id(game_id)
            print("")
            click.echo(f"These are the details for the game with id {game_id}")
            if game_details:
                print(f"ID: {game_details[0]}")
                print(f"Game Name: {game_details[1]}")
                print(f"Number of Players per team: {game_details[2]}")
                print(f"Game Coach: {game_details[3]}")
                print("")
            pass
        
        elif self.admin_role == "player manager":
             print("")
             player_id = input("Enter the ID of the player you want to get details of: ")
             player_details = Player.get_player_by_id(player_id)
             if player_details:
                print("")
                click.echo(f"These are the details for player with id {player_id}")
                print(f"ID: {player_details[0]}")
                print(f"Name: {player_details[1]}")
                print(f"Age: {player_details[5]}")
                print(f"Gender: {player_details[3]}")
                print("")
                pass
             
        elif self.admin_role == "equipment manager":
             print("")
             equipment_id = input("Enter the ID of the equipment you want to get details of: ")
             equipment_details = Equipment.get_equipment_by_id(equipment_id)
             if equipment_details:
                print("")
                click.echo(f"These are the details for equipment with id {equipment_id}")
                print(f"ID: {equipment_details[0]}")
                print(f"Name: {equipment_details[1]}")
                print(f"Game Name: {equipment_details[2]}")
                print("")
                pass

        elif self.admin_role == "coach manager":
             print("")
             coach_id = input("Enter the ID of the coach you want to get details of: ")
             coach_details = Coach.get_coach_by_id(coach_id)
             if coach_details:
                print("")
                click.echo(f"These are the details for coach with id {coach_id}")
                print(f"ID: {coach_details[0]}")
                print(f"Name: {coach_details[1]}")
                print(f"Year of Birth: {coach_details[2]}")
                print(f"Gender: {coach_details[3]}")
                print(f"Game Name: {coach_details[4]}")
                print("")
                pass
             
    def manage_get_all(self):
        if self.admin_role == "games manager":
            print("")
            click.echo("These are details for all games in Sportzy")
            all_games = Game.get_all_games()
            for game in all_games:
                print("ID:", game["id"])
                print("Game Name:", game["game_name"])
                print("Number of Players per team:", game["number_of_players"])
                print("Game Coach:", game["coach_name"])
                print("")
                pass

        if self.admin_role == "player manager":
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

        elif self.admin_role == "equipment manager":
             click.echo("These are details for all equipment in Sportzy")
             all_equipment = Equipment.get_all_equipment()
             for equipment in all_equipment:
                print("ID:", equipment["id"])
                print("Equipment Name:", equipment["equipment_name"])
                print("Game Name:", equipment["game_name"])
                print("")
                pass

        elif self.admin_role == "coach manager":
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
