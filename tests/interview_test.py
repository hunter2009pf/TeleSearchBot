import pickle
import numpy as np


class Employee:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def __str__(self):
        return f"name: {self.name}, age: {self.age}, job: {self.job}"


class Circle:
    def __init__(self):
        self.__radius = 10

    @property
    def radius(self):
        print("call radius method")
        return self.__radius

    @radius.setter
    def radius(self, value):
        print(f"set up radius to {value}")
        self.__radius = 20


def generate_sth():
    for i in range(0, 3):
        yield i


def say_hello(*args, **kargs):
    for v in args:
        print(v)
    print("print key arguments:")
    for i, j in kargs.items():
        print(i, j)


def multipliers():
    return [lambda x: i * x for i in range(4)]


num = 1


def fn():
    global num
    num += 1
    return lambda: print(num)


def outer(fn):
    print("outer")

    def inner():

        print("inner")

        return fn

    return inner


@outer
def fun():
    print("fun")


if __name__ == "__main__":
    # a = []
    # if a:
    #     print("List is not empty")
    # else:
    #     print("List is empty")
    # b = ""
    # if b:
    #     print("string is not empty")
    # else:
    #     print("string is empty")
    # c = {}
    # if c:
    #     print("dict is not empty")
    # else:
    #     print("dict is empty")
    # emp = Employee(name="Jack", age=18, job="coder")
    # with open("temp.pickle", "wb") as f:
    #     f.write(pickle.dumps(emp))
    # with open("temp.pickle", "rb") as f:
    #     emp = pickle.load(f)
    #     print(emp)
    # with open("temp.pickle", "rb") as f:
    #     raw_data = f.read()
    # emp = pickle.loads(raw_data)
    # print(emp)
    # d = None
    # x = pickle.dumps(d)
    # print(x)
    # yuan = Circle()
    # print(yuan.radius)
    # yuan.radius = 20
    # print(yuan.radius)

    # gen = generate_sth()
    # for x in gen:
    #     print(x)

    # say_hello("hahah", 18, x="yes", y="ton")

    # print([m(2) for m in multipliers()])

    # m = {
    #     "1": "abc",
    #     "2": "yzg",
    #     "3": "hij",
    # }
    # keys = list(m.keys())
    # vals = list(m.values())
    # indices = np.argsort(vals)
    # sorted_dict = {keys[i]: vals[i] for i in indices}
    # print(sorted_dict)

    # arr = [1, 2, 3]
    # arr.insert(2, [7, 8, 9])
    # print(arr)

    # x = fn()
    # x()

    # str = "Hello,Python"
    # suffix = "Python"
    # print(str.endswith(suffix, 2))

    # dicts = {"one": 1, "two": 2, "three": 3}
    # print(dicts["one"])

    # temp = "ab".join(["1", "2", "3"])
    # print(temp)
    # temp = False
    # print(temp)

    # x = [1, 2, 3]
    # x.insert(0, 10)
    # print(x)

    with open("nginx.log", "r") as f:
        temp = f.readlines()
        for line in temp:
            print(line)
