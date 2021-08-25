import json
import matplotlib.pyplot as plt

class graph:
    def __init__(self,name,age,job,salary_got,salary_spend):
        self.name = name
        self.age = age
        self.job = job
        self.salary_got = salary_got
        self.salary_spend = salary_spend

    def mydetail(self):
        my_detail = {
            'name': self.name,
            'age': self.age,
            'job': self.job,
            'salary_got': self.salary_got,
            'salary_spend':self.salary_spend
        }
        return my_detail

def my_file():
    name = input("Name: ")
    age = input("Age: ")
    job = input("Job: ")
    salary_got = []
    for i in range(4):
        x = int(input("Enter your salary: "))
        salary_got.append(x)
    salary_spend = []
    for i in range(4):
        x = int(input("Enter your usage of Money: "))
        salary_spend.append(x)
    return {
        'name' : name,
        'age' : age,
        'job' : job,
        'salary_got': salary_got,
        'salary_spend': salary_spend

    }


def create_file():
    create_file_input = my_file()
    information = graph((create_file_input['name']),(create_file_input['age']),(create_file_input['job']),
                        (create_file_input['salary_got']),(create_file_input['salary_spend']))
    return information.mydetail()

def save_file(info):
    information=[]
    for i in info:
        information.append(i)
    try:
        text = open('detail1.dat', 'w')
        text.write(json.dumps(information,indent=4))
        text.close()
    except:
        print("bye bye")
def find_file():
    try:
        user = input("Enter the user name of the account: ")
        myfile = open('detail1.dat','r')
        myfile= json.loads(myfile.read())
        for text in myfile:
            if text['name'] == user:
                x = text['salary_got']
                y = text['salary_spend']
                fig, axes = plt.subplots(figsize=(12, 3), dpi=100)
                axes.plot(x,'g')
                axes.plot(y, 'r.-')
                plt.show()
    except:
        print("something went wrong....")
