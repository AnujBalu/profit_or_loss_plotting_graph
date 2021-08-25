import json

class graph:
    def __init__(self,name,age,job,salary_got,salary_spend):
        self.name = name
        self.age = age
        self.job = job
        self.salary_got = salary_got
        self.salary_spend = salary_spend

    #money_got = salary_got(self)

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
    for i in range(2):
        x = int(input("Enter your salary: "))
        salary_got.append(x)
    salary_spend = []
    for i in range(2):
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
#print(create_file())
#print(create_file())
#h =create_file()
#print(h)
    #money_got = salary_got(self)
#information = create_file()


#print(type(create_file()))
def save_file(info):
    information=[]
    print(info)
    for i in info:
        information.append(i)

    print(information)
    try:
        text = open('detail1.dat', 'w')
        text.write(json.dumps(information,indent=4))
        text.close()
    except:
        print("bye bye")
def find_file():
    information = open('detail.txt','r')
    information = information.read()
    text = list(information)
    #print(information)
    #x = information['name']
    #print(x)
    for i in text:
        print(i)
        #print(text[i])
        #if i['name' == user:
         #   print(i.salary_got)
#find_file()
#print(type(load_file()))


#def find_file():



#def load_file(index)