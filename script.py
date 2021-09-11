import tkinter as tkr
app = tkr.Tk(__name__)
app.title('My App')
app.geometry('250x200')

k = tkr.Label(app, text='Welcome')
k.pack(anchor=tkr.NW)

tkr.Label(app, text='Hello').pack(anchor=tkr.NW)
tkr.Label(app, text='Bye').pack(anchor=tkr.NW)

##tkr.Label(app, text='Welcome').grid(row=0,column=2)
##tkr.Label(app, text='Hello').grid(row=1,column=0)
##tkr.Label(app, text='Bye').grid(row=0,column=1)

##tkr.Label(app, text='Welcome').place(x=10, y=10)
##tkr.Label(app, text='Hello').place(x=10,y=120)
##tkr.Label(app, text='Bye').place(x=100, y=130)


app.mainloop()
