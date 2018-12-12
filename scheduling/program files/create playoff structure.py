import csv
from operator import itemgetter

def get_points(info):
    games_played = len(info) - 3
    points = 0
    sportsmanship = 0

    for game_played in info[3:]:
        diff = game_played[1]
        
        if diff > 0:
            result = 3
        elif diff == 0:
            result = 1
        elif diff < 0:
            result = 0
            
        points += (result + diff * 10**(-2))
        sportsmanship += game_played[2]

    if not(games_played):
        games_played += 1

    totals = [round(points/games_played,4), round(sportsmanship/games_played,4)]

    return totals

def seed_pool(pool):
    pool.sort(reverse=True)

    for team in pool:
        if [t[0] for t in pool].count(team[0]) > 1 and len(team) > 3:
            team[0] += team[1] * 10**(-5)
    for team in pool:
        if [t[0] for t in pool].count(team[0]) > 1 and len(team) > 3:
            #print('Exact same point total and differential... need to address\n',pool)
            pass
    return pool

def det_playoff_size(div):
    rd_defs = [0 for p in div]
    rd2_defs = [0 for p in div]
    for p in range(len(div)):
        sz = div[p]
        if sz:
            max_similar = div.count(sz)
            if max_similar > 4: max_similar = 4
            for similar in range(1,max_similar):
                div[p] += div[p+similar]
                div[p+similar] = 0
            rd_defs[p] = playoff_defaults[str(div[p])]
            rd2_defs[p] = playoff_defaults_rd2[str(div[p])]

    return [div, rd_defs, rd2_defs]

def make_playoffs(e,rnd,rnd2,d,p):
    global place_key

    if not(int(e)):
        return

    #div = [[[team[2] for team in pool] for pool in div] for div in scores][d]
    e = str(e)
    place_key = {'0' : '1st', '1' : '2nd', '2' : '3rd', '3' : '4th', '4' : '5th', '5' : '6th', '6' : '7th', '7' : '8th', '8' : '9th', '9' : '10th', '10' : '11th', '11' : '12th'}

    for game in playoff_tree[e][0][rnd]:
        if type(game[0]) == int:
            pMatchup = [[0,game[0]],[0,game[1]]]
        else:
            pMatchup = [[int(game[0]),abs(int(round((game[0] - int(game[0])) * 10)))],[int(game[1]),abs(int(round((game[1] - int(game[1])) * 10)))]]
        pAllOpp[d][p][0].append(pMatchup)

    for game in playoff_tree[e][1][rnd2]:
        pAllOpp[d][p][1].append(game)

scores_from_LH = 'program files/patriot-13.csv'
scoresCSV = []
pNumberOfGames = 2
alpha_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
winner_key = [' (Loser)',' (Winner)']

playoff_tree_master = {
                '2':    {
                            '4':  [[[[0,3],[1,2]],[[0,1]]],
                                 [[],[[0.1,1.1],[0.0,1.0]]]],
                            '6':  [[[[0,5],[1,4],[2,3]], [[0,2],[1,3],[4,5]], [[0,1]]],
                                 [[],[[0.1,1.1],[0.0,2.1],[1.0,2.0]]]],
                            '8':  [[[[0,3],[1,2],[4,7],[5,6]], [[0.0,1.1],[0.1,1.0],[0.2,1.3],[0.3,1.2]], [[0.0,1.1],[0.1,1.0]], [[0.0,1.0]]],
                                 [[],[[0.1,1.1],[0.0,1.0],[2.1,3.1],[2.0,3.0]],[[0.1,1.1]],[[0.1,1.1],[0.0,1.0]]]],   
                            '10': [[[[0,3],[1,2],[4,9],[5,8],[6,7]],  [[0.0,1.1],[0.1,1.0],[0.2,1.2],[0.3,1.4],[0.4,1.3]], [[0.0,1.1],[0.1,1.0]], [[0.0,1.0]]],
                                 [[],[[0.1,1.1],[0.0,1.0],[2.1,3.1],[2.0,4.1],[3.0,4.0]],[[0.1,1.1]]]],
                            '12': [[[[0,3],[1,2],[4,7],[5,6],[8,11],[9,10]],  [[0.0,1.1],[0.1,1.0],[0.2,1.3],[0.3,1.2],[0.4,1.5],[0.5,1.4]], [[0.0,1.1],[0.1,1.0]], [[0.0,1.0]]],
                                 [[],[[0.1,1.1],[0.0,1.0],[2.1,3.1],[2.0,3.0],[4.1,5.1],[4.0,5.0]],[[0.1,1.1]]]],
                            '14': [[[[0,3],[1,2],[4,7],[5,6],[8,13],[9,12],[10,11]],  [[0.0,1.1],[0.1,1.0],[0.2,1.3],[0.3,1.2],[0.4,1.4],[0.5,1.6],[0.6,1.5]], [[0.0,1.1],[0.1,1.0]], [[0.0,1.0]]],
                                 [[],[[0.1,1.1],[0.0,1.0],[2.1,3.1],[2.0,3.0],[4.1,5.1],[4.0,6.1],[5.0,6.0]],[[0.1,1.1]]]],
                            '16': [[[[0.0,1.0],[2.0,3.0]]],
                                 [[[0.1,1.1],[0.0,1.0]]]],
                            '18': [[[[0.0,1.0],[2.0,3.0]]],
                                 [[[0.1,1.1],[0.0,1.0]]]],
                            '20': [[[[0.0,1.0],[2.0,3.0]]],
                                 [[[0.1,1.1],[0.0,1.0]]]],
                            '22': [[[[0.0,1.0],[2.0,3.0]]],
                                 [[[0.1,1.1],[0.0,1.0]]]],
                            '24': [[[[0.0,1.0],[2.0,3.0]]],
                                 [[[0.1,1.1],[0.0,1.0]]]],
                            '28': [[[[0.0,1.0],[2.0,3.0]]],
                                 [[[0.1,1.1],[0.0,1.0]]]],
                        }
                }

playoff_defaults_master = {
                            '2':    {
                                        '4':     1,
                                        '6':     2,
                                        '8':     2,
                                        '10':    2,
                                        '12':    2,
                                        '14':    2,
                                        '16':    0,
                                        '18':    0,
                                        '20':    0,
                                        '22':    0,
                                        '24':    0,
                                        '28':    0
                                    }
                          }

playoff_defaults_rd2_master = {
                            '2':    {
                                        '4':     0,
                                        '6':     0,
                                        '8':     3,
                                        '10':    2,
                                        '12':    2,
                                        '14':    2,
                                        '16':    0,
                                        '18':    0,
                                        '20':    0,
                                        '22':    0,
                                        '24':    0,
                                        '28':    0
                                    }
                          }

playoff_tree = playoff_tree_master[str(pNumberOfGames)]
playoff_defaults = playoff_defaults_master[str(pNumberOfGames)]
playoff_defaults_rd2 = playoff_defaults_rd2_master[str(pNumberOfGames)]

try:
    have_scores = True
    with open(scores_from_LH, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            scoresCSV.append(row)


    scoresCSV = scoresCSV[1:]

    for row in scoresCSV:
        for c in [12,11,10,9,3,2,1]:
            del row[c]

    scores = [[[[0,0,''] for team in pool] for pool in div] for div in listTeamsDiv]

    for r in range(len(scoresCSV)):
        game = []
    
        gid = int(scoresCSV[r][0])
        rnd = int(scoresCSV[r][2]) - 1
        team_team = scoresCSV[r][3]
        team_div = scoresCSV[r][1]
    
        try:
            d = listDivInfo.index(team_div)
        except ValueError:
            listDivInfo.append(team_div)
            listTeamsDiv.append([[]])
            scores.append([[]])
            d = listDivInfo.index(team_div)

        p = 0

        while not(listTeamsDiv[d][p].count(team_team)):
            p += 1
            if p == len(listTeamsDiv[d]):
                #print("\tCan't find pool",listTeamsDiv[d])
                if len(listTeamsDiv[d]) == 1:
                    p = 0
                    listTeamsDiv[d][p].append(team_team)
                    scores[d][p].append([0,0,''])
                    #print('\tFound pool')
                else:
                    pass
                    #print('Error!!!')
                break
    
        try:
            t = listTeamsDiv[d][p].index(team_team)
        except ValueError:
            #print("\tCan't find team")
            pass

        team_score = int(scoresCSV[r][4])
        team_sms = int(scoresCSV[r][5])
    
        if r%2:
            o = r - 1
        else:
            o = r + 1
        
        opp_team = scoresCSV[o][3]
        opp_div = scoresCSV[o][1]
        opp_score = int(scoresCSV[o][4])
    
        goal_differential = team_score - opp_score
    
        game.append(opp_team)
        game.append(goal_differential)
        game.append(team_sms)
    
        scores[d][p][t].append(game)
        scores[d][p][t][1] += team_sms

    for d in scores:
        
        for p in d:
            for t in p:
                t[2] = listTeamsDiv[scores.index(d)][d.index(p)][p.index(t)]
                points_sms = get_points(t)
                t[0] = points_sms[0]
                t[1] = points_sms[1]
            p = seed_pool(p)
            
    rList = [[sum([sum([t[0] for t in p]) for p in d])] for d in scores]
    rList_scores = [(scores[r] * (not(int(rList[r][0])))) for r in range(len(rList))]
    rList_LDI = [(listDivInfo[r] * (not(int(rList[r][0])))) for r in range(len(rList))]

    for r in range(len(rList_scores)):
        try:
            scores.remove(rList_scores[r])
            listDivInfo.remove(rList_LDI[r])
        except ValueError:
            pass

except FileNotFoundError:
    have_scores = False
    scores = [[[[0,0,team] for team in pool] for pool in div] for div in listTeamsDiv]

pAllOpp = [[[[],[]] for pool in div] for div in scores]

for d in range(len(scores)):
    dp_sizes = [len(p) for p in scores[d]]
    divInfo = det_playoff_size(dp_sizes)
    for p in range(len(divInfo[0])):
        sz = str(divInfo[0][p])
        rnd_default = divInfo[1][p]
        rnd2_default = divInfo[2][p]
        make_playoffs(sz, rnd_default, rnd2_default, d, p)
        
"""
with open('program files/p-schedule-gui.py') as f:
    code = compile(f.read(),f,'exec')
    exec(code, globals())
    
print(set([p[0] for p in listPoolSize]))
for d in scores:
	print(listDivInfo[scores.index(d)])
	for p in d:
		for t in p:
			print(t[2],'\t',t[0],'\t',t[1])
		print('\n')
	print('\n')
"""
