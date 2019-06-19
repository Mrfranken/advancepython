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

    # 增加这个方法之后类的实例变成一个可迭代的对象,这个方法充分体现了鸭子类型
    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)

    def __str__(self):
        return "/".join(self.employee)


a = ["bobby1", "bobby2"]
b = ["bobby3", "bobby4"]
name_tuple = ("bobby5", "bobby6")

name_set = set()
name_set.add("bobby7")
name_set.add("bobby8")

a.extend(b)
a.extend(name_tuple)
a.extend(name_set)  # list可以extend tuple, set. extend方法接受一个可迭代的对象

company = Company(['a', 'b', 'c'])  # company作为一个可迭代的对象也可以作为一个元素添加到list中
a.extend(company)

print(a)
