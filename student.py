
class Student:
    def __init__(self,first_name,last_name,year_of_birth,age,country):
        self.first_name=first_name
        self.last_name=last_name
        self.year_of_birth=year_of_birth
        self.age=age
        self.country=country
    
    def full_name(self):
        return f"Hello your name is {self.first_name} {self.last_name}"
    def years_of_birth(self):
        year_of_birth=2022-self.age   
        return f"Hello{self.first_name},{self.second_name} you age is {year_of_birth}"
    def your_initials(self):
        return f"Hello your initials are {self.first_name[0]} {self.last_name[0]}"
    

            
        
        
