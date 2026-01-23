# pg1: Group names by age using dictionary

def group_by_age(people):
    result = {}

    for person in people:
        age = person['age']
        name = person['name']

        if age not in result:
            result[age] = []
        result[age].append(name)

    return result


people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 25}
]

print(group_by_age(people))
