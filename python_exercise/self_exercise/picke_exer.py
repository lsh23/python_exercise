import pickle
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class Student(object):
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def information(self):
        print("학생이름 : ", self.name , "학번 : ", self.number)


students = [ Student("이세형",201502087) , Student("김은아",201802000)]

with open("student_object.pickle","wb") as f:
    pickle.dump(students,f)


f = open("student_object.pickle","rb")

students_pickle = pickle.load(f)



for student in students_pickle:
    student.information()
