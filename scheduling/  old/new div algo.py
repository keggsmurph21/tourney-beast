from random import randrange

def getCombos(numberTeams):
    combo = []
    allCombos = []
    count = 0
    while count < numberTeams ** 2:
        n = numberTeams
        while n:
            seed = randrange(6,13,2)
            if (n - seed) == 0 or (n - seed) > 5:
                n = n - seed
                combo.append(seed)
        combo.sort()
        if not(combo in allCombos):
            count = 0
            allCombos.append(combo)
        combo = []
        count = count+1
    return sorted(allCombos)

def chooseCombo(n):
    listCombos = getCombos(n)
    evenCombos = []
    if len(listCombos) == 1:
        return listCombos[0]
    for combo in listCombos:
        if sum([combo[p] == combo[0] for p in range(len(combo))]) == len(combo):
            evenCombos.append(combo)
    for p in [8,6,10,12]:
        for evenCombo in evenCombos:
            if evenCombo[0] == p: return evenCombo
    return "No best combo."

for i in range(6,101,2):
    print(chooseCombo(i))
