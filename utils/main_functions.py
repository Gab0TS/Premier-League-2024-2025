from .player_stats import *
from .team_stats import *
from .charts import *

def show_options():
    global option_1, option_2
    print('*' * 40)
    print('\tMENU:')
    print('\t1. PLAYERS STATISTICS')
    print('\t2. TEAMS STATISTICS\n')
    try:
        option_1 = int(input('PLEASE, SELECT 1 OR 2 => '))
        if option_1 == 1:
            print('\t* PLAYERS STATISTICS *')
            print('\t1. Top scorers')
            print('\t2. Top assists')
            print('\t3. Top yellow cards')
            print('\t4. Top red cards')
            print('\t5. Most frequent nationalities')
            print('\t6. Players by nationality (provide the country)')
            option_2 = int(input("PLEASE, SELECT AN OPTION FROM 1 TO 6 => "))
            if option_2 not in [1,2,3,4,5,6]:
                print('Please select a valid option')
                show_options()

        elif option_1 == 2:
            print('\t*TEAMS STATISTICS*')
            print('\t1. Top team scorers')
            print('\t2. Top team assists')
            print('\t3. Most offsides by team')
            print('\t4. Most yellow cards by team')
            print('\t5. Most red cards by team')
            print('\t6. Teams with the most amount of players by nationality (provide the country)')
            print('\t7. Most frequent nationalities in a certain team (provide the team)')
            option_2 =int(input('PLEASE, SELECT AN OPTION FROM 1 TO 7 => '))
            if option_2 not in [1,2,3,4,5,6,7]:
                print('Please select a valid option')
                show_options()
        else:
            print('Please select a valid option')
            show_options()
    except ValueError:
        print('Please select a valid option')
        show_options()

    return option_1, option_2

def generate_output(option_1, option_2):
    if option_1 == 1:
        match option_2:
            case 1:
                label, values = top_scorers()
                title = 'Top scorers EPL 2024/2025'
                generate_bar_chart(label, values, title)
            case 2:
                label, values = top_assists()
                title = 'Top assists EPL 2024/2025'
                generate_bar_chart(label, values, title)
            case 3:
                label, values = top_yellow_cards()
                title = 'Top yellow cards EPL 2024/2025'
                generate_bar_chart(label, values, title)
            case 4:
                label, values = top_red_cards()
                title = 'Top red cards EPL 2024/2025'
                generate_bar_chart(label, values, title)
            case 5:
                label, values = top_nationalities()
                title = 'Most frequent nationalities EPL 2024/2025'
                generate_pie_chart(label, values, title)
            case 6:
                country = input('\tWhich country are you interested in? => ')
                if len(players_by_nationality(country)) > 0:
                    print(f'\t This are all the players from {country} that played in the EPL 2024/2025:')
                    print('\t',players_by_nationality(country))
                else:
                    print(f'\tNo players from {country} played in the EPL 2024/2025')
                    print('\tOr maybe you misspelled the country name, you can try again.️')
    elif option_1 == 2:
        match option_2:
            case 1:
                label, values = team_top_goals()
                title = 'Teams with the most goals scored EPL 2024/2025\n(No own goals)'
                generate_bar_chart(label, values, title)
            case 2:
                label, values = team_top_assists()
                title = 'Teams with the most assists EPL 2024/2025'
                generate_bar_chart(label, values, title)
            case 3:
                label, values = team_top_offsides()
                title = 'Teams with the most amount of offsides commited EPL 2024/2025'
                generate_bar_chart(label, values, title)
            case 4:
                label, values = team_top_yellow_cards()
                title = 'Teams with the most amount of yellow cards EPL 2024/2025\n(Only players)'
                generate_bar_chart(label, values, title)
            case 5:
                label, values = team_top_red_cards()
                title = 'Teams with the most amount of red cards EPL 2024/2025\n(Only players)'
                generate_bar_chart(label, values, title)
            case 6:
                country = input('\tWhich country are you interested in? => ')
                label, values = team_top_nationality(country)
                title = f'Teams with the most amount of players from {country}'
                generate_pie_chart(label, values, title)
            case 7:
                team = input('\tWhich team are you interested in? => ')
                label, values = nationalities_by_team(team)
                title = f'This are the most frequent nationalities in {team}'
                generate_pie_chart(label, values, title)