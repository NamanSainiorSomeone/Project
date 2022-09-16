students = ["naman",'anshumaan','atul','someone']

students.sort()

for i in students:
    print(i)


studentss = ("naman",'anshumaan','atul','someone') #tauple

sorted_students = sorted(studentss)
for i in sorted_students:
    print(i)


student = [ ( " Squidward " , " F " , 60 ) ,
            ( " Sandy " , " A " , 33 ) ,
            ( " Patrick " , " D " , 36 ) ,
            ( " Spongebob " , " B " , 20 ) ,
            ( " Mr.Krabs " , " C " , 78 ) ]
grade = lambda grades: grades[1]
student.sort(key=grade,reverse=True)

for i in student:
    print(i)