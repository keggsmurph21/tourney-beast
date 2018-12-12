#DEFINE Functions
def newList(L):
    """Pulls out of a file that has already been opened and reads each line.
It appends each line to a list until it reaches an empty line, upon which it
returns the list."""
    while 1:
        line = f.readline().strip()
        L.append(line)
        if line == "":
            return L

def breakupIntoPools(N):
    # find out the best teams out of the division, separate them, totally different script that doesn't interact
    # make tournament day 2 sched capabilities
    """Takes the number of teams in the divisions and determines by brute
force how best to arrange those divisions into pools.  Acceptable number of
teams are even numbers between 8 and 40, inclusive."""
    if N == 8: L = [4,4]
    elif N == 10: L = [5,5] #
    elif N == 12: L = [6,6]
    elif N == 14: L = [7,7]
    elif N == 16: L = [4,4,4,4]
    elif N == 18: L = [5,5,4,4]
    elif N == 20: L = [5,5,5,5]
    elif N == 22: L = [4,4,4,4,3,3] # Unconfirmed, could also be [7,7,4,4]
    elif N == 24: L = [6,6,6,6] # Confirmed, was [6,6,3,3,3,3]
    elif N == 26: L = [5,5,4,4,4,4] # Unconfirmed
    elif N == 28: L = [7,7,7,7] # [6,6,4,4,4,4] # Confirmed, but could also be [7,7,7,7]
    elif N == 30: L = [7,7,4,4,4,4]
    elif N == 32: L = [4,4,4,4,4,4,4,4] #
    elif N == 34: L = [5,5,4,4,4,4,4,4] #
    elif N == 36: L = [5,5,5,5,4,4,4,4] #
    elif N == 38: L = [5,5,5,5,5,5,4,4] #
    elif N == 40: L = [5,5,5,5,5,5,5,5] #
    else:
        print("Invalid entry.")
        L = [0]
    return L

def checkNumTeams(num_list,name_list):
    """Cuts the divisions into their correct size based on the pools assigned
by the method breakup_into_pools."""
    total = 0
    div_by_pool = []
    for j in pool_list[i]:
        temp_name_list = name_list[total:total+j]
        total += j
        div_by_pool.append(temp_name_list)
    return div_by_pool

def schedPoolDay1(L):
    pool_game_list = []
    print 
    if len(L) == 4: #Scheduling a pool of 4 teams for pool play
        pool_game_list.append([[1,2,3],[0,3,2],[3,0,1],[2,1,0],[5,6,7],[4,7,6],[7,4,5],[6,5,4]])
    elif len(L) == 5: #Scheduling a pool of 5 teams for pool play
        pool_game_list.append([[1,5,3],[0,2,4],[3,1,7],[2,4,0],[9,3,1],[6,0,8],[5,7,9],[8,6,2],[7,9,5],[4,8,6]])
    elif len(L) == 6: #Scheduling a pool of 6 teams for pool play
        pool_game_list.append([[1,5,2],[0,2,4],[3,1,0],[2,4,5],[5,3,1],[4,0,3],[7,11,8],[6,8,10],[9,7,6],[8,10,11],[11,9,7],[10,6,9]])
    elif len(L) == 7: #Scheduling a pool of 7 teams for pool play
        pool_game_list.append([[1,3,2],[0,2,3],[3,1,0],[2,0,1],[5,13,6],[4,6,12],[11,5,4],[8,10,9],[7,9,10],[10,8,7],[9,7,8],[6,12,13],[13,11,5],[12,4,11]])
    return pool_game_list
    
def navigateToTeam(cpx_list,pool_names,game_list):
    """Scroll through the various directories to find the indices of a specific team.
The method searchForTeam (which hasn't been written yet) allows you to simply enter the
name of the team in order to find itws indices."""
    print() # find team method, returns 3-point list, other methods = view sched, view time
    print("Available divisions:")
    for i in cpx_list:
        if type(i) == type(""):
            print("\t"+i)
    division = input("Choose a division:\t").upper()
    div_index = int(cpx_list.index(division)/3)
    pool_index = int(input("Which pool in %s? (%d available)\t" % (division,len(pool_names[div_index])))) - 1
    for i in pool_names[div_index][pool_index]:
        print ("\t"+i)
    team_index = pool_names[div_index][pool_index].index(input("Which team in %s pool %d?\t" % (division,pool_index+1)).upper())
    x = [div_index,pool_index,team_index]
    return x

def accessSchedDay1(pool_names,pool_list,game_list,main_index):
    L = []
    for i in range(3):
        #print("modified: ",main_index[0],main_index[1]+(pool_list[main_index[0]][main_index[1]]<=game_list[main_index[0]][int(main_index[1]/2)][0][main_index[2]+(main_index[1]%2*pool_list[main_index[0]][main_index[1]])][i]-(main_index[1]%2*pool_list[main_index[0]][main_index[1]])),game_list[main_index[0]][int(main_index[1]/2)][0][main_index[2]+(main_index[1]%2*pool_list[main_index[0]][main_index[1]])][i]-(main_index[1]%2*pool_list[main_index[0]][main_index[1]])-(pool_list[main_index[0]][main_index[1]]<=game_list[main_index[0]][int(main_index[1]/2)][0][main_index[2]+(main_index[1]%2*pool_list[main_index[0]][main_index[1]])][i]-(main_index[1]%2*pool_list[main_index[0]][main_index[1]]))*pool_list[main_index[0]][main_index[1]])
        #print(pool_list[main_index[0]][main_index[1]]<=game_list[main_index[0]][int(main_index[1]/2)][0][main_index[2]+(main_index[1]%2*pool_list[main_index[0]][main_index[1]])][i]-(main_index[1]%2*pool_list[main_index[0]][main_index[1]]))
        #print(main_index[1]-((game_list[main_index[0]][int(main_index[1]/2)][0][main_index[2]+(main_index[1]%2*pool_list[main_index[0]][main_index[1]])][i]-(main_index[1]%2*pool_list[main_index[0]][main_index[1]])-(pool_list[main_index[0]][main_index[1]]<=game_list[main_index[0]][int(main_index[1]/2)][0][main_index[2]+(main_index[1]%2*pool_list[main_index[0]][main_index[1]])][i]-(main_index[1]%2*pool_list[main_index[0]][main_index[1]]))*pool_list[main_index[0]][main_index[1]])<0))
        """print("Game %d: %s vs. %s at %s on Field %d (%s)" %
              (i+1,pool_names[main_index[0]][main_index[1]][main_index[2]],
               pool_names[main_index[0]] # Find right division.
                   [main_index[1]+(pool_list[main_index[0]][main_index[1]]<=game_list[main_index[0]][int(main_index[1]/2)][0][main_index[2]+(main_index[1]%2*pool_list[main_index[0]][main_index[1]])][i]-(main_index[1]%2*pool_list[main_index[0]][main_index[1]]))-((game_list[main_index[0]][int(main_index[1]/2)][0][main_index[2]+(main_index[1]%2*pool_list[main_index[0]][main_index[1]])][i]-(main_index[1]%2*pool_list[main_index[0]][main_index[1]])-(pool_list[main_index[0]][main_index[1]]<=game_list[main_index[0]][int(main_index[1]/2)][0][main_index[2]+(main_index[1]%2*pool_list[main_index[0]][main_index[1]])][i]-(main_index[1]%2*pool_list[main_index[0]][main_index[1]]))*pool_list[main_index[0]][main_index[1]])<0)]      # Find the right pool
[game_list[main_index[0]][int(main_index[1]/2)][0][main_index[2]+(main_index[1]%2*pool_list[main_index[0]][main_index[1]])][i]-(main_index[1]%2*pool_list[main_index[0]][main_index[1]])-(pool_list[main_index[0]][main_index[1]]<=game_list[main_index[0]][int(main_index[1]/2)][0][main_index[2]+(main_index[1]%2*pool_list[main_index[0]][main_index[1]])][i]-(main_index[1]%2*pool_list[main_index[0]][main_index[1]]))*pool_list[main_index[0]][main_index[1]]],
 "9:00", 1, "Herbst"))"""
        l = [pool_names[main_index[0]][main_index[1]][main_index[2]],pool_names[main_index[0]][main_index[1]+(pool_list[main_index[0]][main_index[1]]<=game_list[main_index[0]][int(main_index[1]/2)][0][main_index[2]+(main_index[1]%2*pool_list[main_index[0]][main_index[1]])][i]-(main_index[1]%2*pool_list[main_index[0]][main_index[1]]))-((game_list[main_index[0]][int(main_index[1]/2)][0][main_index[2]+(main_index[1]%2*pool_list[main_index[0]][main_index[1]])][i]-(main_index[1]%2*pool_list[main_index[0]][main_index[1]])-(pool_list[main_index[0]][main_index[1]]<=game_list[main_index[0]][int(main_index[1]/2)][0][main_index[2]+(main_index[1]%2*pool_list[main_index[0]][main_index[1]])][i]-(main_index[1]%2*pool_list[main_index[0]][main_index[1]]))*pool_list[main_index[0]][main_index[1]])<0)][game_list[main_index[0]][int(main_index[1]/2)][0][main_index[2]+(main_index[1]%2*pool_list[main_index[0]][main_index[1]])][i]-(main_index[1]%2*pool_list[main_index[0]][main_index[1]])-(pool_list[main_index[0]][main_index[1]]<=game_list[main_index[0]][int(main_index[1]/2)][0][main_index[2]+(main_index[1]%2*pool_list[main_index[0]][main_index[1]])][i]-(main_index[1]%2*pool_list[main_index[0]][main_index[1]]))*pool_list[main_index[0]][main_index[1]]]]
        L.append(l)
    return L

def viewSched(L,i):
    for game in L[i[0]][i[1]][i[2]]:
        print("Game %d:\t%s vs. %s" % (L[i[0]][i[1]][i[2]].index(game)+1,game[0],game[1]))
              
def doubleCheck(cpx_list,pool_names):
    list_of_all_opponents = []
    for div in day_1_games:
        div_name = cpx_list[3*day_1_games.index(div)]
        for pool in div:
            for team in pool:
                for game in team:
                    list_of_all_opponents.append(div_name+game[1])
    for div in pool_names:
        div_name = cpx_list[3*pool_names.index(div)]
        for pool in div:
            for team in pool:
                if list_of_all_opponents.count(div_name+team) != 3:
                    print ("Error with", game[1])
    #Check for duplicates as well
                    
#DEFINE Variables
div_teams = []
cpx_list = []
cpx_list_ext = []
div_num_teams = []
pool_list = []
pool_names = []
game_list = []
day_1_games = []

# Executing code
f = open("divisions.txt","r") # This file should contain all of the teams names, grouped by division and ending with the string "end_list"
while 1:
    L = []
    newList(L)
    L.remove("")
    cpx_list.extend(L.pop(0).split())
    div_teams.append(L)
    if L[len(L)-1] == "end_list":
        L.remove("end_list")
        break
f.close()

for i in range(int(len(cpx_list)/3)):
    div_num_teams.append(len(div_teams[i]))
    
for i in div_num_teams:
    pool_list.append(breakupIntoPools(i))

for i in range(len(div_teams)):
    pool_names.append(checkNumTeams(pool_list,div_teams[i]))

for i in range(len(cpx_list)):
    if i%3:
        cpx_list[i] = int(cpx_list[i])
    else:
        for j in pool_list[int(i/3)]:
            cpx_list_ext.append(j)

for i in pool_names:
    # If you need to print out names, do this ... print(cpx_list[3 * pool_names.index(i)])
    game_list_int = []
    for j in range(len(i)):
        if j%2:
            game_list_int.append(schedPoolDay1(i[j]))
    game_list.append(game_list_int)

# Generates a perfectly indexable list of all the games going on during the day of Pool Play.
for i in range(len(pool_names)):
    div_games = []
    for j in range(len(pool_names[i])):
        pool_games = []
        for k in range(len(pool_names[i][j])):
            pool_games.append(accessSchedDay1(pool_names,pool_list,game_list,[i,j,k]))
        div_games.append(pool_games)
    day_1_games.append(div_games)

doubleCheck(cpx_list,pool_names)

while 1:
    print()
    print()
    user = input("Options:\t1. View all\n\t\t2. View specific division\n\t\t3. View specific team\n\t\t4. Exit\n\t\t")
    if user == "1":
        for div in range(len(pool_names)):
            print()
            print("Division:",cpx_list[3*div])
            for pool in range(len(pool_names[div])):
                print("Pool:",pool+1)
                for team in range(len(pool_names[div][pool])):
                    print(pool_names[div][pool][team])
                    viewSched(day_1_games,[div,pool,team])
                    print()
                print()
    elif user == "2":
        print()
        print("\t\t   Divisions:\n")
        for entry in range(int(len(cpx_list)/3)):
            print("\t\t\t",cpx_list[3*entry])
        print()
        search = input("\t\t\t")
        div = int(cpx_list.index(search.upper())/3)
        print()
        print("Division:",search.upper())
        for pool in range(len(pool_names[div])):
                print("Pool:",pool+1)
                for team in range(len(pool_names[div][pool])):
                    print(pool_names[div][pool][team])
                    viewSched(day_1_games,[div,pool,team])
                    print()
                print()
    elif user == "3":
        main_index = navigateToTeam(cpx_list,pool_names,game_list)
        viewSched(day_1_games, main_index)
    elif user == "4":
        break
    else:
        print("Invalid entry.")
    
# __TROUBLESHOOTING__
# Choose a team with this syntax:       main_index = select_team(cpx_list,pool_names,game_list)
#       print(main_index)
# View that team's schedule on Day 1:   view_sched_day_1(pool_names,pool_list,game_list,main_index)
