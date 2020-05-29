import firebase_admin
from firebase_admin import credentials, firestore
import xlsxwriter
from datetime import datetime
import os

now = datetime.now() # current date and time
date_time = now.strftime("%m-%d-%Y,%H-%M-%S")

def user():

	docs = db.collection("users").stream()

	filename = 'Users('+date_time+').xlsx'

	excel = xlsxwriter.Workbook(filename)
	sheet = excel.add_worksheet()

	sheet.write("A1","Name")
	sheet.write("B1","Location")
	sheet.write("C1","Phone")
	sheet.write("D1","Zone")
	sheet.write("E1","Unit")
	sheet.write("F1","People")
	sheet.write("G1","Departure Date")
	sheet.write("H1","Expected Arrival")
	sheet.write("I1","Movement Status")
	sheet.write("J1","Final Approval")
	sheet.write("K1","Officer Remark")
	sheet.write("L1","Medical Remark")

	row = 1
	col = 0

	for doc in docs:
		data = doc.to_dict()
		
		movstatus = "Pending"
		finalstatus = "Pending"
		if data["movement"] == 1:
			movstatus = "Approved"
		elif data["movement"] == 1:
			movstatus = "Declined"
		if data["final"] == 1:
			movstatus = "Approved"
		elif data["final"] == 1:
			movstatus = "Declined"
		
		sheet.write(row , col , data["first"] + " " + data["last"])
		sheet.write(row , col + 1, data["location"])
		sheet.write(row , col + 2, data["phone"])
		sheet.write(row , col + 3, data["zone"])
		sheet.write(row , col + 4, data["unit"])
		sheet.write(row , col + 5, data["people"])
		sheet.write(row , col + 6, data["DepartureDate"])
		sheet.write(row , col + 7, data["ExpectedArrival"])
		
		sheet.write(row , col + 8, movstatus)
		sheet.write(row , col + 9, finalstatus)
		sheet.write(row , col + 10, data["movRemark"])
		sheet.write(row , col + 11, data["Remark"])

		row +=1

	excel.close()
	print("Users data saved in " + filename)



def admin():

	
	
	docs = db.collection("admin").stream()

	filename = 'Admins('+date_time+').xlsx'

	excel = xlsxwriter.Workbook(filename)
	sheet = excel.add_worksheet()

	sheet.write("A1","Name")
	sheet.write("B1","Location")
	sheet.write("C1","Phone")
	sheet.write("D1","Unit")
	sheet.write("E1","Profile Type")
	sheet.write("F1","Profile Status")

	row = 1
	col = 0

	for doc in docs:
		data = doc.to_dict()
		
		Profilestat = "Not Active"
		Profiletype = "Admin"
		if data["approved"] == 1:
			Profilestat = "Active"
		
		if data["type"] == 2:
			Profiletype = "Medical Officer"
		elif data["type"] == 3:
			Profiletype = "Super User"
		
		sheet.write(row , col , data["first"] + " " + data["last"])
		sheet.write(row , col + 1, data["location"])
		sheet.write(row , col + 2, data["phone"])
		sheet.write(row , col + 3, data["unit"])
		sheet.write(row , col + 4, Profiletype)
		sheet.write(row , col + 5, Profilestat)

		row +=1

	excel.close()
	print("Admins data saved in " + filename)

if __name__ == '__main__':
	cred = credentials.Certificate("./fire.json") # from firebase project settings for auth.
	firebase_admin.initialize_app(cred) 
	db = firebase_admin.firestore.client()
	user()
	admin()


