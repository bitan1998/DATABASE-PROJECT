from tkinter import *
import tkinter.messagebox
import backend
import os
import tempfile
from tkinter import ttk
import tkinter.filedialog

class Student:

	def __init__(self,root):
		self.root=root
		self.root.title("*Asterix Educations")
		width, height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
		# self.root.geometry('%dx%d+0+0' % (width,height))
		self.root.geometry("1980x900+0+0")
		self.root.config(width=width,height=height,bg="cadet blue")

		StdId           =       StringVar()
		Firstname       =       StringVar()
		Surname         =       StringVar()
		Dob             =       StringVar()
		Emailid         =       StringVar()
		Subject         =       StringVar()
		Address         =       StringVar()
		Mobile          =       StringVar()
		RfId            =       StringVar()
		SearchID        =       StringVar()

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
				backend.addStdRec(StdId.get(),Firstname.get(),Surname.get(),Dob.get(),Emailid.get(), Subject.get(),Address.get(),Mobile.get(),RfId.get())
				clearData()
				roo = Tk()
				roo.geometry("500x500+0+0")
				roo.title("Main Loop")
				lblfna = Label(roo,font=('arial',15,), text="Reciept Will be Generated!!",padx=2,pady=2,bg="Ghost White")
				lblfna.grid()
				roo.mainloop()
			else:
				iExit = tkinter.messagebox.askyesno("Error","Enter Values")

		
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

		def searchDatabase(StdId=""):
			
			if(len(str(StdId))==0 and len(SearchID.get())==0):
				iExit = tkinter.messagebox.askyesno("Error","Enter Values")
				return
			roo = Tk()
			roo.geometry("810x630+0+0")
			roo.title("Main Loop")
			roo.configure(background='Cadet Blue')

			MenuFrame = Frame(roo,bg='Cadet Blue',bd=10,relief=RIDGE)
			MenuFrame.pack()

			FraTitle = Frame(MenuFrame,bg='powder blue',bd=10,relief=RIDGE)
			FraTitle.pack(side=TOP)

			ReceiptCal_F = Frame(MenuFrame,bg='powder blue',bd=10,relief=RIDGE)
			ReceiptCal_F.pack(side=TOP)

			Buttons_F = Frame(MenuFrame,bg='powder blue',bd=10,relief=RIDGE)
			Buttons_F.pack(side=BOTTOM)

			def Exiti():
				roo.destroy()
				return 
			def iPrint():
				q= lblfna.cget("text")
				filetypes=[('Text', '*.txt'),('All files', '*'),('PDF','*.pdf'),('Word Document','*.docx')]
				filename=tkinter.filedialog.asksaveasfilename(defaultextension='.txt',filetypes=filetypes)
				f=open(filename,"w")
				f.write(q)
				f.close()

			lblTitle = Label(FraTitle,width=40,bg='white',fg='black',bd=4,font=('arial',24,'bold'),text="Print Details")
			lblTitle.grid(row=0,column=0)

			txtReceipt = Text(ReceiptCal_F,width=84,bg='white',height=24,font=('arial',12,'bold'),bd=4)
			txtReceipt.grid(row=1,column=0)

			btn1 = Button(Buttons_F,font=('arial',16,'bold'),width=19,text="Print",command=iPrint)
			btn1.grid(row=2,column=0)
			btn2 = Button(Buttons_F,font=('arial',16,'bold'),width=19,text="Update")
			btn2.grid(row=2,column=1)
			btn3 = Button(Buttons_F,font=('arial',16,'bold'),width=19,text="Delete")
			btn3.grid(row=2,column=2)

			if(len(SearchID.get())!=0):
				if(len(backend.searchData(SearchID.get()))==0):
					lblfna = Label(ReceiptCal_F,font=('arial',15,), text="No Records in this Roll Number is Available",padx=2,pady=2,bg="Ghost White")
					lblfna.grid(row=1,column=0)
				else:
					for row in backend.searchData(SearchID.get()):
						lblfna = Label(ReceiptCal_F,font=('arial',15,), text="Enrollment ID:  %s\nRoll Number:  %s\nName:  %s %s" % (row[0],row[1],row[2],row[3]))
						lblfna.grid(row=1,column=0)
			else:
				for row in backend.searchData(StdId):
					lblfna = Label(ReceiptCal_F,font=('arial',15,), text="Enrollment ID:  %s\nRoll Number:  %s\nName:  %s %s" % (row[0],row[1],row[2],row[3]))
					lblfna.grid(row=1,column=0)

			roo.mainloop()


		def update():	
			if(len(StdId.get())!=0):
				backend.deleteRec(std[0])
			if(len(StdId.get())!=0):
				backend.addStdRec(StdId.get(),Firstname.get(),Surname.get(),Dob.get(),Emailid.get(), \
					Subject.get(),Address.get(),Mobile.get(),RfId.get())
				studentlist.delete(0,END)
				backend.insert(END,(StdId.get(),Firstname.get(),Surname.get(),Dob.get(),Emailid.get(), \
					Subject.get(),Address.get(),Mobile.get(),RfId.get()))

		def displayStudentData():
			root = Tk()
			tree = ttk.Treeview(root)
			root.geometry("1100x500+0+0")
			root.title("Main Loop")
			root.configure(background='Cadet Blue') 
			
			lblfna = Label(root,font=('arial',15,), text="DOUBLE CLICK ON EACH OF THE ENTRY TO GET DETAILED VIEW")
			lblfna.pack(side=BOTTOM)
			
			def on_double_click(event):
				region = tree.identify("region", event.x, event.y)
				if region == "cell" or region != "cell":
					curItem = tree.focus()
					searchDatabase(tree.item(curItem)['values'][0])


			tree["columns"]=("Roll Number","Name","Email ID","Phone Number")
			
			tree.column("Roll Number", width=200)
			tree.column("Name", width=200 )
			tree.column("Email ID", width=200)
			tree.column("Phone Number", width=200)

			tree.heading("Roll Number", text="Roll Number")
			tree.heading("Name", text="Name")
			tree.heading("Email ID", text="Email ID")
			tree.heading("Phone Number", text="Phone Number")
			tree.bind("<Double-1>",on_double_click)

			for row in backend.searchAllData():
				tree.insert('', 'end', text="Student "+str(row[0]),values=(row[1],row[2],row[5],row[8]))
				
			tree.pack()
			root.mainloop()
						    
			
				

	#=========================================================Frames==================================================
		MainFrame = Frame(self.root,bg="cadet blue")
		MainFrame.grid()

		TitleFrame = Frame(MainFrame, bd=2, padx=67, pady=8, bg="Ghost White", relief= RIDGE)
		TitleFrame.pack(side=TOP)

		self.lblTit = Label(TitleFrame,font=('arial',46,'bold'),text="Student Management Asterix Educations" , bg="Ghost White")
		self.lblTit.grid()

		ButtonFrame = Frame(MainFrame,width=1000, height = 70 ,padx=10, pady=10, bg="Ghost White")
		ButtonFrame.pack(side=BOTTOM)

		DataFrame = Frame(MainFrame, width=1800, height = 400 ,padx=10, pady=10, bg="White", relief= RIDGE)
		DataFrame.pack(side=BOTTOM)

		DataFrameLEFT = LabelFrame(DataFrame, width=500, bd=2,height = 800 ,padx=20,pady=10, bg="Ghost White",font=('arial',20,'bold'),text="Student Information")
		DataFrameLEFT.pack(side=LEFT)

		# DataFrameRIGHT =LabelFrame(DataFrame, width=500, height = 600 ,padx=20, pady=3, bg="Ghost White", relief= RIDGE,font=('arial',20,'bold'),text="Student Details\n\n")
		# DataFrameRIGHT.pack(side=RIGHT)

	#=========================================================Labels and Entry Widget==================================================
		self.lblRfId = Label(DataFrameLEFT,font=('arial',15), text="Type Roll Number To Search:",padx=2,pady=2,bg="Ghost White")
		self.lblRfId .grid(row=0,column=0,sticky=W)
		self.searchID = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=SearchID,width=20)
		self.searchID.grid(row=1,column=0)
		self.btnSearchData = Button(DataFrameLEFT, text="SEARCH",font=('arial',15,'bold'),height=1,width=10,command=searchDatabase)
		self.btnSearchData.grid(row=1,column=2)

		self.lblSTDID = Label(DataFrameLEFT,font=('arial',15), text="Student ID:",padx=2,pady=2,bg="Ghost White")
		self.lblSTDID.grid(row=2,column=0,sticky=W)
		self.txtStdID = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=StdId,width=20)
		self.txtStdID.grid(row=3,column=0)     

		self.lblfna = Label(DataFrameLEFT,font=('arial',15,), text="Firstname:",padx=2,pady=2,bg="Ghost White")
		self.lblfna .grid(row=4,column=0,sticky=W)
		self.txtfna = Entry(DataFrameLEFT,font=('arial',20,'bold'), textvariable=Firstname, width=20)
		self.txtfna .grid(row=5,column=0)       

		self.lblSna = Label(DataFrameLEFT,font=('arial',15), text="Surname:",padx=2,pady=2,bg="Ghost White")
		self.lblSna .grid(row=6,column=0,sticky=W)
		self.txtSna = Entry(DataFrameLEFT,font=('arial',20,'bold'), textvariable=Surname, width=20)
		self.txtSna .grid(row=7,column=0)       

		self.lblDoB = Label(DataFrameLEFT,font=('arial',15), text="Date of Birth:",padx=2,pady=2,bg="Ghost White")
		self.lblDoB .grid(row=8,column=0,sticky=W)
		self.txtDoB = Entry(DataFrameLEFT,font=('arial',20,'bold'), textvariable=Dob, width=20)
		self.txtDoB .grid(row=9,column=0)       

		self.lblEmail = Label(DataFrameLEFT,font=('arial',15), text="Email-id:",padx=2,pady=2,bg="Ghost White")
		self.lblEmail .grid(row=10,column=0,sticky=W)
		self.txtEmail = Entry(DataFrameLEFT,font=('arial',20,'bold'), textvariable=Emailid, width=20)
		self.txtEmail .grid(row=11,column=0)     

		self.lblSubject = Label(DataFrameLEFT,font=('arial',15), text="Subject:",padx=2,pady=2,bg="Ghost White")
		self.lblSubject .grid(row=2,column=2,sticky=W)
		self.txtSubject = Entry(DataFrameLEFT,font=('arial',20,'bold'), textvariable=Subject, width=20)
		self.txtSubject .grid(row=3,column=2)   

		self.lblAdr = Label(DataFrameLEFT,font=('arial',15), text="Address:",padx=2,pady=2,bg="Ghost White")
		self.lblAdr .grid(row=4,column=2,sticky=W)
		self.txtAdr = Entry(DataFrameLEFT,font=('arial',20,'bold'), textvariable=Address, width=20)
		self.txtAdr .grid(row=5,column=2)       

		self.lblMob = Label(DataFrameLEFT,font=('arial',15), text="Mobile no:",padx=2,pady=2,bg="Ghost White")
		self.lblMob .grid(row=6,column=2,sticky=W)
		self.txtMob = Entry(DataFrameLEFT,font=('arial',20,'bold'), textvariable=Mobile, width=20)
		self.txtMob .grid(row=7,column=2)

		self.lblRfId = Label(DataFrameLEFT,font=('arial',15), text="RF ID:",padx=2,pady=2,bg="Ghost White")
		self.lblRfId .grid(row=8,column=2,sticky=W)
		self.txtRfId = Entry(DataFrameLEFT,font=('arial',20,'bold'), textvariable=RfId, width=20)
		self.txtRfId .grid(row=9,column=2)   

		self.btnAddData = Button(DataFrameLEFT , text="Add",font=('arial',15,'bold'),height=1,width=7,bd=4,command=addData)
		self.btnAddData.grid(row=11,column=2)  
	
		#================================================Listbox and ScrollBar Widget=================================================
		# scrollbar = Scrollbar(DataFrameRIGHT)
		# scrollbar.grid(row=0,column=1,sticky='ns')


		# studentlist = Listbox(DataFrameRIGHT, width=41, height=19,yscrollcommand=scrollbar.set,xscrollcommand=scrollbar.set)
		# studentlist.grid(row=0,column=0,padx=8)
				      
		# scrollbar.config(command = studentlist.yview)
		# scrollbar.config(command= studentlist.xview) 

		#================================================Button Widget=================================================================
		# self.btnAddData = Button(ButtonFrame , text="Add New",font=('arial',20,'bold'),height=1,width=7,bd=4,command=addData)
		# self.btnAddData.grid(row=0,column=0)

		self.btnDisplayData = Button(ButtonFrame , text="Display",font=('arial',20,'bold'),height=1,width=7,bd=4,command=DisplayData)
		self.btnDisplayData.grid(row=0,column=1)

		self.btnClearData = Button(ButtonFrame , text="Clear",font=('arial',20,'bold'),height=1,width=7,bd=4,command=clearData)
		self.btnClearData.grid(row=0,column=2)

		# self.btnDeleteData = Button(ButtonFrame , text="Delete",font=('arial',20,'bold'),height=1,width=7,bd=4,command=DeleteData)
		# self.btnDeleteData.grid(row=0,column=3)

		self.btnUpdateData = Button(ButtonFrame , text="Search",font=('arial',20,'bold'),height=1,width=7,bd=4,command=displayStudentData)
		self.btnUpdateData.grid(row=0,column=4)

		# self.btnSearchData = Button(ButtonFrame , text="Update",font=('arial',20,'bold'),height=1,width=7,bd=4,command=update)
		# self.btnSearchData.grid(row=0,column=5)

		self.btnExit = Button(ButtonFrame , text="Exit",font=('arial',20,'bold'),height=1,width=7,bd=4,command=iExit)
		self.btnExit.grid(row=0,column=6)

if __name__=='__main__':
	root=Tk()
	application=Student(root)
	root.mainloop()
