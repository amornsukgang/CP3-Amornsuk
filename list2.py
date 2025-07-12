menuList = []
totalprice=0
while True:
    menuName = input("Enter menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Enter price :")
        menuList.append([menuName,menuPrice])
        totalprice += int(menuPrice)


def showBill ():
    print("Bill")
    for i in range(len(menuList)):
        print(menuList[i])
    print("total :",totalprice,"thb")


showBill()
