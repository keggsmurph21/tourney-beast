sec = Frame(root)
sec.grid(column=0, row=200, sticky=(N,W,E,S))

bt_filter_div = Button(sec, 'Filter', command=lambda: get_spec(filter_div, get_filter_div))
bt_filter_div.grid(row=0, column=0, sticky=E)
