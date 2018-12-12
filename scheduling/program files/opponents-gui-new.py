lTeamsDiv = [[[['Team 1','Team 2', 'Team 3', 'Team 4']],[['t1','t2','t3','t4','t5','t6']],[['s1','s2','s3','s4','s5'],['s6','s7','s8','s9','s0']]],[]]
lPoolSize = [[[[4]],[[6]],[[5,5]]],[]]
numberOfGames = 3

import random
"""
def getOppIndex(expPoolSize,expTeamIndex,gameIndex):
    listOppIndicesBySize = [[],
                            [],
                            [],
                            [],
                            [[1,2,3],[0,3,2],[3,0,1],[2,1,0]],
                            [],
                            [[1,5,2],[0,2,4],[3,1,0],[2,4,5],[5,3,1],[4,0,3]],
                            [],
                            [[1,2,3],[0,3,2],[3,0,1],[2,1,0],[5,6,7],[4,7,6],[7,4,5],[6,5,4]],[],
                            [[1,5,3],[0,2,4],[3,1,7],[2,4,0],[9,3,1],[6,0,8],[5,7,9],[8,6,2],[7,9,5],[4,8,6]],[],
                            [[1,5,2],[0,2,4],[3,1,0],[2,4,5],[5,3,1],[4,0,3],[7,11,8],[6,8,10],[9,7,6],[8,10,11],[11,9,7],[10,6,9]],[],
                            [[1,3,2],[0,2,3],[3,1,0],[2,0,1],[5,13,6],[4,6,12],[11,5,4],[8,10,9],[7,9,10],[10,8,7],[9,7,8],[6,12,13],[13,11,5],[12,4,11]] ]

    oppIndex = listOppIndicesBySize[expPoolSize][expTeamIndex][gameIndex]
    return oppIndex
"""    
def getListOpp(day,d,p,t):
    listOpp = []
    if len(lPoolSize[day][d]) > 1: expPool = lTeamsDiv[day][d][2 * int(p/2)] + lTeamsDiv[day][d][2 * int(p/2) + 1]
    else: expPool = lTeamsDiv[day][d][p]
    expTeamIndex = t + p%2 * len(lTeamsDiv[day][d][p])
    for game in range(numberOfGames):
        oppIndex = getOppIndex(len(expPool),expTeamIndex,game)
        listOpp.append(expPool[oppIndex])
    return listOpp

def genListOppIndex(p):
    print(p)
    listOpps = []
    
    if p%2: p += 1
    
    for game in range(numberOfGames):
        games = []
        for t in range(p):
            tries = 0
            while not(([g[0] for g in games] + [g[1] for g in games]).count(t)) and tries < 100:
                other_t = random.randint(0, p - 1)
                if other_t != t and not(([g[0] for g in games] + [g[1] for g in games]).count(other_t)) and not(sum([opp_games.count([t, other_t]) for opp_games in listOpps])):
                    games.append([t, other_t])
                tries += 1
        listOpps.append(games)
        
    listOppsI = [['' for g in range(numberOfGames)] for t in range(p)]
    
    for g in range(len(listOpps)):
        for m in listOpps[g]:
            listOppsI[m[0]][g] = m[1]
            listOppsI[m[1]][g] = m[0]

    return(listOppsI)

def getAllOpp():
    listGamesAll = []
    for dayIndex in range(len(lTeamsDiv[:-1])):
        listGamesDay = []
        for divIndex in range(len(lTeamsDiv[dayIndex])):
            listGamesDiv = []
            for poolIndex in range(len(lTeamsDiv[dayIndex][divIndex])):
                listGamesPool = []
                if len(lPoolSize[dayIndex][divIndex]) > 1: expPool = lTeamsDiv[day][d][2 * int(p/2)] + lTeamsDiv[day][d][2 * int(p/2) + 1]
                else: expPool = lTeamsDiv[dayIndex][divIndex][poolIndex]
                listMatchupsPool = genListOppIndex(len(expPool))
                for team in listMatchupsPool:
                    listGamesTeam = []
                    for matchup in team:
                        try:
                            listGamesTeam.append(lTeamsDiv[dayIndex][divIndex][poolIndex][matchup])
                        except IndexError:
                            listGamesTeam.append(lTeamsDiv[dayIndex][divIndex][poolIndex+1][matchup - int(len(expPool)/2)])
                    listGamesPool.append(listGamesTeam)
                        
                #for teamIndex in range(len(lTeamsDiv[dayIndex][divIndex][poolIndex])):
#                    listGamesTeam = getListOpp(dayIndex,divIndex,poolIndex,teamIndex)
#                    listGamesPool.append(listGamesTeam)
                listGamesDiv.append(listGamesPool)
                print(listMatchupsPool)
            listGamesDay.append(listGamesDiv)
        listGamesAll.append(listGamesDay)
    return listGamesAll
                   
allOpp = getAllOpp()
