def new_list(L):
    while 1:
        line = f.readline().strip()
        L.append(line)
        if line == "":
            return L

def sub_10(k):
    if k-10 >= 0 and k-10 != 2 and k-10 != 4:
        return True
    else: return False

def sub_8(k):
    if k-8 >= 0 and k-8 != 2 and k-8 != 4:
        return True
    else: return False

def sub_6(k):
    if k-6 >= 0 and k-6 != 2 and k-6 != 4:
        return True
    else: return False

def breakup_into_pools(num):
    result = []
    if not num%2 and num > 5:
        L = []
        T = num
        if sub_10(T):
            T = T - 10
            L.append(10)
            if sub_10(T):
                T = T - 10
                L.append(10)
                if sub_10(T):
                    T = T - 10
                    L.append(10)
                if sub_8(T):
                    T = T - 8
                    L.append(8)
                if sub_6(T):
                    T = T - 6
                    L.append(6)
            if sub_8(T):
                T = T - 8
                L.append(8)
                if sub_8(T):
                    T = T - 8
                    L.append(8)
                if sub_6(T):
                    T = T -6
                    L.append(6)
            if sub_6(T):
                T = T - 6
                L.append(6)
                if sub_6(T):
                    T = T -6
                    L.append(6)
            if sum(L) == num: result.append(L)    
        T = num # Without any 10's
        L = []
        if sub_8(T):
            T = T - 8
            L.append(8)
            if sub_8(T):
                T = T - 8
                L.append(8)
                if sub_8(T):
                    T = T - 8
                    L.append(8)
                    if sub_8(T):
                        T = T - 8
                        L.append(8)
                        if sub_8(T):
                            T = T - 8
                            L.append(8)
                        if sub_6(T):
                            T = T - 6
                            L.append(6)
                    if sub_6(T):
                        T = T - 6
                        L.append(6)
                        if sub_6(T):
                            T = T - 6
                            L.append(6)
                if sub_6(T):
                    T = T - 6
                    L.append(6)
                    if sub_6(T):
                        T = T - 6
                        L.append(6)
                        if sub_6(T):
                            T = T - 6
                            L.append(6)
            if sub_6(T):
                T = T - 6
                L.append(6)
                if sub_6(T):
                    T = T - 6
                    L.append(6)
                    if sub_6(T):
                        T = T - 6
                        L.append(6)
                        if sub_6(T):
                            T = T - 6
                            L.append(6)
            if sum(L) == num: result.append(L)
        T = num # Without any 10's or 8's
        L = []
        if sub_6(T):
            T = T - 6
            L.append(6)
            if sub_6(T):
                T = T - 6
                L.append(6)
                if sub_6(T):
                    T = T - 6
                    L.append(6)
                    if sub_6(T):
                        T = T - 6
                        L.append(6)
                        if sub_6(T):
                            T = T - 6
                            L.append(6)
            if sum(L) == num: result.append(L)
    else:
        print("Invalid entry.")
        result = [0]
    return result

def choose_best_breakup(L,S):
    if len(L) == 1:
        k = 0
    elif sum(L[0]) == 20:
        L = [[10,10]]
        k = 0
    else:
        count_list = []
        for i in L:
            count_list.append(5*i.count(8) + 2*i.count(6) + i.count(10))
        k = count_list.index(max(count_list))
    if S == "print":
        print("Given",L, "the best arrangement is %d pools of 5, %d pools of 4, and %d pools of 3" % (2*L[k].count(10),2*L[k].count(8),2*L[k].count(6)))
    return L[k]

def sort_division_list(N):
    sort_list = choose_best_breakup(breakup_into_pools(N),"")
    sorted_list = []
    for i in sort_list:
        sorted_list.append(int(i/2))
        sorted_list.append(int(i/2))
    return sorted_list

def check_num_teams(L):
    if len(L)>14:
        print("Too many teams in",cpx_list[3*i],"... reorganizing ...","("+str(len(L))+")")
        if len(L)>40:
            print("Error: too many teams in",cpx_list[3*i],"("+str(len(L))+").  Maximum = 40 teams.")
            return
    else:
        print("Acceptable number of teams in",cpx_list[3*i],"("+str(len(L))+")")

div_teams = []
cpx_list = []
div_num_teams = []

f = open("divisions.txt","r")
while 1:
    L = []
    new_list(L)
    L.remove("")
    cpx_list.extend(L.pop(0).split())
    div_teams.append(L)
    if L[len(L)-1] == "end_list":
        L.remove("end_list")
        break
    
for i in range(len(div_teams)):
    check_num_teams(div_teams[i])
        
for i in range(len(cpx_list)):
    if i%3:
        cpx_list[i] = int(cpx_list[i])
f.close()

for i in range(int(len(cpx_list)/3)):
    div_num_teams.append(len(div_teams[i]))

for i in div_num_teams:
    print(sort_division_list(i))
    
