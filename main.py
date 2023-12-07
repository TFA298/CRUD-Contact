import os
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["Contact"]
col = db["contacts"]


def menu():
    clearScreen()
    print("===MY CONTACT===")
    print("1. Show Contact")
    print("2. Add Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("0. Exit")

    input_menu = input("Select Action : ")

    if input_menu == "1":
        viewContact()
    elif input_menu == "2":
        insertData()
    elif input_menu == "3":
        updateData()
    elif input_menu == "4":
        deleteData()
    elif input_menu == "5" :
        searchData()
    elif input_menu == "0":
        exit()
    else:
        print("Inputan yang anda masukkan salah!")
        backToMenu()


def backToMenu():
    clearScreen()
    input("\nTekan enter untuk kembali ke menu awal")
    menu()

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def viewContact():
    clearScreen()
    count_contacts = col.count_documents({})

    if count_contacts == 0:
        print("You dont have contacts, Try socializing")
    else:
        contacts = col.find({}, {"_id": 0}).sort({"nama": 1})
        for contact in contacts:
            print(contact)
    backToMenu()

def insertData():
    clearScreen()
    nama = input("Nama     : ")
    nomor = input("Number   : ")
    category = input("Category : ")

    temp = {
        "nama" : nama,
        "nomor" : nomor,
        "kategori" : category
    }
    col.insert_one(temp)
    print("Insert Success")
    backToMenu()

def updateData():
    clearScreen()
    oldName = input("Name : ")
    check = col.find_one({"nama": oldName})

    if check:
        print("\nData found, Insert new update")
        newData = {
            "nama": input("New Name : "),
            "nomor": input("New Number : "),
            "kategori": input("New Category : ")
        }

        col.update_one(
            {"nama": oldName},
            {"$set": newData}
        )
        print("Update Success")

    else:
        print("Name not found")
        return updateData()

def deleteData():
    clearScreen()
    nama = input("Nama : ")
    checkDel = col.find_one({"nama": nama})

    if checkDel:
        col.delete_one(checkDel)
        print("Delete Success")
    else:
        print("Name not found")

def searchData():
    name = input("Name : ")
    check = col.find_one({"nama": name},{"_id": 0})

    if check:
        print("\nData found, Insert new update")
        print(check)

    else:
        print("Name not found")
        return searchData()

while True:
    menu()
