# students =["harry", "harmoine", "ron","draco"]

# for student in range(len(students)):
#     print(student+1,students[student])

# students ={
#     "harry":"grifendore",
#     "harmoine":"grifendore",
#     "ron":"grifendore",
#     "draco":"slythrin",}

# for student in students:
#     print(student,students[student],sep=", ")

students =[
    {"name":"harry","house":"grifendore","patronus":"dire"},
    {"name":"harmoine","house":"grifendore","patronus":"stag"},
    {"name":"ron","house":"grifendore","patronus":"dare"},
    {"name":"draco","house":"slythrin","patronus":None}
    ]

for student in students:
    print(student["name"],student["house"],student["patronus"])