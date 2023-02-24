class Ulstu:
    def __init__(self, facultet, special, teacher, student):
        self.facultet = facultet
        self.special = special
        self.teacher = teacher
        self. student = student

fist = Ulstu("FIST the best", "IVT", 30, 600)
print(fist.facultet)
print(fist.special)
print(fist.teacher)
print(fist.student)

ief = Ulstu("ECONOM", "marketing", 40, 500)
print(ief.facultet)
print(ief.special)
print(ief.teacher)
print(ief.student)



class Ulsu(Ulstu):
    def __init__(self, facultet, special, teacher, student, budget):
        super().__init__(facultet, special, teacher, student,)
        self.budget = budget

med = Ulsu("med", "dentist", 40, 500, 100000)
print(med.facultet)
print(med.special)
print(med.teacher)
print(med.student)
print(med.budget)





