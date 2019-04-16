from tkinter import *
import tkinter.messagebox
import backend
import os
import tempfile
from tkinter import ttk
import tkinter.filedialog
import word_generation

class Student:

	def __init__(self,root):
		self.root=root
		self.root.title("*Asterix Educations")
		width, height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
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
				word_generation.generateCashMemo(StdId.get())
				clearData()
				iExit = tkinter.messagebox.askyesno("Success","Reciept is be Generated!!")

			else:
				iExit = tkinter.messagebox.askyesno("Error","Enter Values")


		def searchDatabase(StdId=""):
			if(len(str(StdId))==0 and len(SearchID.get())==0):
				iExit = tkinter.messagebox.askyesno("Error","Enter Values")
				return

			roo = Tk()
			roo.geometry("900x700+0+0")
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
			Buttons_F1 = Frame(MenuFrame,bg='powder blue',bd=10,relief=RIDGE)
			Buttons_F1.pack(side=BOTTOM)

			def Exiti():
				roo.destroy()
				return

			def refresh():
				self.btnSearchData.config(state="normal")
				self.btnAddData.config(state="normal")
				self.btnClearData.config(state="normal")
				self.btnSearchAllData.config(state="normal")
				self.lblRfId.config(state="normal")
				self.btnExit.config(state="normal")
				self.searchID.config(state="normal")
				self.txtStdID.config(state="normal")
				self.btnBack.grid_forget()
				
				self.txtStdID.delete(0,END)
				self.txtfna.delete(0,END)
				self.txtSna.delete(0,END)
				self.txtDoB.delete(0,END)
				self.txtEmail.delete(0,END)
				self.txtSubject.delete(0,END)
				self.txtAdr.delete(0,END)
				self.txtMob.delete(0,END)
				self.txtRfId.delete(0,END)
				self.searchID.delete(0,END)
				self.txtStdID.delete(0,END)


				self.btnBack.grid_forget()
				self.btnUpdateData.grid_forget()

			def iDelete():
				if(len(SearchID.get())!=0):
					backend.deleteRec(SearchID.get())
					iExit = tkinter.messagebox.askyesno("Error","Records have been succesfully deleted")
					roo.destroy()
				else:
					backend.deleteRec(StdId)
					iExit = tkinter.messagebox.askyesno("Error","Records have been succesfully deleted")
					roo.destroy()

				

			def iPrint():
				q= lblfna.cget("text")
				filetypes=[('Text', '*.txt'),('All files', '*'),('PDF','*.pdf'),('Word Document','*.docx')]
				filename=tkinter.filedialog.asksaveasfilename(defaultextension='.txt',filetypes=filetypes)
				f=open(filename,"w")
				f.write(q)
				f.close()

			def iUpdate():
				roo.destroy()
				
				self.btnSearchData.config(state="disabled")
				self.btnAddData.config(state="disabled")
				self.btnClearData.config(state="disabled")
				self.btnSearchAllData.config(state="disabled")
				self.btnExit.config(state="disabled")

				self.btnBack = Button(ButtonFrame , text="Back",font=('arial',20,'bold'),height=1,width=7,bd=4,command=refresh)
			
				if(len(StdId)==0):
					for row in backend.searchData(SearchID.get()):
						self.txtStdID.insert(0,row[0])
						self.txtfna.insert(0,row[2])
						self.txtSna.insert(0,row[3])
						self.txtDoB.insert(0,row[4])
						self.txtEmail.insert(0,row[5])
						self.txtSubject.insert(0,row[6])
						self.txtAdr.insert(0,row[7])
						self.txtMob.insert(0,row[8])
						self.txtRfId.insert(0,row[9])	
				else:
					for row in backend.searchData(StdId):
						self.txtStdID.insert(0,row[0])
						self.txtfna.insert(0,row[2])
						self.txtSna.insert(0,row[3])
						self.txtDoB.insert(0,row[4])
						self.txtEmail.insert(0,row[5])
						self.txtSubject.insert(0,row[6])
						self.txtAdr.insert(0,row[7])
						self.txtMob.insert(0,row[8])
						self.txtRfId.insert(0,row[9])

				self.searchID.config(state="disabled")
				self.txtStdID.config(state="disabled")
				self.btnUpdateData.grid(row=11,column=2)
				self.btnBack.grid(row=11,column=3)
				MainFrame.grid()

			lblTitle = Label(FraTitle,width=40,bg='white',fg='black',bd=4,font=('arial',24,'bold'),text="Print Details")
			lblTitle.grid(row=0,column=0)

			txtReceipt = Text(ReceiptCal_F,width=84,bg='white',height=24,font=('arial',12,'bold'),bd=4)
			txtReceipt.grid(row=1,column=0)

			btn1 = Button(Buttons_F,font=('arial',16,'bold'),width=19,text="Print",command=iPrint)
			btn1.grid(row=2,column=0)
			btn2 = Button(Buttons_F,font=('arial',16,'bold'),width=19,text="Update",command=iUpdate)
			btn2.grid(row=2,column=1)
			btn3 = Button(Buttons_F,font=('arial',16,'bold'),width=19,text="Delete",command=iDelete)
			btn3.grid(row=2,column=2)

			btn1 = Button(Buttons_F1,font=('arial',16,'bold'),width=19,text="Print",command=iPrint)
			btn1.grid(row=2,column=0)
			btn2 = Button(Buttons_F1,font=('arial',16,'bold'),width=19,text="Update",command=iUpdate)
			btn2.grid(row=2,column=1)
			btn3 = Button(Buttons_F1,font=('arial',16,'bold'),width=19,text="Delete",command=iDelete)
			btn3.grid(row=2,column=2)

			if(len(SearchID.get())!=0):
				if(len(backend.searchData(SearchID.get()))==0):
					lblfna = Label(ReceiptCal_F,font=('arial',15,), text="No Records in this Roll Number is Available",padx=2,pady=2,bg="Ghost White")
					lblfna.grid(row=1,column=0)
					btn2.config(state="disabled")
					btn3.config(state="disabled")
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
				backend.dataUpdate(StdId.get(),Firstname.get(),Surname.get(),Dob.get(),Emailid.get(),\
						Subject.get(),Address.get(),Mobile.get(),RfId.get())
			iExit = tkinter.messagebox.askyesno("Success!!","The values have been Updated")


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
					x = tree.item(curItem)['values'][0]
					root.destroy()
					searchDatabase(x)


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

		self.btnUpdateData = Button(DataFrameLEFT , text="Update",font=('arial',15,'bold'),height=1,width=7,bd=4,command=update)

		#================================================Button Widget=================================================================

		self.btnClearData = Button(ButtonFrame , text="CLEAR",font=('arial',20,'bold'),height=1,width=7,bd=4,command=clearData)
		self.btnClearData.grid(row=0,column=2)

		self.btnSearchAllData = Button(ButtonFrame , text="DISPLAY",font=('arial',20,'bold'),height=1,width=7,bd=4,command=displayStudentData)
		self.btnSearchAllData.grid(row=0,column=4)

		self.btnExit = Button(ButtonFrame , text="EXIT",font=('arial',20,'bold'),height=1,width=7,bd=4,command=iExit)
		self.btnExit.grid(row=0,column=6)

if __name__=='__main__':
	root=Tk()
	application=Student(root)
	root.mainloop()
