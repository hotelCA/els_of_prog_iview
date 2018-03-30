class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.age < other.age
        return NotImplemented
        
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.age == other.age
        return NotImplemented
        
def sort_groups(students):
    age_count_lookup = dict()

    for student in students:
        if student.age not in age_count_lookup:
            age_count_lookup[student.age] = 1
        else:
            age_count_lookup[student.age] += 1
    
    # Sort the ages in incresing order
    all_ages = age_count_lookup.keys()
    print(all_ages)
    
    age_index_lookup = {all_ages[0]: 0}
    curr_index = 0

    # age_group_indexes = [[0, all_ages[0]]]
    for i in range(1, len(all_ages)):
        curr_index = age_index_lookup[all_ages[i]] = curr_index + age_count_lookup[all_ages[i-1]]
        
    curr_index = 0
    while curr_index is not None:
        curr_age = students[curr_index].age
        if curr_index != age_index_lookup[curr_age]:
            swap(students, curr_index, age_index_lookup[curr_age])
        else:
            curr_index += 1
        age_index_lookup[curr_age] += 1
        age_count_lookup[curr_age] -= 1
        if age_count_lookup[curr_age] == 0:
            age_count_lookup.pop(curr_age)
            age_index_lookup.pop(curr_age)
            print(age_index_lookup.values())
            curr_index = list(age_index_lookup.values())[0] if age_index_lookup else None
            
    return students
            
def swap(students, index_1, index_2):
    students[index_1], students[index_2] = students[index_2], students[index_1]
    
students = [Student('John', 5),
            Student('John', 3),
            Student('John', 3),
            Student('John', 5),
            Student('John', 2),
            Student('John', 7),
            Student('John', 1),
            Student('John', 2),
            Student('John', 5)]
    
result = sort_groups(students)

for student in students:
    print(student.age)