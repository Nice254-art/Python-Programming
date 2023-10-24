courses = ["MIT", "Cyber Security", "Data Science"]

print(courses)

# accessing an element in an array
print(courses[1])

# looping through an array
for course in courses:
    print(course)

# adding an element in an array
courses.append("Android Development")
print(courses)

# removing an element  from an array
courses.remove("MIT")
print(courses)
