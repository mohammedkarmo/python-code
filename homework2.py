list1 = ["ALI" , "MOHAMAD" , "KHODER" , "HAIDER" , "HUSSEIN" , "MOHANNAD"]
while True:
    name = input("ENTER YOUR NAME: (UPPERCASE) EXIT TO STOP ")
    if name == "EXIT":
        break
    if name in list1: 
        print("OK")
    else:
         print("FALIED")


