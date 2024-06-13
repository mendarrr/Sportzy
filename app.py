import click
from db.connection import get_connection
from models.admin import Admin

@click.group()
def cli():
    pass
def sportzy():
    pass

def welcome_back_to_sportzy():
    # The entry point of the Sportzy CLI app
    user_name = click.prompt("Please enter your name", type=str)
    click.echo(f"Hello {user_name}, welcome back to Sportzy!")
    print("")

def prompt_for_user_role():
    user_role = click.prompt("What is your role in Sportzy?", type=click.Choice(['Player', 'Coach', 'Admin'], case_sensitive=False))
    return user_role.lower()

def handle_user_role(user_role):
    if user_role == "admin":
        admin()
        pass
    elif user_role == "player":
        player()
        pass
    elif user_role == "coach":
        coach()
        pass

def prompt_for_admin_role():
    admin_role = click.prompt(f"What type of Manager are you?\n"
        + "\n".join(f"  {choice}" for choice in ['Games Manager', 'Coach Manager', 'Player Manager', 'Equipment Manager']),
        type=click.Choice(['Games Manager', 'Coach Manager', 'Player Manager', 'Equipment Manager']),
        show_choices=False,
    )
    return admin_role.lower()

@cli.command()
def player():
    welcome_back_to_sportzy()
    # Functionality for Player role"""
    click.echo(f"This is a list of games played in sportzy")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT game_name FROM games")
    games = cursor.fetchall()
    for game in games:
        click.echo(f"{game[0]}")
        
    print('')
    game_name = click.prompt("Which game would you like to join?", type=str)
    print("")
    click.echo(f"These are the details for {game_name}")
    cursor.execute("SELECT * FROM games WHERE game_name =?", (game_name,))
    game_details = cursor.fetchone()
    if game_details:
        click.echo(f"Game Name: {game_details[1]}")
        click.echo(f"Number of Players per team: {game_details[2]}")  
        click.echo(f"Game Coach: {game_details[3]}")
        print("")
    else:
        click.echo("Game not found")

@cli.command()
def coach():
    welcome_back_to_sportzy()
    # Functionality for the Coach role
    print("")
    click.echo("This is a list of games played in Sportzy")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT game_name FROM games")
    games = cursor.fetchall()
    for game in games:
        click.echo(f"{game[0]}")

    print("")
    game_name = click.prompt("Which game do you coach?", type=str)
    cursor.execute("SELECT player_name FROM players WHERE game_name =?", (game_name,))
    players = cursor.fetchall()
    if players:
        print("")
        click.echo(f"The list of players you are coaching in {game_name} are:")
        for player in players:
            click.echo(f"{player[0]}")
        print("")
        player_name = click.prompt("Which player's details would you like to view?", type=str)
        cursor.execute("SELECT * FROM players WHERE player_name =?", (player_name,))
        player_details = cursor.fetchone()

    else:
        print("")
        click.echo(f"No players found for {game_name}")
        
    if player_details:
        print("")
        click.echo(f"These are the details for {player_details[1]}")
        click.echo(f"Player Name: {player_details[1]}")
        click.echo(f"Age: {player_details[5]}")
        click.echo(f"Gender: {player_details[3]}")
    else:
        click.echo(f"The player chosen is either a NON-SPORTZY player or does not play {game_name}")
        print("")
        print("")

@cli.command()
def admin():
    welcome_back_to_sportzy()
    # Functionality for the Admin role
    admin_role = prompt_for_admin_role()
    admin = Admin(admin_role)
    admin_action = admin.prompt_admin_for_action()
    admin.manage_admin_action(admin_action)

if __name__ == "__main__":
    cli()