while 1:
    while 1:
        print("Please choose a division to edit:\n(Enter the number index, e.g. 1)\n")
        for divIndex in range(len(listDivInfo)):
            print(str(divIndex+1) + ".\t" + listDivInfo[divIndex])
        divToEdit = int(input("\n")) - 1
        listAlphabet = ["A","B","C","D","E","F","G","H","I"]    
        print("Please choose which two teams should be switched:\n(Enter the letter-number index, e.g. A1)\n")
        for poolIndex in range(len(listTeamsDiv[divToEdit])):
            print("Pool %s" % listAlphabet[poolIndex])
            for teamIndex in range(len(listTeamsDiv[divToEdit][poolIndex])):
                print("\t"+str(teamIndex+1)+".\t"+listTeamsDiv[divToEdit][poolIndex][teamIndex])
        teamOneUserEntry = input("\nTeam One: ").upper()
        teamTwoUserEntry = input("Team Two: ").upper()
        teamOneVector = [divToEdit,listAlphabet.index(teamOneUserEntry[0]),int(teamOneUserEntry[1])-1]
        teamTwoVector = [divToEdit,listAlphabet.index(teamTwoUserEntry[0]),int(teamTwoUserEntry[1])-1]
        proceed = input("Switch %s and %s? (y/n)\n" %(listTeamsDiv[teamOneVector[0]][teamOneVector[1]][teamOneVector[2]], listTeamsDiv[teamTwoVector[0]][teamTwoVector[1]][teamTwoVector[2]])).upper()
        if proceed == "N": break
        placeholder = listTeamsDiv[teamOneVector[0]][teamOneVector[1]][teamOneVector[2]]
        listTeamsDiv[teamOneVector[0]][teamOneVector[1]][teamOneVector[2]] = listTeamsDiv[teamTwoVector[0]][teamTwoVector[1]][teamTwoVector[2]]
        listTeamsDiv[teamTwoVector[0]][teamTwoVector[1]][teamTwoVector[2]] = placeholder
        print("Switched %s and %s\n" %(listTeamsDiv[teamOneVector[0]][teamOneVector[1]][teamOneVector[2]], listTeamsDiv[teamTwoVector[0]][teamTwoVector[1]][teamTwoVector[2]]))
        for poolIndex in range(len(listTeamsDiv[divToEdit])):
            print("Pool %s" % listAlphabet[poolIndex])
            for teamIndex in range(len(listTeamsDiv[divToEdit][poolIndex])):
                print("\t"+str(teamIndex+1)+".\t"+listTeamsDiv[divToEdit][poolIndex][teamIndex])
        break
    finish = input("Continue editing? (y/n)\n").upper()
    if finish == "N": break
