# class definition
class Student:
    def __init__(self, fname, lname, age, section):
        self.firstname = fname
        self.lastname = lname
        self.age = age
        self.section = section


# creating a new object
stu1 = Student("Sara", "Ansh", 22, "A2")

str1 = 'GeeksforGeeks'
def upper(string): return string.upper()


print(upper(str1))

# upper = lambda string: string.upper()


def format_numeric(num): return f"{num:e}" if isinstance(
    num, int) else f"{num:,.2f}"


print("Int formatting:", format_numeric(1000000))
print("float formatting:", format_numeric(999999.789541235))
