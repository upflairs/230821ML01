import tkinter as tkr
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter.filedialog as tkfd

app = tkr.Tk(__name__)
app.title('Trial App')
app.geometry('400x800')

def show():
    print('msg:',msg.get())
    print('cb1:',cb1.get())
    print('cb2:',cb2.get())
    print('radio:',rb.get())
    print('spin:',sp.get())
    print('combo:',cmb.get())
    print('option:',opt.get())
    print(list_box.curselection())
    print(list_box.get(list_box.curselection()))

tkr.Button(app,text='click',command=show).pack()

msg = tkr.Variable(app)
msg.set('''First line here
second line here
and more lines
all around''')
tkr.Message(app, textvariable=msg).pack()

cb1 = tkr.Variable(app, '0')
tkr.Checkbutton(app, text='Python', variable=cb1, onvalue=1, offvalue=0).pack()

cb2 = tkr.Variable(app, '0')
tkr.Checkbutton(app, text='AI', variable=cb2, onvalue=1, offvalue=0).pack()


rb = tkr.Variable(app,'1')
rb_values = { 'ML with Data Science':'1',
              'Artificial Intelligence':'2',}
for k,v in rb_values.items():
    tkr.Radiobutton(app, text=k, variable=rb, value=v).pack()


sp = tkr.Variable(app)
tkr.Spinbox(app, from_ = 1, to=12, textvariable=sp).pack()


cmb = tkr.Variable(app)
cmb_values = ('Python','Java','C','C++','C#','PHP','Javascript','NodeJS','HTML','ASP.Net')
cmb.set(cmb_values[0])
ttk.Combobox(app, textvariable=cmb, values=cmb_values).pack()

tkr.Entry(app).pack()
ttk.Entry(app).pack()

opt = tkr.Variable(app)
opt_values = ('Python','Java','C','C++','C#','PHP','Javascript','NodeJS','HTML','ASP.Net')
ttk.OptionMenu(app, opt, *opt_values).pack()


list_box = tkr.Listbox(app, height=5, activestyle='dotbox', fg='white',bg='blue')
list_box.insert(1, 'Face Recognition')
list_box.insert(2, 'Gaana Smart Downloader')
list_box.insert(3, 'Grammarly App')
list_box.insert(4, 'Smart Personal Assistant')
list_box.insert(5, 'Speech Recognition')
list_box.insert(6, 'Voice Recognition')
list_box.insert(7, 'Sound Recognition')
list_box.pack()

def selection():
    global cnv
    global img
    file = tkfd.askopenfiles(mode='r', filetypes=[('Images','*.png')])    
    if file:
        file_name = file[0].name
        img = ImageTk.PhotoImage(Image.open(file_name))
        cnv.create_image(0,0, anchor=tkr.NW , image=img)

tkr.Button(app, text='Open', command=selection).pack()

cnv = tkr.Canvas(app, width=300, height=300)
cnv.pack()

app.mainloop()
