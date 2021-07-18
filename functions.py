class MathFunctions:

    # Adds a and b, and returns the value (sum)
    def sum(self, a, b):
        return a + b

    # Substracts b from a, and returns the difference
    def difference(self, a, b):
        return a - b

    # Calculates the area of a rectangle/square
    def area(self, height, width):
        return height * width


class PersonFunctions:

    # Takes a list of Person as input, and doubles everyone's age
    def double_ages(self, people):
        for person in people:
            person.age *= 2
        return people

    # Counts the number of Person in the list that are older than 18
    def count_adults(self, people):
        nb_adults = 0
        for person in people:
            if person.age >= 18:
                nb_adults += 1
        return nb_adults

    # Converts list of people to a {Person.name: Person.age} dictionary
    def convert_to_dict(self, people):
        dict = {}
        for person in people:
            dict[person.name] = person.age
        return dict

    # Removes last name from Person object
    def remove_last_name(self, person):
        full_name = person.name.split(" ")
        person.name = full_name[0]

    # Input is 2 lists, returns a dict with {Person: grade} key-value pair
    # Throws IndexError if lists are not the same size
    def assign_grades(self, people, grades):
        if len(people) != len(grades):
            raise IndexError("Lists are not the same size")
        grades_dict = {}
        for i in range(0, len(people)):
            grades_dict[people[i]] = grades[i]
        return grades_dict
