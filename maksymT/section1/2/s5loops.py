marks = int(input("enter exam marks (1,100): "))
H = 0
L = 100
total = 0 
count = 0
while marks != -1 :
    if marks > 100 and marks < 0: 
         print  ("invalid marks, enter again")
         marks = int(input("enter exam marks (1,100): "))
    else:
         total = total + marks
         count = count + 1 
if marks > H: 
     H = marks
if marks < L:
     L = marks
print 