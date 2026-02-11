#sorting tuples using lambda

students = [('Amey', 25), ('Anshul', 20), ('Molu', 30)]
sorted_s = sorted(students, key=lambda x: x[1])
print(sorted_s)


#sorting dictionaries using lambda
students = [{'name': 'Amey', 'age': 25}, {'name': 'Anshul', 'age': 20}, {'name': 'Molu', 'age': 30}]

sorted_s = sorted(students, key=lambda x: x['age'])
print("\n",sorted_s)


#sorting list of strings using lambda
names = ['Amey', 'Anshul', 'Molu']
sorted_names = sorted(names, key=lambda x: len(x))
print("\n",sorted_names)


#sorting list of strings in reverse order using lambda
names = ['Amey', 'Anshul', 'Molu']
sorted_names = sorted(names, key=lambda x: len(x), reverse=True)
print("\n",sorted_names)


#conditional logic using lambda

check_even = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check_even(4))
print(check_even(7))