class Cat(object):
    def say(self):
        print("i am a cat")


class Dog(object):
    def say(self):
        print("i am a fish")


class Duck(object):
    def say(self):
        print("i am a duck")


animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)

    def __str__(self):
        return "/".join(self.employee)


a = ["bobby1", "bobby2"]
b = ["bobby3", "bobby4"]
name_tuple = ("bobby3", "bobby4")

name_set = set()
name_set.add("bobby5")
name_set.add("bobby6")

a.extend(b)
# a.extend(name_tuple)
# a.extend(name_set)  # list可以extend tuple, set

company = Company(['a', 'b', 'c'])  # company作为一个可迭代的对象也可以作为一个元素添加到list中
a.extend(company)

print(a)
