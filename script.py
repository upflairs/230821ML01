import tkinter as tkr
app = tkr.Tk(__name__)
app.title('Calculator')
app.geometry('300x400')

tkr.Label(app, text='Calculator',font=('Arial',20),fg='red').place(x=75,y=10)
tkr.Label(app,text='First Value').place(x=30,y=70)
tkr.Label(app,text='Second Value').place(x=150,y=70)

fv = tkr.Variable(app)
sv = tkr.Variable(app)

tkr.Entry(app, textvariable=fv, font=('Arial',13), width=11).place(x=30,y=90)
tkr.Entry(app, textvariable=sv, font=('Arial',13), width=11).place(x=150,y=90)

def operate(op):
    res.set(eval(fv.get()+op+sv.get()))


tkr.Button(app, text='+',font=('Arial',15),bg='red',fg='white', width=3,
           command=lambda:operate('+')).place(x=30,y=130)
tkr.Button(app, text='-',font=('Arial',15),bg='red',fg='white', width=3,
           command=lambda:operate('-')).place(x=90,y=130)
tkr.Button(app, text='x',font=('Arial',15),bg='red',fg='white', width=3,
           command=lambda:operate('*')).place(x=150,y=130)
tkr.Button(app, text='/',font=('Arial',15),bg='red',fg='white', width=3,
           command=lambda:operate('/')).place(x=210,y=130)


tkr.Label(app,text='Result:').place(x=90,y=240)

res = tkr.Variable(app)
res.set('0')
tkr.Label(app,textvariable=res,bg='white',font=('Arial',15),).place(x=130,y=235)

app.mainloop()
