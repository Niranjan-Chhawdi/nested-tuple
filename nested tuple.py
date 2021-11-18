#write a program to create nested tuple roll number name percentage

stud = []

ch = 'y'

while ch == 'y' :
    roll = int(input("Enter the Roll Number : "))
    name = input("Enter the Name : ")
    per = int(input("Enter the Percentage : "))
    stud_data = [roll , name , per]
    b = tuple(stud_data)
    print("Roll :" ,roll)
    print("Name : " , name)
    print("Percentage : ", per)
    stud.append(b)
    c = tuple(stud)
    print(c)
    