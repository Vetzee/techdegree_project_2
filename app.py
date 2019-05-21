import constants
import os
import time
from copy import deepcopy

teams_1 = constants.TEAMS
teams = deepcopy(teams_1)
players_1 = constants.PLAYERS
players = deepcopy(players_1)

experienced_players = []
non_experienced_players = []

for player in players:
    player['height'] = int(player['height'][:2])
    player['guardians'] = player['guardians'].split(' and ')

    if player['experience'] == 'YES':
        player['experience'] = True
        experienced_players.append(player)
    else:
        player['experience'] = False
        non_experienced_players.append(player)

panthers = experienced_players[:3] + non_experienced_players[:3]
bandits = experienced_players[3:6] + non_experienced_players[3:6]
warriors = experienced_players[6:] + non_experienced_players[6:]
all_teams = [panthers, bandits, warriors]


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def a_menu():
    print("BASKETBALL TEAM STATS TOOL\n")
    print("-----******MENU******-----\n")
    print("Here are your choices:\n1) Display Team Stats\n2) Quit Stats Tool\n")


def first_option():
    while True:
        try:
            option_one = int(input("Enter an option > "))
            print()
            count = 1
            if option_one == 1:
                for team in teams:
                    print(f'{count}) {team}')
                    count += 1
                print()
                break

            elif option_one == 2:
                print('Thanks for using our Stats Tool, have a great day!')
                time.sleep(4)
                exit()

            elif option_one < 1 or option_one >= 3:
                print('Enter a valid option [1-2]')
                continue

        except ValueError:
            print("Invalid option, try again ")
            continue


def second_option():
    while True:
        try:
            option_two = int(input("Enter an option > "))
            if option_two < 1 or option_two >= 4:
                print('Enter a valid option [1-3]')
                continue

        except ValueError:
            print("That's not a valid option, try again")
            continue

        return option_two


def picked_team(option):

    team_player_names = []
    true_experience = 0
    false_experience = 0
    height_values = []
    player_guardians = []
    team_picked = None
    guardians_list = []

    if option == 1:
        team_picked = panthers
    elif option == 2:
        team_picked = bandits
    elif option == 3:
        team_picked = warriors

    for player in team_picked:
        team_player_names.append(player['name'])
        height_values.append(player['height'])
        player_guardians.append(player['guardians'])

        if player['experience']:
            true_experience += 1
        else:
            false_experience += 1

    for guardian in player_guardians:
        for item in guardian:
            guardians_list.append(item)

    parents = ', '.join(guardians_list)
    player_names = ', '.join(team_player_names)
    current_team = teams[option-1]

    print(f'Team: {current_team} Stats')
    print('-'*20)
    print(f'Total players: {len(all_teams[option-1])}\n')
    print(f'Players on team:\n{player_names}\n')
    print(f'Total number of experienced players: {true_experience}')
    print(f'Total number of inexperienced players: {false_experience}')
    average_height = round(sum(height_values) / len(height_values), 2)
    print(f'The average height of the players is {average_height} inches\n')
    print(f'Player Guardians:\n{parents}\n')
    input("Press ENTER to continue...")
    clear_screen()
    main()


def main():
    a_menu()
    first_option()
    picked_team(second_option())


if __name__ == '__main__':
    main()
