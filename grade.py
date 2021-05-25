name=input("Enter the name of the student\n")
roll=int(input("Enter the roll of the student\n"))
clas=input("Enter the class of the student\n")
sec=input("Enter the section of the student\n")
marks=int(input("Enter total marks of the student\n"))
if(marks>=90):
    grade="Excellent"
elif(marks>=80 and marks<90):
    grade='A'
elif(marks>=70 and marks<80):
    grade='B'
elif(marks>=60 and marks<70):
    grade='C'
elif(marks>=50 and marks<60):
    grade='D'
elif(marks<50):
    grade="Fail"
print(f'''The name of the student is {name}    The roll of the student is {roll}
                 Class:{clas}                       Section:{sec} 
                            Total marks obtained:{marks}
                                  Grade:{grade}'''
)
