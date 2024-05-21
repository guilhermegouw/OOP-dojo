"""
Define a Student class with 2 instance attributes (name, age) and 1 class 
attribute (educational_platform='Udemy');
- Make it so that instances of Student could be created by simply specifying
the name. Hint: set the default age to a number.
- Define a greet() method which alternates between various name greetings.
When invoked, the method should randonly select a greeting and interpolate
in the name of the student.
    - Hi, I'm ...
    - Hey there, my name is...
    - Hi. Oh, my name is...
    - What's up, my name is ...
    - Good morning. My name is ...
- Starting with a list of several student names, create student instances from
each, and have each student introduce themselves.
"""
import random


class Student:
    educational_platform = "Udemy"

    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def greet(self):
        """
        Randonly prints a greeting from a list of greetings.
        This greeting is interpolated in the name of the student.
        """
        grettings = [
                f"Hi, I'm {self.name}",
                f"Hey there, my name is {self.name}",
                f"Hi. Oh, my name is {self.name}",
                f"What's up, my name is {self.name}",
                f"Good morning. My name is {self.name}"
            ]
        return random.choice(grettings)


if __name__ == "__main__":
    students = ["John", "Jane", "Bob", "Alice", "Charlie", "David", "Eve"]

    students = [Student(name) for name in students]
    for student in students:
        print(student.greet())
        
