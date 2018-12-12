pool_standings = [[file_path + ' - | Standings by Pool'],[]]

listTeamsDiv = []
listDivInfo = list(set([row[4].split('-')[0] for row in chrono[1:]]))
for no_div in range(listDivInfo.count('No division')): listDivInfo.remove('No division')
listDivInfo.sort()

for div in listDivInfo:
    pools = list(set([row[4].split('-')[-1] * (row[4].split('-')[0]==div) for row in chrono]))
    pools.remove('')
    pools = [int(p) for p in pools]
    listTeamsDiv.append([[] for i in range(max(pools))])

for row in chrono[1:]:
    team = row[6]
    while team[-1]==' ': team = team[:-1]
    div_and_pool = row[4]
    try: d = listDivInfo.index(div_and_pool.split('-')[0])
    except ValueError: break
    p = int(div_and_pool.split('-')[1]) - 1
    listTeamsDiv[d][p].append(team)

listTeamsDiv = [[list(set(p)) for p in d] for d in listTeamsDiv]

for div in range(len(listTeamsDiv)):
    div_results = [['' for i in range(4*len(listTeamsDiv[div]))] for team in range(max([len(p) for p in listTeamsDiv[div]])+1)]
    for pool in range(len(listTeamsDiv[div])):
        div_results[0][4*pool+0] = 'Pool ' + str(pool+1)
        div_results[0][4*pool+1] = 'Win'
        div_results[0][4*pool+2] = 'Loss'
        div_results[0][4*pool+3] = 'Seed'
        for team in range(len(listTeamsDiv[div][pool])):
            div_results[team+1][4*pool] = listTeamsDiv[div][pool][team]
    div_results = [['Division: ' + listDivInfo[div]]] + div_results + [[]]
    pool_standings += div_results
    
with open(file_path[:-4] + ' standings.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(pool_standings)
