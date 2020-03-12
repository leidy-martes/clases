dict_plants = {
    "R": "Radishes",
    "G": "Grass",
    "C": "Clover",
    "V": "Violets"
}

students_default = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']


class Garden:
    def __init__(self, diagram, students=students_default):
        self.rows = diagram.split("\n")
        self.students = sorted(students)
  
    def plants(self, student):
        ind_student = self.students.index(student)
        return [dict_plants[plant] for plant in "".join([self.rows[i][2 * ind_student : 2 * ind_student + 2] for i in [0, 1]])]
