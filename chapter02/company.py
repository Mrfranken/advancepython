class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    # 魔法函数既不属于object类，也不是Company类特有的方法，作为一个独立的存在的特殊方法可以加强类的功能
    # 直接影响类的使用语法，如果不添加__getitem__方法，对这个类的实力的遍历和切片都将不可用
    def __getitem__(self, index):
        return self.employee[index]

    def __len__(self):
        """
        添加这个魔法函数可以使用len方法
        """
        return len(self.employee)


company = Company(["tom", "bob", "jane"])

company1 = company[:2]  # 对实例进行切片

for em in company1:  # 对实例进行遍历
    print(em)

print(len(company))
