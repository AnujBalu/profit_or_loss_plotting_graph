class graph:
    def __init__(self,name,age,job,salary_got,salary_spend):
        self.name = name
        self.age = age
        self.job = job
        self.salary = salary_got
        self.salary_spend = salary_spend

    #money_got = salary_got(self)

    def mydetail(self):
        my_detail = {
            'name': self.name,
            'age': self.age,
            'job': self.job,
        }
        return my_detail

    def salary_got(self):
        money_got = []
        for i in range(2):
            x = int(input())
            money_got.append(x)
        return money_got
    #def salary_spend(self):

#print(hi.salary_got('self'))
#my_detail = my_detail()