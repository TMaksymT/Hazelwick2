sl = int(input("choose an option 1-5: "))
list = []
#item = input("add an item: ")

while sl != 5:
    item = input("add an item: ")
    if sl == 1:
         print(item, "added")
         list.append(item)
         print("your current list is ", list)
    elif sl == 2:
        for n in list:
            print(n)
    