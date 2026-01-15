import csv
from pathlib import Path

CSV_PATH = Path(__file__).parent / 'epl_player_stats_24_25.csv'

def top_scorers():
    with open(CSV_PATH, encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        player_goals = []
        for row in reader:
            pg = {'Player Name': row['Player Name'], 'Goals': int(row['Goals'])}
            player_goals.append(pg)
        player_goals = sorted(player_goals, key=lambda k: k['Player Name'], reverse=False)
        player_goals = sorted(player_goals, key=lambda k: k['Goals'], reverse=True)
        player_goals = player_goals[:5]
        players = list(map(lambda k: k['Player Name'], player_goals))
        goals = list(map(lambda k: k['Goals'], player_goals))
    return players, goals

def top_assists():
    with open(CSV_PATH, encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        player_assists = []
        for row in reader:
            pa = {'Player Name': row['Player Name'], 'Assists': int(row['Assists'])}
            player_assists.append(pa)
        player_assists = sorted(player_assists, key=lambda k: k['Player Name'], reverse=False)
        player_assists = sorted(player_assists, key=lambda k: k['Assists'], reverse=True)
        player_assists = player_assists[:5]
        players = list(map(lambda k: k['Player Name'], player_assists))
        assists = list(map(lambda k: k['Assists'], player_assists))
    return players, assists

def top_yellow_cards():
    with open(CSV_PATH, encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        player_yellow_cards = []
        for row in reader:
            pyc = {'Player Name': row['Player Name'], 'Yellow Cards': int(row['Yellow Cards'])}
            player_yellow_cards.append(pyc)
        player_yellow_cards = sorted(player_yellow_cards, key=lambda k: k['Player Name'], reverse=False)
        player_yellow_cards = sorted(player_yellow_cards, key=lambda k: k['Yellow Cards'], reverse=True)
        player_yellow_cards = player_yellow_cards[:5]
        players = list(map(lambda k: k['Player Name'], player_yellow_cards))
        yellows = list(map(lambda k: k['Yellow Cards'], player_yellow_cards))
    return players, yellows

def top_red_cards():
    with open(CSV_PATH, encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        player_red_cards = []
        for row in reader:
            prc = {'Player Name': row['Player Name'], 'Red Cards': int(row['Red Cards'])}
            player_red_cards.append(prc)
        player_red_cards = sorted(player_red_cards, key=lambda k: k['Player Name'], reverse=False)
        player_red_cards = sorted(player_red_cards, key=lambda k: k['Red Cards'], reverse=True)
        player_red_cards = player_red_cards[:5]
        players = list(map(lambda k: k['Player Name'], player_red_cards))
        reds = list(map(lambda k: k['Red Cards'], player_red_cards))
    return players, reds

def top_nationalities():
    with open(CSV_PATH, encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        nationalities = []
        for row in reader:
            nationalities.append(row[2])
        countries = set(nationalities)
        nationalities = {country: nationalities.count(country) for country in countries}
        nationalities = sorted(nationalities.items(), key=lambda k: k[0], reverse=False)
        nationalities = sorted(nationalities, key=lambda k: k[1], reverse=True)
        nationalities = nationalities[:5]
        country = list(map(lambda k: k[0], nationalities))
        player_count= list(map(lambda k: k[1], nationalities))
    return country, player_count

def players_by_nationality(country):
    with open(CSV_PATH, encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        players_by_nationality = []
        for row in reader:
            if row[2] == country:
                players_by_nationality.append(row[0])
    return players_by_nationality

# players, goals = top_scorers()
# print(players)
# print(goals)

# players, assists = top_assists()
# print(players)
# print(assists)

# players, yellows = top_yellow_cards()
# print(players)
# print(yellows)

# players, reds = top_red_cards()
# print(players)
# print(reds)

# country, player_count = top_nationalities()
# print(country)
# print(player_count)


# players_by_nationality('England')