import pickle
import os

contact="contact.dat"


class phonenumber():
    def __init__(self,name,phonenumber,email):
        self.name=name
        self.phonenumber=phonenumber
        self.email=email

    def display(self):
        print("\nname:",self.name)
        print("\nphonenumber:",self.phonenumber)
        print("\nemail:",self.email)

import re  

import re

import re

def add_contact():
    with open(contact, "ab") as f:
        name = input("\nEnter the name: ")

        # ✅ Phone number validation
        while True:
            number = input("\nType the phone number: ")
            if re.fullmatch(r"^[6-9]\d{9}$", number):
                number = int(number)
                break
            else:
                print("❌ Invalid phone number! Please enter a 10-digit number starting with 6–9.")

        
        while True:
            email = input("\nEmail: ")
            
            if re.fullmatch(r"^[a-z0-9._-]+@[a-z0-9.-]+\.[a-z]{2,}$", email):
                break
            else:
                print("❌ Invalid email format!")
                print("   - Use only lowercase letters")
                print("   - Example: name123@gmail.com")

        
        p = phonenumber(name, number, email)
        pickle.dump(p, f)
        print("\n✅ Contact added successfully!")



def display_contact():
    if not os.path.exists(contact):
        print("No records.\n")
        return
    with open(contact, "rb") as f:
        while True:
                try:
                    b = pickle.load(f)
                    b.display()
                except EOFError:
                    break



def delete_contact(name):
    if not os.path.exists(contact):
        print("contacts are not found")
        return
    found=False
    temp="temp.dat"
    with open(contact,"rb")as f,open(temp,"wb")as f2:
        while True:
            try:
                p=pickle.load(f)
                if p.name.lower() != name.lower(): 
                    pickle.dump(p,f2)
                else:
                    found=True
            except EOFError:
                break
    os.remove(contact)
    os.rename(temp,contact)
    if found:
        print("contact deleted seccessfully")
    else:
        print("\n no such a contact exists")
while True:
    print("1.create new contact\n2.view contact\n3.delete contact\n4exit")
    ch=int(input("\nenter ur choice:"))

    if ch==1:
        add_contact()
    elif ch==2:
        display_contact()
    elif ch==3:
        name=input("\nenter the name of contact u wnat to delete:")
        delete_contact(name)
    elif ch==4:
        print("\nprogram is exiting....")
        break
    else:
        print("\ninvalid input")