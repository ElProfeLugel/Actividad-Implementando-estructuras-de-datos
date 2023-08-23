from models.student import Student

dic = [{
    "name": "Lugel",
    "age": 27,
    "grades": [3, 4, 5, 3, 4]
},{
    "name": "Carlos",
    "age": 27,
    "grades": [3, 2, 1, 2, 4]
}]

students = [Student(s["name"], s["age"], s["grades"]) for s in dic]


print([s.name for s in students if s.average_grade() > 3])

promoted = { s.name: s for s in students if s.average_grade() > 3}
print(promoted)