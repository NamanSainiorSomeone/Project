from fileinput import filename
from re import L
import time
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import ttk

#window , button
def click():
    print('clcik')

window = Tk()
window.geometry("1230x530")
window.title("GUI")
window.config(background='black')

bphoto = PhotoImage(file="D:\\Downloads\\21-210418_like-png-thumbs-up-emoji-messenger-transparent-png (1).png")

button = Button(window,
text= 'click me',
command=click,
fg='green',
bg='black',
activeforeground='green',
activebackground='blue',
state=ACTIVE,image=bphoto,
compound=TOP)

button.place(x=420,y=10)

photo = PhotoImage(file="D:\\Downloads\\beautiful-hologram-water-color-frame-png_119551.png")
label = Label(window,
text='This is a GUI',
font=('Arial',20,'bold'),
fg='green',
bg='black',
bd=0,
padx=0,
image=photo,
compound='bottom')

label.place(x=0,y=0)


def submits():
    if entry.get() != "":
        submit.config(state=ACTIVE)
        username = entry.get()
        print(username)

#widget
#entry box

entry = Entry(window)
entry.place(x=400, y=200)
entry.get()== None

submit =Button(window,text='SUBMIT',command=submits)
submit.place(x=430,y=230)

#Checkbox


def submitss():
    print("aggreed")


def display():
    if (x.get()==1):
        print("yes")
        submit_button.config(state=ACTIVE)
    else:
        print("np")
        submit_button.config(state=DISABLED)


x= IntVar()
checkbox = Checkbutton(window,text= 'aggreed',
variable=x,
onvalue=1,
offvalue=0,
command=display)
checkbox.place(x=500, y=260)

submit_button = Button(window,text="submit", command=submitss,state=DISABLED)
submit_button.place(x=550,y=300)


#Radiobutton

food = ["pizza","buger","hotdog"]
y= IntVar()
for index in range(len(food)):
    radiobutton = Radiobutton(window,text=food[index],variable=y,value=index,width=24)
    radiobutton.pack(anchor=W)


#scale


def temp():
    print(scale.get())


scale= Scale(window,from_=100,to=00,length=100,tickinterval=40,
troughcolor='RED'

)
scale.place(x=430,y=250)
buttons = Button(window,text='submit',command=temp)
buttons.place(x=430,y=370)


#Listbox

def sf1():
    food =[]
    for index in LISTBOX.curselection():
        food.insert(index,LISTBOX.get(index))
    #print(LISTBOX.get(LISTBOX.curselection()))
    for index in food:
        print(index)


LISTBOX= Listbox(window,bg='cyan',fg='green',selectmode=MULTIPLE)
LISTBOX.place(x=550,y=0)
LISTBOX.insert(0,'pizza')
LISTBOX.insert(1,'hotdog')
LISTBOX.insert(2,'bugur')
LISTBOX.config(height=LISTBOX.size())


def af1():

    LISTBOX.insert(LISTBOX.size()+1,e1.get())
    LISTBOX.config(height=LISTBOX.size())


e1 = Entry(window)
e1.place(x=585,y=100)



a1 = Button(window,text='add',command=af1)
a1.place(x=585,y=56)

s1 = Button(window,text='submit',command=sf1)
s1.place(x=580,y=125)


#msgbox
def c1():
    #messagebox.showinfo(title='Virus.exe',message='Click OK to get a virus',)
    #messagebox.showerror(title='Virus.exe',message='Click OK to get a virus')
    #messagebox.showwarning(title='Virus.exe',message='Click OK to get a virus')
    if messagebox.askokcancel(title='Virus.exe',message='Click OK to get a virus',icon='warning'):
        print("you got a virus")
    else:
        print("you got two virus")
bm = Button(window,text='Virus',command=c1)
bm.place(x=600,y=200)



#color

def bf3():
    color = colorchooser.askcolor()
    colorhex = color[1]
    window.config(bg=colorhex)

b3 = Button(window,text="color chooser",command=bf3)
b3.place(x=600,y=250)

#text area
def bf4():
    print(texta.get('1.0',END))



texta = Text(window,
bg='light yellow', height=4,width=14)
texta.place(x=600,y=350)
b4 = Button(text="submit",command=bf4)
b4.place(x=550,y=350)

#open a file
def bf5():
    filepath = filedialog.askopenfilename(title='Open file')
    filee = open(filepath,'r')  #r = read text
    print(filee.read())
    filee.close()
b5 = Button(text="open",command= bf5)
b5.place(x=100,y=420)


#save a file, go to text area first
def bf6():
    files =filedialog.asksaveasfile(title="Save file",defaultextension=".txt",filetypes=[("text file",".txt"),
    ("python",".py")])

    if files is None:
        return
    filetextt = str(texta.get(1.0,END))
    files.write(filetextt)
    files.close()


b6 = Button(text="Save",command=bf6)
b6.place(x=550,y=380)


#menu bar


menubar = Menu(window)
window.config(menu=menubar)


filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='open',command=bf5)
filemenu.add_command(label='save',command=bf6)
filemenu.add_separator()
filemenu.add_command(label='exit',command=quit)

# Frames

frame =Frame(window,relief=RAISED)
frame.place(x=450,y=400)
Button(frame,text='W').pack(side=TOP)
Button(frame,text='A').pack(side=LEFT)
Button(frame,text='S').pack(side=LEFT)
Button(frame,text='D').pack (side=LEFT)

#New window
def cw():
    nwe_win =Toplevel()

    #grid
    
    def Bf7():
        print(firstnamess)

    firstnamess = Label(nwe_win,text="Name").grid()
    first = Entry(nwe_win).grid(row=0,column=1)

    B7 = Button(nwe_win,text="Submit",command=Bf7).grid(row=2,column=1)




#New window cnd

Button(window,text="New window",command=cw).place(x=269,y=420)


#Tabs


notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1,text="tab1")

notebook.add(tab2,text="tab2")

notebook.place(x=372,y=399)


Label(tab1,text='TAB1').pack()
Label(tab2,text='TAB2').pack()


#progress bar
percent = StringVar()
def Start():
    task = 10
    x=0
    while x<task:
        time.sleep(1)
        bar["value"]+=10
        x+=1
        percent.set(str((x/task)*100)+"%")
        window.update_idletasks()

bar = ttk.Progressbar(window,orient=HORIZONTAL)
bar.place(x=450,y=450)

b8 = Button(window,text='Download',command=Start).place(x=550,y=450)


per = Label(window,textvariable=percent).place(x=480,y=470)

#Canvas


canvas = Canvas(window,height=500,width=500)
canvas.create_line(2,2,500,500, fill="red")
                 #start# e n d
canvas.place(x=720,y=20)


#Key event


def smt(event):
    print("forward "+ event.keysym)

window.bind("<w>",smt)

#Mouse events


def smtt(event):
    print("smt " + str(event.x)+ " "+str(event.y))


window.bind("<Button-1>",smtt)


#Drag and drop

def drag(event):
    labell.startX = event.x
    labell.startY = event.y


def dragm(event):
    x = labell.winfo_x() - labell.startX + event.x
    y = labell.winfo_y() - labell.startY + event.y
    labell.place(x=x,y=y)

labell = Label(window,bg="Red",width=10,height=5)
labell.place(x=179,y=408)

labell2 = Label(window,bg="blue",width=10,height=5)
labell2.place(x=5,y=408)


labell.bind("<Button-1>",drag)
labell.bind("<B1-Motion>",dragm)


#animation

H=500
W=500
xv = 1
yv = 3

png = PhotoImage(file="pppp.png")

pnn = canvas.create_image(0,0,image=png,anchor=NW)

iw = png.width()
ih = png.height()


'''while True:
    cods= canvas.coords(pnn)
    print(cods)
    if cods[0]>=W-iw or cods[0]<0:
        xv = -xv
    if cods[1]>=H-ih or cods[1]<0:
        yv = -yv
    canvas.move(pnn,xv,yv)
    window.update()
    time.sleep(0.01)
    
'''

#Clock


def bf9():
    def upd():
        strt = time.strftime("%I:%M:%S %p")
        timel.config(text=strt)
        timel.after(1000,upd)


    new_window = Tk()
    timel = Label(new_window,fg="red",bg="black",height=5,width=30,font=300)
    timel.pack() 
    upd()
 
    new_window.mainloop()

#Getting boared


B9 = Button(window,text="Clock",command=bf9)

B9.place(x=370,y=300)

def bf10():
    Label(window,text='Getting boarde').place(x=604,y=303)



b10 = Button(window,text="Just to fill lies",command=bf10)

b10.place(x=417,y=165)


window.mainloop()