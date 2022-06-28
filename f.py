class schoolmember:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print('(создан schoolmember : {0})'.format(self.name))
	def tell(self):
		print('имя:"{0}" вораст:"{1}" '.format(self.name, self.age), end=" ")

class Teacher(schoolmember):
    def __init__(self, name, age, salary):
        schoolmember.__init__(self, name, age)
        self.salary = salary
        print('(создан Teacher: {0})'.format(self.salary))

    def tell(self):
        schoolmember.tell(self)
        print('зарплата: "{0:d}"'.format(self.salary))

class Student(schoolmember):
    def __init__(self, name, age, marks):
        schoolmember.__init__(self, name, age)
        self.marks = marks
        print('(Создан Student: {0})'.format(self.name))
    def tell(self):
        schoolmember.tell(self)
        print('оценки: "{0:d}"'.format(self.marks))
t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('твоё имя', 20, 75)

print()

members = [t, s]
for member in members:
    member.tell() 
