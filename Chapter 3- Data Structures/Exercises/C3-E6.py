New_Invitation_List=["Nicola Tesla","Muhammad Ali","Mr Beast"]

print("Unfortunatly, my new table is not here so i can only invite two people")
remove_guest=New_Invitation_List.pop(2)
print(f"sorry {remove_guest} but you will have to miss out on the party")

for item in New_Invitation_List:
    if item =="Nicola Tesla":
        print(f"Dear {item}, you are invited to dinner!")
    elif item == "Muhammad Ali":
        print(f"Dear {item}, you are invited to dinner at my place!")