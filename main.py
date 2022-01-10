# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


class SimpleGradeBook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self,name):
        grades = self._grades[name]
        return sum(grades)/len(grades)

book = SimpleGradeBook()
book.add_student('Leeghim H')  #  book = SimpleGradeBook()
book.report_grade('Leeghim H', 90)
print(book.average_grade('Leeghim H'))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm, T branch test')
    print_hi('PyCharm, This is leeghim; a New message is given for you; this is for branch test')
    print_hi('PyCharm, This is leeghim; a New message is given for you; this is for branch test')
    print_hi('PyCharm, This is leeghim; a New message is given for you; this is for branch test')
    print_hi('PyCharm, This is leeghim; a New message is given for you; this is for branch test')
    print_hi('PyCharm, This is leeghim; a New message is given for you; this is for branch test')
    print_hi('PyCharm, This is leeghim; a New message is given for you; this is for branch test')
    print_hi('PyCharm, This is leeghim; a New message is given for you; this is for branch test')
    print_hi('PyCharm, This is leeghim; a New message is given for you; this is for branch test')
    print_hi('PyCharm, This is leeghim; a New message is given for you; this is for branch test')
    print_hi('PyCharm, This is leeghim; a New message is given for you; this is for branch test')
    print_hi('PyCharm, This is leeghim; a New message is given for you; this is for branch test')
    print_hi('PyCharm, This is leeghim; a New message is given for you; this is for branch test')
    print_hi('PyCharm, T branch test')
    print_hi('PyCharm, This is leeghim; a New message is given for you; this is for branch test')
    print_hi('PyCharm, This is leeghim; a New message is given for you; this is for branch test')
    print_hi('teststestestestPyCharm, This is leeghim; a New message is given for you; this is for branch test')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
