class employee():
    def __init__(self, name, salary, level):
        
        self.name = name
        self.salary = salary
        
        assert level == "junior" or "mid-level" or "senior"
        self.level = level
    
    def view(self):
        print self.name
        print self.salary
        print self.level
        
    def bonus(self):
        
        if self.level == "junior":
            bonus = self.salary * 0.25
        elif self.level == "mid-level":
            bonus = self.salary * 0.50
        else:
            bonus = self.salary * 0.75
        
        print bonus
    
test = employee("mattia", 10000, "senior")
test.view()
test.bonus()