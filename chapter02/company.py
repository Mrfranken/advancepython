# -*- coding: utf-8 -*-


class Company(object):
    def __init__(self, num, num1, employee_list):
        self.num, self.num1 = num, num1
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __str__(self):
        """
        使用print时会调用这个方法
        """
        return "/".join(self.employee)

    def __repr__(self):
        return "&".join(self.employee)

    def __abs__(self):
        """
        自定义abs函数
        """
        return self.num + 1

    def __add__(self, other):
        return {"num": self.num + other.num, "num1": self.num1 + other.num1}

    def __len__(self):
        return len(self.employee)


if __name__ == '__main__':
    company = Company(1, 2, ["tom", "bob", "jane"])

    company1 = company[:2]

    for em in company1:
        print(em)

    print(company)

    print(repr(company))

    print(abs(company))

    print(company + Company(3, 4, [1, 2 ,3]))
