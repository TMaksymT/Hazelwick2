sl = int(input("choose an option 1-5: "))
list = []
while sl != 5:
 item = input("add an item to your list: ")
if sl == 1 :
    print(item)
    while item in list == False:
       list.append(item)
       print( item, "has been added to your list")
else :
    print(item , "is already in your list")

