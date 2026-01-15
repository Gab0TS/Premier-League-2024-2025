import csv
from pathlib import Path

CSV_PATH = Path(__file__).parent / 'epl_player_stats_24_25.csv'

def team_top_goals():
    with open(CSV_PATH, encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        team_goals = dict({})
        for row in reader:
            club = row['Club']
            goals = int(row['Goals'])
            try:
                team_goals[club] += goals
            except KeyError:
                team_goals[club] = goals
        team_goals = dict(sorted(team_goals.items(), key = lambda x: x[0], reverse = False))
        team_goals = dict(sorted(team_goals.items(), key = lambda x: x[1], reverse = True))
        teams = list(team_goals.keys())[:5]
        goals = list(team_goals.values())[:5]
    return teams , goals

def team_top_assists():
    with open(CSV_PATH, encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        team_assists = dict({})
        for row in reader:
            club = row['Club']
            assists = int(row['Assists'])
            try:
                team_assists[club] += assists
            except KeyError:
                team_assists[club] = assists
        team_assists = dict(sorted(team_assists.items(), key = lambda x: x[0], reverse = False))
        team_assists = dict(sorted(team_assists.items(), key = lambda x: x[1], reverse = True))
        teams = list(team_assists.keys())[:5]
        assists = list(team_assists.values())[:5]
        return teams , assists

def team_top_offsides():
    with open(CSV_PATH, encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        team_offsides = dict({})
        for row in reader:
            club = row['Club']
            offsides = int(row['Offsides'])
            try:
                team_offsides[club] += offsides
            except KeyError:
                team_offsides[club] = offsides
        team_offsides = dict(sorted(team_offsides.items(), key = lambda x: x[0], reverse = False))
        team_offsides = dict(sorted(team_offsides.items(), key = lambda x: x[1], reverse = True))
        teams = list(team_offsides.keys())[:5]
        offsides = list(team_offsides.values())[:5]
    return teams , offsides

def team_top_yellow_cards():
    with open(CSV_PATH, encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        team_yellow_cards = dict({})
        for row in reader:
            club = row['Club']
            yellow_cards = int(row['Yellow Cards'])
            try:
                team_yellow_cards[club] += yellow_cards
            except KeyError:
                team_yellow_cards[club] = yellow_cards
        team_yellow_cards = dict(sorted(team_yellow_cards.items(), key = lambda x: x[0], reverse = False))
        team_yellow_cards = dict(sorted(team_yellow_cards.items(), key = lambda x: x[1], reverse = True))
        teams = list(team_yellow_cards.keys())[:5]
        yellow_cards = list(team_yellow_cards.values())[:5]
    return teams , yellow_cards

def team_top_red_cards():
    with open(CSV_PATH, encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        team_red_cards = dict({})
        for row in reader:
            club = row['Club']
            red_cards = int(row['Red Cards'])
            try:
                team_red_cards[club] += red_cards
            except KeyError:
                team_red_cards[club] = red_cards
        team_red_cards = dict(sorted(team_red_cards.items(), key = lambda x: x[0], reverse = False))
        team_red_cards = dict(sorted(team_red_cards.items(), key = lambda x: x[1], reverse = True))
        teams = list(team_red_cards.keys())[:5]
        red_cards = list(team_red_cards.values())[:5]
    return teams , red_cards

def team_top_nationality(country):
    with open(CSV_PATH, encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        team_nationality = dict({})
        for row in reader:
            club = row['Club']
            nationality = row['Nationality']
            if nationality == country:
                try:
                    team_nationality[club] += 1
                except KeyError:
                    team_nationality[club] = 1
        team_nationality = dict(sorted(team_nationality.items(), key = lambda x: x[0], reverse = False))
        team_nationality = dict(sorted(team_nationality.items(), key = lambda x: x[1], reverse = True))
        teams = list(team_nationality.keys())[:5]
        counter = list(team_nationality.values())[:5]
    return teams , counter

def nationalities_by_team(team):
    with open(CSV_PATH, encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        nationalities = dict({})
        for row in reader:
            nationality = row['Nationality']
            if row['Club'] == team:
                try:
                    nationalities[nationality] += 1
                except KeyError:
                    nationalities[nationality] = 1
        nationalities = dict(sorted(nationalities.items(), key = lambda x: x[0], reverse = False))
        nationalities = dict(sorted(nationalities.items(), key = lambda x: x[1], reverse = True))
        country = list(nationalities.keys())[:5]
        counter = list(nationalities.values())[:5]
    return country , counter


# teams, goals = team_top_goals()
# print(teams)
# print(goals)

# teams, assists = team_top_assists()
# print(teams)
# print(assists)

# teams, offsides = team_top_offsides()
# print(teams)
# print(offsides)


# teams, yellow_cards = team_top_yellow_cards()
# print(teams)
# print(yellow_cards)

# teams, red_cards = team_top_red_cards()
# print(teams)
# print(red_cards)

# teams, counter = team_top_nationality('South Korea')
# print(teams)
# print(counter)

# country, counter = nationalities_by_team('Liverpool')
# print(country)
# print(counter)