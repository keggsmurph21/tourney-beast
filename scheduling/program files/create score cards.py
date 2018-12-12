chrono = chrono[1:]
chrono.sort()

score_card = []

for r in range(len(chrono)):
    if not(r%2):
        home = chrono[r]
        away = chrono[r+1]
        game = [['Game Number', home[0]],
                ['Start Time', home[2]],
                ['Field', 'Field #' + home[3]],
                [],
                ['Bracket: ' + home[4].split('-')[0].upper(), 'Division: ' + away[4].split('-')[0].upper()],
                ['Pool: ' + home[4].split('-')[-1].upper(), 'Pool: ' + away[4].split('-')[-1].upper()],
                ['Home: ' + home[6], 'Away Team: ' + away[6]],
                ['Score:', 'Score:'],
                ['Sportsmanship (Circle one):  1  2  3  4  5', 'Sportsmanship (Circle one): 1 2 3 4 5'],
                ['Comments', 'Comments'],
                ['',''], []]

        score_card += game

with open(file_path[:-4] + ' score cards.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(score_card)
