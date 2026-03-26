# Creating a class called student
class student:

    # Constructor: runs automatically when a student object is created
    def __init__(self, name, age , grade):
        self.name = name      # store student's name
        self.age = age        # store student's age
        self.grade = grade    # store student's grade

    # Method to return the student's grade
    def get_grade(self):
        return self.grade
        

# Creating a class called course
class course:

    # Constructor for course
    def __init__(self , name , max_size):
        self.name = name              # name of the course
        self.max_size = max_size      # maximum number of students allowed
        self.students = []            # empty list to store student objects

    # Method to add a student to the course
    def add_student(self , student):

        # Check if course is not full
        if len(self.students) < self.max_size:

            # Add student object to the list
            self.students.append(student)

            return True     # return True if student was added
        
        return False        # return False if course is already full


    # Method to calculate average grade of students in course
    def get_avg_grade(self):
        value = 0   # variable to store total grades

        # Loop through each student object in the students list
        for student in self.students:

            # Call get_grade() method of each student
            # and add it to total value
            value += student.get_grade()

        # Divide total grades by maximum course size
        return value / self.max_size
    

# Creating student objects
s1 = student("osama",25,75)
s2 = student("nouman",22,95)
s3 = student("hassan",25,85)


# Creating course object
course1 = course("Python" , 2)


# Try to add students to the course
print(course1.add_student(s1))   # True (added)
print(course1.add_student(s2))   # True (added)
print(course1.add_student(s3))   # False (course is full)


# Calculate and print average grade of students in the course
print(course1.get_avg_grade())