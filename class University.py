class University:
    def __init__(self,student_name,course_unit,lecturer_name):
        # Initialize some data for demonstration
        self.student_name = student_name
        self.course_unit = course_unit
        self.lecturer_name = lecturer_name
obj1 = University("Olax","OOP","DR.Musa")
obj2 = University("Assasira","Research Methods","Dr. Otto")
obj3 = University("Robinnah","Advanced Christian Ethics","Rev. Henry")

print(obj1.student_name)
print(obj1.course_unit)
print(obj1.lecturer_name)
print(obj2.student_name)
print(obj2.course_unit)
print(obj2.lecturer_name)
print(obj3.student_name)
print(obj3.course_unit)
print(obj3.lecturer_name)