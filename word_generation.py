from __future__ import print_function
from mailmerge import MailMerge
from datetime import date
import backend



def generateCashMemo(StdId):
	template = "Reciepts/new.docx"

	document = MailMerge(template)
	for row in backend.searchData(StdId):
		document.merge(
			StdID 		= row[1],
			Firstname 	= row[2],
			Surname 	= row[3],
			Dob 		= row[4],
			Emailid		= row[5],
			Subject		= row[6],
			Address		= row[7],
			Mobile		= row[8],
			Amount 		= '1000',
			Type 		= 'Registration'
			)
	
	document.write('Reciepts/'+row[1]+row[2]+row[3]+'.docx')

