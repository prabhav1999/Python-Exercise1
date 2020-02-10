class Student:
	studentCount=0
	def __init__(self, name,id):
		self.name=name
		self.id=id
		Student.studentCount=Student.studentCount+1
	def getStudentCount(self):
		return Student.studentCount

	def getGrade(self,key):
		return self.grades(key)
	
	def addGrade(self,key,value):
		self.grades[key]=value

s=Student('Steve','8789')
s.addGrade('Math','90')
s.addGrade('English','89')
s.getGrade('Math')