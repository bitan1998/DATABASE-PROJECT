from tkinter import *
import tkinter.messagebox
import backend

class Student:
        def __init__(self,root):
                self.root=root
                self.root.title("Student Database Management System")
                self.root.geometry("19200x7500+0+0")
                self.root.config(bg="cadet blue")

                StdId=StringVar()
                Firstname=StringVar()
                Surname=StringVar()
                Dob=StringVar()
                Emailid=StringVar()
                Subject=StringVar()
                Address=StringVar()
                Mobile=StringVar()
                RfId=StringVar()

                #======================================================Function=============================================
                def iExit():
                        iExit = tkinter.messagebox.askyesno("Student Database Management System","Confirm if you want to exit")
                        if iExit>0:
                                root.destroy()
                                return 

                def clearData():
                        self.txtStdID.delete(0,END)
                        self.txtfna.delete(0,END)
                        self.txtSna.delete(0,END)
                        self.txtDoB.delete(0,END)
                        self.txtEmail.delete(0,END)
                        self.txtSubject.delete(0,END)
                        self.txtAdr.delete(0,END)
                        self.txtMob.delete(0,END)
                        self.txtRfId.delete(0,END)

                def addData():
                        if (len(StdId.get())!=0):
                                backend.addStdRec(StdId.get(),Firstname.get(),Surname.get(),Dob.get(),Emailid.get(), \
                                        Subject.get(),Address.get(),Mobile.get(),RfId.get())
                                studentlist.delete(0,END)
                                studentlist.insert(END,(StdId.get(),Firstname.get(),Surname.get(),Dob.get(),Emailid.get(),Subject.get(),Address.get(), \
                                        Mobile.get(),RfId.get()))

                
                def DisplayData():
                        studentlist.delete(0,END)
                        for row in backend.viewData():
                                studentlist.insert(END,row,str(""))

                def StudentRec(event):
                        global sd
                        searchStd = studentlist.curselection()[0]
                        sd= studentlist.get(searchStd)
                        self.txtStdID.delete(0,END)
                        self.txtStdID.insert(END,sd[1])
                        self.txtfna.delete(0,END)
                        self.txtfna.insert(END,sd[2])
                        self.txtSna.delete(0,END)
                        self.txtSna.insert(END,sd[3])
                        self.txtDoB.delete(0,END)
                        self.txtDoB.insert(END,sd[4])
                        self.txtEmail.delete(0,END)
                        self.txtEmail.insert(END,sd[5])
                        self.txtSubject.delete(0,END)
                        self.txtSubject.insert(END,sd[6])
                        self.txtAdr.delete(0,END)
                        self.txtAdr.insert(END,sd[7])
                        self.txtMob.delete(0,END)
                        self.txtMob.insert(END,sd[8])
                        self.txtRfId.delete(0,END)
                        self.txtRfId.insert(END,sd[9])

                def DeleteData():
                        if(len(StdId.get())!=0):
                                backend.deleteRec(sd[0])
                                clearData()
                                DisplayData()

                def searchDatabase():
                        studentlist.delete(0,END)
                        for row in backend.searchData(StdId.get(),Firstname.get(),Surname.get(),Dob.get(),Emailid.get(), \
                                        Subject.get(),Address.get(),Mobile.get(),RfId.get()):
                                studentlist.insert(END,row,str(""))

                def update():
                        if(len(StdId.get())!=0):
                                backend.deleteRec(std[0])
                        if(len(StdId.get())!=0):
                                backend.addStdRec(StdId.get(),Firstname.get(),Surname.get(),Dob.get(),Emailid.get(), \
                                        Subject.get(),Address.get(),Mobile.get(),RfId.get())
                                studentlist.delete(0,END)
                                backend.insert(END,(StdId.get(),Firstname.get(),Surname.get(),Dob.get(),Emailid.get(), \
                                        Subject.get(),Address.get(),Mobile.get(),RfId.get()))                              
                        
                                

                #=========================================================Frames==================================================
                MainFrame = Frame(self.root,bg="cadet blue")
                MainFrame.grid()

                TitleFrame = Frame(MainFrame, bd=2, padx=67, pady=8, bg="Ghost White", relief= RIDGE)
                TitleFrame.pack(side=TOP)

                self.lblTit = Label(TitleFrame,font=('arial',47,'bold'),text="Student Database Management System" , bg="Ghost White")
                self.lblTit.grid()

                ButtonFrame = Frame(MainFrame, bd=2, width=1350, height = 70 ,padx=18, pady=10, bg="Ghost White", relief= RIDGE)
                ButtonFrame.pack(side=BOTTOM)

                DataFrame = Frame(MainFrame, bd=1, width=1300, height = 400 ,padx=20, pady=20, bg="cadet blue", relief= RIDGE)
                DataFrame.pack(side=BOTTOM)

                DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height = 600 ,padx=20, bg="Ghost White", relief= RIDGE,
                                                font=('arial',20,'bold'),text="Student Information\n")
                DataFrameLEFT.pack(side=LEFT)

                DataFrameRIGHT =LabelFrame(DataFrame, bd=1, width=450, height = 300 ,padx=31, pady=3, bg="Ghost White", relief= RIDGE,
                                                font=('arial',20,'bold'),text="Student Details\n")
                DataFrameRIGHT.pack(side=RIGHT)

        #=========================================================Labels and Entry Widget==================================================

       

                self.lblSTDID = Label(DataFrameLEFT,font=('arial',20,'bold'), text="Student ID:",padx=2,pady=2,bg="Ghost White")
                self.lblSTDID .grid(row=0,column=0,sticky=W)
                self.txtStdID = Entry(DataFrameLEFT,font=('arial',20,'bold'), textvariable=StdId, width=39)
                self.txtStdID .grid(row=0,column=1)     

                self.lblfna = Label(DataFrameLEFT,font=('arial',20,'bold'), text="Firstname:",padx=2,pady=2,bg="Ghost White")
                self.lblfna .grid(row=1,column=0,sticky=W)
                self.txtfna = Entry(DataFrameLEFT,font=('arial',20,'bold'), textvariable=Firstname, width=39)
                self.txtfna .grid(row=1,column=1)       

                self.lblSna = Label(DataFrameLEFT,font=('arial',20,'bold'), text="Surname:",padx=2,pady=2,bg="Ghost White")
                self.lblSna .grid(row=2,column=0,sticky=W)
                self.txtSna = Entry(DataFrameLEFT,font=('arial',20,'bold'), textvariable=Surname, width=39)
                self.txtSna .grid(row=2,column=1)       

                self.lblDoB = Label(DataFrameLEFT,font=('arial',20,'bold'), text="Date of Birth(dd-mm-yyyy):",padx=2,pady=2,bg="Ghost White")
                self.lblDoB .grid(row=3,column=0,sticky=W)
                self.txtDoB = Entry(DataFrameLEFT,font=('arial',20,'bold'), textvariable=Dob, width=39)
                self.txtDoB .grid(row=3,column=1)       

                self.lblEmail = Label(DataFrameLEFT,font=('arial',20,'bold'), text="Email-id:",padx=2,pady=2,bg="Ghost White")
                self.lblEmail .grid(row=4,column=0,sticky=W)
                self.txtEmail = Entry(DataFrameLEFT,font=('arial',20,'bold'), textvariable=Emailid, width=39)
                self.txtEmail .grid(row=4,column=1)     

                self.lblSubject = Label(DataFrameLEFT,font=('arial',20,'bold'), text="Subject:",padx=2,pady=2,bg="Ghost White")
                self.lblSubject .grid(row=5,column=0,sticky=W)
                self.txtSubject = Entry(DataFrameLEFT,font=('arial',20,'bold'), textvariable=Subject, width=39)
                self.txtSubject .grid(row=5,column=1)   

                self.lblAdr = Label(DataFrameLEFT,font=('arial',20,'bold'), text="Address:",padx=2,pady=2,bg="Ghost White")
                self.lblAdr .grid(row=6,column=0,sticky=W)
                self.txtAdr = Entry(DataFrameLEFT,font=('arial',20,'bold'), textvariable=Address, width=39)
                self.txtAdr .grid(row=6,column=1)       

                self.lblMob = Label(DataFrameLEFT,font=('arial',20,'bold'), text="Mobile no:",padx=2,pady=2,bg="Ghost White")
                self.lblMob .grid(row=7,column=0,sticky=W)
                self.txtMob = Entry(DataFrameLEFT,font=('arial',20,'bold'), textvariable=Mobile, width=39)
                self.txtMob .grid(row=7,column=1)

                self.lblRfId = Label(DataFrameLEFT,font=('arial',20,'bold'), text="RF ID:",padx=2,pady=2,bg="Ghost White")
                self.lblRfId .grid(row=8,column=0,sticky=W)
                self.txtRfId = Entry(DataFrameLEFT,font=('arial',20,'bold'), textvariable=RfId, width=39)
                self.txtRfId .grid(row=8,column=1)      

                #================================================Listbox and ScrollBar Widget=================================================
                scrollbar = Scrollbar(DataFrameRIGHT)
                scrollbar.grid(row=0,column=1,sticky='ns')

                studentlist = Listbox(DataFrameRIGHT, width=41, height=16,font=('arial',12,'bold'),yscrollcommand=scrollbar.set,xscrollcommand=scrollbar.set)
                studentlist.grid(row=0,column=0,padx=8)
                scrollbar.config(command = studentlist.yview)
                scrollbar.config(command= studentlist.xview)                       

                #================================================Button Widget=================================================================
                self.btnAddData = Button(ButtonFrame , text="Add New",font=('arial',20,'bold'),height=1,width=10,bd=4,command=addData)
                self.btnAddData.grid(row=0,column=0)

                self.btnDisplayData = Button(ButtonFrame , text="Display",font=('arial',20,'bold'),height=1,width=10,bd=4,command=DisplayData)
                self.btnDisplayData.grid(row=0,column=1)

                self.btnClearData = Button(ButtonFrame , text="Clear",font=('arial',20,'bold'),height=1,width=10,bd=4,command=clearData)
                self.btnClearData.grid(row=0,column=2)

                self.btnDeleteData = Button(ButtonFrame , text="Delete",font=('arial',20,'bold'),height=1,width=10,bd=4,command=DeleteData)
                self.btnDeleteData.grid(row=0,column=3)

                self.btnUpdateData = Button(ButtonFrame , text="Search",font=('arial',20,'bold'),height=1,width=10,bd=4,command=update)
                self.btnUpdateData.grid(row=0,column=4)

                self.btnSearchData = Button(ButtonFrame , text="Update",font=('arial',20,'bold'),height=1,width=10,bd=4,command=searchDatabase)
                self.btnSearchData.grid(row=0,column=5)

                self.btnExit = Button(ButtonFrame , text="Exit",font=('arial',20,'bold'),height=1,width=10,bd=4,command=iExit)
                self.btnExit.grid(row=0,column=6)



if __name__=='__main__':
        root=Tk()
        application=Student(root)
        root.mainloop()
