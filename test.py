class Person():
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name  = last_name
        self.age = age
        self.gender = gender

    def view_personal_data(self):
        print(self.first_name, self.last_name, self.age, self.gender)