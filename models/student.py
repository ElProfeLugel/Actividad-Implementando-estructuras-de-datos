class Student:
    def __init__(self, name, age, grades) -> None:
        self.name = name
        self.age = age
        self.grades = grades

    def add_grade(self, grade: float):
        self.grades.append(grade)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)
    
    def __str__(self) -> str:
        return f"{self.name} ({self.age}) -> {self.grades}"
