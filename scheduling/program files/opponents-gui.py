import random

def getOppIndex(expPoolSize,expTeamIndex,gameIndex):
    global listOppIndicesBySize

    oppIndex = listOppIndicesBySize[expPoolSize][expTeamIndex][gameIndex]
    
    return oppIndex
    
def getListOpp(day,d,p,t):
    listOpp = []
    if len(lPoolSize[day][d]) > 1: expPool = lTeamsDiv[day][d][2 * int(p/2)] + lTeamsDiv[day][d][2 * int(p/2) + 1]
    else: expPool = lTeamsDiv[day][d][p]
    expTeamIndex = t + p%2 * len(lTeamsDiv[day][d][p])
    for game in range(numberOfGames):
        oppIndex = getOppIndex(len(expPool),expTeamIndex,game)
        listOpp.append(expPool[oppIndex])
    return listOpp

def getAllOpp():
    listGamesAll = []
    for dayIndex in range(len(lTeamsDiv[:-1])):
        listGamesDay = []
        for divIndex in range(len(lTeamsDiv[dayIndex])):
            listGamesDiv = []
            for poolIndex in range(len(lTeamsDiv[dayIndex][divIndex])):
                listGamesPool = []
                for teamIndex in range(len(lTeamsDiv[dayIndex][divIndex][poolIndex])):
                    listGamesTeam = getListOpp(dayIndex,divIndex,poolIndex,teamIndex)
                    listGamesPool.append(listGamesTeam)
                listGamesDiv.append(listGamesPool)
            listGamesDay.append(listGamesDiv)
        listGamesAll.append(listGamesDay)
    return listGamesAll

def getListOppIndicesBySize(iters, list_sizes):
    size_options = []
    
    for day in list_sizes:
        for div in day:
            size_options += div

    matchups = [[['' for g in range(iters)] for p in range(t)] for t in range(2 * max(size_options)+1)]

    for p in range(2 * max(size_options)+1):
        listOpps = []
        
        for game in range(iters):
            games = []
            for t in range(p):
                tries = 0
                while not(([g[0] for g in games] + [g[1] for g in games]).count(t)) and tries < 100:
                    other_t = random.randint(0, p-1)
                    if other_t != t and not(([g[0] for g in games] + [g[1] for g in games]).count(other_t)) and not(sum([opp_games.count([t, other_t]) for opp_games in listOpps])):
                        games.append([t, other_t])
                    tries += 1
            listOpps.append(games)
            
        if not(p%2):   
            for g in range(len(listOpps)):
                for m in listOpps[g]:
                    matchups[p][m[0]][g] = m[1]
                    matchups[p][m[1]][g] = m[0]
            
    return matchups
            

listOppIndicesBySize = getListOppIndicesBySize(numberOfGames, lPoolSize)
                   
allOpp = getAllOpp()
