student= {}

while True:
    print("\n--------student manager app-----------")
    print("1. add Student")
    print("2. view Student")
    print("3. Check Student")
    print("4. Exit")
    
    
    choice = input("Enter your choice:")
    
    #Add  student 
    if choice == "1":
        name = input("enter student name:")
        marks = int(input("Enter marks: "))
        student[name] = marks
        print(f"{name} successfully Added!")
        
        #view students
    elif choice  == "2":
        if not student:
            print("No Student found!")
        else: 
            for name,marks in student.item():
                print(name,":",marks) 
                
                # check result 
    elif choice == "3":
                name = input("enter student name:")
                
                if name in student:
                    marks = student[name]
                    if marks >= 40:
                        print("student Pass")
                        
                    else: 
                        print("studebt fail")
                else:
                        print("student not found")
                    #exit 
    elif choice == "4":
        print("exiting....")
        
    else:
        print("invalid input")
                    
        
    
    