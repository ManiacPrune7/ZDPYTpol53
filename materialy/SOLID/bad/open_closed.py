"""
    Modul napisany w sposob zmuszajacy do modyfikacji
    kodu, zamiast jego rozszerzenia.
"""


class Profession:
    ARTIST = "artist"
    LAWYER = "lawyer"
    TEACHER = "teacher"
    PROGRAMMER = "programmer"


class TaxPayer:

    def __init__(self, profession, salary):
        self.profession = profession
        self.salary = salary

    def calculate_tax(self):
        if self.profession == Profession.ARTIST:
            return self.salary * 0.25
        elif self.profession == Profession.LAWYER:
            return self.salary * 0.34
        elif self.profession == Profession.TEACHER:
            return self.salary * 0.15
        elif self.profession == Profession.PROGRAMMER:
            return self.salary * 0.0
