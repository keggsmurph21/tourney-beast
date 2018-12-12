from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from datetime import *
import csv
import time as time_module

"""
class lineFromDiv(Frame):
    def __init__(self, master, name, **options):
        Frame.__init__(self, master, **options)
        lbl = Label(self, text=name)
        lbl2 = Label(self, text='pool')
        lbl.grid(row=0, column=1)
        lbl.grid(row=0, column=0)
"""        
def get_data(*args):
    global numberOfGames
    global gamesPerDay
    global blocks
    global start_h
    global start_m
    global gmWidth
    global input_path
    global schedule_name
    global complex_path
    global use_manual_pools
    global span_days
    global incl_playoffs
    global tournament_days

    global listTeamsDiv
    global listDivInfo
    global listDivNumTeams
    global listPoolSize
    
    try:
        numberOfGames = int(get_nOG.get())
        gamesPerDay = int(get_gPD.get())
        blocks = int(gamesPerDay / numberOfGames)
        start_h = int(get_time.get().split(':')[0])
        start_m = int(get_time.get().split(':')[1])
        gmWidth = int(get_gmW_NU.get()) #int(gmWidth_NU[get_gmW_NU.get()]) * int(gmWidth_UL[get_gmW_UL.get()]) + 10
        input_path = get_ip_t.get()
        schedule_name = get_s_n.get()
        complex_path = get_ip_c.get()
        tournament_days = int(get_tournament_num_days.get())
        use_manual_pools = get_u_m_p.get()
        span_days = get_span_days.get()
        incl_playoffs = get_incl_playoffs.get()
        
        gen_listT()
        get_listComp()
        gen_cumFieldsNum()
        
        run('generate.py')
        
    except ValueError:
        pop_up('Error','Please fill out all fields')
        main_window()

def gen_listT(*args):
    global listT

    offH = 0
    offM = 0
    listT = []
    
    for t in range(gamesPerDay + pGamesPerDay):
        over_by = int((start_m + t*gmWidth + offM)/60)
        offH += over_by
        if offH + start_h > 12:
            offH -= 12
        offM -= 60 * over_by
        listT.append(str(time(start_h + offH, start_m + t*gmWidth + offM)))

def get_listComp(*args):
    global listComp

    comp_csv = []
    
    with open(complex_path, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row[0]):
                comp_csv.append(row)

    for c in comp_csv[1:]:
        c[1] = int(c[1])

    listComp = comp_csv[1:]

def gen_cumFieldsNum(*args):
    global colH
    global cumFieldsNum

    colH = []
    cumFieldsNum = []

    for c in listComp:
        colH += [c[0] for i in range(c[1])]

    for c in range(len(listComp)):
        if c:
            cumFieldsNum.append(cumFieldsNum[c-1] + listComp[c-1][1])
        else:
            cumFieldsNum.append(0)

def run(prgm):
    with open(prgm) as f:
        code = compile(f.read(), f, 'exec')
        exec(code, globals())

def collect_data_prompt_complexes(*args):
    global lComp
    global tournament_days

    get_data()
    restrict_complexes_to_days_show_all()

def restrict_divisions_to_complexes_show_all(*args):
    global chooseableComps
    global lTeamsDiv
    global lDivInfo
    global restricted_divs

    for wchild in init.winfo_children():
        wchild.destroy()

    chooseableComps = []

    for day in lComp:
        chooseableComp = ''
        compSum = 0
        for comp in day:
            chooseableComp += (comp[0] + ', ')
            compSum += comp[1]
        chooseableComp = chooseableComp[:-2] + ' [' + str(compSum) + ' fields]'
        chooseableComps.append(chooseableComp)

    chooseableComps.append('Custom placement')

    lTeamsDiv = [[[[] for pool in div] for div in listTeamsDiv] for day in range(len(lComp)+1)]
    lDivInfo = [[] for day in range(len(lComp)+1)]

    restricted_divs = [StringVar() for div in listDivInfo]

    Label(init, text='Division Name').grid(row=10,column=0,pady=10)
    Label(init, text='Day/complexes playing').grid(row=10,column=1,pady=10)

    for div in range(len(listDivInfo)):
        OptionMenu(init, restricted_divs[div], *chooseableComps).grid(row=100+div,column=1,sticky=W)
        Label(init, text=listDivInfo[div]).grid(row=100+div,column=0)
        restricted_divs[div].set(chooseableComps[0])
        
    Button(init, text='Save', command=restrict_divisions_to_complexes_save).grid(columnspan=2)

def restrict_divisions_to_complexes_save(*args):
    global lPoolSize
    
    for div in range(len(restricted_divs)):
        day = chooseableComps.index(restricted_divs[div].get())
        if day != len(chooseableComps):
            lTeamsDiv[day][div] = listTeamsDiv[div]
            lDivInfo[day].append(listDivInfo[div])
        
    for day in lTeamsDiv:
        del_pools = []
        del_divs = []
        for d in range(len(day)):
            for p in range(len(day[d])):
                if len(day[d][p]) == 0:
                    del_pools.append([d,p])
            if sum([len(pool) for pool in day[d]]) == 0:
                del_divs.append(d)
        for div_pool in del_pools[::-1]:
            del day[div_pool[0]][div_pool[1]]
        for div in del_divs[::-1]:
            del day[div]

    lPoolSize = [[[len(pool) for pool in div] for div in day] for day in lTeamsDiv]

    run('opponents-gui.py')
    run('schedule-gui.py')

    pop_up('Schedule','Schedule generated')

    #run('pull info.py')

def pop_up(ttl, msg):
    top = Toplevel()
    top.title(ttl)
    top.geometry('200x120+800+100')
    Message(top, text=msg).pack(fill=X,expand=True)
    Button(top, text='Ok', command=top.destroy).pack(fill=X)
    
"""        
def view(*args):
    get_data()

    global lComp
    global chooseableComps
    global lTeamsDiv
    global lDivInfo
    global tournament_days

    restrict_complexes_to_days_show_all()
    
    chooseableComps = []
    span_days = tournament_days

    for day in lComp:
        chooseableComp = ''
        compSum = 0
        for comp in day:
            chooseableComp += (comp[0] + ', ')
            compSum += comp[1]
        chooseableComp = chooseableComp[:-2] + ' [' + str(compSum) + ' fields]'
        chooseableComps.append(chooseableComp)

    chooseableComps.append('Custom placement')

    for wchild in init.winfo_children():
        wchild.destroy()
    
    Button(init, text='Generate pool play', command=save_divs_by_day).grid()
    dyn_vars = []

    lTeamsDiv = [[[[] for pool in div] for div in listTeamsDiv] for day in range(len(lComp)+1)]
    lDivInfo = [[] for day in range(len(lComp)+1)]
    
    for btn in dyn_btns:
        btn.destroy()

    display_at_row = 1

    for div in listTeamsDiv:
        for pool in div:
            show_div_for_sort(listDivInfo[listTeamsDiv.index(div)],div.index(pool),display_at_row)
            display_at_row += 1

def save_divs_by_day(*args):
    global allOpp
    global lPoolSize

    try:
        if dyn_vars[0].get()[:3] == 'Day':
            del dyn_vars[0]
            del dyn_vars[0]
            del dyn_btns[0]
            del dyn_btns[0]
        
        for b in range(len(dyn_btns)):
            day_str = dyn_vars[b].get()
            day = chooseableComps.index(day_str)
            div_and_pool = dyn_lbls[b].cget('text')
            div = listDivInfo.index(div_and_pool.split('-')[0])
            pool = int(div_and_pool.split('-')[1].split(' (')[0]) - 1
            lTeamsDiv[day][div][pool] = listTeamsDiv[div][pool]
            lDivInfo[day].append(listDivInfo[div])

        for day in lTeamsDiv:
            del_pools = []
            del_divs = []
            for d in range(len(day)):
                for p in range(len(day[d])):
                    if len(day[d][p]) == 0:
                        del_pools.append([d,p])
                if sum([len(pool) for pool in day[d]]) == 0:
                    del_divs.append(d)
            for div_pool in del_pools[::-1]:
                del day[div_pool[0]][div_pool[1]]
            for div in del_divs[::-1]:
                del day[div]

        lPoolSize = [[[len(pool) for pool in div] for div in day] for day in lTeamsDiv]

    except ValueError:
        pass
    
    if 0:
        for day in lTeamsDiv:
            for div in day:
                for pool in div:
                    print('Day',lTeamsDiv.index(day),'Div',listDivInfo[day.index(div)],'Pool',div.index(pool))
                    for team in pool:
                        print(team)
                    print()
                print()
            print()

    run('opponents-gui.py')

    gen_sched()
"""
def restrict_complexes_to_days_show_all(*args):
    global restricted_complexes

    for wchild in init.winfo_children():
        wchild.destroy()

    Label(init, text='Choose which days the complexes are in use').grid(row=0,column=0,columnspan=2+tournament_days,pady=20)

    restricted_complexes = [[IntVar() for c in listComp] for d in range(tournament_days)]

    for d in range(len(restricted_complexes)):
        for c in range(len(restricted_complexes[d])):
            if c==0: Label(init, text=('Day ' + str(d+1))).grid(row=5,column=1+d,padx=10)
            if d==0: Label(init, text=(str(listComp[c][0])+' ['+str(listComp[c][1])+']')).grid(row=10+c,column=0,sticky=W)
            restricted_complexes[d][c].set(1)
            Checkbutton(init, variable=restricted_complexes[d][c]).grid(row=10+c,column=1+d)

    Button(init, text='Save', command=restrict_complexes_to_days_save).grid()

def restrict_complexes_to_days_save(*args):
    global restricted_complexes
    global lComp
    global listComp

    lComp = [[] for i in range(tournament_days)]

    for d in range(len(restricted_complexes)):
        for c in range(len(restricted_complexes[d])):
            if restricted_complexes[d][c].get():
                lComp[d].append(listComp[c])

    print(lComp)

    restrict_divisions_to_complexes_show_all()

        
def gen_sched(*args):
    global dyn_lbls
    global dyn_btns
    global dyn_vars

#    for wchild in init.winfo_children():
#        wchild.destroy()
        
    dyn_lbls = []
    dyn_btns = []
    dyn_vars = []    

    run('schedule-gui.py')
"""                
def view2(*args):
    for wchild in init.winfo_children():
        wchild.destroy()
    
    om_filter_div = OptionMenu(init, get_filter_div, *listDivInfo)
    om_filter_div.grid(row=200, column=1, sticky=(W, E), columnspan=200)

    bt_filter_div = ttk.Button(init, text='Filter', command=filter_divs)
    bt_filter_div.grid(row=200, column=0, sticky=E)
    
def find_opponents(*args):
    pass

def show_div_for_sort(dName, p, r):    
    get_om_var = StringVar()
    get_om_var.set(chooseableComps[0])

    div_and_pool = Label(init, text = dName + '-' + str(p+1) + ' (' + str(len(listTeamsDiv[listDivInfo.index(dName)][p])) + ' teams)')
    div_and_pool.grid(column=0, row=r, sticky=W)
        
    om = OptionMenu(init, get_om_var, *chooseableComps)
    om.grid(column=2, sticky=W, row=r)

    dyn_btns.append(om)
    dyn_vars.append(get_om_var)
    dyn_lbls.append(div_and_pool)

def show_div_teams(name):        
    button = ttk.Label(init, text=name)
    button.grid(column=1, pady=5, padx=5, sticky=W, columnspan=200)
    dyn_btns.append(button)
    
def filter_divs(*args):    
    filter_div = get_filter_div.get()
    
#    ttk.Label(init, text='Pool').grid(row=201, column=0, sticky=E, pady=20, padx=20)
#    ttk.Label(init, text='Team').grid(row=201, column=1, sticky=W, pady=20, padx=20)
    
    for btn in dyn_btns:
        btn.destroy()
        
    try:
        for pool in listTeamsDiv[listDivInfo.index(filter_div)]:
            for team in pool:
                show_div_teams(team)
            
    except ValueError:
        pass

def set_span_days(*args):    
    for wchild in init.winfo_children():
        wchild.destroy()

    Button(init, text='Next', command=leave_span_days).grid(row=0)

    get_span = StringVar()

    Label(init, text='Number of days of pool play').grid(row=1,column=0)
    OptionMenu(init, get_span, *range(1,6)).grid(row=1,column=1,sticky=W)
    Button(init, text='Display', command=lambda: _get_span_days(get_span)).grid(row=1, column=2)

def _get_span_days(var):
    global lComp
    
    for btn in dyn_btns:
        btn.destroy()

    try:
        availableDays = [day_dict[str(i+1)] for i in range(int(var.get()))]
        lComp = [[] for i in range(len(availableDays))]
    except ValueError:
        pass

    startrow = 100
    
    try:
        for c in listComp:
            disp_span_days(c[0],availableDays,startrow)
            startrow += 1
    except NameError:
        pass

def disp_span_days(comp, choose, r):
    get_what_day = StringVar()
    
    Label(init, text=comp).grid(row=r,column=0,sticky=E)
    
    om = OptionMenu(init, get_what_day, *choose)
    om.grid(row=r, column=1,sticky=W, columnspan=50)

    dyn_btns.append(om)
    dyn_vars.append(get_what_day)

def leave_span_days(*args):
    get_span_days.set(0)

    for b in range(len(dyn_btns)):
        chosen_day = dyn_vars[b].get()
        for key in day_dict.keys():
            if day_dict[key] == chosen_day:
                lComp[int(key)-1].append(listComp[b])

    view()
"""
def save_tourn(*args):
    global isSaveAsNew
    
    if isLoggedIn:
        try:
            all_user_data[tourn_id] = [choose_user.get(), entered_pwd.get(), get_s_n.get(), get_nOG.get(), pNumberOfGames*incl_playoffs, get_gPD.get(), pGamesPerDay*incl_playoffs, get_time.get(), get_gmW_NU.get(), get_tournament_num_days.get(), get_ip_t.get(), get_ip_c.get(), get_u_m_p.get(), get_span_days.get(), get_incl_playoffs.get()]
            pop_up('',('Saved tournament: ' + get_s_n.get()))
        except NameError:
            if isSaveAsNew:
                all_user_data[-1] = [choose_user.get(), entered_pwd.get(), get_s_n.get(), get_nOG.get(), pNumberOfGames*incl_playoffs, get_gPD.get(), pGamesPerDay*incl_playoffs, get_time.get(), get_gmW_NU.get(), get_tournament_num_days.get(), get_ip_t.get(), get_ip_c.get(), get_u_m_p.get(), get_span_days.get(), get_incl_playoffs.get()]
                pop_up('',('Saved tournament: ' + get_s_n.get()))
            else:
                pop_up('Error','Please select a tournament to edit')
                return
    else:
        pop_up('Error','Please select a tournament to edit')
        return

    try:
        with open('user data.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(all_user_data)
    except NameError: pass

def save_as_tourn(*args):
    global isSaveAsNew
    
    if isLoggedIn:
        if user_tourns.count(get_s_n.get()):
            pop_up('Error','Tournament name is already in use by this user')
            return
        else:
            all_user_data.append([choose_user.get(), entered_pwd.get(), get_s_n.get(), get_nOG.get(), pNumberOfGames*incl_playoffs, get_gPD.get(), pGamesPerDay*incl_playoffs, get_time.get(), get_gmW_NU.get(), get_tournament_num_days.get(), get_ip_t.get(), get_ip_c.get(), get_u_m_p.get(), get_span_days.get(), get_incl_playoffs.get()]) 
            isSaveAsNew = True
            pop_up('',('Saved tournament: ' + get_s_n.get()))
    else:
        pop_up('Error','Please log in or create a new account')
        return

    try:
        with open('user data.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(all_user_data)
    except NameError: pass
    
def create_new_user(*args):
    global get_new_username
    global get_new_password
    global new_user_message
    
    for wchild in init.winfo_children():
        wchild.destroy()

    get_new_username = StringVar()
    get_new_password = StringVar()
    new_user_message_lbl = StringVar()

    try: new_user_message_lbl.set(new_user_message)
    except NameError: new_user_message_lbl.set('')
    
    Label(init, text='Create new user').grid(row=0,column=0, columnspan=2)
    Label(init, text='Username').grid(row=10,column=0,sticky=E)
    Label(init, text='Password').grid(row=11,column=0,sticky=E)
    Entry(init, textvariable=get_new_username).grid(row=10,column=1,sticky=W)
    Entry(init, textvariable=get_new_password).grid(row=11,column=1,sticky=W)
    Button(init, text='Create', command=create_new_user_validate).grid(row=12,column=0,columnspan=2,sticky=(W,E))
    Label(init, textvariable=new_user_message_lbl).grid(row=13,column=0,columnspan=2,sticky=(W,E))

def create_new_user_validate(*args):
    new_username = get_new_username.get()
    new_password = get_new_password.get()

    if len(new_username) < 5:
        pop_up('Error','Username must be at least 5 characters')
        create_new_user()
        return
        
    if usrs.count(new_username):
        pop_up('Error','Username taken')
        create_new_user()
        return

    all_user_data.append([new_username, new_password,'','','','','','',''])

    with open('user data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(all_user_data)

    load_tourn_disp_users()

def load_tourn_disp_users(*args):
    global all_user_data
    global usrs
    global choose_user

    all_user_data = []
    
    with open('user data.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            all_user_data.append(row)

    for wchild in init.winfo_children():
        wchild.destroy()

    choose_user = StringVar()
    choose_user.set('')

    unique_users = list(set([user[0] for user in all_user_data]))
    try: unique_users.remove('')
    except ValueError: pass
    usrs = [user[0] for user in all_user_data]
    
    Label(init, text='User:').grid(row=1, column=0)
    OptionMenu(init, choose_user, *unique_users).grid(row=1, column=1, sticky=(W, E))
    Button(init, text='Load data', command=load_tourn_disp_pwds).grid(row=1, column=2)
    Button(init, text='New user', command=create_new_user).grid(row=1,column=3)
    
def load_tourn_disp_pwds(*args):
    if not(len(choose_user.get())):
        load_tourn_disp_users()
        return

    global user
    global entered_pwd

    entered_pwd = StringVar()

    Label(init, text='Username').grid(row=10,column=1,sticky=E)
    Label(init, text='Password').grid(row=11,column=1,sticky=E)
    Label(init, text=choose_user.get()).grid(row=10,column=2,sticky=W)
    get_entered_pwd = Entry(init, width=10, textvariable=entered_pwd)
    get_entered_pwd.grid(row=11,column=2)
    Button(init, text='Login', command=check_pwd).grid(row=12,column=1,columnspan=2,sticky=(W,E))
    
def check_pwd(*args):
    global isLoggedIn
    
    actual_pwd = all_user_data[usrs.index(choose_user.get())][1]
    attempt_pwd = entered_pwd.get()

    if actual_pwd == attempt_pwd:
        isLoggedIn = True
        load_tourn_disp_tourns()
    else:
        pop_up('Login failed','Password incorrect, please try again')
        load_tourn_disp_users()
        return

def load_tourn_disp_tourns(*args):
    global choose_tourn
    global user_tourns
    
    user_tourns = [line[2]*(line[0]==choose_user.get()) for line in all_user_data]

    for i in range(user_tourns.count('')):
        user_tourns.remove('')

    choose_tourn = StringVar()
    
    OptionMenu(init, choose_tourn, *(user_tourns + ['**New Tournament**'])).grid(row=30,column=0,columnspan=3)
    Button(init, text='Load', command=load_tourn).grid(row=30,column=3)

def load_tourn(*args):
    global numberOfGames
    global gamesPerDay
    global blocks
    global start_h
    global start_m
    global gmWidth
    global input_path
    global schedule_name
    global complex_path
    global use_manual_pools
    global span_days
    global incl_playoffs
    global listTeamsDiv
    global listDivInfo
    global listDivNumTeams
    global listPoolSize
    global lComp
    global allOpp
    global lPoolSize
    global tourn_id

    if choose_tourn.get()=='**New Tournament**': main_window()
    
    tourn_id = 0
    
    while choose_tourn.get() != all_user_data[tourn_id][2] or choose_user.get() != all_user_data[tourn_id][0]:
        tourn_id += 1
        
    user = all_user_data[tourn_id][2:]

    try: get_s_n.set(user[0])
    except ValueError: pass
    try: get_nOG.set(user[1])
    except ValueError: pass
    try: pNumberOfGames = int(user[2])
    except ValueError: pass
    try: get_gPD.set(user[3])
    except ValueError: pass
    try: pGamesPerDay = int(user[4])
    except ValueError: pass
    try: get_time.set(user[5])
    except ValueError: pass
    try: get_gmW_NU.set(int(user[6]))
    except ValueError: pass
    try: get_tournament_num_days.set(user[7])
    except ValueError: pass
    try: get_ip_t.set(user[8])
    except ValueError: pass
    try: get_ip_c.set(user[9])
    except ValueError: pass
    try: get_u_m_p.set(bool(int(user[10])))
    except ValueError: pass
    try: get_span_days.set(bool(int(user[11])))
    except ValueError: pass
    try: get_incl_playoffs.set(bool(int(user[12])))
    except ValueError: pass
    try:
        raw_lTeamsDiv = user[13]
        raw_lComp = user[14]
        raw_lDivInfo = user[15]
        raw_lPoolSize = user[16]
        isAlreadySetup = True
    except IndexError: pass

    main_window()

def manual_add_teams(*args):
    get_ip_t.set('Added manually')

def manual_add_complex(*args):
    get_ip_c.set('Added manually')

def main_window(*args):
    for wchild in init.winfo_children():
        wchild.destroy()

    Label(init, text='Tournament name').grid(row=1, column=0, sticky=E)
    Label(init, text='Number of games for each team per day').grid(row=2, column=0, sticky=E)
    Label(init, text='Total number of games played on each field per day').grid(row=3, column=0, sticky=E)
    Label(init, text='Start time for first game').grid(row=4, column=0, sticky=E)
    Label(init, text='Length of each game-slot (in minutes)').grid(row=5, column=0, sticky=E)
    #Label(init, text='Length of each period').grid(row=6, column=0, sticky=E)
    Label(init, text='Choose file to input teams/divisions').grid(row=7, column=0, sticky=E)
    Label(init, text='Choose file to input complexes').grid(row=9, column=0, sticky=E)
    Label(init, textvariable=get_ip_t).grid(row=8, column=1, columnspan=100)
    Label(init, textvariable=get_ip_c).grid(row=10, column=1, columnspan=100)
    
    Entry(init, width=7, textvariable=get_s_n).grid(row=1, column=1, sticky=(W, E), columnspan=1000)
    OptionMenu(init, get_nOG, *[str(i) for i in range(1,5)]).grid(row=2, column=1, sticky=(W, E))
    OptionMenu(init, get_gPD, *[str(i) for i in range(1,16)]).grid(row=3, column=1, sticky=(W, E))
    OptionMenu(init, get_time, '6:00', '6:30', '7:00', '7:30', '8:00', '8:30', '9:00', '9:30').grid(row=4, column=1, sticky=(W, E))
    Entry(init, width=5, textvariable=get_gmW_NU).grid(row=5, column=1, sticky=W)

    Button(init, text='Browse', command=lambda: get_ip_t.set(filedialog.askopenfilename())).grid(row=7, column=1)
    Button(init, text='Add manually', command=manual_add_teams).grid(row=7,column=2,sticky=E)
    Button(init, text='Add manually', command=manual_add_complex).grid(row=9,column=2,sticky=E)
    Button(init, text='Browse', command=lambda: get_ip_c.set(filedialog.askopenfilename())).grid(row=9, column=1)

    Label(init, text='Length of tournament (days)').grid(row=11,column=0, sticky=E)
    Entry(init, width=5, textvariable=get_tournament_num_days).grid(row=11,column=1,sticky=W)
    Checkbutton(init, text='Use manual pools', variable=get_u_m_p).grid(row=21,column=1,sticky=W)
    Checkbutton(init, text='Multiple days of pool play with different teams', variable=get_span_days).grid(row=22,sticky=W,column=1,columnspan=1000)
    Checkbutton(init, text='Include playoffs', variable=get_incl_playoffs).grid(row=23,sticky=W,column=1,columnspan=500)

    Button(init, text='Next', command=collect_data_prompt_complexes).grid(row=0, column=1, sticky=W)
    Button(init, text='Login/New User', command=load_tourn_disp_users).grid(row=0, column=0, sticky=E)
    Button(init, text='Save', command=save_tourn).grid(row=0, column=0)
    Button(init, text='Save as New', command=save_as_tourn).grid(row=0, column=0, sticky=W)
    
    for child in init.winfo_children(): child.grid_configure(padx=5, pady=5)

    init.bind('<Return>', get_data)

    root.mainloop()

root = Tk()
root.title('Tournament Scheduler v0.0')
root.geometry('650x800+750+50')

init = Frame(root)
init.grid(column=0, sticky=(N, W, E, S))

get_nOG = StringVar()
get_gPD = StringVar()
get_time = StringVar()
get_gmW_NU = StringVar()
#get_gmW_UL = StringVar()
get_ip_t = StringVar()
get_s_n = StringVar()
get_ip_c = StringVar()
get_filter_div = StringVar()
get_start_date = StringVar()
get_sport = StringVar()
get_dead_time = StringVar()
get_u_m_p = IntVar()
get_span_days = IntVar()
get_incl_playoffs = IntVar()
get_allow_ties = IntVar()
get_show_goals_scores = IntVar()
get_show_goals_allowed = IntVar()
get_show_goal_diff = IntVar()
get_tournament_num_days = StringVar()

dyn_btns = []
dyn_vars = []
dyn_chxs = []
dyn_lbls = []

sport_choices = ['Baseball', 'Basketball', 'Hockey', 'Soccer', 'Lacrosse']
#gmWidth_NU = {'One game' : 1, 'Two halves' : 2, 'Three periods' : 3, 'Four quarters' : 4}
#gmWidth_UL = {'05 minutes':5, '10 minutes':10, '15 minutes':15, '20 minutes':20, '25 minutes':25, '30 minutes':30, '35 minutes':35, '40 minutes':40, '45 minutes':45, '50 minutes':50, '55 minutes':55, '60 minutes':60}
day_dict = {'1' : 'Day One', '2' : 'Day Two', '3' : 'Day Three', '4' : 'Day Four', '5' : 'Day Five'}
pGamesPerDay = 8
pNumberOfGames = 2

isLoggedIn = False
isSaveAsNew = False
isAlreadySetup = False

main_window()
