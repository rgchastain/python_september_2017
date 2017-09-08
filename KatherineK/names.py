# Part 1

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

for i in range (0, len(students)) :
    print "{} {}" .format(students[i]["first_name"],students[i]["last_name"])


print "-------------------------"

# Part 2


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

i = 0
a = 1

print "Students"
for items in users["Students"] :
    print "{} - {} {} - {}" .format(a, users["Students"][i]["first_name"], users["Students"][i]["last_name"], len(users["Students"][i]["first_name"])+len(users["Students"][i]["last_name"]))
    i += 1
    a += 1

i = 0
a = 1

print "Instructors"
for items in users["Instructors"] :
    print "{} - {} {} - {}" .format(a, users["Instructors"][i]["first_name"], users["Instructors"][i]["last_name"], len(users["Instructors"][i]["first_name"])+len(users["Instructors"][i]["last_name"]))
    i += 1
    a += 1


 #
