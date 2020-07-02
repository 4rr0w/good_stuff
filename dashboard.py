import firebase_admin
from firebase_admin import credentials, firestore
from huepy import *
import sys


cred = credentials.Certificate("./fire.json") # from firebase project settings for auth.
firebase_admin.initialize_app(cred) 
db = firebase_admin.firestore.client()

numbers =[]

filehandle = open('numbers.txt', 'r')

for line in filehandle:
    currentPlace = line.strip()
    numbers.append(currentPlace)
filehandle.close()




def activate(numbers):
	for number in numbers:
		act = db.collection(u"admin").where(u"phone",u"==",number).stream()
		exist = False
		for doc in act:
			exist = True
			data = doc.to_dict()
			
			if data["approved"] == 0:
				db.collection(u"admin").document(str(doc.id)).set({"approved":1},merge=True)
				print(good(str(number) + "PROFILE ACTIVATED"))
			elif data["approved"] == 1:
				print(info(str(number) + " PROFILE ALREADY ACTIVE"))

		if not exist:
			print(bad(str(number) + " DATA NOT FOUND"))


def deactivate(numbers):
	for number in numbers:
		act = db.collection(u"admin").where(u"phone",u"==",number).stream()
		exist = False
		for doc in act:
			exist = True
			data = doc.to_dict()
			
			if data["approved"] == 1:
				db.collection(u"admin").document(str(doc.id)).set({"approved":0},merge=True)
				print(good(str(number) + "PROFILE DEACTIVATED"))
			elif data["approved"] == 0:
				print(info(str(number) + " PROFILE IS NOT ACTIVE ALREADY"))

		if not exist:
			print(bad(str(number) + " DATA NOT FOUND"))

if len(sys.argv) == 1:
	activate(numbers)
else:

	if sys.argv[1] == 'deactivate':
		deactivate(numbers)
	else:
		print(bad("Invalid argument passed"))
		print(que("""Do you mean "deactivate"."""))

	
	



