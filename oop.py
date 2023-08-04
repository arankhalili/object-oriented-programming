class company:
    count = 0
    def __init__(self, name, age, level_of_education, gender):
        self.name = name
        self.age = age
        self.loe = level_of_education
        self.gender = gender
#codes about name              
    def get_name(self):
            print('he/she is %s.' % self.name)        
#codes about age        
    def get_age(self):
        print('%s is %i years old.' % (self.name,self.age))    
#codes about level_of_education
    def get_loe(self):
        print("%s's level of education is %s." %(self.name,self.loe)) 
#codes about gender        
    def get_gender(self):
         print('%s gender is %s' % (self.name, self.gender))
#Codes related to all the information of an employee of this company
    def get_info(self):
        print("%s is a employee in this company.He/she is %i and He/she has a %s." % (self.name,self.age,self.loe))
 
#examples:
john = company('John', 28, "Bachelor's degree", 'male')
john.get_name()
john.get_age()
john.get_loe()
john.get_gender()
john.get_info()

x = ''''''
print(x)

Isabella = company('Isabella', 32, "Master's degree", 'female')
Isabella.get_name()
Isabella.get_age()
Isabella.get_loe()
Isabella.get_gender()
Isabella.get_info()
