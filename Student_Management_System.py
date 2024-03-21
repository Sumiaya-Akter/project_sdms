#-----------------student function -------------------------------------

#-----------------ADD ----------------------------------------------------------------
def addstudent():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        email = emailval.get()
        mobile = mobileval.get()
        address = addressval.get()
        dob = dobval.get()


        try:
            strr = 'insert into studentdata1 values(%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,email,mobile,address,dob))
            con.commit()
            res = messagebox.askyesnocancel('Notifications','Id {} ,Name {} added successfully....'.format(id,name), parent = addwindow)
            if res == True:
                idval.set('')
                nameval.set('')
                emailval.set('')
                mobileval.set('')
                addressval.set('')
                dobval.set('')

        except:
            messagebox.showerror('Notifications','Id already exists..',parent = addwindow)
        strr = 'select * from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        print(datas)
        studentTable.delete(*studentTable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5]]
            studentTable.insert('',END,values=vv)

    addwindow = Toplevel(master = DataEntryFrame)
    addwindow.grab_set()
    addwindow.geometry('470x470+220+200')
    addwindow.config(bg = 'purple')
    addwindow.resizable(False, False)

    #-----------------Add student labels------------------------------------------

    idlabel = Label(addwindow,text = 'Enter ID: ',font=('times new roman', 15, 'italic bold'), relief=GROOVE,
                      borderwidth=3, width=15, anchor='w')
    idlabel.place(x=10,y=10)
    Namelabel = Label(addwindow, text='Enter Your Name: ', font=('times new roman', 15, 'italic bold'), relief=GROOVE,
                    borderwidth=3, width=15, anchor='w')
    Namelabel.place(x=10, y=70)
    emaillabel = Label(addwindow, text='Enter Email: ', font=('times new roman', 15, 'italic bold'), relief=GROOVE,
                    borderwidth=3, width=15, anchor='w')
    emaillabel.place(x=10, y=130)
    Mobilelabel = Label(addwindow, text='Enter Mobile No: ', font=('times new roman', 15, 'italic bold'),
                        relief=GROOVE,
                        borderwidth=3, width=15, anchor='w')
    Mobilelabel.place(x=10, y=190)
    addresslabel = Label(addwindow, text='Enter Address: ', font=('times new roman', 15, 'italic bold'),
                        relief=GROOVE,
                        borderwidth=3, width=15, anchor='w')
    addresslabel.place(x=10, y=250)
    Dateofbirthlabel = Label(addwindow, text='Enter Date Of Birth: ', font=('times new roman', 15, 'italic bold'), relief=GROOVE,
                       borderwidth=3, width=15, anchor='w')
    Dateofbirthlabel.place(x=10, y=310)

    #----------------- Student Entry Labels ---------------------------
    idval = StringVar()
    nameval = StringVar()
    emailval = StringVar()
    mobileval = StringVar()
    addressval = StringVar()
    dobval = StringVar()

    identry = Entry(addwindow, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)
    nameentry = Entry(addwindow, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    emailentry = Entry(addwindow, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=130)

    mobileentry = Entry(addwindow, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=190)

    addressentry = Entry(addwindow, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    dobentry = Entry(addwindow, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=310)

    # -----------Submit button--------
    addsubmitbutton = Button(addwindow, text='Submit', font=('roman', 18, 'italic bold'), width=20,command=submitadd)
    addsubmitbutton.place(x=120, y=370)

    addwindow.mainloop()


#-----------------Search ----------------------------------------------------------------
def searchstudent():
    def submitsearch():
        id = idval.get()
        name = nameval.get()
        email = emailval.get()
        if id != '':
            strr = 'select * from studentdata1 where id = %s'
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
                studentTable.insert('', END, values=vv)

        elif email != '':
            strr = 'select * from studentdata1 where email = %s'
            mycursor.execute(strr,(email))
            datas = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
                studentTable.insert('', END, values=vv)

        elif name != '':
            strr = 'select * from studentdata1 where name = %s'
            mycursor.execute(strr,(name))
            datas = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
                studentTable.insert('', END, values=vv)

    searchwindow = Toplevel(master = DataEntryFrame)
    searchwindow.grab_set()
    searchwindow.geometry('470x300+220+150')
    searchwindow.config(bg = 'purple')
    searchwindow.resizable(False, False)

    #-----------------Add student labels------------------------------------------

    idlabel = Label(searchwindow,text = 'Enter ID: ',font=('times new roman', 15, 'italic bold'), relief=GROOVE,
                      borderwidth=3, width=15,  anchor='w')
    idlabel.place(x=10,y=10)

    Namelabel = Label(searchwindow, text='Enter Your Name: ', font=('times new roman', 15, 'italic bold'), relief=GROOVE,
                    borderwidth=3, width=15,  anchor='w')
    Namelabel.place(x=10, y=70)

    emaillabel = Label(searchwindow, text='Enter Email: ', font=('times new roman', 15, 'italic bold'), relief=GROOVE,
                    borderwidth=3, width=15,  anchor='w')
    emaillabel.place(x=10, y=130)



    #----------------- Student Entry Labels ---------------------------
    idval = StringVar()
    nameval = StringVar()
    emailval = StringVar()


    identry = Entry(searchwindow, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(searchwindow, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    emailentry = Entry(searchwindow, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=130)


    # -----------Submit button--------
    searchsubmitbutton = Button(searchwindow, text='Submit', font=('roman', 18, 'italic bold'), width=20,command=submitsearch)
    searchsubmitbutton.place(x=120, y=220)

    searchwindow.mainloop()
def deletestudent():
    cc = studentTable.focus()
    content = studentTable.item(cc)
    print(content)
    dlt = content['values'][0]
    strr = 'delete from studentdata1 where id = %s'
    mycursor.execute(strr,(dlt))
    con.commit()
    messagebox.showinfo('Notification','Id {} deleted successfully'.format(dlt))

    strr = 'select * from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
        studentTable.insert('', END, values=vv)

#-----------------Update ----------------------------------------------------------------
def updatestudent():
    def submitupdate():
        id = idval.get()
        name = nameval.get()
        email = emailval.get()
        mobile = mobileval.get()
        address = addressval.get()
        dob = dobval.get()

        strr = 'update studentdata1 set name = %s,email = %s,mobile = %s,address = %s,dob = %s where id=%s'
        mycursor.execute(strr,(name,email,mobile,address,dob,id))
        con.commit()
        messagebox.showinfo('Notification', 'Id {} updated successfully'.format(id),parent = updatewindow)

        strr = 'select * from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
            studentTable.insert('', END, values=vv)


    updatewindow = Toplevel(master = DataEntryFrame)
    updatewindow.grab_set()
    updatewindow.geometry('470x470+220+200')
    updatewindow.config(bg = 'purple')
    updatewindow.resizable(False, False)

    #-----------------Add student labels------------------------------------------

    idlabel = Label(updatewindow,text = 'Enter ID: ',font=('times new roman', 15, 'italic bold'), relief=GROOVE,
                      borderwidth=3, width=15, anchor='w')
    idlabel.place(x=10,y=10)
    Namelabel = Label(updatewindow, text='Enter Your Name: ', font=('times new roman', 15, 'italic bold'), relief=GROOVE,
                    borderwidth=3, width=15, anchor='w')
    Namelabel.place(x=10, y=70)
    emaillabel = Label(updatewindow, text='Enter Email: ', font=('times new roman', 15, 'italic bold'), relief=GROOVE,
                    borderwidth=3, width=15, anchor='w')
    emaillabel.place(x=10, y=130)
    Mobilelabel = Label(updatewindow, text='Enter Mobile No: ', font=('times new roman', 15, 'italic bold'),
                        relief=GROOVE,
                        borderwidth=3, width=15, anchor='w')
    Mobilelabel.place(x=10, y=190)
    addresslabel = Label(updatewindow, text='Enter Address: ', font=('times new roman', 15, 'italic bold'),
                        relief=GROOVE,
                        borderwidth=3, width=15, anchor='w')
    addresslabel.place(x=10, y=250)
    Dateofbirthlabel = Label(updatewindow, text='Enter Date Of Birth: ', font=('times new roman', 15, 'italic bold'), relief=GROOVE,
                       borderwidth=3, width=15, anchor='w')
    Dateofbirthlabel.place(x=10, y=310)

    #----------------- Student Entry Labels ---------------------------
    idval = StringVar()
    nameval = StringVar()
    emailval = StringVar()
    mobileval = StringVar()
    addressval = StringVar()
    dobval = StringVar()

    identry = Entry(updatewindow, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)
    nameentry = Entry(updatewindow, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    emailentry = Entry(updatewindow, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=130)

    mobileentry = Entry(updatewindow, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=190)

    addressentry = Entry(updatewindow, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    dobentry = Entry(updatewindow, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=310)

    # -----------Submit button--------
    updatesubmitbutton = Button(updatewindow, text='Submit', font=('roman', 18, 'italic bold'), width=20,command=submitupdate)
    updatesubmitbutton.place(x=120, y=370)

    cc = studentTable.focus()
    content = studentTable.item(cc)
    dlt = content['values']
    if len(dlt) != 0:
        idval.set(dlt[0])
        nameval.set(dlt[1])
        emailval.set(dlt[2])
        mobileval.set(dlt[3])
        addressval.set(dlt[4])
        dobval.set(dlt[5])




    updatewindow.mainloop()
def showallstudent():
    strr = 'select * from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
        studentTable.insert('', END, values=vv)
def exitstudent():
    res = messagebox.askyesnocancel('Notification','Do you want to exit')
    if res == TRUE:
        window.destroy()

#--------------------------------Database Connection---------------------------
def ConnectDatabase():
    def submitdb():
        global con,mycursor
        #hello
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        print(host,user,password)
        try:
            con = pymysql.connect(host = host,user = user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notification','Data is incorrect,please try again',parent = dbwindow)
            return
        try:
            strr = 'create database StudentManagementSystem'
            mycursor.execute(strr)
            strr = 'use StudentManagementSystem'
            mycursor.execute(strr)
            strr = 'create table StudentData1(Id int,Name varchar(50),Email varchar(30),Mobile varchar(15),Address varchar(100),DateOfBirth varchar(50))'
            mycursor.execute(strr)
            strr = 'alter table StudentData1 modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table StudentData1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', "Database Connected", parent=dbwindow)

        except:
            strr = 'use StudentManagementSystem'
            mycursor.execute(strr)
            messagebox.showinfo('Notification',"Now you are connecting to the database....",parent = dbwindow)
        dbwindow.destroy()



    dbwindow = Toplevel()
    dbwindow.grab_set()
    dbwindow.geometry('470x250+800+230')
    dbwindow.resizable(False,False)
    dbwindow.config(bg = 'purple')
    #-------------------------------Database Connection labels---------------------------
    hostlabel = Label(dbwindow,text = "Enter host: ",font=('times new roman',15,'italic bold'),relief = GROOVE,
                      borderwidth = 3,width=15,anchor = 'w')
    hostlabel.place(x = 10,y = 10)

    userlabel = Label(dbwindow, text="Enter User: ", font=('times new roman', 15, 'italic bold'), relief=GROOVE,
                      borderwidth=3, width=15, anchor='w')
    userlabel.place(x=10, y=70)

    passwordlabel = Label(dbwindow, text="Enter Password: ", font=('times new roman', 15, 'italic bold'), relief=GROOVE,
                      borderwidth=3, width=15, anchor='w')
    passwordlabel.place(x=10, y=130)
    # -------------------------------Database Connection Entry---------------------------
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbwindow,font=('roman',15,'bold'),bd = 5,textvariable= hostval)
    hostentry.place(x = 220,y=10)
    userentry = Entry(dbwindow, font=('roman', 15, 'bold'), bd=5, textvariable=userval)
    userentry.place(x=220,y= 70)
    passwordentry = Entry(dbwindow, font=('roman', 15, 'bold'), bd=5, textvariable=passwordval)
    passwordentry.place(x=220, y= 130)
    #-----------Submit button--------
    submitbutton = Button(dbwindow,text = 'Submit',font=('roman', 18, 'italic bold'),width=20,command=submitdb)
    submitbutton.place(x=150,y=190)
    dbwindow.mainloop()

#-------------------------------------------------------------------------------
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text= "Date : "+date_string+"\n"+"Time : "+time_string)
    clock.after(200,tick)
#-------------------------------------------------------------------------------
def IntroLabelTick():
    global count,text
    if count>=len(ss):
        count = -1
        text =''
        SliderLabel.config(text=text)
    else:
        text=text+ss[count]
        SliderLabel.config(text=text)
    count += 1
    SliderLabel.after(200,IntroLabelTick)

#-------- Main code ------------------------
from tkinter import *
from tkinter import Toplevel,messagebox
import time
from tkinter.ttk import Treeview
import pymysql

window = Tk()
window.title('Student Management System')
window.config(bg='skyblue')
window.geometry('1174x700+200+50')
window.iconbitmap('')
window.resizable(False,False)

#------  Frame -------------------------------
DataEntryFrame = Frame(window,bg = 'skyblue',relief = GROOVE,borderwidth = 5)
DataEntryFrame.place(x=10,y=80,width = 500, height = 600)

#-------------Data Entry Frame -----
Frontlabel = Label(DataEntryFrame,text = '----------Welcome---------',width=30,font=('arial',22,'italic bold'),bg='skyblue')
Frontlabel.pack(side=TOP,expand=True)

addbtn = Button(DataEntryFrame,text = "Add",width=25,font=('Times new roman',20,'italic bold'),bg='pink',command = addstudent)
addbtn.pack(side=TOP,expand=True)

srcbtn = Button(DataEntryFrame,text = "Search",width=25,font=('Times new roman',20,'italic bold'),bg='pink',command = searchstudent)
srcbtn.pack(side=TOP,expand=True)

dltbtn = Button(DataEntryFrame,text = "Delete",width=25,font=('Times new roman',20,'italic bold'),bg='pink',command = deletestudent)
dltbtn.pack(side=TOP,expand=True)

updtbtn = Button(DataEntryFrame,text = "Update",width=25,font=('Times new roman',20,'italic bold'),bg='pink',command = updatestudent)
updtbtn.pack(side=TOP,expand=True)

showallbtn = Button(DataEntryFrame,text = "Show all",width=25,font=('Times new roman',20,'italic bold'),bg='pink',command = showallstudent)
showallbtn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame,text = "Exit",width=25,font=('Times new roman',20,'italic bold'),bg='pink',command = exitstudent)
exitbtn.pack(side=TOP,expand=True)

ShowDataFrame = Frame(window,bg = 'skyblue',relief = GROOVE,borderwidth = 5)
ShowDataFrame.place(x=550,y=80,width = 620, height = 600)

#------ Student Form ---------------------------------------------------------------
scrolll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scrolll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)
studentTable = Treeview(ShowDataFrame,columns = ('Id','Name','Email','Mobile No','Address','Date of Birth'),xscrollcommand=scrolll_x.set,yscrollcommand=scrolll_y.set)
scrolll_x.pack(side=BOTTOM,fill=X)
scrolll_y.pack(side=RIGHT,fill=Y)
scrolll_x.config(command=studentTable.xview)
scrolll_y.config(command=studentTable.yview)
studentTable.heading('Id',text='ID')
studentTable.heading('Name',text='Name')
studentTable.heading('Email',text='Email')
studentTable.heading('Mobile No',text='IMobile NoD')
studentTable.heading('Address',text='Address')
studentTable.heading('Date of Birth',text='Date of Birth')
studentTable['show'] = 'headings'
studentTable.pack(fill = BOTH,expand = True)

#------ slider ---------------------------------
ss = "Welcome to Student Management System"
count = 0
text = ''
SliderLabel = Label(window,text = ss,font=('times new roman',20,'italic bold'),relief = RIDGE,borderwidth = 5,width=38,bg='pink')
SliderLabel.place(x = 250,y = 10)
IntroLabelTick()


clock = Label(window,font = ('times',12,'bold'),relief = RIDGE,borderwidth = 5,width=20,bg='pink')
clock.place(x = 10,y = 10)
tick()

#--------------------Connect to database------------------
button = Button(window,text = 'Connect to Database',font=('times new roman',14,'italic bold'),relief = RIDGE,borderwidth = 5,width=20,bg='pink',command=ConnectDatabase)
button.place(x = 930,y=10)
window.mainloop()


